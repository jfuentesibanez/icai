"""Engine for the Customer Development workshop decks (same look as ../hypotheses).

Content lives in slides.py. Run:  python3 build.py   (stdlib only) -> ../index.html
"""
import html
import pathlib

NAVY, PAPER, TEAL, YELLOW, CREAM = "#15233B", "#FAF8F3", "#0F6E96", "#F7DC5C", "#FBF0C2"
LTEAL, GREY, LINE, RUST, WHITE = "#EAF3F7", "#4A5568", "#E4E7EB", "#B5520B", "#FFFFFF"
D_COL, F_COL, V_COL = YELLOW, "#CFE4EE", "#F2C9B0"
RUBIK = "font-family:Rubik, Arial, sans-serif"
CAVEAT = "font-family:Caveat, 'Brush Script MT', cursive"
SHADOW = "box-shadow:0 12px 24px rgba(21,35,59,0.18)"

BG = {"paper": (PAPER, NAVY), "navy": (NAVY, PAPER), "teal": (TEAL, PAPER), "cream": (CREAM, NAVY)}
LAYOUT = {"gap": "gap:40px", "between": "justify-content:space-between",
          "center": "justify-content:center;gap:32px"}


def section(sid, body, bg="paper", layout="gap", extra=""):
    b, c = BG[bg]
    return (f'<section id="{sid}" data-transition="fade" style="background:{b};color:{c};'
            f"font-family:'Nunito Sans', Arial, sans-serif;padding:128px;display:flex;"
            f'flex-direction:column;{LAYOUT[layout]}{extra}">\n{body}\n</section>\n')


def kicker(text, color=TEAL):
    return (f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;'
            f'color:{color}">{text}</p>')


def head(k, title, kcolor=TEAL, size=72):
    return (f'<div style="display:flex;flex-direction:column;gap:12px">{kicker(k, kcolor)}'
            f'<h2 style="{RUBIK};font-size:{size}px;font-weight:700;line-height:1.1">{title}</h2></div>')


def postit(text, rot=0, bg=YELLOW, size=44, extra=""):
    return (f'<p style="{CAVEAT};font-size:{size}px;line-height:1.15;background:{bg};color:{NAVY};'
            f'padding:32px;{SHADOW};transform:rotate({rot}deg);{extra}">{text}</p>')


def pill(text, bg=LTEAL, color=NAVY, bold=False):
    w = "font-weight:700;" if bold else ""
    return (f'<p style="font-size:24px;{w}background:{bg};color:{color};padding:10px 20px;'
            f'border-radius:999px">{text}</p>')


def pills(label, items):
    return ('<div style="display:flex;gap:16px;align-items:center;flex-wrap:wrap">'
            f'<p style="font-size:24px;font-weight:700;color:{GREY}">{label}</p>'
            + "".join(pill(i) for i in items) + "</div>")


def tag(letter, on_colour=False):
    col = WHITE if on_colour else {"D": D_COL, "F": F_COL, "V": V_COL}[letter]
    return (f'<span style="display:inline-flex;width:40px;height:40px;border-radius:8px;background:{col};'
            f'{RUBIK};font-size:22px;font-weight:800;color:{NAVY};align-items:center;'
            f'justify-content:center">{letter}</span>')


def tags(letters):
    if letters == "!":
        return (f'<span style="font-size:18px;font-weight:700;letter-spacing:1px;text-transform:uppercase;'
                f'color:{RUST};border:2px solid {RUST};border-radius:8px;padding:6px 10px">Not evidence</span>')
    return '<span style="display:flex;gap:6px">' + "".join(tag(l) for l in letters) + "</span>"


def technique(name, what, tools, letters, build=None, goto=None):
    b = f' data-build-in="rise {build}"' if build else ""
    g = f' data-goto="{goto}"' if goto else ""
    more = (f'<span style="font-size:20px;font-weight:700;color:{GREY};white-space:nowrap">Card →</span>'
            if goto else "")
    return (f'<div{b}{g} style="display:flex;flex-direction:column;gap:10px;padding:26px 28px;background:{WHITE};'
            f'border:2px solid {LINE};border-radius:14px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:12px">'
            f'<h3 style="{RUBIK};font-size:32px;font-weight:700;line-height:1.1">{name}</h3>{tags(letters)}</div>'
            f'<p style="flex:1;font-size:24px;line-height:1.3;color:{GREY}">{what}</p>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:16px">'
            f'<p style="font-size:20px;line-height:1.3;color:{TEAL};font-weight:700">{tools}</p>{more}</div></div>')


