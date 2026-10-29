from build import *

META = dict(title="Problem Interviews", file="index.html")

VPD = "Osterwalder, Pigneur, Bernarda and Smith, <i>Value Proposition Design</i>, Wiley, 2014"
MOM = "Rob Fitzpatrick, <i>The Mom Test</i>, 2013"
LA = "Croll and Yoskovitz, <i>Lean Analytics</i>, O’Reilly, 2013 · leananalyticsbook.com"

S = []

# ---------- Opening ----------

S.append(section("cover", f"""
{kicker("ICAI · Innovation &amp; Entrepreneurship · Customer Discovery")}
<div style="display:flex;flex-direction:column;gap:32px;width:1100px">
<h1 style="{RUBIK};font-size:136px;font-weight:700;line-height:1.02">Problem interviews</h1>
<p style="font-size:44px;color:{GREY}">How to learn from customers when everybody is polite to you</p>
</div>
<p style="font-size:24px;color:{GREY}">Javier Fuentes</p>
<p style="position:absolute;left:1330px;top:170px;width:420px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{GREY}">Last session</p>
{postit("We chose the cheapest test for each hypothesis", -4, YELLOW, 48, "position:absolute;left:1330px;top:220px;width:400px")}
<p style="position:absolute;left:1350px;top:540px;width:420px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEAL}">Today</p>
{postit("We prepare the first one: talking to customers", 3, YELLOW, 48, "position:absolute;left:1350px;top:590px;width:420px")}
""", layout="between"))

S.append(section("route", f"""
{head("Today’s route · 95 min", "Five steps, from a hypothesis to an interview script")}
<table style="font-family:'Nunito Sans', Arial, sans-serif;font-size:28px;color:{NAVY}">
<tr><th style="width:8%">#</th><th style="width:12%">Time</th><th style="width:46%">Step</th><th style="width:34%">Output</th></tr>
<tr><td>1</td><td>10 min</td><td>Why a problem interview</td><td>Shared context</td></tr>
<tr><td>2</td><td>25 min</td><td>Good and bad interviews</td><td>The rules</td></tr>
<tr><td>3</td><td>10 min</td><td>The structure of an interview</td><td>A 30-minute script</td></tr>
<tr style="background:{LTEAL}"><td>4</td><td>30 min</td><td>Team work: boards 15 and 16</td><td>Your script and your questions</td></tr>
<tr style="background:{CREAM}"><td>5</td><td>20 min</td><td>After the interview</td><td>Notes, score, plan for the week</td></tr>
</table>
"""))

# ---------- Step 1 · Why ----------

SKIN, INK = "#F2C9A5", NAVY
GLASSES = (f'<circle cx="89" cy="94" r="10" fill="none" stroke="{INK}" stroke-width="4"/>'
           f'<circle cx="111" cy="94" r="10" fill="none" stroke="{INK}" stroke-width="4"/>'
           f'<line x1="99" y1="94" x2="101" y2="94" stroke="{INK}" stroke-width="4"/>')
SMILE = f'<path d="M90 107 Q100 115 110 107" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'


def person(fid, bg, shirt, hair, front="", face=SMILE):
    """A simple bust in a circle; front is drawn over the body (the figure's tool)."""
    return (f'<svg viewBox="0 0 200 200" width="132" height="132" aria-hidden="true">'
            f'<defs><clipPath id="c-{fid}"><circle cx="100" cy="100" r="96"/></clipPath></defs>'
            f'<circle cx="100" cy="100" r="96" fill="{bg}"/><g clip-path="url(#c-{fid})">'
            f'<path d="M36 214 Q36 140 100 140 Q164 140 164 214Z" fill="{shirt}"/>'
            f'<rect x="88" y="116" width="24" height="28" fill="{SKIN}"/>'
            f'<circle cx="100" cy="92" r="32" fill="{SKIN}"/>{hair}'
            f'<circle cx="89" cy="94" r="3.4" fill="{INK}"/><circle cx="111" cy="94" r="3.4" fill="{INK}"/>{face}{front}</g></svg>')


