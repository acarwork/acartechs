const ROBOTS = `User-agent: *
Disallow: /wp-admin/
Disallow: /*?s=
Disallow: /*?p=
Disallow: /wp-json/
Disallow: /xmlrpc.php
Allow: /wp-admin/admin-ajax.php

User-agent: Google-Extended
Allow: /

Sitemap: https://acartechs.com/sitemap.xml
`;

const LLMS = `# Acartechs

Acartechs, teknoloji, yapay zeka, mobil, yazilim, oyun ve dijital medya alanlarindaki gelismeleri sade bir dille aktaran Turkce teknoloji haber sitesidir.

Site: https://acartechs.com/
Sitemap: https://acartechs.com/sitemap.xml
Iletisim: acarr.ffatih@gmail.com

## Ana bolumler

- Yapay Zeka: https://acartechs.com/yapay-zeka/
- Yazilim: https://acartechs.com/yazilim/
- Teknoloji: https://acartechs.com/teknoloji/
- Mobil: https://acartechs.com/mobil/
- Oyun: https://acartechs.com/oyun/
- Sinema-Dizi: https://acartechs.com/sinema-dizi/
- Uygulamalar: https://acartechs.com/uygulamalar/

## Kullanim notu

Icerikler resmi kaynaklara dayanan, editoryal yorum ve pratik rehber eklenmis ozgun Turkce yazilardir. Kisa duyuru metinleri oldugu gibi kopyalanmaz.
`;

