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

Icerikler kullanicilara teknoloji haberlerini ve resmi duyurulari ozetlemek icin hazirlanir. Kaynak gostererek kisa alinti ve baglamsal ozetleme yapilabilir.
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
  ['/populer-dizinin-yeni-sezon-tarihi-aciklandi-2/', '/populer-dizinin-yeni-sezon-tarihi-aciklandi/'],
  ['/teknoloji-dunyasinda-bugun-one-cikan-her-seyi-anlattik-2/', '/teknoloji-dunyasinda-bugun-one-cikan-her-seyi-anlattik/'],
  ['/yayin-platformlari-yaz-takvimini-guncelledi-2/', '/yayin-platformlari-yaz-takvimini-guncelledi/'],
  ['/yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-goruntuleri-paylasildi/', '/yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-videosu-geldi/'],
  ['/yeni-film-ve-dizi-haberleri-tek-sayfada-toplandi-2/', '/yeni-film-ve-dizi-haberleri-tek-sayfada-toplandi/'],
  ['/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-geliyor/', '/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor/'],
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
.acartechs-adsense-shell.is-ad-empty,.acartechs-adsense-shell.is-ad-checking{display:block!important}
.acartechs-adsense-shell.is-ad-empty .acartechs-adsense-unit,.acartechs-adsense-shell.is-ad-checking .acartechs-adsense-unit{background:linear-gradient(120deg,#061b31 0%,#0a477a 48%,#2188f6 78%,#26c9f4 100%)!important;border:1px dashed rgba(255,255,255,.44)!important;border-radius:8px!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08);position:relative}
.acartechs-adsense-shell.is-ad-empty .acartechs-adsense-unit:before,.acartechs-adsense-shell.is-ad-checking .acartechs-adsense-unit:before{background:repeating-linear-gradient(90deg,rgba(255,255,255,.18) 0 2px,transparent 2px 34px);content:"";inset:0;opacity:.38;position:absolute;z-index:0}
.acartechs-adsense-shell.is-ad-empty .acartechs-adsense-unit:after,.acartechs-adsense-shell.is-ad-checking .acartechs-adsense-unit:after{align-items:center;color:#fff;content:"ACARTECHS REKLAM ALANI";display:flex;font-size:clamp(18px,2vw,28px);font-weight:900;inset:0;justify-content:center;letter-spacing:.02em;position:absolute;text-align:center;text-shadow:0 8px 22px rgba(2,6,23,.35);z-index:1}
.acartechs-adsense-shell.placement-sidebar.is-ad-empty .acartechs-adsense-unit:after,.acartechs-adsense-shell.placement-sidebar.is-ad-checking .acartechs-adsense-unit:after{content:"ACARTECHS\\A REKLAM ALANI";font-size:24px;line-height:1.18;white-space:pre-line}
.acartechs-adsense-shell.is-ad-filled .acartechs-adsense-unit:before,.acartechs-adsense-shell.is-ad-filled .acartechs-adsense-unit:after{display:none!important}
.acartechs-adsense-shell .adsbygoogle{position:relative;z-index:2}
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
      if (status === 'unfilled' || unit.childElementCount === 0) {
        shell.classList.remove('is-ad-filled');
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

function withDynamicPolish(html) {
  if (html.includes('id="acartechs-dynamic-js"')) {
    return html;
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
  // Soft human byline fallback in HTML source
  out = out.replace(/acaradmin/gi, 'Acartechs Editör');
  return out;
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
