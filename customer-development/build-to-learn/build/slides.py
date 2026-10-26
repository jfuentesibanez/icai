from build import *
from experiments import E, LEVELS

META = dict(title="Build to Learn", file="index.html")

TB = "Bland and Osterwalder, <i>Testing Business Ideas</i>, Wiley, 2019"

S = []

# ---------- Opening ----------

S.append(section("cover", f"""
{kicker("ICAI · Innovation &amp; Entrepreneurship · Customer Discovery")}
<div style="display:flex;flex-direction:column;gap:32px;width:1100px">
<h1 style="{RUBIK};font-size:136px;font-weight:700;line-height:1.02">Build to learn</h1>
<p style="font-size:44px;color:{GREY}">Prototypes and experiments in the age of AI</p>
</div>
<p style="font-size:24px;color:{GREY}">Javier Fuentes</p>
<p style="position:absolute;left:1330px;top:170px;width:420px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{GREY}">Last session</p>
{postit("We wrote our hypotheses", -4, YELLOW, 48, "position:absolute;left:1330px;top:220px;width:400px")}
<p style="position:absolute;left:1350px;top:500px;width:420px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEAL}">Today</p>
{postit("We find the cheapest way to prove them wrong", 3, YELLOW, 48, "position:absolute;left:1350px;top:550px;width:420px")}
""", layout="between"))

S.append(section("route", f"""
{head("Today’s route · 95 min", "Five steps, from a hypothesis to a plan for the week")}
<table style="font-family:'Nunito Sans', Arial, sans-serif;font-size:28px;color:{NAVY}">
<tr><th style="width:8%">#</th><th style="width:12%">Time</th><th style="width:46%">Step</th><th style="width:34%">Output</th></tr>
<tr><td>1</td><td>10 min</td><td>What changed with AI</td><td>Shared context</td></tr>
<tr><td>2</td><td>30 min</td><td>Four levels: say, show, fake, real</td><td>A menu of techniques</td></tr>
<tr><td>3</td><td>20 min</td><td>Experiments: the test card</td><td>How to measure</td></tr>
<tr style="background:{LTEAL}"><td>4</td><td>20 min</td><td>Team work: design your experiment</td><td>One test card per team</td></tr>
<tr style="background:{CREAM}"><td>5</td><td>15 min</td><td>On stage: your experiment</td><td>A plan for the week</td></tr>
</table>
"""))

# ---------- Step 1 · What changed ----------

S.append(section("recap", f"""
{head("Step 1 · Where we are", "You have 3 critical hypotheses. Now we test them.")}
<div style="display:flex;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:24px">{kicker("D · Desirable", GREY)}{postit("I think 6 in 10 students away from home spend more than 40 euros a week on delivery", -2, D_COL, 40)}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:24px">{kicker("F · Feasible", GREY)}{postit("I think 2 kitchens in Madrid will cook 200 meals a day for us", 1, F_COL, 40)}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:24px">{kicker("V · Viable", GREY)}{postit("I think we can cook and deliver a meal for less than 4 euros and sell it for 6", -1, V_COL, 40)}</div>
</div>
{lead(f"Each one ended with <b style='color:{NAVY}'>“and we will know it is true when…”</b>. Today we build that “when”.")}
""", layout="between"))

S.append(section("before", f"""
{head("Step 1 · What changed", "Our old rule: your first MVP with less than 100 euros, in less than a day")}
{row(
    card("Low fidelity", "Paper, cardboard, storyboard", "A first draft. No interaction at all.", WHITE),
    card("Medium fidelity", "Clickable mockup, landing page", "Incomplete. Some parts done by hand behind the screen.", WHITE),
    card("High fidelity", "Real software", "Close to the final product. Needed a developer and weeks of work.", LINE),
)}
{lead("Low fidelity was the default because <b style='color:" + NAVY + "'>building real things was slow and expensive.</b>")}
""", layout="between"))

