const ROBOTS = `User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

User-agent: Google-Extended
Allow: /

Sitemap: https://acartechs.com/wp-sitemap.xml
`;

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

    return env.ASSETS.fetch(request);
  },
};