const REDIRECTS = new Map([
  ['/wp-login.php', '/'],
  ['/category/haberler/', '/haberler/'],
  ['/category/yazilim/', '/yazilim/'],
  ['/category/yapay-zeka/', '/yapay-zeka/'],
  ['/category/teknoloji/', '/teknoloji/'],
  ['/category/bilgisayar/', '/bilgisayar/'],
  ['/category/mobil/', '/mobil/'],
  ['/category/oyun/', '/oyun/'],
  ['/category/sinema-dizi/', '/sinema-dizi/'],
  ['/animasyon-dunyasinda-yeni-proje-duyuruldu-2/', '/animasyon-dunyasinda-yeni-proje-duyuruldu/'],
  ['/bagimsiz-oyunlardan-haftanin-dikkat-cekenleri-2/', '/bagimsiz-oyunlardan-haftanin-dikkat-cekenleri/'],
  ['/bilim-kurgu-filmi-icin-ilk-fragman-yayinlandi-2/', '/bilim-kurgu-filmi-icin-ilk-fragman-yayinlandi/'],
  ['/e-spor-turnuvasinda-final-haftasi-heyecani-basladi/', '/e-spor-turnuvalarinda-final-haftasi-heyecani-basladi/'],
  ['/hayatta-kalma-oyunlarinda-yeni-sezon-icerikleri-2/', '/hayatta-kalma-oyunlarinda-yeni-sezon-icerikleri/'],
  ['/mobil-oyunlarda-grafik-kalitesi-hizla-artiyor-2/', '/mobil-oyunlarda-grafik-kalitesi-hizla-artiyor/'],
  ['/oyun-abonelik-servislerine-yeni-yapimlar-eklendi-2/', '/oyun-abonelik-servislerine-yeni-yapimlar-eklendi/'],
  ['/oyuncu-ekipmanlarinda-fiyat-performans-secimleri-2/', '/oyuncu-ekipmanlarinda-fiyat-performans-secimleri/'],
  ['/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti-2/', '/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti/'],
  ['/playstation-plus-haziran-kataloguna-final-fantasy-xvi-ve-sonic-x-shadow-generations-eklendi/', '/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti/'],
  ['/bagimsiz-oyunlardan-haftanin-dikkat-cekenleri/', '/bagimsiz-oyunlar-yaratici-fikirleriyle-one-cikiyor/'],
  ['/haftanin-oyun-indirimleri-oyuncularin-ilgisini-cekiyor/', '/haftanin-oyun-firsatlari-ve-ucretsiz-yapimlari-aciklandi/'],
  ['/oyuncu-ekipmanlarinda-fiyat-performans-secenekleri-araniyor/', '/oyuncu-ekipmanlarinda-fiyat-performans-secimleri/'],
  ['/konsol-guncellemeleri-sosyal-ozellikleri-gelistiriyor/', '/konsol-oyunculari-icin-sistem-guncellemesi-yayinlandi/'],
  ['/populer-dizinin-yeni-sezon-tarihi-aciklandi-2/', '/populer-dizinin-yeni-sezon-tarihi-aciklandi/'],
  ['/teknoloji-dunyasinda-bugun-one-cikan-her-seyi-anlattik-2/', '/teknoloji-dunyasinda-bugun-one-cikan-her-seyi-anlattik/'],
  ['/yayin-platformlari-yaz-takvimini-guncelledi-2/', '/yayin-platformlari-yaz-takvimini-guncelledi/'],
  ['/yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-goruntuleri-paylasildi/', '/yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-videosu-geldi/'],
  ['/yeni-film-ve-dizi-haberleri-tek-sayfada-toplandi-2/', '/yeni-film-ve-dizi-haberleri-tek-sayfada-toplandi/'],
  ['/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-geliyor/', '/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor/'],
  ['/yeni-nesil-yapay-zeka-araclari-is-dunyasinda-nasil-fark-olusturuyor/', '/yapay-zeka-araclari-is-dunyasinda-yeni-verimlilik-donemi-baslatti/'],
  ['/netflix-bu-hafta-color-book-ve-the-american-experiment-gibi-yapimlari-one-cikardi/', '/netflix-haftanin-izlenecek-yapimlarini-yeni-listeyle-paylasti/'],
  ['/netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-cikti/', '/netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti/'],
  ['/yeni-nesil-teknoloji-haberlerini-tek-ekranda-yakala/', '/haftanin-kisa-teknoloji-ozeti-yayinda/'],
  ['/haftanin-en-cok-izlenen-yapimlari-belli-oldu/', '/yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor/'],
  ['/bilgisayar-donaniminda-performans-yarisi-buyuyor/', '/donanim-pazarinda-fiyat-ve-performans-dengesi-degisiyor/'],
  ['/acik-kaynak-kutuphanelerde-haftanin-one-cikanlari/', '/acik-kaynak-projeler-teknoloji-dunyasinda-etkisini-artiriyor/'],
  ['/siber-guvenlik-ekipleri-icin-kritik-yama-uyarisi/', '/siber-guvenlik-yamalarini-geciktirmek-buyuk-risk-olusturuyor/'],
  ['/ogrenciler-icin-yapay-zeka-destekli-calisma-araclari/', '/egitimde-yapay-zeka-destekli-calisma-araclari-yayginlasiyor/'],
  ['/akilli-telefonlarda-batarya-odakli-yeni-donem/', '/yeni-nesil-telefon-bataryalari-daha-uzun-omur-hedefliyor/'],
  ['/teknoloji-alisverisinde-dikkat-edilmesi-gerekenler/', '/teknoloji-alisverisinde-garanti-ve-servis-destegi-neden-onemli/'],
  ['/ai-araclari-is-dunyasinda-yeni-donemi-baslatti/', '/yapay-zeka-araclari-is-dunyasinda-yeni-verimlilik-donemi-baslatti/'],
  ['/verimlilik-uygulamalari-ekip-calismasini-kolaylastiriyor/', '/verimlilik-uygulamalari-gunluk-planlamayi-kolaylastiriyor/'],
  ['/teknoloji-dunyasinda-bugun-one-cikan-her-seyi-anlattik/', '/teknoloji-gundeminde-bugun-one-cikan-basliklar/'],
  ['/yayin-platformlari-yaz-takvimini-guncelledi/', '/yayin-platformlari-yaz-kataloglarini-guncelliyor/'],
  ['/kult-serinin-devam-filmi-icin-hazirlik-basladi/', '/kult-serinin-devam-filmi-icin-hazirliklar-basladi/'],
  ['/gorsel-uretme-araclari-tasarim-surecini-hizlandiriyor/', '/gorsel-uretme-araclari-tasarim-surecini-degistiriyor/'],
  ['/ekran-teknolojilerinde-parlaklik-ve-enerji-yarisi/', '/ekran-teknolojilerinde-parlaklik-ve-enerji-verimliligi-yarisi/'],
  ['/elektrikli-otomobil-pazarinda-fiyat-rekabeti-hizlandi/', '/elektrikli-araclarda-sarj-altyapisi-rekabeti-hizlandi/'],
  ['/api-servislerinde-hiz-ve-guvenilirlik-yarisi/', '/api-kullaniminda-hiz-ve-guvenilirlik-neden-onemli/'],
  ['/ai-destekli-arama-motorlari-daha-dogal-cevap-veriyor/', '/yapay-zeka-destekli-arama-motorlari-klasik-aramayi-zorluyor/'],
  ['/yeni-film-ve-dizi-haberleri-tek-sayfada-toplandi/', '/yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor/'],
  ['/bilim-kurgu-filmi-icin-ilk-fragman-yayinlandi/', '/bilim-kurgu-filmi-ilk-fragmaniyla-dikkat-cekti/'],
  ['/yerli-girisimlerden-yapay-zeka-destekli-yeni-cozumler/', '/yerli-girisimler-yapay-zeka-destekli-cozumler-gelistiriyor/'],
  ['/video-uretme-modellerinde-kalite-yarisi-hizlandi/', '/video-uretme-yapay-zekalari-icerik-ureticilerin-radarinda/'],
  ['/sosyal-medya-uygulamalarinda-yeni-guvenlik-ozellikleri/', '/sosyal-medya-uygulamalarinda-guvenlik-ozellikleri-artiyor/'],
  ['/mobil-uygulama-gelistirmede-yeni-performans-donemi/', '/mobil-uygulama-gelistirmede-performans-odakli-yeni-yaklasimlar/'],
  ['/kucuk-isletmeler-otomasyon-araclarini-benimsiyor/', '/kucuk-isletmeler-yapay-zeka-ile-otomasyon-firsatlarini-arastiriyor/'],
  ['/kablosuz-kulakliklarda-yapay-zeka-destekli-ses-modu/', '/kablosuz-kulakliklarda-gurultu-engelleme-ozellikleri-gelisiyor/'],
  ['/giyilebilir-teknolojiler-saglik-takibini-gelistiriyor/', '/giyilebilir-teknolojiler-saglik-takibinde-daha-iddiali/'],
  ['/ev-internetinde-yeni-hiz-paketleri-gundemde/', '/ev-internetinde-hiz-ve-gecikme-degerleri-daha-fazla-onem-kazaniyor/'],
  ['/dijital-servislerde-abonelik-fiyatlari-yeniden-gundemde/', '/dijital-servislerde-yeni-abonelik-paketleri-gundemde/'],
  ['/bulut-tabanli-ofis-araclari-daha-akilli-hale-geliyor/', '/bulut-tabanli-calisma-araclari-ekiplerin-is-akisini-degistiriyor/'],
  ['/bulut-depolama-servislerinde-yeni-kapasite-paketleri/', '/bulut-depolama-servisleri-kapasite-paketlerini-guncelliyor/'],
  ['/belgesel-turunde-haftanin-dikkat-ceken-onerileri/', '/belgesel-onerileri-teknoloji-ve-doga-meraklilarini-hedefliyor/'],
  ['/akilli-ev-urunlerinde-uyumluluk-sorunu-azaliyor/', '/akilli-ev-cihazlari-daha-uyumlu-hale-geliyor/'],
  ['/google-i-o-2026-gelistiriciler-icin-ajan-odakli-yeni-donemi-one-cikardi/', '/google-i-o-2026-gelistirici-oturumlarinda-yapay-zeka-araclari-one-cikti/'],
  ['/android-haziran-guncellemesi-kisilestirme-ve-guvenlik-ozelliklerini-genisletti/', '/android-haziran-drop-guvenlik-ve-kisisellestirme-ozelliklerini-buyuttu/'],
]);