def figure(name, bg):
    short = lambda c: f'<path d="M68 92 Q66 58 100 58 Q134 58 132 92 Q126 72 100 72 Q78 74 68 92Z" fill="{c}"/>'
    if name == "Data analyst":
        return person("da", bg, "#D9643A",
                      f'<circle cx="100" cy="50" r="14" fill="#3B2A20"/>{short("#3B2A20")}',
                      f'<line x1="79" y1="106" x2="56" y2="138" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
                      f'<circle cx="89" cy="94" r="16" fill="#FFFFFF" fill-opacity=".35" stroke="{INK}" stroke-width="5"/>')
    if name == "Journalist":
        return person("jo", bg, TEAL, short("#4A3426"),
                      f'<path d="M66 92 Q66 48 100 48 Q134 48 134 92" fill="none" stroke="#6B7685" stroke-width="6"/>'
                      f'<rect x="60" y="82" width="12" height="24" rx="5" fill="#6B7685"/>'
                      f'<rect x="128" y="82" width="12" height="24" rx="5" fill="#6B7685"/>'
                      f'<path d="M134 102 Q132 118 112 118" fill="none" stroke="#6B7685" stroke-width="4"/>'
                      f'<rect x="141" y="152" width="12" height="44" rx="4" fill="{INK}"/>'
                      f'<circle cx="147" cy="148" r="12" fill="#2B3443"/>')
    if name == "Anthropologist":
        return person("an", bg, "#5DA9D6", short("#E2B36A"),
                      f'{GLASSES}<line x1="86" y1="142" x2="82" y2="162" stroke="{INK}" stroke-width="3"/>'
                      f'<line x1="114" y1="142" x2="118" y2="162" stroke="{INK}" stroke-width="3"/>'
                      f'<rect x="78" y="160" width="44" height="30" rx="6" fill="{INK}"/>'
                      f'<circle cx="100" cy="175" r="10" fill="#9FB7C6" stroke="#FFFFFF" stroke-width="2"/>')
    if name == "Immersion":
        return person("im", bg, "#9BC53D",
                      '<path d="M66 100 Q62 56 100 56 Q138 56 134 100 L134 136 L122 136 L122 84 Q100 70 78 84 L80 136 L66 136Z" fill="#1F2A3A"/>',
                      f'<line x1="160" y1="122" x2="150" y2="168" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
                      f'<ellipse cx="160" cy="96" rx="22" ry="28" fill="#F7E6D6" stroke="{INK}" stroke-width="3"/>'
                      f'<circle cx="152" cy="92" r="7" fill="none" stroke="{TEAL}" stroke-width="3"/>'
                      f'<circle cx="169" cy="92" r="7" fill="none" stroke="{TEAL}" stroke-width="3"/>'
                      f'<path d="M153 108 Q160 113 167 108" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    if name == "Co-creation":
        return person("co", bg, "#D84B3A",
                      f'{short("#C0502A")}<path d="M69 80 Q100 62 131 80" fill="none" stroke="{YELLOW}" stroke-width="7"/>',
                      '<rect x="58" y="160" width="32" height="32" rx="3" fill="#3BA7D9"/>'
                      '<rect x="92" y="160" width="32" height="32" rx="3" fill="#F7DC5C"/>'
                      '<rect x="75" y="128" width="32" height="32" rx="3" fill="#2E8C6A"/>')
    if name == "Experiments":
        return person("ex", bg, "#FFFFFF",
                      '<path d="M68 96 Q66 78 74 74 L76 100Z M132 96 Q134 78 126 74 L124 100Z" fill="#8A8378"/>',
                      f'<path d="M36 214 Q36 140 100 140 Q164 140 164 214Z" fill="none" stroke="{LINE}" stroke-width="3"/>'
                      f'<rect x="92" y="144" width="16" height="60" fill="{INK}"/>{GLASSES}'
                      f'<path d="M132 140 L132 156 L118 186 Q116 194 124 194 L156 194 Q164 194 162 186 L148 156 L148 140Z" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>'
                      f'<path d="M124 174 L156 174 L160 186 Q161 190 157 190 L123 190 Q119 190 120 186Z" fill="{TEAL}"/>',
                      f'<path d="M88 108 Q100 100 112 108 Q100 113 88 108Z" fill="#3B2A20"/>')
    raise KeyError(name)


METHODS = [
    ("Data analyst", "Reads reports and studies about the market"),
    ("Journalist", "Talks to customers"),
    ("Anthropologist", "Observes what customers do"),
    ("Immersion", "Lives the customer’s day, in their place"),
    ("Co-creation", "Designs the product with customers"),
    ("Experiments", "Measures what customers actually do"),
]
methods = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;padding:28px;border-radius:16px;'
    f'background:{YELLOW if n == "Journalist" else WHITE};{"" if n == "Journalist" else f"border:2px solid {LINE};"}">'
    f'{figure(n, PAPER if n == "Journalist" else LTEAL)}'
    f'<p style="{RUBIK};font-size:24px;font-weight:800;color:{NAVY if n == "Journalist" else TEAL}">{k + 1}</p>'
    f'<h3 style="{RUBIK};font-size:32px;font-weight:700;line-height:1.1">{n.replace("-", "&#8209;")}</h3>'
    f'<p style="font-size:24px;line-height:1.35;color:{NAVY if n == "Journalist" else GREY}">{t}</p></div>'
    for k, (n, t) in enumerate(METHODS))
