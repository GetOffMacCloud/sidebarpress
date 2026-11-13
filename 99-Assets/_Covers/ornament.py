#!/usr/bin/env python3
"""Pen-and-ink ornament kit for the Sidebar Press covers: wrought-iron scrollwork, ivy, the
Sidebar Press shield logo. Everything is drawn as SVG and rendered with rsvg-convert, so the
ironwork stays crisp at any size and matches the black-and-white crosshatch art."""
import math, subprocess, tempfile, io
from pathlib import Path
from PIL import Image

INK = "#111"

# ---------- primitives --------------------------------------------------------------------
def pts_path(pts):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)

def spiral(cx, cy, r0, turns=1.6, start=0.0, k=None, cw=True, n=140):
    """logarithmic spiral from radius r0 inward"""
    k = k if k is not None else math.log(6) / (turns * 2 * math.pi)
    out = []
    for i in range(n + 1):
        t = i / n * turns * 2 * math.pi
        r = r0 * math.exp(-k * t)
        a = start + (t if cw else -t)
        out.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return out

def iron(d, w=9):
    """forged bar: heavy ink stroke with a fine white highlight down the middle"""
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{max(1.2, w*0.28):.1f}" stroke-linecap="round" stroke-linejoin="round"/>')

def c_scroll(x, y, h, flip=1, w=8):
    """a C-scroll standing on (x,y), curling at both ends — the classic railing cresting unit"""
    top = spiral(x + flip * h * 0.22, y - h * 0.78, h * 0.22, turns=1.25, start=math.pi if flip > 0 else 0, cw=flip > 0)
    bot = spiral(x + flip * h * 0.20, y - h * 0.16, h * 0.16, turns=1.1, start=math.pi if flip > 0 else 0, cw=flip < 0)
    spine = [(x + flip * h * 0.0, y - h * 0.16 + (y - h * 0.78 - (y - h * 0.16)) * t) for t in [i / 20 for i in range(21)]]
    spine = [(sx - flip * math.sin(t * math.pi) * h * 0.10, sy) for (sx, sy), t in zip(spine, [i / 20 for i in range(21)])]
    return iron(pts_path(list(reversed(top)) + spine[::-1][1:]), w) + iron(pts_path(bot[::-1] + spine[1:2]), w)

def ivy_leaf(x, y, s, ang):
    """three-lobed ivy leaf, white fill, inked outline and veins, light hatching on one side"""
    d = ("M0,4 C-8,6 -20,6 -26,-2 C-31,-9 -26,-16 -19,-16 C-24,-25 -18,-35 -8,-32 "
         "C-9,-41 -4,-47 0,-52 C4,-47 9,-41 8,-32 C18,-35 24,-25 19,-16 C26,-16 31,-9 26,-2 C20,6 8,6 0,4 Z")
    veins = "M0,4 L0,-44 M0,-6 L-20,-6 M0,-6 L20,-6 M0,-14 L-14,-26 M0,-14 L14,-26"
    hatch = "".join(f'<path d="M{3+i*3.2},{0} L{3+i*3.2},{-30+i*2}" stroke="{INK}" stroke-width="0.9"/>' for i in range(8))
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f}) scale({s/52:.3f})">'
            f'<path d="{d}" fill="#fff" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>'
            f'<clipPath id="lf{int(x)}{int(y)}"><path d="{d}"/></clipPath><g clip-path="url(#lf{int(x)}{int(y)})">{hatch}</g>'
            f'<path d="{veins}" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"/></g>')

def vine(x0, x1, y, amp, period, leaf=34, seed=0, skip=()):
    """ivy vine weaving along a rail, leaves alternating above/below"""
    pts = [(x, y + amp * math.sin((x - x0) / period * 2 * math.pi + seed)) for x in range(int(x0), int(x1) + 1, 4)]
    out = [f'<path d="{pts_path(pts)}" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>']
    step = period / 2
    i, x = 0, x0 + step * 0.5
    while x < x1 - 10:
        if not any(a <= x <= b for a, b in skip):
            yy = y + amp * math.sin((x - x0) / period * 2 * math.pi + seed)
            up = i % 2 == 0
            out.append(ivy_leaf(x, yy, leaf * (0.85 + 0.3 * ((i * 37 % 10) / 10)), (-35 if up else 145) + (i * 23 % 30) - 15))
            # tendril
            tx = x + step * 0.25
            ty = y + amp * math.sin((tx - x0) / period * 2 * math.pi + seed)
            out.append(f'<path d="{pts_path(spiral(tx + 6, ty + (10 if up else -10), 7, turns=1.3, start=math.pi, cw=up))}" fill="none" stroke="{INK}" stroke-width="1.8"/>')
        i += 1; x += step
    return "".join(out)

def rail(x0, x1, y, w=12):
    return (f'<rect x="{x0}" y="{y-w/2}" width="{x1-x0}" height="{w}" fill="{INK}"/>'
            f'<line x1="{x0+4}" y1="{y-w/2+3}" x2="{x1-4}" y2="{y-w/2+3}" stroke="#fff" stroke-width="1.6"/>')

