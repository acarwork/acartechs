# -*- coding: utf-8 -*-
"""Remove generic second-half filler headings/paragraphs from article bodies."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"

HEADINGS = (
    r"Kimleri ilgilendiriyor\??",
    r"Takip edilmesi gereken noktalar",
    r"Duyuruda öne çıkan başlıklar",
    r"Duyuruda one cikan basliklar",
    r"Okuyucu icin kisa ozet",
    r"Okuyucu için kısa özet",
    r"Gelişmenin arka planı",
    r"Gelismenin arka plani",
    r"Oyuncular için anlamı",
    r"Oyuncular icin anlami",
    r"Gündemin okura yansıması",
    r"Gundemin okura yansimasi",
    r"Haberi değerlendirirken",
    r"Haberi degerlendirirken",
    r"Kullanıcıya yansıması",
    r"Kullaniciya yansimasi",
)

HEAD_RE = re.compile(
    r"<h2>\s*(?:" + "|".join(HEADINGS) + r")\s*</h2>"
    r"(?:\s*(?:<p\b(?![^>]*acartechs-source-note)[\s\S]*?</p>|<ul\b[\s\S]*?</ul>))+\s*",
    re.I,
)

PHRASE_RE = re.compile(
    r"<p\b[^>]*>[\s\S]*?(?:"
    r"Teknoloji gündemindeki bu tür başlıklar"
    r"|Teknoloji haberlerinde aynı başlık farklı"
    r"|kullanıcıya yansıyan pratik fayda"
    r"|resmi teknik ayrıntılar"
    r"|Haberin hedef kitlesi, duyurunun türüne göre"
    r"|resmi kaynakta paylaşılan bilgiler doğrultusunda değerlendirildiğinde birkaç ana noktaya"
    r"|haberin yalnızca tek cümlelik bir duyuru olarak kalmasını değil"
    r"|Sonuç olarak bu başlık, tek seferlik bir duyurudan çok"
    r")[\s\S]*?</p>\s*",
    re.I,
)


def strip_body(html: str) -> str:
    def repl_body(m: re.Match) -> str:
        inner = m.group(1)
        prev = None
        while prev != inner:
            prev = inner
            inner = HEAD_RE.sub("", inner)
            inner = PHRASE_RE.sub("", inner)
        inner = re.sub(r"\n{3,}", "\n\n", inner)
        return f'<div class="acartechs-single-body">{inner}</div>'

    return re.sub(
        r'<div class="acartechs-single-body">(.*?)</div>\s*(?=</article>)',
        repl_body,
        html,
        count=1,
        flags=re.S,
    )


def main() -> None:
    n = 0
    for p in ROOT.rglob("index.html"):
        html = p.read_text(encoding="utf-8")
        if 'class="acartechs-single-body"' not in html:
            continue
        new = strip_body(html)
        if new != html:
            p.write_text(new, encoding="utf-8")
            n += 1
            print("stripped", p.parent.name)
    print("files", n)


if __name__ == "__main__":
    main()