const DYNAMIC_HEAD = `
<style id="acartechs-dynamic-css">
.acartechs-live-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 0 rgba(34,197,94,.7);animation:acarPulse 1.6s infinite;margin-right:8px;vertical-align:middle}
@keyframes acarPulse{0%{box-shadow:0 0 0 0 rgba(34,197,94,.55)}70%{box-shadow:0 0 0 10px rgba(34,197,94,0)}100%{box-shadow:0 0 0 0 rgba(34,197,94,0)}}
.acartechs-live-strip strong{gap:6px}
.acartechs-now-badge{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(135deg,#0f172a,#1e3a5f);color:#e2e8f0;border-radius:999px;font-size:12px;font-weight:700;padding:6px 12px;letter-spacing:.02em}
.acartechs-now-badge time{color:#7dd3fc;font-variant-numeric:tabular-nums}
.acartechs-read-progress{position:fixed;top:0;left:0;height:3px;width:0;z-index:99999;background:linear-gradient(90deg,#2188f6,#26c9f4);box-shadow:0 0 12px rgba(33,136,246,.55);transition:width .08s linear}
.acartechs-news-feed article a,.acartechs-trending-list a,.acartechs-feature-slide a{transition:transform .25s ease,box-shadow .25s ease}
.acartechs-news-feed article:hover a,.acartechs-trending-list a:hover{transform:translateY(-2px)}
.acartechs-fresh-pill{display:none!important}
.acartechs-topbar,.acartechs-nav,.acartechs-nav-list .sub-menu{position:relative;z-index:40}
.acartechs-nav-list .sub-menu{z-index:60!important}
.acartechs-login-modal,.acartechs-modal-card{z-index:10050!important}
.acartechs-arcade-banner,.acartechs-arcade-thumb,.acartechs-arcade-banner-cta{position:relative;z-index:8}
.acartechs-adsense-shell{position:relative!important;z-index:1!important;clear:both;margin:28px 0}
.acartechs-adsense-shell.is-ad-empty,.acartechs-adsense-shell.is-ad-checking{display:none!important;min-height:0!important;margin:0!important}
.acartechs-adsense-shell:not(.is-ad-filled) .acartechs-adsense-unit{background:transparent!important;border:0!important}
.acartechs-adsense-shell:not(.is-ad-filled) .acartechs-adsense-unit:before,.acartechs-adsense-shell:not(.is-ad-filled) .acartechs-adsense-unit:after{content:none!important;display:none!important}
.acartechs-adsense-shell .adsbygoogle{position:relative;z-index:1}
body.acar-ready .acartechs-home{animation:acarFade .45s ease}
@keyframes acarFade{from{opacity:.001;transform:translateY(4px)}to{opacity:1;transform:none}}
.acartechs-back-top{position:fixed;right:18px;bottom:22px;z-index:9999;width:44px;height:44px;border:0;border-radius:999px;background:linear-gradient(135deg,#2188f6,#26c9f4);color:#fff;font-size:20px;cursor:pointer;box-shadow:0 10px 28px rgba(33,136,246,.35);opacity:0;pointer-events:none;transition:opacity .2s,transform .2s}
.acartechs-back-top.is-on{opacity:1;pointer-events:auto}
.acartechs-back-top:hover{transform:translateY(-2px)}
@media (prefers-reduced-motion:reduce){
  .acartechs-live-track,.acartechs-feature-track,.acartechs-live-dot,body.acar-ready .acartechs-home{animation:none!important}
}
</style>
`;

