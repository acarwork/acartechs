#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export public/data/live-feed.json from published static article pages.

Usage:
  python scripts/export_live_feed.py
  python scripts/export_live_feed.py --public public --out public/data/live-feed.json

Wire-in:
  - npm run export:live-feed
  - GitHub Actions (auto on content push)
  - Call after adding/updating any article under public/<slug>/
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path

TR = timezone(timedelta(hours=3))

SKIP_DIRS = {
    "assets",
    "data",
    "wp-content",
    "wp-includes",
    "wp-json",
    "wp-admin",
    "cdn-cgi",
    # category / static / tools
    "oyun",
    "yazilim",
    "yapay-zeka",
    "teknoloji",
    "mobil",
    "bilgisayar",
    "sinema-dizi",
    "haberler",
    "uygulamalar",
    "hakkimizda",
    "iletisim",
    "gizlilik-politikasi",
    "cerez-politikasi",
    "kullanim-sartlari",
    "pdf-birlestirici",
    "pdf-word-excel-donusturucu",
    "gorselden-metne-ocr",
    "format-donusturucu",
    "gorsel-sikistirici",
    "kelime-karakter-sayici",
}

CAT_RULES: list[tuple[re.Pattern[str], str, str]] = [
    (re.compile(r"xbox|playstation|game-pass|oyun|nintendo|steam|halo|espor|e-spor", re.I), "oyun", "Oyun"),
    (re.compile(r"yapay-zeka|chatgpt|openai|gemini|copilot|claude|ai-|siri", re.I), "yapay-zeka", "Yapay Zeka"),
    (re.compile(r"github|yazilim|kodlama|api-|vscode|developer|android-studio", re.I), "yazilim", "Yazılım"),
    (re.compile(r"samsung|android|iphone|ios|telefon|pixel|galaxy|mobil", re.I), "mobil", "Mobil"),
    (re.compile(r"laptop|bilgisayar|windows|ssd|mini-pc|dizustu", re.I), "bilgisayar", "Bilgisayar"),
    (re.compile(r"netflix|disney|dizi|film|sinema|fragman|prime-video", re.I), "sinema-dizi", "Sinema-Dizi"),
]

LABEL_HINTS = [
    ("Yapay Zeka", "yapay-zeka"),
    ("Yazılım", "yazilim"),
    ("Yazilim", "yazilim"),
    ("Oyun", "oyun"),
    ("Mobil", "mobil"),
    ("Teknoloji", "teknoloji"),
    ("Bilgisayar", "bilgisayar"),
    ("Sinema-Dizi", "sinema-dizi"),
    ("Sinema", "sinema-dizi"),
]


def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def guess_category(slug: str, html: str) -> tuple[str, str]:
    for label, cat in LABEL_HINTS:
        if re.search(rf">\s*{re.escape(label)}\s*<", html[:12000]):
            return cat, label.replace("Yazilim", "Yazılım")
    for rx, cat, label in CAT_RULES:
        if rx.search(slug) or rx.search(html[:4000]):
            return cat, label
    return "haberler", "Haberler"