S.append(section("methods", f"""
{head("Step 1 · Why a problem interview", "Six ways to learn about customers. Today: the journalist.")}
<div style="display:flex;gap:20px">{methods}</div>
{lead("An interview is level 1 of the ladder from last session: <b style='color:" + NAVY + "'>they talk, you listen.</b> Cheap, fast, and the start of everything else.")}
{source(VPD)}
""", layout="between"))

S.append(section("problem-solution", f"""
{head("Step 1 · Why a problem interview", "Two kinds of interview. Today, only the first one.")}
{row(
    card("First · Today", "Problem interview", "Does this customer have the problem? How often? How do they solve it today, and what does it cost them? <b style='color:" + NAVY + "'>You never show your idea.</b>", YELLOW, NAVY, NAVY),
    card("Later", "Solution interview", "You show a first version of your solution. Does it solve the problem they told you about? Would they pay for it?", WHITE),
)}
{lead("Do not mix them. When you show your idea too early, people start to talk about your idea, not about their life.")}
""", layout="between"))

S.append(section("anchor", f"""
{kicker("Step 1 · The one rule", YELLOW)}
<p style="{RUBIK};font-size:96px;font-weight:700;line-height:1.1;width:1500px">Talk about their life,<br><span style="color:{YELLOW}">not about your idea.</span></p>
""", bg="navy", layout="center"))

def say(who, text, real=None, build=None):
    right = who == "Mom"
    col = TEAL if right else NAVY
    align = "align-items:flex-end;text-align:right" if right else "align-items:flex-start"
    r = (f'<p data-build-in="fade {build}" style="font-size:28px;line-height:1.3;font-weight:700;color:{RUST};max-width:1100px">'
         f'What she means: {real}</p>') if real else ""
    return (f'<div style="display:flex;flex-direction:column;gap:6px;{align}">'
            f'<p style="font-size:32px;line-height:1.3;max-width:1200px"><b style="color:{col}">{who}:</b> {text}</p>{r}</div>')

S.append(section("mom-test", f"""
{head("Step 1 · The Mom Test", "Even your mother will lie to you. She loves you.")}
<div style="display:flex;flex-direction:column;gap:14px">
{say("You", "Mom, I have a business idea. Do you have five minutes?")}
{say("Mom", "Of course, dear.", "I am proud of you and I do not want to hurt you.", 1)}
{say("You", "You use your iPad a lot, right?")}
{say("Mom", "Yes, it is great.", "I use it to read email on the sofa. Nothing else.", 2)}
{say("You", "Would you buy a cookbook app?")}
{say("Mom", "Sounds nice! Does it have vegan recipes?", "I have plenty of cookbooks, and I have never bought an app.", 3)}
</div>
{source(MOM)}
"""))

GOOD_Q = ["When did you last use your iPad? For what?", "Have you ever used it in the kitchen?",
          "Have you ever bought an app? Which one? How much did it cost?",
          "When did you last buy a cookbook? Why?", "Do you use your cookbooks? What do you dislike about them?"]
S.append(section("mom-right", f"""
{head("Step 1 · The Mom Test", "The same conversation, done right")}
<div style="display:flex;flex-direction:column;border-bottom:2px solid {LINE}">
{"".join(f'<p data-build-in="rise {k + 1}" style="font-size:36px;line-height:1.3;padding:20px 0;border-top:2px solid {LINE}">{q}</p>' for k, q in enumerate(GOOD_Q))}
</div>
{lead("No idea, no app, no “would you”. <b style='color:" + NAVY + "'>Only her real life, in the past.</b> She cannot lie to be nice, because there is nothing to be nice about.")}
""", layout="between"))

# ---------- Step 2 · Good and bad interviews ----------