const DYNAMIC_BODY = `
<script id="acartechs-dynamic-js">
(function(){
  if (window.__acarDynamic) return;
  window.__acarDynamic = true;

  function ready(fn){
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn);
    else fn();
  }

  function relTime(iso){
    var d = new Date(iso + 'T12:00:00');
    if (isNaN(d.getTime())) return null;
    var now = Date.now();
    var diff = Math.round((now - d.getTime()) / 1000);
    if (diff < 0) diff = 0;
    if (diff < 90) return 'az önce';
    if (diff < 3600) return Math.floor(diff/60) + ' dk önce';
    if (diff < 86400) return Math.floor(diff/3600) + ' saat önce';
    if (diff < 86400*2) return 'dün';
    if (diff < 86400*7) return Math.floor(diff/86400) + ' gün önce';
    if (diff < 86400*30) return Math.floor(diff/86400/7) + ' hafta önce';
    return null;
  }

  function enhanceDates(){
    document.querySelectorAll('time[data-acar-date], time[datetime]').forEach(function(el){
      var iso = el.getAttribute('datetime');
      if (!iso) return;
      var r = relTime(iso);
      if (!r) return;
      if (!el.dataset.original) el.dataset.original = el.textContent.trim();
      el.textContent = r;
      el.title = el.dataset.original;
    });
    document.querySelectorAll('.acartechs-fresh-pill').forEach(function(el){ el.remove(); });
  }

  function liveDot(){
    var strong = document.querySelector('.acartechs-live-strip strong');
    if (!strong || strong.querySelector('.acartechs-live-dot')) return;
    var dot = document.createElement('span');
    dot.className = 'acartechs-live-dot';
    dot.setAttribute('aria-hidden', 'true');
    strong.prepend(dot);
  }

  function nowBadge(){
    if (document.querySelector('.acartechs-now-badge')) return;
    var top = document.querySelector('.acartechs-topbar .acartechs-actions') || document.querySelector('.acartechs-topbar');
    if (!top) return;
    var badge = document.createElement('div');
    badge.className = 'acartechs-now-badge';
    badge.innerHTML = '<span>Canlı</span> <time id="acar-now-clock"></time>';
    top.prepend(badge);
    function tick(){
      var el = document.getElementById('acar-now-clock');
      if (!el) return;
      el.textContent = new Date().toLocaleString('tr-TR', {
        weekday: 'short', day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit'
      });
    }
    tick();
    setInterval(tick, 30000);
  }

  function readingProgress(){
    if (document.querySelector('.acartechs-read-progress')) return;
    var bar = document.createElement('div');
    bar.className = 'acartechs-read-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    function onScroll(){
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var p = max > 0 ? (h.scrollTop / max) * 100 : 0;
      bar.style.width = p + '%';
    }
    window.addEventListener('scroll', onScroll, {passive:true});
    onScroll();
  }

  function backTop(){
    if (document.querySelector('.acartechs-back-top')) return;
    var btn = document.createElement('button');
    btn.className = 'acartechs-back-top';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Yukarı çık');
    btn.textContent = '↑';
    btn.addEventListener('click', function(){ window.scrollTo({top:0, behavior:'smooth'}); });
    document.body.appendChild(btn);
    window.addEventListener('scroll', function(){
      btn.classList.toggle('is-on', window.scrollY > 480);
    }, {passive:true});
  }

  function markEmptyAds(){
    document.querySelectorAll('.acartechs-adsense-shell').forEach(function(shell){
      var unit = shell.querySelector('.adsbygoogle');
      if (!unit) return;
      var status = unit.getAttribute('data-ad-status');
      var hasFrame = !!shell.querySelector('iframe');
      if (status === 'filled' || hasFrame) {
        shell.classList.remove('is-ad-empty', 'is-ad-checking');
        shell.classList.add('is-ad-filled');
        return;
      }
      if (status === 'unfilled' || (!hasFrame && unit.childElementCount === 0)) {
        shell.classList.remove('is-ad-filled', 'is-ad-checking');
        shell.classList.add('is-ad-empty');
      }
    });
  }

  function humanBylines(){
    document.querySelectorAll('body').forEach(function(){});
    // leftover admin strings
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function(n){
      if (n.nodeValue && /acaradmin/i.test(n.nodeValue)) {
        n.nodeValue = n.nodeValue.replace(/acaradmin/gi, 'Acartechs Editör');
      }
    });
  }

  function pauseMarqueeOnFocus(){
    document.querySelectorAll('.acartechs-live-marquee a').forEach(function(a){
      a.addEventListener('focus', function(){
        var track = document.querySelector('.acartechs-live-track');
        if (track) track.style.animationPlayState = 'paused';
      });
      a.addEventListener('blur', function(){
        var track = document.querySelector('.acartechs-live-track');
        if (track) track.style.animationPlayState = '';
      });
    });
  }

  ready(function(){
    document.body.classList.add('acar-ready');
    humanBylines();
    enhanceDates();
    liveDot();
    nowBadge();
    readingProgress();
    backTop();
    pauseMarqueeOnFocus();
    window.setTimeout(markEmptyAds, 4000);
    window.setTimeout(markEmptyAds, 9000);
  });
})();
</script>
`;