def parse_article(path: Path) -> dict | None:
    slug = path.parent.name
    if slug in SKIP_DIRS or slug.startswith("."):
        return None

    try:
        html = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    # Require a real article signal
    time_m = re.search(r'<time[^>]*datetime="([^"]+)"[^>]*>(.*?)</time>', html, re.I | re.S)
    if not time_m:
        # fallback meta
        meta_t = re.search(
            r'property="article:published_time"\s+content="([^"]+)"',
            html,
            re.I,
        )
        if not meta_t:
            return None
        date_raw = meta_t.group(1)
        date_label = date_raw[:10]
    else:
        date_raw = time_m.group(1)
        date_label = clean(time_m.group(2)) or date_raw[:10]

    date = date_raw[:10]
    try:
        datetime.fromisoformat(date)
    except ValueError:
        return None

    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    if not title_m:
        title_m = re.search(r'property="og:title"\s+content="([^"]+)"', html, re.I)
        title = clean(title_m.group(1)) if title_m else ""
    else:
        title = clean(title_m.group(1))
    if not title or len(title) < 8:
        return None

    desc_m = re.search(r'name="description"\s+content="([^"]+)"', html, re.I)
    if not desc_m:
        desc_m = re.search(r'property="og:description"\s+content="([^"]+)"', html, re.I)
    excerpt = clean(desc_m.group(1))[:240] if desc_m else ""

    img_m = re.search(r'property="og:image"\s+content="([^"]+)"', html, re.I)
    if not img_m:
        img_m = re.search(
            r'<img[^>]+class="[^"]*acartechs[^"]*"[^>]+src="([^"]+)"',
            html,
            re.I,
        )
    if not img_m:
        img_m = re.search(r'<img[^>]+src="(/wp-content/uploads/[^"]+)"', html, re.I)
    image = img_m.group(1) if img_m else ""
    if image.startswith("http"):
        image = re.sub(r"^https?://[^/]+", "", image)

    cat, cat_label = guess_category(slug, html)

    # ISO datetime
    iso_full = date_raw
    if "T" not in iso_full:
        iso_full = f"{date}T12:00:00+03:00"
    elif iso_full.endswith("Z"):
        iso_full = iso_full.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(iso_full)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=TR)
    except ValueError:
        dt = datetime.fromisoformat(f"{date}T12:00:00").replace(tzinfo=TR)

    # Breaking rules:
    # 1) explicit marker in HTML
    # 2) or published within last 12 hours
    explicit = bool(
        re.search(
            r'data-breaking=["\']?(true|1|yes)|acartechs-breaking|son\s*dakika',
            html[:5000],
            re.I,
        )
    )
    age_h = (datetime.now(TR) - dt.astimezone(TR)).total_seconds() / 3600
    breaking = explicit or (0 <= age_h <= 12)

    return {
        "id": slug,
        "title": title,
        "url": f"/{slug}/",
        "category": cat,
        "categoryLabel": cat_label,
        "date": date,
        "iso": dt.astimezone(TR).isoformat(timespec="seconds"),
        "excerpt": excerpt,
        "image": image,
        "breaking": breaking,
        "_sort": dt.timestamp(),
    }


def export_feed(public: Path, out: Path, limit: int = 20) -> dict:
    items: list[dict] = []
    for index in public.glob("*/index.html"):
        item = parse_article(index)
        if item:
            items.append(item)

    items.sort(key=lambda x: x["_sort"], reverse=True)
    items = items[:limit]
    for it in items:
        it.pop("_sort", None)

    # Cap breaking to top 3 freshest
    breaking_seen = 0
    for it in items:
        if it.get("breaking"):
            breaking_seen += 1
            if breaking_seen > 3:
                it["breaking"] = False

    payload = {
        "updatedAt": datetime.now(TR).isoformat(timespec="seconds"),
        "items": items,
    }

    out.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    out.write_text(text, encoding="utf-8")
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export AcarTechs live-feed.json")
    parser.add_argument(
        "--public",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "public",
        help="Public site root",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output JSON path (default: public/data/live-feed.json)",
    )
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if output would change (CI drift check)",
    )
    args = parser.parse_args(argv)

    public = args.public.resolve()
    out = (args.out or (public / "data" / "live-feed.json")).resolve()

    if not public.is_dir():
        print(f"public dir not found: {public}", file=sys.stderr)
        return 2

    if args.check and out.exists():
        old = out.read_text(encoding="utf-8")
    else:
        old = None

    payload = export_feed(public, out, limit=args.limit)
    print(f"Wrote {out} ({len(payload['items'])} items)")
    breaking = [i["title"] for i in payload["items"] if i.get("breaking")]
    if breaking:
        print("breaking:")
        for t in breaking:
            print(f"  - {t}")

    if args.check and old is not None:
        # ignore updatedAt-only drift: compare items
        try:
            old_items = json.loads(old).get("items")
        except json.JSONDecodeError:
            old_items = None
        if old_items != payload["items"]:
            print("live-feed items drifted", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