def bad(title, text, example):
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;padding:36px;background:{WHITE};'
            f'border:2px solid {RUST};border-radius:16px">'
            f'<h3 style="{RUBIK};font-size:44px;font-weight:700;color:{RUST}">{title}</h3>'
            f'<p style="font-size:28px;line-height:1.4">{text}</p>'
            f'<p style="{CAVEAT};font-size:40px;line-height:1.15;color:{GREY}">{example}</p></div>')

S.append(section("bad-data", f"""
{head("Step 2 · Bad interviews", "Three kinds of answer that look like data, and are not")}
{row(
    bad("Compliments", "People are kind. A compliment costs them nothing and tells you nothing.", "“What a great idea!”"),
    bad("Ideas", "People love to give opinions, also about business. Do not write down the idea: ask why they want it.", "“You should add a chat!”"),
    bad("Wishful thinking", "The future and the conditional. Everybody is a perfect customer in the future.", "“I would buy it.” “I will use it.”"),
)}
{lead("Your job: bring the conversation back to <b style='color:" + NAVY + "'>facts from the past.</b>")}
""", layout="between"))

PHRASES = [
    ("“That is so cool. I love it!”", "Compliment"),
    ("“Looks great. Tell me when it launches.”", "Compliment"),
    ("“I know a couple of people for you, when you are ready.”", "Compliment"),
    ("“I would definitely buy that.”", "Compliment"),
    ("“What are the next steps?”", "Commitment"),
    ("“When can we start the trial?”", "Depends"),
    ("“Can I buy the prototype?”", "Commitment"),
    ("“When can you come back to talk to my team?”", "Commitment"),
]
VERDICT = {"Compliment": (RUST, WHITE), "Commitment": ("#1E7B4F", WHITE), "Depends": ("#C98A00", WHITE)}
quiz = "".join(
    f'<div style="display:flex;justify-content:space-between;align-items:center;gap:24px;padding:14px 0;border-top:2px solid {LINE}">'
    f'<p style="font-size:32px;line-height:1.25">{p}</p>'
    f'<p data-build-in="fade 1" style="flex:none;font-size:22px;font-weight:700;letter-spacing:1px;text-transform:uppercase;'
    f'background:{VERDICT[v][0]};color:{VERDICT[v][1]};padding:8px 18px;border-radius:999px">{v}</p></div>'
    for p, v in PHRASES)
S.append(section("compliment-commitment", f"""
{head("Step 2 · Quiz", "Compliment or commitment?", size=64)}
<div style="display:flex;flex-direction:column;border-bottom:2px solid {LINE}">{quiz}</div>
<p data-build-in="fade 1" style="font-size:28px;line-height:1.4;color:{GREY}">A commitment costs them something: <b style="color:{NAVY}">time, reputation or money.</b> A trial counts only with a date and a price.</p>
{source(MOM)}
""", layout="between"))

RULES = [
    ("Beginner’s mind", "Listen and do not interpret. Look for the unexpected."),
    ("Listen more than you talk", "You are there to learn, not to convince. They talk 80%."),
    ("Facts, not opinions", "Not “Would you…?” but “When was the last time…?”"),
    ("Ask why", "“Why is that important to you?” Ask it until you reach the real reason."),
    ("Learn, do not sell", "Not “Would you buy it?” but “How did you choose the last time?”"),
    ("No solution too early", "Do not explain your idea. Ask what bothers them most."),
    ("Follow up", "Ask permission to contact them again, to test a prototype later."),
    ("Leave the door open", "Always end with: “Who else should I talk to?”"),
]
rules = "".join(
    f'<div style="display:flex;flex-direction:column;gap:12px;padding:26px 28px;background:{WHITE};border:2px solid {LINE};border-radius:14px">'
    f'<p style="{RUBIK};font-size:32px;font-weight:800;color:{TEAL}">{k + 1}</p>'
    f'<h3 style="{RUBIK};font-size:32px;font-weight:700;line-height:1.1">{t}</h3>'
    f'<p style="font-size:24px;line-height:1.35;color:{GREY}">{x}</p></div>'
    for k, (t, x) in enumerate(RULES))
S.append(section("rules", f"""
{head("Step 2 · Good interviews", "Eight rules for interviewing customers")}
<div style="flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:1fr;gap:20px;margin-bottom:40px">{rules}</div>
{source(VPD)}
"""))