function normalizePath(pathname) {
  if (!pathname || pathname === '/') {
    return '/';
  }
  return pathname.endsWith('/') ? pathname : `${pathname}/`;
}

function redirectForPath(pathname) {
  const normalized = normalizePath(pathname);
  if (normalized === '/feed/' || normalized === '/comments/feed/') {
    return '/haberler/';
  }
  if (normalized.startsWith('/wp-json/') || normalized === '/wp-json/' || pathname === '/xmlrpc.php') {
    return '/';
  }
  if (normalized.startsWith('/wp-admin/')) {
    return '/';
  }
  if (normalized.startsWith('/tag/')) {
    return '/haberler/';
  }
  if (normalized.startsWith('/author/')) {
    return '/';
  }
  return REDIRECTS.get(normalized) || null;
}

function withSearchNoindex(html) {
  if (html.includes('noindex')) {
    return html;
  }
  return html.replace('<head>', "<head>\n<meta name='robots' content='noindex, follow' />");
}

function withCorporateNav(html) {
  if (html.includes('href="/kunye/"')) {
    return html;
  }
  return html.replaceAll(
    '<li><a href="/hakkimizda/">Hakkımızda</a></li>',
    '<li><a href="/hakkimizda/">Hakkımızda</a></li>\n\t\t\t\t\t<li><a href="/kunye/">Künye</a></li>\n\t\t\t\t\t<li><a href="/yayin-ilkeleri/">Yayın İlkeleri</a></li>'
  );
}