S.append(section("now", f"""
{head("Step 1 · What changed", "Now one person with an AI tool can build a working product")}
<table style="font-family:'Nunito Sans', Arial, sans-serif;font-size:32px;color:{NAVY}">
<tr><th style="width:24%"></th><th style="width:38%;color:{GREY}">Before</th><th style="width:38%;color:{TEAL}">Now</th></tr>
<tr><td style="font-weight:700">Who builds</td><td style="color:{GREY}">A developer</td><td>You, describing it in plain words</td></tr>
<tr><td style="font-weight:700">How long</td><td style="color:{GREY}">Weeks</td><td>Hours or days</td></tr>
<tr><td style="font-weight:700">What you get</td><td style="color:{GREY}">Screens that look real</td><td>Login, data, payments, AI features</td></tr>
<tr style="background:{CREAM}"><td style="font-weight:700">The hard part</td><td style="color:{GREY}">Building it</td><td style="font-weight:700">Knowing what to build, and for whom</td></tr>
</table>
{lead("So is it still a prototype? Often it is a real product. <b style='color:" + NAVY + "'>The question changes: not “can we build it?” but “should we?”</b>")}
""", layout="between"))

S.append(section("anchor", f"""
{kicker("Step 1 · What changed", YELLOW)}
<p style="{RUBIK};font-size:96px;font-weight:700;line-height:1.1;width:1500px">Building is no longer the hard part.<br><span style="color:{YELLOW}">Knowing what to build is.</span></p>
""", bg="navy", layout="center"))

S.append(section("risk-moved", f"""
{head("Step 1 · What changed", "AI made one risk cheaper. Not the other two.")}
{row(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;padding:40px;background:{D_COL};border-radius:16px">{tag("D", True)}<h3 style="{RUBIK};font-size:44px;font-weight:700">Desirable</h3><p style="font-size:28px;line-height:1.4">Do customers want it? <b>Still yours to prove.</b> AI cannot want things for your customers.</p></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;padding:40px;background:{WHITE};border:2px dashed {F_COL};border-radius:16px">{tag("F")}<h3 style="{RUBIK};font-size:44px;font-weight:700;color:{GREY}">Feasible</h3><p style="font-size:28px;line-height:1.4;color:{GREY}">Can we build it? <b>For software, much cheaper now.</b> Hardware, kitchens and partners: not yet.</p></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;padding:40px;background:{V_COL};border-radius:16px">{tag("V", True)}<h3 style="{RUBIK};font-size:44px;font-weight:700">Viable</h3><p style="font-size:28px;line-height:1.4">Do we earn more than we spend? <b>Still yours to prove.</b> Your rivals can build fast too.</p></div>',
)}
{lead("The trap: <b style='color:" + NAVY + "'>build the wrong thing, faster.</b> A working app feels like evidence. It is not.")}
""", layout="between"))

# ---------- Step 2 · Four levels ----------

LADDER = [
    ("1", "Say", "They talk, you listen", "Interviews, observation", LINE),
    ("2", "Show", "They see it, but cannot use it", "Storyboard, video, mockup", LTEAL),
    ("3", "Fake", "They try to use it. You, or an AI, do the work behind", "Landing page, Wizard of Oz", F_COL),
    ("4", "Real", "They use it, come back and pay", "Working app, pre-sale, pilot", YELLOW),
]
steps = "".join(
    f'<div data-build-in="rise {n}" style="position:absolute;left:{128 + (int(n) - 1) * 420}px;top:{640 - (int(n) - 1) * 110}px;'
    f'width:400px;height:{300 + (int(n) - 1) * 110}px;background:{col};border-radius:16px 16px 0 0;padding:28px;'
    f'display:flex;flex-direction:column;gap:10px">'
    f'<p style="{RUBIK};font-size:28px;font-weight:800;color:{TEAL}">Level {n}</p>'
    f'<h3 style="{RUBIK};font-size:56px;font-weight:800;line-height:1">{name}</h3>'
    f'<p style="font-size:26px;line-height:1.3">{what}</p>'
    f'<p style="font-size:22px;line-height:1.3;color:{GREY}">{ex}</p></div>'
    for n, name, what, ex, col in LADDER)