SWAPS = [
    ("Would you buy a meal plan for students?", "How much did you spend on food last week?"),
    ("Do you like healthy food?", "What did you eat yesterday? Where and when?"),
    ("Would you use an app that plans your meals?", "How do you decide what to eat on a weekday?"),
    ("Is eating well a problem for you?", "What are the three hardest things about eating well during exams?"),
]
swaps = "".join(
    f'<tr data-build-in="rise {k + 1}"><td style="color:{RUST};padding:20px 16px">{a}</td>'
    f'<td style="font-weight:700;padding:20px 16px">{b}</td></tr>'
    for k, (a, b) in enumerate(SWAPS))
S.append(section("rewrite", f"""
{head("Step 2 · Case: home-cooked meals for students", "Change the question, not the topic")}
<table style="font-size:32px;line-height:1.3;color:{NAVY}">
<tr><th style="width:46%;color:{RUST}">Do not ask</th><th style="width:54%;color:{TEAL}">Ask instead</th></tr>
{swaps}
</table>
{lead("Open questions, about the past. A yes or a no teaches you nothing.")}
""", layout="between"))

WHYS = [
    ("“I order delivery three times a week.”", "Why?"),
    ("“I get home from the lab at nine.”", "Why does that matter?"),
    ("“At nine I am too tired to cook.”", "Why not cook earlier, or at the weekend?"),
    ("“I never have food at home. I do not plan my shopping.”", None),
]
whys = "".join(
    f'<div data-build-in="rise {k + 1}" style="display:flex;gap:32px;align-items:baseline;padding:18px 0;border-top:2px solid {LINE}">'
    f'<p style="flex:1;font-size:34px;line-height:1.3">{a}</p>'
    + (f'<p style="width:560px;flex:none;font-size:28px;font-weight:700;color:{TEAL}">→ You: {q}</p>' if q else
       f'<p style="width:560px;flex:none"></p>')
    + '</div>' for k, (a, q) in enumerate(WHYS))
S.append(section("whys", f"""
{head("Step 2 · Ask why", "The first answer is rarely the real one")}
<div style="display:flex;flex-direction:column;border-bottom:2px solid {LINE}">{whys}</div>
<p data-build-in="fade 5" style="font-size:34px;line-height:1.4;font-weight:700;background:{YELLOW};padding:24px 32px;border-radius:12px">The problem is not cooking. It is planning and shopping. A different business.</p>
""", layout="between"))

S.append(section("practical", f"""
{head("Step 2 · Good interviews", "The practical side")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px 48px">
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">1</p><p style="flex:1;font-size:32px;line-height:1.3">One person per interview, 20 to 60 minutes. Watch the face, not only the words.</p></div>
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">2</p><p style="flex:1;font-size:32px;line-height:1.3">Go in pairs: one person asks, the other one writes.</p></div>
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">3</p><p style="flex:1;font-size:32px;line-height:1.3">Take notes on paper, in front of them. Do not record: people talk less.</p></div>
<div style="display:flex;gap:20px;align-items:center;padding:24px 0;border-top:2px solid {LINE}"><p style="{RUBIK};font-size:44px;font-weight:800;color:{TEAL}">4</p><p style="flex:1;font-size:32px;line-height:1.3">Ask an important question twice, in other words, to check the answer.</p></div>
</div>
{lead("Be ready to hear things you do not like. That is the point. And always say thank you.")}
""", layout="between"))

# ---------- Step 3 · Structure ----------

SCRIPT = [
    ("Welcome", "Set the ground: who you are, why, how long", 2, "15"),
    ("Get to know them", "Test the customer segment", 2, "15"),
    ("Tell a story", "Give context to the problem", 2, "15"),
    ("Rank the problems", "Test the problem: which one hurts most?", 4, "16"),
    ("Explore their view", "Past, tools, cost, other solutions", 15, "16"),
    ("Close", "Repeat what you heard in your words. Ask for names.", 2, ""),
    ("Write it down", "Five lessons, right after", 5, ""),
]
bars = "".join(
    f'<div data-build-in="rise {k + 1}" style="display:flex;gap:24px;align-items:center;padding:12px 0;border-top:2px solid {LINE}">'
    f'<p style="width:360px;flex:none;{RUBIK};font-size:30px;font-weight:700">{t}</p>'
    f'<p style="width:520px;flex:none;font-size:24px;line-height:1.3;color:{GREY}">{x}</p>'
    f'<div style="flex:1;display:flex;align-items:center;gap:16px">'
    f'<span style="display:block;height:36px;width:{m * 38}px;background:{YELLOW if m == 15 else TEAL};border-radius:6px"></span>'
    f'<span style="font-size:24px;font-weight:700;white-space:nowrap">{m} min</span></div>'
    f'<p style="width:130px;flex:none;font-size:20px;font-weight:700;color:{TEAL};text-align:right">{"Board " + b if b else ""}</p></div>'
    for k, (t, x, m, b) in enumerate(SCRIPT))
