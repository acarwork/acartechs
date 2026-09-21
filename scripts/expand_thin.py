# -*- coding: utf-8 -*-
"""Lengthen unique thin/mid articles; 301 leftover duplicate stubs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_publisher_policy import ARTICLE_AD, ROOT, rewrite_article
from apply_sitewide_policy import DUPLICATES
from thin_extras import GUIDE_EXTRA, MORE_DUPLICATES
from thin_news import NEWS, NEWS_EXTRA

BODY_RE = re.compile(
    r'(<div class="acartechs-single-body">)(.*?)(</div>\s*</article>)',
    re.S,
)


def extra_html(block: dict) -> str:
    bullets = "".join(f"<li>{c}</li>" for c in block["checks"])
    ad = "" if block.get("skip_ad") else ARTICLE_AD
    return (
        f'\n<section class="acartechs-depth">\n'
        f'<h2>{block["h2a"]}</h2>\n<p>{block["a"]}</p>\n'
        f"{ad}"
        f'<h2>{block["h2b"]}</h2>\n<p>{block["b"]}</p>\n'
        f'<h2>{block["h2c"]}</h2>\n<p>{block["c"]}</p>\n'
        f"<ul>{bullets}</ul>\n<p>{block['close']}</p>\n"
        f"</section>\n"
    )


def insert_extra(slug: str, block: dict) -> None:
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    if "acartechs-depth" in html:
        print("skip existing depth", slug)
        return
    extra = extra_html(block)
    m = BODY_RE.search(html)
    if not m:
        raise SystemExit(f"no body {slug}")
    inner = m.group(2)
    if 'class="acartechs-source-note"' in inner:
        inner = re.sub(
            r'(<p class="acartechs-source-note")',
            extra + r"\1",
            inner,
            count=1,
        )
    else:
        inner = inner.rstrip() + extra
    html = html[: m.start()] + m.group(1) + inner + m.group(3) + html[m.end() :]
    if block.get("title"):
        from apply_publisher_policy import replace_h1_dek, set_meta

        html = set_meta(html, block["title"], block.get("description") or block["title"], slug)
        html = replace_h1_dek(html, block["title"], block.get("dek"))
    path.write_text(html, encoding="utf-8")
    print("expanded", slug)


def patch_redirects(pairs: dict[str, str]) -> None:
    extra_lines = [f"/{src}/ /{dest}/ 301" for src, dest in pairs.items()]
    p = ROOT / "_redirects"
    text = p.read_text(encoding="utf-8")
    for line in extra_lines:
        if line.split()[0] not in text:
            text += line + "\n"
    p.write_text(text, encoding="utf-8")

    needle_anchor = "['/akilli-ev-urunlerinde-uyumluluk-sorunu-azaliyor/', '/akilli-ev-cihazlari-daha-uyumlu-hale-geliyor/'],"
    for js in (ROOT.parent / "src" / "worker.js", ROOT.parent / "functions" / "_middleware.js"):
        t = js.read_text(encoding="utf-8")
        for src, dest in pairs.items():
            item = f"['/{src}/', '/{dest}/']"
            if item not in t and needle_anchor in t:
                t = t.replace(needle_anchor, needle_anchor + "\n  " + item + ",", 1)
        js.write_text(t, encoding="utf-8")


def noindex(slugs: list[str]) -> None:
    tag = "<meta name='robots' content='noindex, follow' />\n"
    for slug in slugs:
        p = ROOT / slug / "index.html"
        if not p.exists():
            continue
        html = p.read_text(encoding="utf-8")
        if "noindex" in html:
            continue
        html = html.replace("<head>", "<head>\n" + tag, 1)
        p.write_text(html, encoding="utf-8")
        print("noindex", slug)


def main() -> None:
    all_dups = dict(DUPLICATES)
    all_dups.update(MORE_DUPLICATES)
    patch_redirects(MORE_DUPLICATES)
    noindex(list(all_dups))

    for slug, data in NEWS.items():
        if slug in all_dups:
            continue
        rewrite_article(slug, data)

    for slug, block in {**GUIDE_EXTRA, **NEWS_EXTRA}.items():
        if slug in all_dups or slug in NEWS:
            continue
        insert_extra(slug, block)


if __name__ == "__main__":
    main()