S.append(section("ladder", f"""
{head("Step 2 · The new fidelity ladder", "Four levels: say, show, fake, real")}
{steps}
<p style="position:absolute;left:128px;top:960px;width:1664px;border-top:3px solid {NAVY};padding-top:12px;font-size:24px;font-weight:700;color:{GREY};display:flex;justify-content:space-between"><span>Cheap and fast · weak evidence</span><span>More effort · strong evidence</span></p>
"""))

def level_slide(lid):
    n, name, title = LEVELS[lid]
    cells = [technique(e["name"], e["short"], e["tools_short"], e["letters"], goto=e["id"])
             for e in E if e["level"] == lid]
    return section(lid, f"""
{head(f"Level {n} of 4 · {name}", title, size=64)}
{grid(cells)}
""")


for lid in LEVELS:
    S.append(level_slide(lid))

S.append(section("why-not-real", f"""
{head("Step 2 · Choosing a level", "Real is cheap now. Why not always start there?")}
<div style="display:flex;flex-direction:column">
<div data-build-in="rise 1" style="display:flex;gap:24px;align-items:center;padding:26px 0;border-top:2px solid {LINE}"><p style="{RUBIK};width:60px;font-size:44px;font-weight:800;color:{TEAL}">1</p><p style="flex:1;font-size:34px;line-height:1.3">A real app answers “can we build it?”. That is rarely your riskiest question.</p></div>
<div data-build-in="rise 2" style="display:flex;gap:24px;align-items:center;padding:26px 0;border-top:2px solid {LINE}"><p style="{RUBIK};width:60px;font-size:44px;font-weight:800;color:{TEAL}">2</p><p style="flex:1;font-size:34px;line-height:1.3">With no users, a real app teaches nothing. Getting users is the experiment.</p></div>
<div data-build-in="rise 3" style="display:flex;gap:24px;align-items:center;padding:26px 0;border-top:2px solid {LINE};border-bottom:2px solid {LINE}"><p style="{RUBIK};width:60px;font-size:44px;font-weight:800;color:{TEAL}">3</p><p style="flex:1;font-size:34px;line-height:1.3">After weeks on a product, you defend it. You stop listening.</p></div>
</div>
<p data-build-in="fade 4" style="font-size:36px;line-height:1.4;font-weight:700;background:{YELLOW};padding:24px 32px;border-radius:12px">Start at the cheapest level that could prove your hypothesis wrong.</p>
""", layout="between"))

# ---------- Step 3 · Experiments ----------

S.append(section("test-card", f"""
{kicker("Step 3 · Experiments · The test card", YELLOW)}
<p style="{RUBIK};font-size:58px;font-weight:500;line-height:1.5">We believe that <span style="color:{YELLOW}">[hypothesis]</span>.<br>To verify that, we will <span style="color:{YELLOW}">[experiment]</span>.<br>And measure <span style="color:{YELLOW}">[metric]</span>.<br>We are right if <span style="color:{YELLOW}">[pass mark]</span>.</p>
<p style="font-size:24px;color:#BFD0DD">Source: Strategyzer Test Card · {TB}</p>
""", bg="navy", layout="between"))

def tc_row(label, text, build, last=False):
    bb = f"border-bottom:2px solid {LINE};" if last else ""
    return (f'<div data-build-in="rise {build}" style="display:flex;gap:32px;padding:22px 0;border-top:2px solid {LINE};{bb}">'
            f'<p style="width:360px;font-size:28px;font-weight:700;color:{TEAL}">{label}</p>'
            f'<p style="flex:1;font-size:30px;line-height:1.35">{text}</p></div>')