S.append(section("script", f"""
{head("Step 3 · The structure", "A 30-minute interview, step by step")}
<div style="display:flex;flex-direction:column;border-bottom:2px solid {LINE}">{bars}</div>
{lead("Half of the time goes to one block: <b style='color:" + NAVY + "'>their view of the problem.</b> Everything before it prepares that conversation.", 28)}
""", layout="between"))

def board_row(title, sub, example, last=False):
    bb = f"border-bottom:2px solid {NAVY};" if not last else ""
    return (f'<div style="display:flex;{bb}">'
            f'<div style="width:520px;flex:none;padding:22px 28px 22px 0;border-right:2px solid {NAVY}">'
            f'<p style="font-size:26px;font-weight:800;text-transform:uppercase;letter-spacing:1px">{title}</p>'
            f'<p style="font-size:24px;line-height:1.3;color:{GREY}">{sub}</p></div>'
            f'<div style="flex:1;padding:18px 0 18px 32px">{example}</div></div>')

def notes(*items, rot=(-1, 1, -2)):
    return ('<div style="display:flex;gap:20px;align-items:flex-start">' + "".join(
        f'<p style="{CAVEAT};flex:1;font-size:30px;line-height:1.1;background:{YELLOW};padding:16px 18px;'
        f'box-shadow:0 6px 12px rgba(21,35,59,0.15);transform:rotate({rot[k % 3]}deg)">{t}</p>'
        for k, t in enumerate(items)) + "</div>")

S.append(section("board-15", f"""
{head("Step 3 · Board 15 · Worked example", "Home-cooked meals for students: the script")}
<div style="display:flex;flex-direction:column;border-top:2px solid {NAVY};border-bottom:2px solid {NAVY}">
{board_row("Welcome", "Set the ground for the interview", notes("“We are ICAI students. We sell nothing.”", "“We want to learn how students eat.”", "“No wrong answers. 20 minutes, OK?”"))}
{board_row("Identify your interlocutor", "Who is this person? Test the segment", notes("“Where do you study?”", "“Who do you live with? Who cooks?”", "“How many days a week do you eat out?”"))}
{board_row("Identify the context", "Their situation and their challenges", notes("“Tell me about yesterday: what did you eat?”", "“How is it different in exam weeks?”", "“What did you eat last Sunday?”"))}
{board_row("Explore the problem", "The problem, how much it matters, what they use today", f'<p style="font-size:28px;font-weight:700;color:{TEAL};padding-top:20px">→ Board 16</p>', last=True)}
</div>
""", layout="between"))

QW = [
    ("Tell me about the last time you…", "…ordered food delivery."),
    ("Tell me how (something) works…", "…how you plan your meals for the week."),
    ("What are the three main challenges you face with this?", "…when you try to eat well during the week?"),
    ("Which tool do you use now to…?", "…get food on a weekday? Which apps?"),
    ("Why do you use this tool?", "Why that app and not another one?"),
    ("What did you expect when you started using it?", "…the first time you ordered with it?"),
    ("Have you tried to solve the problem before? How?", "Cooking in batches, a meal plan? What happened?"),
    ("How do other people solve it?", "How do your flatmates do it?"),
]
qw = "".join(
    f'<tr data-build-in="rise {1 if k < 4 else 2}"><td style="padding:12px 16px 12px 0">{a}</td>'
    f'<td style="padding:12px 0 12px 24px;border-left:2px solid {NAVY};{CAVEAT};font-size:34px;color:{TEAL}">{b}</td></tr>'
    for k, (a, b) in enumerate(QW))
S.append(section("board-16", f"""
{head("Step 3 · Board 16 · Worked example", "Questions that work, applied to our case")}
<table style="font-size:26px;line-height:1.3;color:{NAVY}">
<tr><th style="width:52%;border-bottom:2px solid {NAVY};padding-left:0">Questions that work</th><th style="width:48%;border-bottom:2px solid {NAVY};border-left:2px solid {NAVY};padding-left:24px">Your questions</th></tr>
{qw}
</table>
<p style="font-size:26px;color:{GREY}"><b style="color:{RUST}">Avoid:</b> “Would you…?”, “Will you…?”, “Do you think…?” Future and conditional questions get you wishful thinking.</p>
""", layout="between"))