function withPolicyStylesheet(html) {
  if (html.includes('acartechs-publisher-policy.css')) {
    return html;
  }
  const tag = '<link rel="stylesheet" href="/assets/acartechs-publisher-policy.css">\n';
  if (html.includes('</head>')) {
    return html.replace('</head>', `${tag}</head>`);
  }
  return html;
}

function withDynamicPolish(html) {
  if (html.includes('id="acartechs-dynamic-js"')) {
    return withCorporateNav(withPolicyStylesheet(html));
  }
  let out = html;
  if (out.includes('</head>')) {
    out = out.replace('</head>', `${DYNAMIC_HEAD}\n</head>`);
  }
  if (out.includes('</body>')) {
    const bodyClose = out.lastIndexOf('</body>');
    out = out.slice(0, bodyClose) + `${DYNAMIC_BODY}
` + out.slice(bodyClose);
  }
  out = out.replace(/acaradmin/gi, 'Acartechs Editör');
  return withCorporateNav(withPolicyStylesheet(out));
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === '/data/live-feed.json' || url.pathname === '/data/live-feed.json/') {
      const asset = await env.ASSETS.fetch(request);
      const headers = new Headers(asset.headers);
      headers.set('cache-control', 'public, max-age=60, stale-while-revalidate=120');
      headers.set('content-type', 'application/json; charset=utf-8');
      headers.set('access-control-allow-origin', '*');
      return new Response(asset.body, { status: asset.status, headers });
    }


    if (url.protocol === 'http:' || url.hostname === 'www.acartechs.com') {
      url.protocol = 'https:';
      url.hostname = 'acartechs.com';
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname === '/ads.txt' || url.pathname === '/ads.txt/') {
      return new Response('google.com, pub-4367344438750629, DIRECT, f08c47fec0942fa0\n', {
        headers: {
          'content-type': 'text/plain; charset=utf-8',
          'cache-control': 'public, max-age=300',
        },
      });
    }

    if (url.pathname === '/robots.txt') {
      return new Response(ROBOTS, {
        headers: {
          'content-type': 'text/plain; charset=utf-8',
          'cache-control': 'public, max-age=300',
        },
      });
    }

    if (url.pathname === '/llms.txt') {
      return new Response(LLMS, {
        headers: {
          'content-type': 'text/plain; charset=utf-8',
          'cache-control': 'public, max-age=300',
        },
      });
    }

    const redirectTarget = redirectForPath(url.pathname);
    if (redirectTarget) {
      return Response.redirect(new URL(redirectTarget, url).toString(), 301);
    }

    const response = await env.ASSETS.fetch(request);
    const contentType = response.headers.get('content-type') || '';
    if (!contentType.includes('text/html') || response.status >= 400) {
      return response;
    }

    let html = await response.text();
    if (url.searchParams.has('s') && url.searchParams.get('s')) {
      html = withSearchNoindex(html);
    }
    html = withDynamicPolish(html);

    const headers = new Headers(response.headers);
    headers.set('content-type', 'text/html; charset=utf-8');
    headers.set('cache-control', 'public, max-age=120, stale-while-revalidate=600');
    return new Response(html, {
      status: response.status,
      statusText: response.statusText,
      headers,
    });
  },
};
