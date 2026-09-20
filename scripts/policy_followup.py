# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"

n = 0
for p in ROOT.rglob("index.html"):
    t = p.read_text(encoding="utf-8")
    nt = re.sub(
        r'<section class="acartechs-editorial-depth">.*?</section>',
        "",
        t,
        flags=re.S,
    )
    if nt != t:
        p.write_text(nt, encoding="utf-8")
        n += 1
print("stripped editorial-depth", n)

slugs = [
    "xbox-wire-temmuz-ayi-indie-selects-listesini-yayimladi",
    "xbox-konsol-fiyatlarinda-agustos-itibariyla-yeni-donem-basliyor",
    "xbox-game-pass-temmuz-listesine-yeni-oyunlar-ekleniyor",
    "xbox-wire-20-24-temmuz-haftasinin-yeni-oyunlarini-duyurdu",
    "xbox-insiders-icin-gamertag-oyun-merkezi-ve-istek-listesi-guncellemeleri-geldi",
    "xbox-22-26-haziran-haftasinda-cikacak-yeni-oyunlari-listeledi",
    "xbox-games-showcase-2026-oyun-dunyasinda-yeni-duyurularla-tamamlandi",
    "halo-campaign-evolved-temmuzda-oyuncularla-bulusmaya-hazirlaniyor",
    "playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti",
    "nintendo-direct-switch-2-icin-yeni-oyunlari-ve-klasik-donusleri-duyurdu",
    "oyun-abonelik-servislerine-yeni-yapimlar-eklendi",
    "bagimsiz-oyunlar-yaratici-fikirleriyle-one-cikiyor",
    "oyuncu-ekipmanlarinda-fiyat-performans-secimleri",
    "mobil-oyunlarda-grafik-kalitesi-hizla-artiyor",
    "oyuncu-bilgisayarlarinda-ekran-karti-secimi-yeniden-gundemde",
    "konsol-oyunculari-icin-sistem-guncellemesi-yayinlandi",
    "haftanin-oyun-firsatlari-ve-ucretsiz-yapimlari-aciklandi",
    "e-spor-turnuvalarinda-final-haftasi-heyecani-basladi",
    "hayatta-kalma-oyunlarinda-yeni-sezon-icerikleri",
    "yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-videosu-geldi",
]
m = 0
for slug in slugs:
    p = ROOT / slug / "index.html"
    t = p.read_text(encoding="utf-8")
    nt = re.sub(
        r'<div class="acartechs-single-top-ad">.*?</div>\s*(?=<div class="acartechs-single-body">)',
        "",
        t,
        flags=re.S,
    )
    if nt != t:
        p.write_text(nt, encoding="utf-8")
        m += 1
print("removed pre-body ads", m)

footer_old = '<li><a href="/hakkimizda/">Hakkımızda</a></li>'
footer_new = (
    '<li><a href="/hakkimizda/">Hakkımızda</a></li>\n'
    '\t\t\t\t\t<li><a href="/kunye/">Künye</a></li>\n'
    '\t\t\t\t\t<li><a href="/yayin-ilkeleri/">Yayın İlkeleri</a></li>'
)
for slug in ["oyun", "hakkimizda", "iletisim", "index", "gizlilik-politikasi", "kullanim-sartlari"]:
    p = ROOT / "index.html" if slug == "index" else ROOT / slug / "index.html"
    t = p.read_text(encoding="utf-8")
    if 'href="/kunye/"' not in t:
        t = t.replace(footer_old, footer_new, 1)
        p.write_text(t, encoding="utf-8")
        print("footer", slug)