def goto_pill(target, text, dark=False):
    bg, col = (NAVY, PAPER) if dark else (LTEAL, NAVY)
    return (f'<p data-goto="{target}" style="font-size:22px;font-weight:700;background:{bg};color:{col};'
            f'padding:10px 20px;border-radius:999px;white-space:nowrap">{text}</p>')


def box(label, text, bg=WHITE, border=LINE, label_color=TEAL):
    return (f'<div style="display:flex;flex-direction:column;gap:10px;padding:24px 28px;background:{bg};'
            f'border:2px solid {border};border-radius:14px">'
            f'<p style="font-size:20px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{label_color}">{label}</p>'
            f'<p style="font-size:25px;line-height:1.35">{text}</p></div>')


def experiment_card(e, n, level_name, level_id, index_id):
    steps = "".join(
        f'<div style="display:flex;gap:20px;align-items:baseline;padding:14px 0;border-top:2px solid {LINE}">'
        f'<p style="{RUBIK};width:36px;flex:none;font-size:34px;font-weight:800;color:{TEAL}">{k + 1}</p>'
        f'<p style="flex:1;font-size:27px;line-height:1.3">{s}</p></div>'
        for k, s in enumerate(e["steps"]))
    src = f' · Source: {e["src"]}' if e["src"] else ""
    body = f"""
<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:32px">
<div style="display:flex;flex-direction:column;gap:12px">{kicker(f"Experiment card · Level {n} · {level_name}")}
<div style="display:flex;gap:24px;align-items:center"><h2 style="{RUBIK};font-size:72px;font-weight:700;line-height:1.1">{e["name"]}</h2>{tags(e["letters"])}</div></div>
<div style="display:flex;gap:12px">{goto_pill(level_id, f"← Level {n}")}{goto_pill(index_id, "All cards")}</div>
</div>
<div style="flex:1;display:flex;gap:48px;min-height:0">
<div style="width:820px;flex:none;display:flex;flex-direction:column;gap:28px">
<p style="font-size:32px;line-height:1.35">{e["what"]}</p>
<div style="display:flex;flex-direction:column">{kicker("How to run it", GREY)}<div style="margin-top:12px;border-bottom:2px solid {LINE}">{steps}</div></div>
</div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:16px">
{box("What you measure", e["measure"], LTEAL, LTEAL)}
{box("Example", e["example"], CREAM, CREAM, "#8A5A00")}
{box("With AI", e["ai"])}
{box("Watch out", e["watch"], WHITE, RUST, RUST)}
</div>
</div>
<p style="font-size:22px;color:{GREY}"><b style="color:{NAVY}">Tools:</b> {e["tools"]} · <b style="color:{NAVY}">Effort:</b> {e["effort"]} · <b style="color:{NAVY}">Evidence:</b> {e["evidence"]}{src}</p>"""
    return section(e["id"], body)


def grid(cells, cols=3, gap=20):
    return (f'<div style="flex:1;display:grid;grid-template-columns:repeat({cols},1fr);'
            f'grid-auto-rows:1fr;gap:{gap}px">' + "".join(cells) + "</div>")


def card(top, title, text, bg=WHITE, top_color=GREY, text_color=GREY, title_color=NAVY, size=36):
    border = f"border:2px solid {LINE};" if bg == WHITE else ""
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;padding:32px;background:{bg};'
            f'{border}border-radius:16px">'
            f'<p style="font-size:24px;font-weight:700;color:{top_color}">{top}</p>'
            f'<h3 style="{RUBIK};font-size:{size}px;font-weight:700;line-height:1.15;color:{title_color}">{title}</h3>'
            f'<p style="font-size:26px;line-height:1.4;color:{text_color}">{text}</p></div>')


def row(*cells, gap=24, align="stretch"):
    return f'<div style="display:flex;gap:{gap}px;align-items:{align}">' + "".join(cells) + "</div>"


def lead(text, size=32, width=None, color=GREY):
    w = f"width:{width}px;" if width else ""
    return f'<p style="font-size:{size}px;line-height:1.4;color:{color};{w}">{text}</p>'


