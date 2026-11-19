#!/usr/bin/env python3
"""Sidebar Press covers (copied from Caffeinated Chronicles z_Assets/5_Covers, 2026-11-13); (DMs Guild trade dress).

Layout (from DMs Guild best practice: 88% of top covers put the title at the top, full-bleed art,
one central focus, outlined block title; DMs Guild allows ONLY its own logo on the cover):
  * full-bleed black-and-white art
  * top: series line, big outlined Cinzel title, italic subtitle
  * foot: wrought-iron fence frieze with ivy (ornament.py); Sidebar Press shield in a centre medallion,
    code plaque (left, with the DMs Guild logo when present), level plaque (right)
The ironwork and logo are pre-rendered in _logos/ ("_cover band (ironwork).png", "SidebarPress (B&W).png").
To redraw them after editing ornament.py, delete those PNGs; that needs rsvg-convert (brew install librsvg),
scipy and the Cinzel fonts installed.

Usage:  python3 make_covers.py            ink covers (print)
        python3 make_covers.py --color    colour covers for codes in COLOR_ART (FGU + PDF)
        python3 make_covers.py --all      both
  1. Finds the Canva downloads (by their Canva file names) in _Inbox/, the CC-HUB Art/_Inbox and any
     folders passed on the command line, and files them in art/ under readable names.
  2. Writes "Cover — <Title>.png" (1600×2400) next to this script for every leap whose art is present.
Logo: put the official DMs Guild logo (from the DMs Guild creator resources) at _logos/DMsGuild.png;
until then the slot is left empty. Sidebar Press goes on the inside title page, not the cover.
"""
import sys, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent                      # z_Assets/5_Covers
VAULT = HERE.parents[1]
FONTS, ART, LOGOS = HERE / "_fonts", HERE / "art", HERE / "_logos"
MASCOT = LOGOS / "SidebarPress mascot (ink).png"
sys.path.insert(0, str(HERE)); import ornament                  # ironwork, ivy and the B&W Sidebar Press logo
W, H = 1600, 2400

COVERS = [  # art path (vault-relative), series line, title, subtitle, code, band text
    ("99-Assets/Ritterstadt/cover/Ritterstadt cover.jpg", "Greyhawk University · Field Station Gazetteer",
     "Ritterstadt", "A Gazetteer of the Field Station Town", "GR1", "A setting book for the Sepia Uplands"),
    ("99-Assets/SP-GA05/cover/SP-GA05 cover.jpg", "Greyhawk University · Field Wardens",
     "The Pilgrims of the Hollow Bell", "A Sidebar Press Greyhawk Adventure", "GA5", "An adventure for 3rd-level characters"),
    ("99-Assets/SP-GA00/cover/SP-GA00 cover.png", "Greyhawk University · Field Wardens",
     "Nobody's Colors", "A Sidebar Press Greyhawk Adventure", "GA0", "An adventure for characters of levels 1–4"),
    ("99-Assets/SP-SQ/cover/SP-GQ00 — Cover.png", "Greyhawk University · Field Wardens",
     "The Shadow on the Quag", "Arc Guide & Prologue", "GQ0", "An adventure for levels 1–4"),
    ("99-Assets/SP-GS01/cover/SP-GS01 cover.png", "Greyhawk Special · A Brewfest Adventure",
     "The Gluttonwretch of Hommlet", "A Sidebar Press Greyhawk Adventure", "GS1", "An adventure for 12th-level characters"),
]

# full-colour cover art (screen: FGU module and PDF). `python3 make_covers.py --color` builds
# "Cover — <Title> (color).png" for every code listed here; plain `make_covers.py` still builds the ink covers.
COLOR_ART = {
    "GS1": "99-Assets/SP-GS01/SP-GS01 - 01 Cover - The Open Door (color).png",
}

# colour trade dress: night-dark washes instead of paper, cream lettering, antique-gold ironwork and rules
INK = dict(paper=(255, 255, 255), wash=235, foot=240, text="black", halo="white", title="black",
           rule="black", metal=None, plate=None)
COLOR = dict(paper=(14, 11, 10), wash=225, foot=235, text=(242, 230, 204), halo=(10, 8, 7), title=(240, 212, 148),
             rule=(196, 156, 82), metal=(196, 156, 82), plate=(243, 233, 210))