S.append(section("test-card-case", f"""
{head("Step 3 · Case: home-cooked meals for students", "One test card, filled in")}
<div style="display:flex;flex-direction:column">
{tc_row("We believe that", "students away from home in Madrid will pay 6 euros for a home-cooked meal.", 1)}
{tc_row("To verify that, we will", "build a landing page with a 6-euro pre-order button and show it with Instagram ads to students in Madrid for 7 days.", 2)}
{tc_row("And measure", "how many visitors pay.", 3)}
{tc_row("We are right if", "<b>at least 20 of the first 100 visitors pre-order.</b>", 4, last=True)}
</div>
<div data-build-in="fade 5">{pills("Level:", ["4 · Real (they pay)", "Time: 1 week", "Evidence: strong"])}</div>
""", layout="between"))

EVID = [
    ("They say", "“I would buy it”, surveys, likes", "Weak", LINE),
    ("They click", "Sign-ups, clicks on an ad or a fake door", "Medium", LTEAL),
    ("They use", "They come back next week, they spend time", "Strong", F_COL),
    ("They pay", "Pre-order, letter of intent, pilot contract", "Strongest", YELLOW),
]
ev = "".join(
    f'<div data-build-in="rise {k + 1}" style="flex:1;display:flex;flex-direction:column;gap:12px;padding:32px;'
    f'background:{col};border-radius:16px;margin-top:{(3 - k) * 60}px">'
    f'<p style="font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{GREY}">{s}</p>'
    f'<h3 style="{RUBIK};font-size:44px;font-weight:800">{t}</h3>'
    f'<p style="font-size:26px;line-height:1.35">{x}</p></div>'
    for k, (t, x, s, col) in enumerate(EVID))
S.append(section("evidence", f"""
{head("Step 3 · Experiments", "What people do is worth more than what they say")}
<div style="display:flex;gap:20px;align-items:flex-start">{ev}</div>
{source(TB)}
"""))

def col_list(letter, title, q, items):
    c = {"D": D_COL, "F": F_COL, "V": V_COL}[letter]
    lis = "".join(f'<li style="padding:12px 0;border-top:1px solid rgba(21,35,59,0.15)">{x}</li>' for x in items)
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;padding:32px;background:{c};border-radius:16px">'
            f'<div style="display:flex;gap:16px;align-items:center">{tag(letter, True)}<h3 style="{RUBIK};font-size:40px;font-weight:700">{title}</h3></div>'
            f'<p style="font-size:26px;color:{GREY}">{q}</p>'
            f'<ul style="list-style:none;padding:0;font-size:28px;line-height:1.3">{lis}</ul></div>')

S.append(section("by-risk", f"""
{head("Step 3 · Experiments", "Which experiment for which risk?")}
{row(
    col_list("D", "Desirable", "Do customers want it?", ["Problem interviews", "Ad test and landing page", "Fake door", "Explainer video", "5-second test"]),
    col_list("F", "Feasible", "Can we build and deliver it?", ["Wizard of Oz", "Concierge", "Frankenstein", "Working app", "Pilot"]),
    col_list("V", "Viable", "Do we earn more than we spend?", ["Pre-sale", "Letter of intent", "Crowdfunding", "Two prices, A/B", "Pilot with a budget"]),
)}
""", layout="between"))

S.append(section("ai-adds", f"""
{head("Step 3 · Experiments", "What AI adds to an experiment")}
{row(
    card("1", "Three versions, not one", "Three landing pages with three promises, in the time one used to take. Let the data choose.", WHITE, TEAL),
    card("2", "Real usage data", "A working product shows who comes back after a week. That is stronger than any “I would use it”.", WHITE, TEAL),
    card("3", "A faster loop", "Build on Monday, show it on Tuesday, decide on Friday. One learning cycle per week.", WHITE, TEAL),
)}
<div style="display:flex;gap:16px;align-items:center;padding:24px 32px;background:{WHITE};border:2px solid {RUST};border-radius:12px"><p style="font-size:30px;line-height:1.35"><b style="color:{RUST}">But:</b> an AI’s opinion of your idea is not evidence. Only real customers can prove a hypothesis wrong.</p></div>
""", layout="between"))

