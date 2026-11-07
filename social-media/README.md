# Social Media Assets

Source files for Black Women Rising's Instagram/Threads graphics. This exists so this
library survives container resets, unlike a scratchpad directory — everything here is
committed to git, not temporary.

## Structure

- `templates/*.html` — one self-contained HTML file per graphic. Each is a static page
  sized to its target canvas (1080x1350 for feed posts, 1080x1920 for Stories/Reels).
  Open any of these in a browser to see the design; edit and re-render to update it.
- `templates/fonts/` — Fraunces + Inter woff2 files the templates `@font-face` in.
- `templates/photos/` — source photos the templates reference (official/public-domain
  portraits, screenshots used as repost material, brand photography).
- `templates/gen_carousel.py` — generates the 6-slide "Historic Night" carousel HTML
  files from one template; run it after editing the data inside the script.
- `output/` — final rendered PNGs, one per template, already cropped to their target
  canvas size.

## Brand system (for new graphics)

Colors: `--forest:#20301F; --forest-dark:#141E13; --forest-soft:#2B3F29;
--cream:#F5F1E6; --cream-dim:#EDE6D4; --blush:#DDBBAE; --gold:#C7C05E;
--oxblood:#5C2331;`. Fonts: Fraunces (display/serif) + Inter (body/sans).

Per `/CLAUDE.md` at the repo root: any event/talk/panel flyer must carry visible BWR
branding and the bold-poster structure (color-block shapes, gold-bordered photo frame
or band, stacked info bands) — vary colors/shapes for "a different design," don't drop
the structure.

## Re-rendering a template to PNG

Templates are rendered with headless Chromium, over-height then cropped (Chrome's
exact-height screenshot has a truncation bug):

```bash
CHROME=/opt/pw-browsers/chromium   # or wherever Chromium is installed
cd templates
"$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --screenshot="/tmp/out-raw.png" --window-size=1080,1700 \
  --virtual-time-budget=3000 "file://$(pwd)/<name>.html"
python3 -c "
from PIL import Image
Image.open('/tmp/out-raw.png').crop((0,0,1080,1350)).save('../output/<name>.png')
"
```

Use `--window-size=1080,2200` and crop to `(0,0,1080,1920)` for Story-format templates.

## Photo rights

Every photo of a named public figure in `templates/photos/` was checked for a usable
license before use (public domain government work, CC0, or CC-BY with credit) — see the
commit history / conversation for sourcing notes on each. Don't add a press/editorial
photo of a public figure without checking its license first; several were rejected for
exactly that reason (see `thread-*` templates, which repost screenshots instead of
lifting a photo directly).