def tint(im, metal, plate):
    """recolour the B&W ironwork/logo: dark line work -> metal, white fills -> plate"""
    if metal is None: return im
    px = im.load()
    for yy in range(im.height):
        for xx in range(im.width):
            r, g, b, a = px[xx, yy]
            if a == 0: continue
            t = (r + g + b) / 765                                  # 0 = ink line, 1 = white fill
            px[xx, yy] = tuple(round(m * (1 - t) + p * t) for m, p in zip(metal, plate)) + (a,)
    return im

# push art down (px) when the subject's head would sit under the title block
ART_SHIFT = {}   # e.g. {"GS1": 200}

def font(name, size): return ImageFont.truetype(str(FONTS / name), size)

def cached(path, build):
    """use the pre-rendered PNG when present (no rsvg-convert needed); delete it to redraw"""
    if path.exists(): return Image.open(path).convert("RGBA")
    im = build(); im.save(path); return im

def collect(extra):
    ART.mkdir(exist_ok=True)
    places = [HERE / "_Inbox", VAULT / "2-Adventures/Twists and Taps/CC-HUB — Campaign Module/Art/_Inbox"] + [Path(e) for e in extra]
    for stem, artname, *_ in COVERS:
        if any((ART / f"{artname}{e}").exists() for e in (".jpg", ".png")): continue
        for d in places:
            hits = [p for p in d.glob(f"{stem}*") if p.suffix.lower() in (".jpg", ".jpeg", ".png")] if d.exists() else []
            if hits:
                dest = ART / f"{artname}{hits[0].suffix.lower()}"
                shutil.copy2(hits[0], dest)
                try: hits[0].unlink()
                except OSError: print("  (left original in place:", hits[0], ")")
                print("filed", dest.name); break

