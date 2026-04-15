#!/usr/bin/env python3
"""Build the ColourPop × Reacher Plus animated 10-slide deck.
Pixel-perfect 1920×1200 stages scaled via CSS transform to fit the viewport.
"""
import base64
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"


def embed(path):
    p = ASSETS / path
    data = p.read_bytes()
    mime = "image/jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else "image/png"
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


IMG = {
    "logo_cp":  embed("hq-logo-cp.png"),
    "logo_r":   embed("hq-logo-r.png"),

    "brand_1_flatlay":     embed("hq-brand-1-flatlay.jpg"),
    "brand_2_rockon":      embed("hq-brand-2-rockon.jpg"),
    "brand_3_eyeshadow":   embed("hq-brand-3-eyeshadow.jpg"),
    "brand_4_sojuicy":     embed("hq-brand-4-sojuicy.jpg"),
    "brand_5_skinjuice":   embed("hq-brand-5-skinjuice.jpg"),
    "brand_6_freshkiss":   embed("hq-brand-6-freshkiss.jpg"),
    "brand_7_goldenstate": embed("hq-brand-7-goldenstate.jpg"),

    "sol1_dash":    embed("hq-sol1-dashboard.png"),
    "sol2_sojuicy":     embed("hq-sol2-sojuicy.jpg"),
    "sol2_rockon":      embed("hq-sol2-rockon.jpg"),
    "sol2_freshkiss":   embed("hq-sol2-freshkiss.jpg"),
    "sol2_goldenstate": embed("hq-sol2-goldenstate.jpg"),
    "sol3_campaign": embed("hq-sol3-campaign-new.png"),
    "sol4_slack":   embed("hq-sol4-slack.png"),
    "qr":           embed("qr-reacher.png"),
}

# Shared background (dark slides) — stronger gradient to match Figma
DARK_BG = (
    "radial-gradient(ellipse 1900px 1358px at 576px 960px, rgba(59,130,246,0.15) 0%, rgba(59,130,246,0) 50%),"
    "radial-gradient(ellipse 1900px 1358px at 1344px 240px, rgba(34,211,238,0.12) 0%, rgba(34,211,238,0) 50%),"
    "linear-gradient(180deg, #060F1F 0%, #0A1628 40%, #0D1E3A 100%)"
)
# Slides with flat navy base + radial overlays (slides 3, 4, 5, 6a, 6c)
DARK_FLAT_BG = (
    "radial-gradient(ellipse 1900px 1358px at 576px 960px, rgba(59,130,246,0.06) 0%, rgba(59,130,246,0) 50%),"
    "radial-gradient(ellipse 1900px 1358px at 1344px 240px, rgba(34,211,238,0.08) 0%, rgba(34,211,238,0) 50%),"
    "#0A1628"
)
# CTA background — deeper bottom-up gradient
CTA_BG = (
    "radial-gradient(ellipse 1900px 1358px at 576px 960px, rgba(59,130,246,0.06) 0%, rgba(59,130,246,0) 50%),"
    "radial-gradient(ellipse 1900px 1358px at 1344px 240px, rgba(34,211,238,0.08) 0%, rgba(34,211,238,0) 50%),"
    "radial-gradient(ellipse 1358px 1019px at 960px 720px, rgba(59,130,246,0.05) 0%, rgba(59,130,246,0) 50%),"
    "radial-gradient(ellipse 2172px 1527px at 1536px 1080px, rgba(34,211,238,0.03) 0%, rgba(34,211,238,0) 50%),"
    "linear-gradient(180deg, #0D1E3A 0%, #0A1628 50%, #060F1F 100%)"
)


def nav(theme="dark"):
    meta_color = "#838EA0" if theme == "dark" else "rgba(0,0,0,0.4)"
    return f"""
    <div class="stage-nav">
      <div class="cobrand-top">COLOURPOP <span class="x">×</span> REACHER PLUS</div>
      <div class="meta" style="color:{meta_color};">CASE STUDY · 2026</div>
    </div>
    """


# Tabler-style SVG icons for the 6 pain cards
ICON_SVGS = {
    "box-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 5v8l-9 5-9-5v-8l9-5z"/><path d="M3 8l9 5 9-5"/><path d="M3 3l18 18"/></svg>',
    "eye-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M10.585 10.587a2 2 0 0 0 2.829 2.828"/><path d="M16.681 16.673a8.717 8.717 0 0 1-4.681 1.327c-3.6 0-6.6-2-9-6 1.272-2.12 2.712-3.678 4.32-4.674m2.86-1.146a9.055 9.055 0 0 1 1.82-.18c3.6 0 6.6 2 9 6-.666 1.11-1.379 2.067-2.138 2.87"/><path d="M3 3l18 18"/></svg>',
    "database-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12.983 8.978c4.416-.176 7.87-1.286 8.016-2.484l.001-.027v-.001c-.002-1.43-4.023-2.6-9-2.6-1.935 0-3.758.222-5.27.588M3 6.25c.146 1.198 3.6 2.308 8.016 2.484"/><path d="M3 6.25v5.75c0 1.598 3.599 3 8.011 3c.056 0 .112 0 .168 0M21 12v-5.75"/><path d="M3 12v6c0 1.598 3.599 3 8 3c.056 0 .112 0 .168 0M21 12v1"/><path d="M3 3l18 18"/></svg>',
    "clipboard-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M17 17v2a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-12a2 2 0 0 1 2-2h2M9 5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2M9 5v1h6V5"/><path d="M3 3l18 18"/></svg>',
    "user-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8.18 8.189a4 4 0 0 0 5.626 5.631m1.447-2.692a4 4 0 0 0-4.389-4.382"/><path d="M6 21v-2a4 4 0 0 1 4-4h4c.348 0 .686.044 1.008.128M20 20.88C19.8 21.58 19.16 22 18.5 22M3 3l18 18"/></svg>',
    "pennant-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M10 21v-7M10 7V3h11l-4 4 4 4H11M10 11v-1"/><path d="M3 3l18 18"/></svg>',
}


HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>ColourPop × Reacher Plus — Case Study</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
:root {{
  --stage-scale: 1;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

html, body {{
  height: 100%;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overflow-y: scroll;
  overflow-x: hidden;
  background: #000;
  font-family: 'Inter', -apple-system, 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #F6F8FD;
}}
body::-webkit-scrollbar {{ display: none; }}

/* ===== Slide = viewport window; Stage = fixed 1920x1200 inside, scaled ===== */
.slide {{
  width: 100vw;
  height: 100vh; height: 100dvh;
  overflow: hidden;
  scroll-snap-align: start;
  position: relative;
  display: flex; align-items: center; justify-content: center;
}}
.slide.dark-bg      {{ background: {DARK_BG}; }}
.slide.dark-flat-bg {{ background: {DARK_FLAT_BG}; }}
.slide.cta-bg       {{ background: {CTA_BG}; }}
.slide.light-bg     {{ background: #F5F5F7; }}

.stage {{
  width: 1920px;
  height: 1080px;
  position: relative;
  transform-origin: center center;
  transform: scale(var(--stage-scale));
  flex-shrink: 0;
}}
/* Absolute positioning helpers — everything inside stage uses px */
.abs {{ position: absolute; }}

/* ===== Top nav strip (inside stage) ===== */
.stage-nav {{
  position: absolute;
  top: 52px; left: 76px; right: 76px;
  height: 15px;
  display: flex; align-items: center; justify-content: space-between;
  z-index: 3;
}}
.cobrand-top {{
  font-weight: 700;
  font-size: 20px;
  letter-spacing: 2.64px;
  color: #3583E9;
  text-transform: uppercase;
}}
.cobrand-top .x {{ opacity: 0.55; margin: 0 4px; }}
.stage-nav .meta {{
  font-size: 20px;
  letter-spacing: 1.2px;
  text-transform: uppercase;
  color: #838EA0;
}}

/* ===== Brand gradient text ===== */
.grad-blue {{
  background: linear-gradient(90deg, #22D3EE 0%, #0FAEFB 19.7%, #189AFC 39.4%, #325FFE 61.5%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}
.grad-blue-alt {{
  background: linear-gradient(119.37deg, #06C3FA 20.5%, #325FFE 101.2%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}
.grad-pill {{
  background: linear-gradient(141.17deg, #22D3EE 20.5%, #325FFE 121.5%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}
.grad-warm {{
  background: linear-gradient(137.5deg, #FFCACE 43.3%, #D0AAE7 58.7%, #A58DFF 67.3%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}

/* ===== Reveal animations ===== */
.reveal {{
  opacity: 0; transform: translateY(28px);
  transition: opacity 0.8s cubic-bezier(0.16,1,0.3,1),
              transform 0.8s cubic-bezier(0.16,1,0.3,1);
}}
.reveal-scale {{
  opacity: 0; transform: scale(0.95);
  transition: opacity 0.9s cubic-bezier(0.16,1,0.3,1),
              transform 0.9s cubic-bezier(0.16,1,0.3,1);
}}
.reveal-left {{
  opacity: 0; transform: translateX(-50px);
  transition: opacity 0.85s cubic-bezier(0.16,1,0.3,1),
              transform 0.85s cubic-bezier(0.16,1,0.3,1);
}}
.reveal-right {{
  opacity: 0; transform: translateX(50px);
  transition: opacity 0.85s cubic-bezier(0.16,1,0.3,1),
              transform 0.85s cubic-bezier(0.16,1,0.3,1);
}}
.reveal-blur {{
  opacity: 0; filter: blur(20px); transform: scale(1.04);
  transition: opacity 0.9s cubic-bezier(0.16,1,0.3,1),
              filter 0.9s cubic-bezier(0.16,1,0.3,1),
              transform 0.9s cubic-bezier(0.16,1,0.3,1);
}}
.slide.visible .reveal,
.slide.visible .reveal-scale,
.slide.visible .reveal-left,
.slide.visible .reveal-right,
.slide.visible .reveal-blur {{
  opacity: 1;
  transform: translate(0,0) scale(1);
  filter: blur(0);
}}
.slide.visible [data-d="1"] {{ transition-delay: 0.08s; }}
.slide.visible [data-d="2"] {{ transition-delay: 0.18s; }}
.slide.visible [data-d="3"] {{ transition-delay: 0.30s; }}
.slide.visible [data-d="4"] {{ transition-delay: 0.42s; }}
.slide.visible [data-d="5"] {{ transition-delay: 0.54s; }}
.slide.visible [data-d="6"] {{ transition-delay: 0.66s; }}
.slide.visible [data-d="7"] {{ transition-delay: 0.78s; }}

/* ===== Chrome: progress bar, dots, keyboard hint ===== */
.progress {{
  position: fixed; top: 0; left: 0;
  height: 2px; width: 0;
  background: linear-gradient(90deg, #22D3EE, #3583E9);
  box-shadow: 0 0 10px rgba(34,211,238,0.4);
  z-index: 60;
  transition: width 0.1s ease;
}}
.dots {{
  position: fixed; right: 24px; top: 50%;
  transform: translateY(-50%);
  z-index: 60;
  display: flex; flex-direction: column; gap: 12px;
}}
.dot {{
  width: 7px; height: 7px; border-radius: 50%;
  background: rgba(255,255,255,0.22);
  border: none; padding: 0; cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16,1,0.3,1);
}}
.dot.active {{
  background: #3583E9;
  transform: scale(1.4);
  box-shadow: 0 0 10px rgba(53,131,233,0.8);
}}
.kb-hint {{
  position: fixed; bottom: 24px; left: 50%;
  transform: translateX(-50%);
  z-index: 60;
  font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;
  color: rgba(255,255,255,0.38);
  display: flex; align-items: center; gap: 10px;
  transition: opacity 0.8s ease;
}}
.kb-hint.hidden {{ opacity: 0; pointer-events: none; }}
.kb-key {{
  display: inline-block;
  width: 20px; height: 20px; line-height: 18px;
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 4px; text-align: center; font-size: 11px;
}}

/* ================= SLIDE 1 — HERO ================= */
.s-hero .stage {{ display: flex; align-items: center; justify-content: center; }}
.s-hero .hero-stack {{
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  display: flex; flex-direction: column; align-items: center;
  gap: 60px;
}}
.hero-logos-block {{
  display: flex; flex-direction: column; align-items: center; gap: 36px;
}}
.hero-logos {{
  width: 342px;
  display: flex; align-items: center; justify-content: space-between;
}}
.hero-logo-tile {{
  width: 115px; height: 115px;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 12px 32px rgba(0,0,0,0.5);
}}
.hero-logo-tile.r {{ border-radius: 18px; }}
.hero-logo-tile img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
.hero-logos .x {{
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 50px;
  color: #2997FF;
  letter-spacing: 1.44px;
}}
.hero-cobrand {{
  display: flex; gap: 16px; align-items: center;
  font-weight: 700; font-size: 28px;
  letter-spacing: 1.44px;
  color: #FFFFFF;
  text-transform: uppercase;
}}
.hero-cobrand .x {{
  width: 17px;
  color: #FFFFFF;
  text-align: center;
}}
.hero-headline-block {{
  display: flex; flex-direction: column; align-items: center; gap: 72px;
}}
.s-hero h1 {{
  font-family: 'Instrument Serif', Georgia, serif;
  font-weight: 400;
  font-size: 120px;
  line-height: 140px;
  letter-spacing: -1.76px;
  color: #FFFFFF;
  width: 902px;
  text-align: center;
}}
.s-hero h1 em {{ font-style: italic; font-weight: 400; }}
.s-hero .pill {{
  display: inline-flex; align-items: center; gap: 12px;
  padding: 7px 21px 8px 21px;
  border: 1px solid rgba(34,211,238,0.6);
  border-radius: 980px;
  color: rgba(255,255,255,0.7);
  font-size: 20px; font-weight: 400;
}}
.s-hero .pill .dot-i {{
  width: 12px; height: 12px; border-radius: 50%;
  background: #22D3EE;
  animation: pulse 2s ease infinite;
  box-shadow: 0 0 12px rgba(34,211,238,0.6);
}}
@keyframes pulse {{
  0%, 100% {{ opacity: 1; transform: scale(1); }}
  50%      {{ opacity: 0.55; transform: scale(1.4); }}
}}

/* ================= SLIDE 2 — BRAND ================= */
.s-brand .brand-container {{
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  width: 1313px;
  display: flex; flex-direction: column; align-items: center;
  gap: 50px;
}}
.brand-heading {{
  display: flex; flex-direction: column; align-items: center; gap: 32px;
}}
.brand-eyebrow {{
  font-size: 20px; font-weight: 700;
  letter-spacing: 2.4px;
  text-transform: uppercase;
  color: rgba(0,0,0,0.4);
}}
.brand-title {{
  font-family: 'Instrument Serif', Georgia, serif;
  font-size: 84px; font-weight: 400;
  line-height: 60px;
  color: #1D1D1F;
  text-align: center;
}}
.brand-collage {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  width: 100%;
}}
.brand-collage .ph {{
  height: 284px;
  border-radius: 14px;
  overflow: hidden;
  background: #ddd;
}}
.brand-collage .ph.span2 {{ grid-column: span 2; }}
.brand-collage .ph img {{
  width: 100%; height: 100%;
  object-fit: cover; display: block;
}}
.brand-caption {{
  font-size: 24px; color: rgba(0,0,0,0.56);
  text-align: center; line-height: 1.4;
  white-space: nowrap;
}}

/* ================= SLIDE 3 — IMPACT ================= */
.s-impact .impact-container {{
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  display: flex; flex-direction: column;
  gap: 120px;
  align-items: center;
}}
.impact-heading-block {{
  display: flex; flex-direction: column; align-items: center; gap: 60px;
}}
.impact-pill {{
  display: inline-flex; align-items: center; justify-content: center;
  padding: 11px 25px 12px 25px;
  border: 1px solid rgba(34,211,238,0.2);
  background: rgba(34,211,238,0.08);
  border-radius: 980px;
  font-weight: 600; font-size: 20px;
}}
.impact-title {{
  font-family: 'Instrument Serif', Georgia, serif;
  font-weight: 400;
  font-size: 84px;
  line-height: 60px;
  color: #FFFFFF;
  text-align: center;
}}
.impact-grid {{
  width: 1230px;
  display: grid;
  grid-template-columns: 1fr 1fr 0.75fr;
  gap: 40px 60px;
}}
.impact-col {{
  display: flex; flex-direction: column; align-items: center; gap: 40px;
}}
.impact-num {{
  font-family: 'Inter', sans-serif;
  font-weight: 900;
  font-size: 90px;
  line-height: 67.38px;
  color: #2997FF;
  letter-spacing: -0.02em;
}}
.impact-lbl {{
  font-size: 24px; font-weight: 500;
  color: rgba(255,255,255,0.6);
  text-align: center; line-height: 32px;
}}
.impact-lbl .sub {{ display: block; }}

/* ================= SLIDE 4 — PROBLEM ================= */
.s-problem .problem-container {{
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  display: flex; flex-direction: column; align-items: center;
  gap: 32px;
}}
.problem-eyebrow {{
  font-size: 20px; font-weight: 700;
  letter-spacing: 2.4px;
  text-transform: uppercase;
  color: #2997FF;
}}
.problem-headline {{
  font-family: 'Instrument Serif', Georgia, serif;
  font-weight: 400;
  font-size: 120px;
  line-height: 140px;
  color: #FFFFFF;
  text-align: center;
}}
.problem-headline em {{ font-style: italic; font-weight: 400; display: block; }}

/* ================= SLIDE 5 — PROBLEM CARDS ================= */
.s-pains .pains-container {{
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  display: grid;
  grid-template-columns: repeat(3, 382px);
  grid-template-rows: 183px 183px;
  gap: 14px;
}}
.pain-card {{
  padding: 22px 21px;
  border: 1px solid rgba(59,130,246,0.15);
  border-radius: 16px;
  background: linear-gradient(139.6deg, #1A3A5C 0%, #1E4A6E 100%);
  position: relative;
}}
.pain-icon-box {{
  width: 40px; height: 40px;
  background: rgba(255,255,255,0.12);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 18px;
}}
.pain-icon-box svg {{
  width: 22px; height: 22px;
  color: rgba(255,255,255,0.9);
}}
.pain-title {{
  font-size: 24px; font-weight: 600;
  line-height: 21px;
  color: #FFFFFF;
  margin-bottom: 9px;
}}
.pain-desc {{
  font-size: 16px; font-weight: 400;
  line-height: 19px;
  color: rgba(255,255,255,0.7);
}}

/* ================= SLIDES 6a / 6c / 6d (SOLUTIONS) — shared grid ================= */
.sol-grid {{
  position: absolute;
  left: 0; top: 0; right: 0; bottom: 0;
  padding: 80px 120px 80px 140px;
  display: grid;
  grid-template-columns: 620px minmax(0, 1fr);
  gap: 60px;
  align-items: center;
}}
.sol-grid.reverse {{
  padding: 80px 140px 80px 120px;
  grid-template-columns: minmax(0, 1fr) 620px;
}}
.sol-grid.s4 {{
  padding: 80px 140px 80px 120px;
  grid-template-columns: minmax(0, 1fr) 620px;
  gap: 80px;
}}
.sol-text {{
  display: flex; flex-direction: column; gap: 40px; align-items: flex-start;
}}
.sol-eyebrow {{
  font-size: 20px; font-weight: 700;
  letter-spacing: 2.4px; text-transform: uppercase;
  color: #2997FF;
}}
.sol-text-inner {{
  display: flex; flex-direction: column; gap: 32px;
}}
.sol-title {{
  font-family: 'Instrument Serif', Georgia, serif;
  font-weight: 400;
  font-size: 84px;
  line-height: 60px;
  white-space: nowrap;
}}
.sol-title.dark {{ color: #FFFFFF; }}
.sol-title.light {{ color: #1D1D1F; }}
.sol-desc {{
  font-size: 20px; font-weight: 400;
  line-height: 25.87px;
  max-width: 481px;
}}
.sol-desc.dark {{ color: rgba(255,255,255,0.55); }}
.sol-desc.light {{ color: rgba(0,0,0,0.56); }}
.sol-visual {{
  display: flex; align-items: center; justify-content: center;
  max-height: 100%;
}}
.sol-visual .frame {{
  width: 100%;
  border-radius: 18px;
  overflow: hidden;
  position: relative;
}}
.sol-visual.dark .frame {{
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 16px 50px rgba(0,0,0,0.4);
}}
.sol-visual.light .frame {{
  box-shadow: 0 12px 40px rgba(0,0,0,0.15);
}}
.sol-visual .frame img {{
  width: 100%; height: auto;
  display: block;
}}
/* Solution 03 overlay (campaign card on top of dashboard) */
.frame.stack img.overlay {{
  position: absolute;
  top: 3.41%; left: 1.31%;
  width: 97.38%; height: 93.19%;
  object-fit: cover;
}}

/* Solution 02 — product targeting UI cards */
.sol2-products {{
  width: 100%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr 1fr;
  gap: 14px;
  aspect-ratio: 1.45 / 1;
  max-height: 720px;
}}
.product-card {{
  background: #FFFFFF;
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 12px 28px -4px rgba(0,0,0,0.08);
  display: flex; flex-direction: column;
  position: relative;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}}
.product-card:hover {{
  transform: translateY(-3px);
  box-shadow: 0 18px 36px -4px rgba(0,0,0,0.14);
}}
.product-card.hero {{
  border: 1.5px solid #2997FF;
  box-shadow: 0 18px 40px -4px rgba(41,151,255,0.22);
}}
.product-card .pc-img {{
  width: 100%;
  flex: 1.2;
  overflow: hidden;
  background: #f3f3f5;
  position: relative;
}}
.product-card .pc-img img {{
  width: 100%; height: 100%;
  object-fit: cover; display: block;
}}
.product-card .pc-badge {{
  position: absolute;
  top: 10px; left: 10px;
  padding: 4px 10px;
  border-radius: 999px;
  background: linear-gradient(135deg, #22D3EE, #3583E9);
  color: white;
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  z-index: 2;
  box-shadow: 0 4px 12px rgba(53,131,233,0.35);
}}
.product-card .pc-meta {{
  padding: 14px 16px 16px;
  display: flex; flex-direction: column; gap: 6px;
  background: white;
}}
.product-card .pc-name {{
  font-size: 15px; font-weight: 600;
  color: #1D1D1F;
  letter-spacing: -0.01em;
}}
.product-card .pc-stats {{
  display: flex; align-items: center; gap: 10px;
  font-size: 12px;
  color: rgba(0,0,0,0.55);
}}
.product-card .pc-stats .stat {{
  display: flex; align-items: center; gap: 4px;
}}
.product-card .pc-stats .gmv {{
  color: #2997FF; font-weight: 600;
}}
.product-card .pc-stats .dot {{
  width: 3px; height: 3px; border-radius: 50%;
  background: rgba(0,0,0,0.25);
}}
.product-card .pc-pill {{
  align-self: flex-start;
  margin-top: 2px;
  padding: 3px 9px;
  background: #EEF6FF;
  color: #2563EB;
  font-size: 10.5px; font-weight: 600;
  letter-spacing: 0.05em;
  border-radius: 999px;
}}
.product-card .pc-pill.live {{
  background: #ECFDF5;
  color: #059669;
}}
.product-card .pc-pill.live::before {{
  content: "";
  display: inline-block;
  width: 5px; height: 5px;
  border-radius: 50%;
  background: #10B981;
  margin-right: 5px;
  vertical-align: middle;
  box-shadow: 0 0 6px rgba(16,185,129,0.6);
}}

/* ================= SLIDE 7 — CTA ================= */
.s-cta .cta-container {{
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  display: flex; flex-direction: column; align-items: center;
  gap: 60px;
}}
.cta-headline {{
  font-family: 'Instrument Serif', Georgia, serif;
  font-weight: 400;
  font-size: 120px;
  line-height: 140px;
  color: #FFFFFF;
  max-width: 900px;
  padding: 0 60px;
  text-align: center;
  overflow: visible;
}}
.cta-headline em {{ font-style: italic; font-weight: 400; }}
.cta-buttons-block {{
  display: flex; flex-direction: column; align-items: center; gap: 24px;
}}
.cta-buttons {{
  display: flex; gap: 12px; align-items: center; padding-top: 6px;
}}
.btn {{
  display: inline-flex; align-items: center; text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 20px;
  border-radius: 999px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}}
.btn:hover {{ transform: translateY(-1px); }}
.btn-primary {{
  padding: 13px 24px;
  background: linear-gradient(138.8deg, #22D3EE 0%, #3583E9 100%);
  color: #04112A;
  box-shadow: 0 10px 28px rgba(34,211,238,0.25);
}}
.btn-primary:hover {{ box-shadow: 0 16px 40px rgba(34,211,238,0.4); }}
.btn-ghost {{
  padding: 15px 26px;
  border: 2px solid rgba(255,255,255,0.14);
  color: #F6F8FD;
}}
.cta-footer {{
  display: flex; gap: 16px; align-items: center;
}}
.cta-footer .txt {{
  font-size: 20px; font-weight: 400;
  letter-spacing: 0.72px;
  color: rgba(255,255,255,0.7);
}}
.cta-footer .sep {{
  width: 6px; height: 6px; border-radius: 50%;
  background: rgba(255,255,255,0.6);
}}
.cta-qr {{
  position: absolute;
  right: 80px; bottom: 80px;
  display: flex; flex-direction: column; align-items: center; gap: 16px;
}}
.cta-qr .qr-frame {{
  width: 180px; height: 180px;
  background: white;
  border-radius: 12px;
  padding: 4px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  display: flex; align-items: center; justify-content: center;
}}
.cta-qr .qr-frame img {{
  width: 100%; height: 100%;
  display: block;
  image-rendering: pixelated;
}}
.cta-qr .qr-cap {{
  font-size: 16px; font-weight: 400;
  color: rgba(255,255,255,0.6);
  text-align: center;
}}
</style>
</head>
<body>

<div class="progress" id="progress"></div>
<div class="dots" id="dots"></div>
<div class="kb-hint" id="kbHint">
  <span class="kb-key">↑</span>
  <span class="kb-key">↓</span>
  <span>Scroll to navigate</span>
</div>

<!-- ============ SLIDE 1 — HERO ============ -->
<section class="slide dark-bg s-hero" data-slide="1">
  <div class="stage">
    {nav("dark")}
    <div class="hero-stack">
      <div class="hero-logos-block">
        <div class="hero-logos reveal-blur" data-d="1">
          <div class="hero-logo-tile"><img src="{IMG['logo_cp']}" alt="ColourPop"></div>
          <span class="x">×</span>
          <div class="hero-logo-tile r"><img src="{IMG['logo_r']}" alt="Reacher"></div>
        </div>
        <div class="hero-cobrand reveal" data-d="2">
          <span>ColourPop</span>
          <span class="x">×</span>
          <span>Reacher Plus</span>
        </div>
      </div>
      <div class="hero-headline-block">
        <h1 class="reveal-blur" data-d="3">
          <em class="grad-blue">463K creators</em> reached in under 3 months.
        </h1>
        <div class="pill reveal" data-d="4">
          <span class="dot-i"></span>
          Active since February 2026
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 2 — BRAND ============ -->
<section class="slide light-bg s-brand" data-slide="2">
  <div class="stage">
    {nav("light")}
    <div class="brand-container">
      <div class="brand-heading">
        <div class="brand-eyebrow reveal" data-d="1">The Brand</div>
        <div class="brand-title reveal" data-d="2">America's favorite affordable beauty.</div>
      </div>
      <div class="brand-collage reveal-scale" data-d="3">
        <div class="ph span2"><img src="{IMG['brand_1_flatlay']}" alt=""></div>
        <div class="ph"><img src="{IMG['brand_2_rockon']}" alt=""></div>
        <div class="ph"><img src="{IMG['brand_3_eyeshadow']}" alt=""></div>
        <div class="ph"><img src="{IMG['brand_4_sojuicy']}" alt=""></div>
        <div class="ph"><img src="{IMG['brand_5_skinjuice']}" alt=""></div>
        <div class="ph"><img src="{IMG['brand_6_freshkiss']}" alt=""></div>
        <div class="ph"><img src="{IMG['brand_7_goldenstate']}" alt=""></div>
      </div>
      <div class="brand-caption reveal" data-d="4">
        <div>ColourPop Cosmetics is one of the most recognized</div>
        <div>affordable beauty brands in the US.</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 3 — IMPACT ============ -->
<section class="slide dark-flat-bg s-impact" data-slide="3">
  <div class="stage">
    {nav("dark")}
    <div class="impact-container">
      <div class="impact-heading-block">
        <div class="impact-pill reveal" data-d="1">
          <span class="grad-pill">In under 3 months</span>
        </div>
        <div class="impact-title reveal" data-d="2">The results speak for themselves.</div>
      </div>
      <div class="impact-grid">
        <div class="impact-col reveal-scale" data-d="3">
          <div class="impact-num"><span class="impact-value" data-target="9343">0</span></div>
          <div class="impact-lbl">Sample Approvals per month<span class="sub">up from 1,886</span></div>
        </div>
        <div class="impact-col reveal-scale" data-d="4">
          <div class="impact-num"><span class="impact-value" data-target="98" data-prefix="$" data-suffix="K">$0K</span></div>
          <div class="impact-lbl">Sample Requests per month<span class="sub">up from $15K</span></div>
        </div>
        <div class="impact-col reveal-scale" data-d="5">
          <div class="impact-num"><span class="impact-value" data-target="463" data-suffix="K">0K</span></div>
          <div class="impact-lbl">Unique Creators reached<span class="sub">from zero</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 4 — PROBLEM ============ -->
<section class="slide dark-flat-bg s-problem" data-slide="4">
  <div class="stage">
    {nav("dark")}
    <div class="problem-container">
      <div class="problem-eyebrow reveal" data-d="1">Before Reacher</div>
      <div class="problem-headline reveal-blur" data-d="2">
        Paying an agency.
        <em class="grad-blue-alt">Getting nothing back.</em>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 5 — PAIN CARDS ============ -->
<section class="slide dark-flat-bg s-pains" data-slide="5">
  <div class="stage">
    {nav("dark")}
    <div class="pains-container">
      <div class="pain-card reveal-scale" data-d="1">
        <div class="pain-icon-box">{ICON_SVGS['box-off']}</div>
        <div class="pain-title">No Sample Tracking</div>
        <div class="pain-desc">No way to know if samples turned into content.</div>
      </div>
      <div class="pain-card reveal-scale" data-d="2">
        <div class="pain-icon-box">{ICON_SVGS['eye-off']}</div>
        <div class="pain-title">No Outreach Visibility</div>
        <div class="pain-desc">Couldn't verify how many creators were actually contacted.</div>
      </div>
      <div class="pain-card reveal-scale" data-d="3">
        <div class="pain-icon-box">{ICON_SVGS['database-off']}</div>
        <div class="pain-title">No Unified Data</div>
        <div class="pain-desc">Metrics split across TikTok, Shopify, and spreadsheets.</div>
      </div>
      <div class="pain-card reveal-scale" data-d="4">
        <div class="pain-icon-box">{ICON_SVGS['clipboard-off']}</div>
        <div class="pain-title">No Performance Proof</div>
        <div class="pain-desc">Agency reported hours billed, not results delivered.</div>
      </div>
      <div class="pain-card reveal-scale" data-d="5">
        <div class="pain-icon-box">{ICON_SVGS['user-off']}</div>
        <div class="pain-title">No Creator Tiering</div>
        <div class="pain-desc">High-value creators treated the same as everyone.</div>
      </div>
      <div class="pain-card reveal-scale" data-d="6">
        <div class="pain-icon-box">{ICON_SVGS['pennant-off']}</div>
        <div class="pain-title">No Product Strategy</div>
        <div class="pain-desc">No targeting by product ID, no plan for tier saturation.</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 6A — SOLUTION 01 ============ -->
<section class="slide dark-flat-bg" data-slide="6">
  <div class="stage">
    {nav("dark")}
    <div class="sol-grid">
      <div class="sol-text">
        <div class="sol-eyebrow reveal-left" data-d="1">Solution 01</div>
        <div class="sol-text-inner">
          <div class="sol-title dark reveal-left" data-d="2">Real-Time Dashboard</div>
          <div class="sol-desc dark reveal-left" data-d="3">Every outreach, sample request, and approval visible as it happens. No more guessing.</div>
        </div>
      </div>
      <div class="sol-visual dark reveal-right" data-d="2">
        <div class="frame"><img src="{IMG['sol1_dash']}" alt="Real-Time Dashboard"></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 6B — SOLUTION 02 (LIGHT) ============ -->
<section class="slide light-bg" data-slide="7">
  <div class="stage">
    {nav("light")}
    <div class="sol-grid reverse">
      <div class="sol-visual reveal-left" data-d="1">
        <div class="sol2-products">
          <div class="product-card hero">
            <span class="pc-badge">Hero · Shadow Stix</span>
            <div class="pc-img"><img src="{IMG['brand_3_eyeshadow']}" alt=""></div>
            <div class="pc-meta">
              <div class="pc-name">Shadow Stix Eyeshadow</div>
              <div class="pc-stats">
                <span class="stat gmv">$350K</span>
                <span class="dot"></span>
                <span class="stat">1,100+ videos</span>
              </div>
              <span class="pc-pill live">Targeting · L3+</span>
            </div>
          </div>
          <div class="product-card">
            <div class="pc-img"><img src="{IMG['sol2_sojuicy']}" alt=""></div>
            <div class="pc-meta">
              <div class="pc-name">So Juicy Lip</div>
              <div class="pc-stats">
                <span class="stat gmv">$58K</span>
                <span class="dot"></span>
                <span class="stat">320 videos</span>
              </div>
              <span class="pc-pill live">Targeting · L2+</span>
            </div>
          </div>
          <div class="product-card">
            <div class="pc-img"><img src="{IMG['sol2_rockon']}" alt=""></div>
            <div class="pc-meta">
              <div class="pc-name">Rock On Palette</div>
              <div class="pc-stats">
                <span class="stat gmv">$42K</span>
                <span class="dot"></span>
                <span class="stat">280 videos</span>
              </div>
              <span class="pc-pill">Targeting · L3+</span>
            </div>
          </div>
          <div class="product-card">
            <div class="pc-img"><img src="{IMG['sol2_freshkiss']}" alt=""></div>
            <div class="pc-meta">
              <div class="pc-name">Fresh Kiss Lip</div>
              <div class="pc-stats">
                <span class="stat gmv">$35K</span>
                <span class="dot"></span>
                <span class="stat">240 videos</span>
              </div>
              <span class="pc-pill">Targeting · L2+</span>
            </div>
          </div>
          <div class="product-card">
            <div class="pc-img"><img src="{IMG['brand_5_skinjuice']}" alt=""></div>
            <div class="pc-meta">
              <div class="pc-name">Skin Juice Tint</div>
              <div class="pc-stats">
                <span class="stat gmv">$26K</span>
                <span class="dot"></span>
                <span class="stat">190 videos</span>
              </div>
              <span class="pc-pill live">Targeting · All</span>
            </div>
          </div>
          <div class="product-card">
            <div class="pc-img"><img src="{IMG['sol2_goldenstate']}" alt=""></div>
            <div class="pc-meta">
              <div class="pc-name">Golden State Palette</div>
              <div class="pc-stats">
                <span class="stat gmv">$52K</span>
                <span class="dot"></span>
                <span class="stat">350 videos</span>
              </div>
              <span class="pc-pill">Targeting · L3+</span>
            </div>
          </div>
        </div>
      </div>
      <div class="sol-text">
        <div class="sol-eyebrow reveal-right" data-d="2">Solution 02</div>
        <div class="sol-text-inner">
          <div class="sol-title light reveal-right" data-d="3">Hero Product Targeting</div>
          <div class="sol-desc light reveal-right" data-d="4">Strategic outreach by product ID. Shadow Stix alone drove $350K in affiliate GMV across 1,100+ videos.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 6C — SOLUTION 03 ============ -->
<section class="slide dark-flat-bg" data-slide="8">
  <div class="stage">
    {nav("dark")}
    <div class="sol-grid">
      <div class="sol-text">
        <div class="sol-eyebrow reveal-left" data-d="1">Solution 03</div>
        <div class="sol-text-inner">
          <div class="sol-title dark reveal-left" data-d="2">Campaign Planning</div>
          <div class="sol-desc dark reveal-left" data-d="3">Super Brand Day campaigns built, tracked, and reported weekly with custom-branded calendars and incentive strategy.</div>
        </div>
      </div>
      <div class="sol-visual dark reveal-right" data-d="2">
        <div class="frame"><img src="{IMG['sol3_campaign']}" alt="Campaign planning UI"></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 6D — SOLUTION 04 (LIGHT) ============ -->
<section class="slide light-bg" data-slide="9">
  <div class="stage">
    {nav("light")}
    <div class="sol-grid s4">
      <div class="sol-visual light reveal-left" data-d="1">
        <div class="frame"><img src="{IMG['sol4_slack']}" alt="Slack conversation"></div>
      </div>
      <div class="sol-text">
        <div class="sol-eyebrow reveal-right" data-d="2">Solution 04</div>
        <div class="sol-text-inner">
          <div class="sol-title light reveal-right" data-d="3">Same-Day Pivots</div>
          <div class="sol-desc light reveal-right" data-d="4">One Slack message shifts product focus within hours. When tiers saturate, the team flags it and pivots together.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 7 — CTA ============ -->
<section class="slide cta-bg s-cta" data-slide="10">
  <div class="stage">
    {nav("dark")}
    <div class="cta-container">
      <div class="cta-headline reveal-blur" data-d="1">
        Want your results <em class="grad-warm">like this?</em>
      </div>
      <div class="cta-buttons-block">
        <div class="cta-buttons reveal" data-d="2">
          <a class="btn btn-primary" href="https://meetings.hubspot.com/reacher" target="_blank" rel="noopener">Book a Demo →</a>
          <a class="btn btn-ghost" href="https://reacherapp.com" target="_blank" rel="noopener">Visit Website</a>
        </div>
        <div class="cta-footer reveal" data-d="3">
          <span class="txt">Official TikTok Shop Partner</span>
          <span class="sep"></span>
          <span class="txt">Y Combinator Backed</span>
        </div>
      </div>
    </div>
    <div class="cta-qr reveal" data-d="4">
      <div class="qr-frame"><img src="{IMG['qr']}" alt=""></div>
      <div class="qr-cap">Scan to visit reacherapp.com</div>
    </div>
  </div>
</section>

<script>
(function() {{
  const slides = document.querySelectorAll('.slide');
  const dotsContainer = document.getElementById('dots');
  const progress = document.getElementById('progress');
  const kbHint = document.getElementById('kbHint');

  // Stage scaling — fit 1920x1200 inside viewport while preserving aspect
  function updateScale() {{
    const sx = window.innerWidth / 1920;
    const sy = window.innerHeight / 1080;
    const scale = Math.min(sx, sy);
    document.documentElement.style.setProperty('--stage-scale', scale);
  }}
  updateScale();
  window.addEventListener('resize', updateScale);

  // Slide anchor ids + preview mode
  slides.forEach((s, i) => {{ s.id = 's' + (i + 1); }});
  const isPreview = new URLSearchParams(location.search).has('preview');
  if (isPreview) {{
    document.documentElement.style.scrollSnapType = 'none';
    const style = document.createElement('style');
    style.textContent = '.reveal,.reveal-scale{{opacity:1!important;transform:none!important;transition:none!important;}} html,body{{height:auto!important;overflow:visible!important;}} .slide{{scroll-snap-align:none!important;}}';
    document.head.appendChild(style);
    slides.forEach(s => {{
      s.classList.add('visible');
      s.dataset.counted = '1';
    }});
    document.querySelectorAll('.impact-value').forEach(el => {{
      const target = parseFloat(el.dataset.target) || 0;
      const prefix = el.dataset.prefix || '';
      const suffix = el.dataset.suffix || '';
      el.textContent = prefix + target.toLocaleString() + suffix;
    }});
    if (location.hash) {{
      const tgt = document.querySelector(location.hash);
      if (tgt) requestAnimationFrame(() => tgt.scrollIntoView({{ behavior:'instant', block:'start' }}));
    }}
  }}

  // Nav dots
  slides.forEach((slide, i) => {{
    const dot = document.createElement('button');
    dot.className = 'dot';
    dot.setAttribute('aria-label', 'Slide ' + (i + 1));
    dot.addEventListener('click', () => slide.scrollIntoView({{ behavior: 'smooth' }}));
    dotsContainer.appendChild(dot);
  }});
  const dots = dotsContainer.querySelectorAll('.dot');

  // Visibility observer + counter animation
  const io = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.intersectionRatio > 0.5) {{
        entry.target.classList.add('visible');
        const idx = Array.from(slides).indexOf(entry.target);
        dots.forEach((d, i) => d.classList.toggle('active', i === idx));
        if (!entry.target.dataset.counted) {{
          entry.target.querySelectorAll('.impact-value').forEach(animateCounter);
          entry.target.dataset.counted = '1';
        }}
      }}
    }});
  }}, {{ threshold: [0, 0.25, 0.5, 0.75, 1] }});
  slides.forEach(s => io.observe(s));
  requestAnimationFrame(() => slides[0].classList.add('visible'));

  function animateCounter(el) {{
    const target = parseFloat(el.dataset.target) || 0;
    const prefix = el.dataset.prefix || '';
    const suffix = el.dataset.suffix || '';
    const duration = 1500;
    const start = performance.now();
    function tick(now) {{
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 4);
      const v = Math.floor(target * eased);
      el.textContent = prefix + v.toLocaleString() + suffix;
      if (t < 1) requestAnimationFrame(tick);
      else el.textContent = prefix + target.toLocaleString() + suffix;
    }}
    requestAnimationFrame(tick);
  }}

  // Progress + keyboard
  function updateProgress() {{
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0) + '%';
  }}
  window.addEventListener('scroll', updateProgress, {{ passive: true }});
  updateProgress();

  function currentIndex() {{
    let closest = 0, min = Infinity;
    slides.forEach((s, i) => {{
      const d = Math.abs(s.getBoundingClientRect().top);
      if (d < min) {{ min = d; closest = i; }}
    }});
    return closest;
  }}
  document.addEventListener('keydown', (e) => {{
    const idx = currentIndex();
    if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') {{
      e.preventDefault();
      if (idx < slides.length - 1) slides[idx + 1].scrollIntoView({{ behavior: 'smooth' }});
    }} else if (e.key === 'ArrowUp' || e.key === 'PageUp') {{
      e.preventDefault();
      if (idx > 0) slides[idx - 1].scrollIntoView({{ behavior: 'smooth' }});
    }} else if (e.key === 'Home') {{
      e.preventDefault();
      slides[0].scrollIntoView({{ behavior: 'smooth' }});
    }} else if (e.key === 'End') {{
      e.preventDefault();
      slides[slides.length - 1].scrollIntoView({{ behavior: 'smooth' }});
    }}
    hideHint();
  }});
  window.addEventListener('scroll', hideHint, {{ passive: true }});
  let hintHidden = false;
  function hideHint() {{
    if (hintHidden) return;
    hintHidden = true;
    kbHint.classList.add('hidden');
  }}
}})();
</script>
</body>
</html>
"""

out = ROOT / "index.html"
out.write_text(HTML)
print(f"Wrote {out} — {len(HTML)//1024} KB")
