# Refresh public/data/live-feed.json from published article pages.
# Run after adding/updating a news page under public/<slug>/
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
python "$Root\scripts\export_live_feed.py" @args
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Done. Commit public/data/live-feed.json when ready."
