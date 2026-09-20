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
]);

function normalizePath(pathname) {
  if (!pathname || pathname === '/') {
    return '/';
  }
  return pathname.endsWith('/') ? pathname : `${pathname}/`;
}

function redirectForPath(pathname) {
  const normalized = normalizePath(pathname);
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

function withAdReviewCleanup(html) {
  if (html.includes('acartechs-ad-review-cleanup')) {
    return html;
  }

  const style = `<style id="acartechs-ad-review-cleanup">
.acartechs-topbar,.acartechs-nav,.acartechs-nav-list .sub-menu{position:relative;z-index:40}
.acartechs-nav-list .sub-menu{z-index:60!important}
.acartechs-login-modal,.acartechs-modal-card{z-index:10050!important}
.acartechs-arcade-banner,.acartechs-arcade-thumb{position:relative;z-index:8}
.acartechs-adsense-shell{position:relative!important;z-index:1!important;clear:both}
.acartechs-adsense-shell.is-ad-empty,.acartechs-adsense-shell.is-ad-checking{display:none!important;min-height:0!important;margin:0!important}
.acartechs-adsense-shell:not(.is-ad-filled) .acartechs-adsense-unit:before,.acartechs-adsense-shell:not(.is-ad-filled) .acartechs-adsense-unit:after{content:none!important;display:none!important}
.acartechs-adsense-shell .adsbygoogle{position:relative;z-index:1}
</style>
<link rel="stylesheet" href="/assets/acartechs-publisher-policy.css">`;

  const script = `<script id="acartechs-ad-review-cleanup-script">
(function(){
  function markEmptyAds(){
    document.querySelectorAll('.acartechs-adsense-shell').forEach(function(shell){
      var unit=shell.querySelector('.adsbygoogle');
      if(!unit){return;}
      var status=unit.getAttribute('data-ad-status');
      var hasFrame=!!shell.querySelector('iframe');
      if(status==='filled'||hasFrame){shell.classList.remove('is-ad-empty','is-ad-checking');shell.classList.add('is-ad-filled');return;}
      if(status==='unfilled'||unit.childElementCount===0){shell.classList.remove('is-ad-filled');shell.classList.add('is-ad-empty');}
    });
  }
  window.addEventListener('load',function(){
    window.setTimeout(markEmptyAds,4500);
    window.setTimeout(markEmptyAds,9000);
  });
})();
</script>`;

  const withHead = html.includes('</head>') ? html.replace('</head>', `${style}
</head>`) : html;
  const bodyClose = withHead.lastIndexOf('</body>');
  if (bodyClose === -1) return withHead;
  return withHead.slice(0, bodyClose) + `${script}
` + withHead.slice(bodyClose);
}

export async function onRequest(context) {
  const url = new URL(context.request.url);

  if (url.protocol === 'http:' || url.hostname === 'www.acartechs.com') {
    url.protocol = 'https:';
    url.hostname = 'acartechs.com';
    return Response.redirect(url.toString(), 301);
  }

  const redirectTarget = redirectForPath(url.pathname);
  if (redirectTarget) {
    return Response.redirect(new URL(redirectTarget, url).toString(), 301);
  }

  const response = await context.next();

  const contentType = response.headers.get('content-type') || '';
  if (!contentType.includes('text/html') || response.status !== 200) {
    return response;
  }

  let html = await response.text();
  if (url.searchParams.has('s') && url.searchParams.get('s')) {
    html = withSearchNoindex(html);
  }
  html = withAdReviewCleanup(html);

  const headers = new Headers(response.headers);
  headers.set('content-type', 'text/html; charset=utf-8');
  return new Response(html, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}