# ---------- Step 4 · Team work ----------

S.append(section("team-intro", f"""
{kicker("Step 4 · Team work · 30 min", YELLOW)}
<h1 style="{RUBIK};font-size:160px;font-weight:800;line-height:1">Your interview</h1>
<p style="{RUBIK};font-size:64px;font-weight:500;line-height:1.15">Boards 15 and 16 on the Mural</p>
<p style="font-size:32px;line-height:1.4;color:#DCEBF2;width:1300px">Goal: a script you can use this week, to test the problem from your most critical hypothesis.</p>
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
{head("Step 4 · Step by step", "Three moves in 30 minutes")}
{row(
    step_card("1", "10 min", "Board 15", "The script: welcome, who they are, their context. One post-it per question."),
    step_card("2", "12 min", "Board 16", "Your questions to explore the problem, using the questions that work."),
    step_card("3", "8 min", "Rehearse", "Interview one person from another team. They stop you at every “would you”.", hi=True),
)}
{pills("House rules:", ["No idea in the questions", "Past, not future", "Different scripts per segment are OK"])}
""", layout="between"))

# ---------- Step 5 · After the interview ----------

def tpl_box(title, lines, h=None):
    ls = "".join(f'<p style="font-size:22px;line-height:1.35;color:{GREY}">{l}</p>' for l in lines)
    return (f'<div style="flex:1;padding:18px 24px;border-top:2px solid {NAVY}">'
            f'<p style="font-size:22px;font-weight:800;letter-spacing:1px;text-transform:uppercase">{title}</p>{ls}</div>')

S.append(section("template", f"""
{head("Step 5 · After the interview", "One page per interview, the same day")}
<div style="flex:1;display:flex;gap:48px">
<div style="flex:1;display:flex;flex-direction:column;border-bottom:2px solid {NAVY}">
{kicker("Your script", GREY)}
{tpl_box("Contact", ["Name · date · place"])}
{tpl_box("About them", ["“Before we talk about problems, I would like to know you a bit better…”"])}
{tpl_box("Problem 1 · hypothesis 1", ["Questions 1, 2, 3"])}
{tpl_box("Problem 2 · hypothesis 2", ["Questions 1, 2, 3"])}
{tpl_box("Ranking", ["Which problem hurts most? Anything else of interest"])}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{kicker("Your notes", GREY)}
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:16px">
{box("Confirms your hypothesis", "Facts that say yes.", LTEAL, LTEAL)}
{box("Contradicts your hypothesis", "Facts that say no. Write these first.", WHITE, RUST, RUST)}
{box("Surprised you", "What you did not expect to hear.", CREAM, CREAM, "#8A5A00")}
{box("Said with emotion", "Anger, laughter, a long story: that is where the pain is.", WHITE)}
</div>
</div>
</div>
""", layout="gap"))

SCORE = [
    ("Did they understand the problems you described?", "10", "5", "0", "Interested in the problems", "Talked about other problems"),
    ("Are they trying to solve it now, or did they try before?", "10", "5", "0", "Already solving it, even with Excel", "Happy with how things are"),
    ("Were they focused during the whole interview?", "8", "4", "0", "Ignored their phone", "Looked at the phone, cut it short"),
    ("Do they want a second meeting?", "8", "4", "0", "Asked for it", "No reason to meet again"),
    ("Did they give you names of other people to interview?", "4", "2", "0", "Offered names", "Could not name anyone"),
    ("Did they offer to pay you for a solution?", "3", "1", "0", "Offered, and said a price", "Did not offer"),
]
srows = "".join(
    f'<tr><td style="padding:12px 16px 12px 0">{q}<br><span style="font-size:20px;color:{GREY}">Yes: {y} · No: {n}</span></td>'
    f'<td style="text-align:center;font-weight:800;color:#1E7B4F">{a}</td><td style="text-align:center;font-weight:800;color:#C98A00">{b}</td>'
    f'<td style="text-align:center;font-weight:800;color:{RUST}">{c}</td></tr>'
    for q, a, b, c, y, n in SCORE)
