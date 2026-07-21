# Scripts

## `export_live_feed.py`

Scans `public/<slug>/index.html` article pages and writes:

`public/data/live-feed.json`

Used by the homepage live feed + son dakika strip.

### Local

```bash
npm run export:live-feed
# or
python scripts/export_live_feed.py
# or
pwsh scripts/export-live-feed.ps1
```

### Auto

- **GitHub Actions** (`.github/workflows/export-live-feed.yml`): runs when article HTML under `public/` changes on `main`, commits refreshed JSON.
- **Deploy workflow**: regenerates feed before Cloudflare deploy.
- **`npm run deploy`**: `predeploy` regenerates feed first.

### Breaking / son dakika

An item is `breaking: true` when:

1. Page HTML has `data-breaking="true"` (or similar marker), or  
2. Publish time is within the last **12 hours**.

Max 3 breaking items are kept.