S.append(section("fair", f"""
{head("Step 3 · Experiments", "Play fair with the people in your test")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px 48px">
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">1</p><p style="flex:1;font-size:32px;line-height:1.3">After a fake door or a Wizard of Oz, tell people the truth.</p></div>
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">2</p><p style="flex:1;font-size:32px;line-height:1.3">Never keep money for something you will not deliver. Refund it.</p></div>
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">3</p><p style="flex:1;font-size:32px;line-height:1.3">Ask before you collect personal data, and collect only what you need.</p></div>
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">4</p><p style="flex:1;font-size:32px;line-height:1.3">Tell people when they are talking to an AI, not to a person.</p></div>
</div>
{lead("A test that tricks people damages your brand before it exists.")}
""", layout="between"))

ARROW = (f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="width:36px;height:24px;flex:none" aria-hidden="true">'
         f'<polygon points="0,30 60,30 60,0 100,50 60,100 60,70 0,70" fill="{TEAL}"/></svg>')

def path(label, steps):
    chips = ARROW.join(
        f'<p style="font-size:24px;background:{YELLOW if k == len(steps) - 1 else LTEAL};padding:12px 20px;border-radius:999px;white-space:nowrap">{s}</p>'
        for k, s in enumerate(steps))
    return (f'<div style="display:flex;gap:24px;align-items:center;padding:28px 0;border-top:2px solid {LINE}">'
            f'<p style="width:300px;flex:none;font-size:30px;font-weight:700">{label}</p>'
            f'<div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">{chips}</div></div>')

S.append(section("paths", f"""
{head("Step 3 · Experiments", "A typical path, from cheap to strong")}
<div style="display:flex;flex-direction:column;border-bottom:2px solid {LINE}">
{path("B2C app", ["Interviews", "Ad test", "Landing page", "Working app", "Pre-sale"])}
{path("B2B software or service", ["Interviews", "Clickable demo", "Concierge", "Letter of intent", "Pilot"])}
{path("Physical product", ["Interviews", "Product box", "3D print", "Pre-sale", "Crowdfunding"])}
</div>
{lead("Each step only if the one before said yes. A no is also a result: change the hypothesis, not the pass mark.")}
""", layout="between"))

# ---------- Step 4 · Team work ----------

S.append(section("team-intro", f"""
{kicker("Step 4 · Team work · 20 min", YELLOW)}
<h1 style="{RUBIK};font-size:160px;font-weight:800;line-height:1">Your experiment</h1>
<p style="{RUBIK};font-size:64px;font-weight:500;line-height:1.15">One hypothesis, one test card</p>
<p style="font-size:32px;line-height:1.4;color:#DCEBF2;width:1300px">Goal: the cheapest test that can prove your most critical hypothesis wrong, ready to run this week.</p>
""", bg="teal", layout="center"))

def step_card(n, mins, title, text, hi=False):
    bg = YELLOW if hi else WHITE
    border = "" if hi else f"border:2px solid {LINE};"
    pillbg = PAPER if hi else LTEAL
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;padding:32px;background:{bg};{border}border-radius:16px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><p style="{RUBIK};font-size:56px;font-weight:800;color:{NAVY if hi else TEAL}">{n}</p>'
            f'<p style="font-size:24px;font-weight:700;background:{pillbg};padding:6px 16px;border-radius:999px">{mins}</p></div>'
            f'<h3 style="{RUBIK};font-size:40px;font-weight:700">{title}</h3>'
            f'<p style="font-size:26px;line-height:1.4;color:{NAVY if hi else GREY}">{text}</p></div>')