S.append(section("scorecard", f"""
{head("Step 5 · After the interview", "Is the problem real? Score every interview", size=64)}
<div style="display:flex;gap:56px;align-items:flex-start">
<table style="flex:1;font-size:26px;line-height:1.25;color:{NAVY}">
<tr><th style="padding-left:0">Question</th><th style="width:120px;text-align:center">Yes</th><th style="width:140px;text-align:center">Sort of</th><th style="width:120px;text-align:center">No</th></tr>
{srows}
</table>
<div data-build-in="rise 1" style="width:360px;flex:none;display:flex;flex-direction:column;gap:12px;padding:36px;background:{NAVY};color:{PAPER};border-radius:16px">
<p style="font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{YELLOW}">Good interview</p>
<p style="{RUBIK};font-size:120px;font-weight:800;line-height:1">31+</p>
<p style="font-size:26px;line-height:1.35">out of 43 points. Below 31, the problem probably does not hurt enough.</p>
</div>
</div>
{source(LA)}
"""))

TICKS = [(2, 250, "Update your script"), (5, 560, "You find one early adopter"),
         (10, 870, "You see patterns: customer types"), (20, 1180, "Few things surprise you now"),
         (50, 1490, "Now a survey makes sense")]
ticks = "".join(
    f'<line x1="{x}" y1="560" x2="{x}" y2="580" stroke="{NAVY}" stroke-width="4"/>'
    f'<text x="{x}" y="620" text-anchor="middle" font-family="Rubik, Arial" font-size="34" font-weight="800" fill="{NAVY}">{n}</text>'
    for n, x, _ in TICKS)
labels = "".join(
    f'<p data-build-in="rise {k + 1}" style="position:absolute;left:{128 + x - 130}px;top:880px;width:240px;{CAVEAT};font-size:32px;line-height:1.1;'
    f'background:{YELLOW};color:{NAVY};padding:14px 16px;{SHADOW};transform:rotate({(-2, 1, -1, 2, -1)[k]}deg)">{t}</p>'
    for k, (_, x, t) in enumerate(TICKS))
S.append(section("how-many", f"""
{head("Step 5 · How many interviews?", "Learning grows fast, then slows down")}
<svg viewBox="0 0 1664 640" style="position:absolute;left:128px;top:240px;width:1664px;height:640px" aria-label="Knowledge against number of interviews">
<line x1="120" y1="570" x2="1640" y2="570" stroke="{NAVY}" stroke-width="4"/>
<line x1="130" y1="20" x2="130" y2="580" stroke="{NAVY}" stroke-width="4"/>
<path d="M130 570 C 300 300, 600 220, 900 200 S 1400 170, 1620 160" fill="none" stroke="{TEAL}" stroke-width="10" stroke-linecap="round"/>
<text x="150" y="80" font-family="Nunito Sans, Arial" font-size="28" font-weight="700" fill="{GREY}">What you know</text>
<text x="1640" y="530" text-anchor="end" font-family="Nunito Sans, Arial" font-size="28" font-weight="700" fill="{GREY}">Interviews</text>
{ticks}
</svg>
{labels}
<p style="position:absolute;left:128px;bottom:40px;font-size:20px;color:{GREY}">A rule of thumb from experience, not a measured curve.</p>
"""))

S.append(section("homework", f"""
{head("Before next session", "Go out and talk to real customers", kcolor="#8A5A00")}
{row(
    card(f'<span style="{RUBIK};font-size:56px;font-weight:800;color:{TEAL}">1</span>', "Interview", "At least 10 interviews per team. Real customers from your segment, not friends or family.", PAPER),
    card(f'<span style="{RUBIK};font-size:56px;font-weight:800;color:{TEAL}">2</span>', "Write it down", "One page per interview, the same day. Five lessons learned.", PAPER),
    card(f'<span style="{RUBIK};font-size:56px;font-weight:800;color:{YELLOW}">3</span>', "Score it", "Every interview gets its score out of 43. Bring them to class.", NAVY, PAPER, "#DCE3EA", PAPER),
)}
{lead(f"A problem nobody has is a good result too, <b style='color:{NAVY}'>if you find out this week and not in a year.</b>", 28)}
""", bg="cream", layout="between"))

S.append(section("close", f"""
<p style="{CAVEAT};font-size:120px;line-height:1.1;color:{YELLOW};text-align:center;width:1500px">Ask about the past. Then listen.</p>
<p style="{RUBIK};font-size:56px;font-weight:500;text-align:center">Your idea can wait.</p>
<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#BFD0DD;text-align:center">ICAI · Innovation &amp; Entrepreneurship · Customer Discovery</p>
""", bg="navy", layout="center", extra=";align-items:center"))