def collar(x, y, h=26, w=10):
    return f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="2" fill="{INK}"/><line x1="{x}" y1="{y-h/2+3}" x2="{x}" y2="{y+h/2-3}" stroke="#fff" stroke-width="1.4"/>'

def finial(x, y, s=1, flip=1):
    """spear-and-ball rail end"""
    return (f'<g transform="translate({x},{y}) scale({flip*s},{s})">'
            f'<circle cx="10" cy="0" r="9" fill="{INK}"/><circle cx="7" cy="-3" r="2.4" fill="#fff"/>'
            f'<path d="M18,0 L40,-10 L58,0 L40,10 Z" fill="#fff" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M22,0 L56,0" stroke="{INK}" stroke-width="1.6"/></g>')

def plaque(x, y, w, h):
    """cartouche with clipped corners and a double rule"""
    c = 18
    def poly(i):
        return (f"M{x+c+i},{y+i} L{x+w-c-i},{y+i} L{x+w-i},{y+c+i} L{x+w-i},{y+h-c-i} L{x+w-c-i},{y+h-i} "
                f"L{x+c+i},{y+h-i} L{x+i},{y+h-c-i} L{x+i},{y+c+i} Z")
    return (f'<path d="{poly(0)}" fill="#fff" stroke="{INK}" stroke-width="6"/>'
            f'<path d="{poly(9)}" fill="none" stroke="{INK}" stroke-width="1.8"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>' for cx, cy in
                      ((x + c * .55, y + c * .55), (x + w - c * .55, y + c * .55), (x + c * .55, y + h - c * .55), (x + w - c * .55, y + h - c * .55))))

def render(svg, w, h, scale=1):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "a.svg"; p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*scale}" height="{h*scale}" viewBox="0 0 {w} {h}">{svg}</svg>')
        png = subprocess.run(["rsvg-convert", str(p)], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(png)).convert("RGBA")

# ---------- Sidebar Press logo ---------------------------------------------------------------
def logo_svg():
    W, H = 1000, 560
    sh = "M320,62 Q500,6 680,62 L680,282 Q680,440 500,546 Q320,440 320,282 Z"
    sh2 = "M338,78 Q500,28 662,78 L662,282 Q662,428 500,524 Q338,428 338,282 Z"
    hatch = "".join(f'<line x1="{x}" y1="0" x2="{x-260}" y2="560" stroke="{INK}" stroke-width="1.6"/>' for x in range(520, 1000, 11))
    hatch2 = "".join(f'<line x1="{x}" y1="0" x2="{x+260}" y2="560" stroke="{INK}" stroke-width="1"/>' for x in range(560, 760, 16))
    rivets = "".join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{INK}"/><circle cx="{x-1.6}" cy="{y-1.6}" r="1.6" fill="#fff"/>'
                     for x, y in ((360, 105), (640, 105), (360, 205), (640, 205), (420, 445), (580, 445), (500, 510), (500, 58)))
    s = [f'<path d="{sh}" fill="#fff" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>',
         f'<clipPath id="sh"><path d="{sh2}"/></clipPath><g clip-path="url(#sh)"><g clip-path="url(#rh)">{hatch}{hatch2}</g></g>',
         '<clipPath id="rh"><rect x="500" y="0" width="200" height="560"/></clipPath>',
         f'<path d="{sh2}" fill="none" stroke="{INK}" stroke-width="2.5"/>',
         f'<line x1="500" y1="40" x2="500" y2="530" stroke="{INK}" stroke-width="2"/>', rivets]
    # filigree scrolls rising from the banner ends, mirrored
    for f in (1, -1):
        cx = 500 - f * 300
        s.append(c_scroll(cx - f * 40, 238, 150, flip=-f, w=7))
        s.append(iron(pts_path(spiral(cx + f * 30, 170, 34, turns=1.4, start=0 if f > 0 else math.pi, cw=f > 0)), 6))
        s.append(ivy_leaf(cx - f * 95, 232, 34, -50 * f))
        s.append(ivy_leaf(cx + f * 70, 230, 28, 40 * f))
        s.append(c_scroll(cx - f * 40, 362, -120, flip=-f, w=6))
    # main banner
    b = "M30,300 L110,224 L890,224 L970,300 L890,376 L110,376 Z"
    b2 = "M52,300 L118,236 L882,236 L948,300 L882,364 L118,364 Z"
    s += [f'<path d="{b}" fill="#fff" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>',
          f'<path d="{b2}" fill="none" stroke="{INK}" stroke-width="2.4"/>']
    for x in (82, 918):
        s.append(f'<path d="M{x},282 L{x+16},300 L{x},318 L{x-16},300 Z" fill="{INK}"/><circle cx="{x}" cy="300" r="4" fill="#fff"/>')
    s.append('<text x="500" y="340" text-anchor="middle" font-family="Cinzel" font-weight="900" font-size="122" '
             f'letter-spacing="6" fill="{INK}">S<tspan font-size="96">IDE</tspan>B<tspan font-size="96">AR</tspan></text>')
    # PRESS tab
    s += [plaque(370, 392, 260, 82),
          f'<text x="500" y="452" text-anchor="middle" font-family="Cinzel" font-weight="700" font-size="54" letter-spacing="8" fill="{INK}">PRESS</text>']
    return "".join(s), W, H

