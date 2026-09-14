#!/usr/bin/env python3
"""Generate assets/header.svg: loader that resolves into the name banner.
Usage: scripts/build-header.py [load_seconds]"""
import sys
LOAD = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
OUT = 0.25          # loader text drop-out
MOVE = 0.5          # bar shrinks into underline
RISE = 0.45         # name/subtitle slide up
W, H = 854, 260
phases = ["[…] INIT PROFILE", "[…] FETCH UPSTREAM PRS", "[…] LOAD ARSENAL", "[…] MOUNT README"]
cuts = [0.0, 0.24, 0.52, 0.86, 1.0]
pct_curve = [4, 11, 23, 37, 51, 63, 74, 84, 90, 92, 100]
pct_at = [0, .095, .19, .29, .4, .52, .64, .76, .86, .93, .965]
TOTAL = LOAD + MOVE + RISE + 0.2

def win(name, a, b, total):
    a, b = a / total * 100, b / total * 100
    return f"@keyframes {name}{{0%,{a:.2f}%{{opacity:0}}{a+.01:.2f}%,{b:.2f}%{{opacity:1}}{b+.01:.2f}%,100%{{opacity:0}}}}"

bw = 280; bx = (W - bw) / 2; by = H / 2
name_y = H / 2 + 2; desc_y = H / 2 + 36; rule_y = H / 2 + 54
css = [
    ".mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}",
    ".sans{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}",
    # progress fill
    "@keyframes fill{0%{transform:scaleX(.04)}20%{transform:scaleX(.3)}55%{transform:scaleX(.7)}85%{transform:scaleX(.9)}94%{transform:scaleX(.92)}100%{transform:scaleX(1)}}",
    f".fill{{transform-box:fill-box;transform-origin:0 50%;animation:fill {LOAD}s cubic-bezier(.25,1,.5,1) forwards}}",
    f".mover{{transform-box:fill-box;transform-origin:50% 50%;animation:toRule {MOVE}s cubic-bezier(.65,0,.35,1) {LOAD}s forwards}}",
    # bar -> short accent rule under subtitle (scale around centre, drop down)
    f"@keyframes toRule{{0%{{transform:scaleX(1) translateY(0)}}100%{{transform:scaleX(.17) translateY({rule_y-by}px)}}}}",
    f"@keyframes trackOut{{to{{opacity:0}}}}",
    f".track{{animation:trackOut {OUT}s linear {LOAD}s forwards}}",
    # loader text out
    f"@keyframes textOut{{to{{opacity:0}}}}",
    f".ltext{{animation:textOut {OUT}s ease {LOAD}s forwards}}",
    # header in: rise + fade
    f"@keyframes rise{{0%{{opacity:0;transform:translateY(14px)}}100%{{opacity:1;transform:translateY(0)}}}}",
    f".name{{opacity:0;animation:rise {RISE}s cubic-bezier(.2,.8,.2,1) {LOAD+MOVE*.5}s forwards}}",
    f".desc{{opacity:0;animation:rise {RISE}s cubic-bezier(.2,.8,.2,1) {LOAD+MOVE*.5+.12}s forwards}}",
]
els = []
for i, t in enumerate(phases):
    css += [win(f"ph{i}", cuts[i]*LOAD, cuts[i+1]*LOAD, LOAD), f".ph{i}{{opacity:0;animation:ph{i} {LOAD}s steps(1) forwards}}"]
    els.append(f'<text class="mono ph{i}" x="{W/2}" y="{H/2-34}" text-anchor="middle" font-size="14" letter-spacing="1.2" fill="#b0b6c2">{t}</text>')
for i, p in enumerate(pct_curve):
    a = pct_at[i] * LOAD
    b = pct_at[i+1] * LOAD if i + 1 < len(pct_at) else LOAD + OUT
    css += [win(f"pc{i}", a, b, LOAD+OUT), f".pc{i}{{opacity:0;animation:pc{i} {LOAD+OUT}s steps(1) forwards}}"]
    els.append(f'<text class="mono pc{i}" x="{W/2}" y="{H/2+32}" text-anchor="middle" font-size="12" letter-spacing="2" fill="rgba(142,174,255,.8)">{p:03d}%</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Daniel Grigoriev, Threat Hunter and Software Engineer">
<style>{"".join(css)}</style>
<defs>
<linearGradient id="bg" x1="0" x2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#161b22"/></linearGradient>
<linearGradient id="acc" x1="0" x2="1"><stop offset="0" stop-color="#4169e1"/><stop offset="1" stop-color="#8eaeff"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g class="ltext">
{chr(10).join(els)}
</g>
<rect class="track" x="{bx}" y="{by}" width="{bw}" height="2" rx="1" fill="rgba(237,237,240,.08)"/>
<g class="mover"><rect class="fill" x="{bx}" y="{by}" width="{bw}" height="2" rx="1" fill="url(#acc)"/></g>
<text class="sans name" x="{W/2}" y="{name_y}" text-anchor="middle" font-size="42" font-weight="700" fill="#e6edf3">Daniel Grigoriev</text>
<text class="sans desc" x="{W/2}" y="{desc_y}" text-anchor="middle" font-size="18" font-weight="500" fill="#8b949e">Threat Hunter · Software Engineer</text>
</svg>'''
open("assets/header.svg", "w").write(svg)
print(f"header.svg: load {LOAD}s, total {TOTAL:.2f}s, {len(svg)} bytes")