S.append(section("team-steps", f"""
{head("Step 4 · Step by step", "Four moves in 20 minutes")}
{row(
    step_card("1", "3 min", "Pick", "One hypothesis from your Top 3: the most critical and the most uncertain."),
    step_card("2", "5 min", "Choose", "The level and the technique. Start as low as you can."),
    step_card("3", "8 min", "Write", "The test card. Set the pass mark now, not after you see the data."),
    step_card("4", "4 min", "Plan", "The tool, who builds it, and the day it goes live.", hi=True),
)}
{pills("House rules:", ["One hypothesis per card", "A number in the pass mark", "Real customers, not friends"])}
""", layout="between"))

S.append(section("team-template", f"""
{kicker("Your test card · copy it onto the board", YELLOW)}
<div style="display:flex;flex-direction:column;gap:8px;font-size:40px;line-height:1.5">
<p><b style="color:{YELLOW}">We believe that</b> ……………………………………………</p>
<p><b style="color:{YELLOW}">To verify that, we will</b> ……………………………………</p>
<p><b style="color:{YELLOW}">And measure</b> …………………………………………………</p>
<p><b style="color:{YELLOW}">We are right if</b> ……………………………………………</p>
</div>
<div style="display:flex;gap:24px;align-items:center">
<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#BFD0DD">Also write</p>
<p style="font-size:32px">Level (1 to 4) · D, F or V · Cost · Live by (date)</p>
</div>
""", bg="navy", layout="between"))

# ---------- Step 5 · On stage ----------

S.append(section("pitch", f"""
{head("Step 5 · On stage · 2 min per team", "Your experiment, out loud", kcolor="#8A5A00")}
{row(
    card(f'<span style="{RUBIK};font-size:56px;font-weight:800;color:{TEAL}">1</span>', "The hypothesis", "Read it exactly as written, and say if it is D, F or V.", PAPER),
    card(f'<span style="{RUBIK};font-size:56px;font-weight:800;color:{TEAL}">2</span>', "The test", "The level, the technique and the tool you will use.", PAPER),
    card(f'<span style="{RUBIK};font-size:56px;font-weight:800;color:{YELLOW}">3</span>', "The pass mark", "The number that proves you right. Or wrong.", NAVY, PAPER, "#DCE3EA", PAPER),
)}
{lead(f"Next session: <b style='color:{NAVY}'>bring the result.</b> A failed test is a good result if you learn from it.", 28)}
""", bg="cream", layout="between"))

S.append(section("close", f"""
<p style="{CAVEAT};font-size:120px;line-height:1.1;color:{YELLOW};text-align:center;width:1500px">Code is cheap now. Evidence is not.</p>
<p style="{RUBIK};font-size:56px;font-weight:500;text-align:center">Build to learn.</p>
<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#BFD0DD;text-align:center">ICAI · Innovation &amp; Entrepreneurship · Customer Discovery</p>
""", bg="navy", layout="center", extra=";align-items:center"))

# ---------- Appendix · Experiment cards ----------

def index_col(lid):
    n, name, _ = LEVELS[lid]
    items = "".join(
        f'<p data-goto="{e["id"]}" style="font-size:28px;padding:12px 0;border-top:1px solid rgba(250,248,243,0.2)">{e["name"]}</p>'
        for e in E if e["level"] == lid)
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
            f'<p style="{RUBIK};font-size:24px;font-weight:800;color:{YELLOW}">Level {n}</p>'
            f'<h3 style="{RUBIK};font-size:48px;font-weight:700;margin-bottom:12px">{name}</h3>{items}</div>')

S.append(section("cards", f"""
<div style="display:flex;flex-direction:column;gap:12px">{kicker("Appendix · Click a name to open its card", YELLOW)}
<h2 style="{RUBIK};font-size:72px;font-weight:700;line-height:1.1">Experiment cards</h2></div>
<div style="display:flex;gap:48px">{"".join(index_col(l) for l in LEVELS)}</div>
""", bg="navy", layout="between"))

for e in E:
    n, name, _ = LEVELS[e["level"]]
    S.append(experiment_card(e, n, name, e["level"], "cards"))