def logo(mascot_png=None, width=None):
    svg, W, H = logo_svg()
    K = 2                                                         # render at 2000 px wide for print
    img = render(svg, W, H, K)
    if mascot_png and Path(mascot_png).exists():
        from PIL import ImageFilter
        m = Image.open(mascot_png).convert("RGBA")
        mh = 236 * K; m = m.resize((round(m.width * mh / m.height), mh), Image.LANCZOS)
        pad = 14 * K; base = Image.new("L", (m.width + 2 * pad, m.height + 2 * pad), 0)
        base.paste(m.getchannel("A").point(lambda v: 255 if v > 90 else 0), (pad, pad))
        ink = base.filter(ImageFilter.MaxFilter(2 * 4 * K + 1))      # bold contour
        halo = ink.filter(ImageFilter.MaxFilter(2 * 5 * K + 1))      # white sticker halo
        sticker = Image.new("RGBA", base.size, (255, 255, 255, 0))
        sticker.paste((255, 255, 255, 255), mask=halo.filter(ImageFilter.GaussianBlur(1)))
        sticker.paste((17, 17, 17, 255), mask=ink.filter(ImageFilter.GaussianBlur(1)))
        sticker.alpha_composite(m, (pad, pad))
        img.alpha_composite(sticker, ((500 + 30) * K - sticker.width // 2, 254 * K - m.height - pad))
    if width:
        img = img.resize((width, round(H * width / W)), Image.LANCZOS)
    return img

# ---------- cover band -----------------------------------------------------------------------
def band_svg(W=1600, H=360, logo_w=470):
    """wrought-iron fence frieze across the cover foot; returns svg, logo box, plaque boxes"""
    R0 = 120                      # rail ends (spear finials stay inside the cover frame)
    yt, yb = 120, H - 34          # top and bottom rails
    lx0, lx1 = W / 2 - logo_w / 2 - 20, W / 2 + logo_w / 2 + 20
    s = []
    # pickets + scroll infill between the rails (behind everything)
    for x in range(R0 + 40, W - R0 - 30, 46):
        if lx0 - 10 < x < lx1 + 10: continue
        s.append(iron(f"M{x},{yt} L{x},{yb}", 5))
    for x in range(R0 + 63, W - R0 - 50, 92):
        if lx0 - 50 < x < lx1 + 50: continue
        s.append(iron(pts_path(spiral(x, (yt + yb) / 2 - 18, 22, turns=1.2, start=-math.pi / 2, cw=True)), 4))
        s.append(iron(pts_path(spiral(x, (yt + yb) / 2 + 18, 22, turns=1.2, start=math.pi / 2, cw=True)), 4))
    s += [rail(R0, W - R0, yt, 18), rail(R0, W - R0, yb, 18), rail(R0, W - R0, yb - 22, 6)]
    for x in range(R0 + 40, W - R0 - 30, 46):
        if lx0 - 10 < x < lx1 + 10: continue
        s.append(collar(x, yt)); s.append(collar(x, yb - 11, 36, 8))
    s += [finial(R0, yt, 0.9, -1), finial(W - R0, yt, 0.9, 1), finial(R0, yb, 0.75, -1), finial(W - R0, yb, 0.75, 1)]
    # cresting: C-scroll pairs rising off the top rail, tallest beside the logo
    for side in (-1, 1):
        xs = [W / 2 + side * (logo_w / 2 + 60 + i * 120) for i in range(6)]
        for i, x in enumerate(xs):
            if not (R0 + 40 < x < W - R0 - 40): continue
            h = 95 - i * 9
            s.append(c_scroll(x - 12, yt - 6, h, flip=-1, w=6)); s.append(c_scroll(x + 12, yt - 6, h, flip=1, w=6))
            s.append(f'<path d="M{x},{yt-h-18} L{x+8},{yt-h-2} L{x},{yt-h+10} L{x-8},{yt-h-2} Z" fill="{INK}"/>')
    # ivy twining along the top rail
    s.append(vine(R0 + 20, W - R0 - 20, yt + 4, 14, 170, leaf=50, seed=0.6, skip=((lx0 - 20, lx1 + 20),)))
    # plaques for the code (left) and level line (right)
    pw, ph = 400, 120
    pl = (150, yt + 32, pw, ph); pr = (W - 150 - pw, yt + 32, pw, ph)
    s += [plaque(*pl), plaque(*pr)]
    # medallion behind the logo
    s.append(f'<ellipse cx="{W/2}" cy="{H/2+6}" rx="{logo_w/2+18}" ry="{H/2-14}" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             f'<ellipse cx="{W/2}" cy="{H/2+6}" rx="{logo_w/2+8}" ry="{H/2-24}" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    return "".join(s), (W / 2 - logo_w / 2, H / 2 + 6), pl, pr, H