def fit(draw, text, fname, max_w, start):
    s = start
    while s > 40:
        f = font(fname, s)
        if draw.textbbox((0, 0), text, font=f, stroke_width=max(4, s // 18))[2] <= max_w: return f
        s -= 4
    return font(fname, s)

def centred(draw, y, text, f, fill, stroke=0, stroke_fill="white", spacing=0):
    if spacing:                                                  # letter-spaced small caps line
        widths = [draw.textlength(ch, font=f) + spacing for ch in text]
        x = (W - sum(widths) + spacing) / 2
        for ch, w in zip(text, widths):
            draw.text((x, y), ch, font=f, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill); x += w
        return y + f.size
    w = draw.textbbox((0, 0), text, font=f, stroke_width=stroke)[2]
    draw.text(((W - w) / 2, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return y + draw.textbbox((0, 0), text, font=f, stroke_width=stroke)[3]

def make(artpath, series, title, subtitle, code, band, color=False):
    st = COLOR if color else INK
    art = Image.open(artpath).convert("RGB")
    s = max(W / art.width, H / art.height)
    art = art.resize((round(art.width * s), round(art.height * s)), Image.LANCZOS)
    art = art.crop(((art.width - W) // 2, (art.height - H) // 2, (art.width - W) // 2 + W, (art.height - H) // 2 + H))
    sh = ART_SHIFT.get(code, 0)
    if sh:
        moved = Image.new("RGB", (W, H), st["paper"]); moved.paste(art, (0, sh))
        fade = Image.new("L", (W, H), 0); fd = ImageDraw.Draw(fade)
        for y in range(sh, sh + 320):                            # feather the art's top edge into paper
            fd.line([(0, y), (W, y)], fill=int(255 * (1 - (y - sh) / 320) ** 1.5))
        fd.rectangle([0, 0, W, sh], fill=255)
        art = Image.composite(Image.new("RGB", (W, H), st["paper"]), moved, fade)
    img = art.convert("RGBA")
    # soft white wash behind the title block so it reads at thumbnail size
    wash = Image.new("RGBA", (W, H), (0, 0, 0, 0)); wd = ImageDraw.Draw(wash)
    top = 640
    for y in range(top):
        a = int(st["wash"] * (1 - (y / top) ** 2.2))
        wd.line([(0, y), (W, y)], fill=st["paper"] + (a,))
    img = Image.alpha_composite(img, wash)
    d = ImageDraw.Draw(img)
    # thin double rule frame, classic module trade dress
    for inset, wdt in ((28, 6), (44, 2)):
        d.rectangle([inset, inset, W - inset, H - inset], outline=st["rule"], width=wdt)
    y = 92
    y = centred(d, y, series.upper(), font("Cinzel_700Bold.ttf", 38), st["text"], spacing=6, stroke=2 if color else 0, stroke_fill=st["halo"]) + 26
    words, lines = title.split(), []
    if len(title) > 15 and len(words) > 1:                       # two-line title, balanced
        best = min(range(1, len(words)), key=lambda i: abs(len(" ".join(words[:i])) - len(" ".join(words[i:]))))
        lines = [" ".join(words[:best]), " ".join(words[best:])]
    else:
        lines = [title]
    tf = min((fit(d, ln.upper(), "Cinzel_900Black.ttf", W - 300, 190) for ln in lines), key=lambda f: f.size)
    for ln in lines:
        y = centred(d, y, ln.upper(), tf, st["title"], stroke=max(6, tf.size // 16), stroke_fill=st["halo"]) + 6
    y = centred(d, y + 14, subtitle, font("EBGaramond_500Medium_Italic.ttf" if (FONTS / "EBGaramond_500Medium_Italic.ttf").exists() else "EBGaramond_400Regular_Italic.ttf", 64), st["text"], stroke=4, stroke_fill=st["halo"])
    # foot: wrought-iron frieze with ivy, Sidebar Press shield in a medallion, code and level plaques
    svg, (lx, lcy), pl, pr, bh = ornament.band_svg(W, 360, logo_w=470)
    y0 = H - 50 - bh
    wash = Image.new("RGBA", (W, H), (0, 0, 0, 0)); wd = ImageDraw.Draw(wash)
    for y in range(y0 - 220, H):                                  # fade the art to paper behind the ironwork
        t = min(1, max(0, (y - (y0 - 220)) / 300))
        wd.line([(0, y), (W, y)], fill=st["paper"] + (int(st["foot"] * t ** 1.6),))
    img = Image.alpha_composite(img, wash)
    img.alpha_composite(tint(cached(LOGOS / "_cover band (ironwork).png", lambda: ornament.render(svg, W, bh)).copy(), st["metal"], st["plate"]), (0, y0))
    lg = cached(LOGOS / "SidebarPress (B&W).png", lambda: ornament.logo(MASCOT)).resize((470, 263), Image.LANCZOS)
    lg = tint(lg, st["metal"] and (20, 16, 14), st["plate"])          # colour cover: warm black lines on cream
    img.alpha_composite(lg, (round(lx), round(y0 + lcy - lg.height / 2)))
    d = ImageDraw.Draw(img)
    for inset, wdt in ((28, 6), (44, 2)):                         # redraw the frame over the wash
        d.rectangle([inset, inset, W - inset, H - inset], outline=st["rule"], width=wdt)
    # left plaque: optional DMs Guild logo + product code
    x, y, w, h = pl; cf = font("Cinzel_900Black.ttf", 66)
    dg = LOGOS / "DMsGuild.png"
    if dg.exists():
        g = Image.open(dg).convert("RGBA"); r = (h - 36) / g.height
        g = g.resize((round(g.width * r), h - 36), Image.LANCZOS)
        img.alpha_composite(g, (round(x + 24), round(y0 + y + 18)))
        cx = x + 24 + g.width + (w - 24 - g.width) / 2
    else:
        cx = x + w / 2
    tb = d.textbbox((0, 0), code, font=cf)
    d.text((cx - (tb[2] - tb[0]) / 2 - tb[0], y0 + y + h / 2 - (tb[3] - tb[1]) / 2 - tb[1]), code, font=cf, fill="black")
    # right plaque: level line, two lines of italic
    x, y, w, h = pr; bf = font("EBGaramond_500Medium_Italic.ttf", 42)
    words = band.split(); cut = band.find(" for ") + 5 if " for " in band else len(band) // 2
    l1, l2 = band[:cut].strip(), band[cut:].strip()
    for i, ln in enumerate((l1, l2)):
        tw = d.textlength(ln, font=bf)
        d.text((x + (w - tw) / 2, y0 + y + 14 + i * 46), ln, font=bf, fill="black")
    out = HERE / (f"Cover — {title} (color).png" if color else f"Cover — {title}.png")
    img.convert("RGB").save(out, optimize=True)
    return out

if __name__ == "__main__":
    args = sys.argv[1:]
    want_color, want_ink = "--color" in args or "--all" in args, "--color" not in args
    for artrel, series, title, subtitle, code, band in COVERS:
        if want_ink:
            art = VAULT / artrel
            if not art.exists(): print("waiting for art:", artrel)
            else: print("cover →", make(art, series, title, subtitle, code, band).name)
        if want_color and code in COLOR_ART:
            art = VAULT / COLOR_ART[code]
            if not art.exists(): print("waiting for colour art:", COLOR_ART[code])
            else: print("cover →", make(art, series, title, subtitle, code, band, color=True).name)
