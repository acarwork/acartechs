# -*- coding: utf-8 -*-
"""Inventory article word counts, near-duplicate titles, category listings."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"
SKIP = {
    "assets", "data", "wp-content", "wp-includes", "wp-json", "wp-admin",
    "kunye", "yayin-ilkeleri", "hakkimizda", "iletisim", "gizlilik-politikasi",
    "cerez-politikasi", "kullanim-sartlari", "mini-oyunlar", "brick-blitz",
    "snake-rewind", "cascade-blocks", "number-fusion", "pixel-glider",
    "galaxy-defender", "neon-maze-muncher", "memory-flash", "reaction-rush",
    "runner-byte", "dx-ball", "grid-runner", "format-donusturucu",
    "gorsel-sikistirici", "gorselden-metne-ocr", "kelime-karakter-sayici",
    "pdf-birlestirici", "pdf-word-excel-donusturucu",
}
CATS = ["oyun", "yazilim", "yapay-zeka", "teknoloji", "mobil", "sinema-dizi", "bilgisayar", "haberler", "uygulamalar"]


def text_of(html: str) -> str:
    m = re.search(r'<div class="acartechs-single-body">(.*?)</div>\s*</article>', html, re.S)
    chunk = m.group(1) if m else ""
    chunk = re.sub(r"<aside[\s\S]*?</aside>", " ", chunk)
    chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    chunk = re.sub(r"&[a-z]+;", " ", chunk)
    return re.sub(r"\s+", " ", chunk).strip()


def title_of(html: str) -> str:
    m = re.search(r"<h1>(.*?)</h1>", html, re.S)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return (m.group(1) if m else "").replace(" – AcarTechs", "").strip()


def main() -> None:
    rows = []
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name in SKIP or d.name.startswith("."):
            continue
        p = d / "index.html"
        if not p.exists():
            continue
        html = p.read_text(encoding="utf-8")
        if 'class="acartechs-single-body"' not in html:
            continue
        body = text_of(html)
        words = len(body.split()) if body else 0
        rows.append((words, d.name, title_of(html), body[:80]))

    rows.sort()
    print("=== ARTICLE WORD COUNTS (low first) ===")
    for w, slug, title, prev in rows:
        flag = "THIN" if w < 280 else ("OK" if w >= 350 else "MID")
        print(f"{flag:4} {w:4}  {slug}  | {title}")

    print("\n=== NEAR DUPLICATE SLUG STEMS ===")
    stems = defaultdict(list)
    for w, slug, title, _ in rows:
        stem = re.sub(r"-(2|nedir|guncelleme.*)$", "", slug)
        key = "-".join(stem.split("-")[:5])
        stems[key].append((slug, title, w))
    for k, items in sorted(stems.items()):
        if len(items) > 1:
            print(k)
            for slug, title, w in items:
                print(f"   {w:4} {slug} | {title}")

    print("\n=== CATEGORY PAGES exist ===")
    for c in CATS:
        print(c, "YES" if (ROOT / c / "index.html").exists() else "NO")

    print("\nTOTAL ARTICLES", len(rows))
    print("THIN", sum(1 for w, *_ in rows if w < 280))
    print("MID", sum(1 for w, *_ in rows if 280 <= w < 350))
    print("OK", sum(1 for w, *_ in rows if w >= 350))


if __name__ == "__main__":
    main()