def source(text):
    return (f'<p style="position:absolute;left:128px;bottom:56px;font-size:20px;color:{GREY}">'
            f"Source: {text}</p>")


def esc(s):
    return html.escape(s, quote=False)


HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TITLE</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@400..800&family=Nunito+Sans:wght@400..800&family=Caveat:wght@400..700&display=swap">
<style>
*{box-sizing:border-box;margin:0}
html,body{height:100%;background:#0b1220;overflow:hidden}
#stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
#stage>section{position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden}
#stage>section:not(.on){display:none!important}
ul{padding-left:1.2em} li{margin:0}
table{border-collapse:collapse;width:100%} th,td{padding:0.35em 0.6em;border-bottom:1px solid #d9dde3;text-align:left}
th{font-weight:700}
[data-build-in]{transition:opacity .45s ease, translate .45s ease}
[data-build-in].hid{opacity:0;translate:0 24px}
#bar{position:fixed;right:16px;bottom:12px;font:14px system-ui,sans-serif;color:#9aa6b8;user-select:none}
[data-goto]{cursor:pointer}
[data-goto]:hover{outline:3px solid #0F6E96;outline-offset:2px}
#bar button{background:#1c2638;color:#dfe6f0;border:0;border-radius:6px;padding:6px 12px;margin-left:6px;cursor:pointer;font:inherit}
</style></head><body>
<div id="stage">
"""

TAIL = """</div>
<div id="bar"><span id="count"></span><button id="prev" aria-label="Previous">‹</button><button id="next" aria-label="Next">›</button><button id="fs" aria-label="Full screen">⛶</button></div>
<script>
const stage=document.getElementById('stage');
const S=[...stage.children];
let i=0, step=0;
function fit(){const k=Math.min(innerWidth/1920,innerHeight/1080);const x=(innerWidth-1920*k)/2,y=(innerHeight-1080*k)/2;stage.style.transform=`translate(${x}px,${y}px) scale(${k})`;}
function builds(s){const els=[...s.querySelectorAll('[data-build-in]')];const ord=[...new Set(els.map(e=>+(e.dataset.buildIn.split(' ')[1]||1)))].sort((a,b)=>a-b);return {els,ord};}
function show(n,all){S.forEach(s=>s.classList.remove('on'));i=Math.max(0,Math.min(S.length-1,n));const s=S[i];s.classList.add('on');const b=builds(s);step=all?b.ord.length:0;paint(b);document.getElementById('count').textContent=(i+1)+' / '+S.length;history.replaceState(null,'','#'+(i+1));}
function paint(b){b.els.forEach(e=>{const o=+(e.dataset.buildIn.split(' ')[1]||1);e.classList.toggle('hid',b.ord.indexOf(o)>=step);});}
function next(){const b=builds(S[i]);if(step<b.ord.length){step++;paint(b);}else if(i<S.length-1)show(i+1,false);}
function prev(){if(i>0)show(i-1,true);}
addEventListener('keydown',e=>{if(['ArrowRight','ArrowDown',' ','PageDown','Enter'].includes(e.key)){e.preventDefault();next();}else if(['ArrowLeft','ArrowUp','PageUp','Backspace'].includes(e.key)){e.preventDefault();prev();}else if(e.key==='f')toggleFs();else if(e.key==='Home')show(0,false);else if(e.key==='End')show(S.length-1,true);});
document.addEventListener('click',e=>{const g=e.target.closest('[data-goto]');if(!g)return;e.stopPropagation();const k=S.findIndex(s=>s.id===g.dataset.goto);if(k>=0)show(k,true);},true);
stage.addEventListener('click',next);
document.getElementById('next').onclick=next;document.getElementById('prev').onclick=prev;
function toggleFs(){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
document.getElementById('fs').onclick=toggleFs;
addEventListener('resize',fit);fit();
show((parseInt(location.hash.slice(1))||1)-1,false);
</script></body></html>
"""

if __name__ == "__main__":
    import slides
    here = pathlib.Path(__file__).parent
    out = here.parent / slides.META["file"]
    out.write_text(HEAD.replace("TITLE", esc(slides.META["title"])) + "\n".join(slides.S) + TAIL)
    print(f"{out} · {len(slides.S)} slides")
