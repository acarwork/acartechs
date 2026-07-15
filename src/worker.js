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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

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
    if (!url.searchParams.has('s') || !url.searchParams.get('s')) {
      return response;
    }

    const contentType = response.headers.get('content-type') || '';
    if (!contentType.includes('text/html') || response.status !== 200) {
      return response;
    }

    const html = withSearchNoindex(await response.text());
    const headers = new Headers(response.headers);
    headers.set('content-type', 'text/html; charset=utf-8');
    return new Response(html, {
      status: response.status,
      statusText: response.statusText,
      headers,
    });
  },
};
