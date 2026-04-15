# ColourPop × Reacher Plus — Case Study Slides

Animated 10-slide HTML deck for client presentations. Single self-contained `index.html` with all assets embedded as base64.

## Local preview

```bash
python3 -m http.server 4321
# open http://127.0.0.1:4321
```

## Rebuild

After updating `assets/` or content in `build.py`, regenerate `index.html`:

```bash
python3 build.py
```

## Slide structure

| # | Slide | Theme |
|---|-------|-------|
| 1 | Hero | dark |
| 2 | Brand | light |
| 3 | Impact (animated counters) | dark |
| 4 | Problem headline | dark |
| 5 | Pain cards (3×2) | dark |
| 6 | Solution 01 — Real-Time Dashboard | dark |
| 7 | Solution 02 — Hero Product Targeting | light |
| 8 | Solution 03 — Campaign Planning | dark |
| 9 | Solution 04 — Same-Day Pivots | light |
| 10 | CTA | dark |

## Navigation

- Mouse wheel / trackpad scroll
- ↑/↓ arrows, PageUp/PageDown, Space
- Right-side dot navigation
- Home/End to jump to first/last slide

## Tech

- Pure HTML + CSS + vanilla JS
- 1920×1200 design baseline scaled via CSS `transform`
- IntersectionObserver for reveal animations
- `requestAnimationFrame` for counter animations
- Self-contained: all images base64-embedded
