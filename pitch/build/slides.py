from build import *

META = dict(title="The Elevator Pitch", file="index.html")

AIRBNB = "Airbnb seed deck, 2008 (market size slide; its own sources: Travel Industry Association of America, World Tourism Organization, comScore)"
FIVE_HUNDRED = "the investor-presentation outline used by 500 Startups"

S = []


# ---------- Figures ----------

import base64
ELEVATOR = "data:image/png;base64," + base64.b64encode((pathlib.Path(__file__).parent / "elevator.png").read_bytes()).decode()


def elevator_icon(w=520):
    return f'<img src="{ELEVATOR}" width="{w}" height="{w}" alt="An elevator with a timer on top">'


def number(n, color=TEAL, size=56):
    return f'<span style="{RUBIK};font-size:{size}px;font-weight:800;color:{color}">{n}</span>'


# ---------- Opening ----------

S.append(section("cover", f"""
{kicker("ICAI · Innovation &amp; Entrepreneurship · Workshop")}
<div style="display:flex;flex-direction:column;gap:32px;width:1100px">
<h1 style="{RUBIK};font-size:136px;font-weight:700;line-height:1.02">The elevator pitch</h1>
<p style="font-size:44px;color:{GREY}">Your startup in a few minutes, to a person who is very busy</p>
</div>
<p style="font-size:24px;color:{GREY}">Javier Fuentes</p>
<div style="position:absolute;left:1240px;top:240px">{elevator_icon(560)}</div>
""", layout="between"))

S.append(section("route", f"""
{head("Today’s route", "Five steps, from an empty slide to a pitch you can give")}
<table style="font-family:'Nunito Sans', Arial, sans-serif;font-size:30px;color:{NAVY}">
<tr><th style="width:8%">#</th><th style="width:50%">Step</th><th style="width:42%">Output</th></tr>
<tr><td>1</td><td>What a pitch is, and who listens</td><td>Shared context</td></tr>
<tr><td>2</td><td>The nine blocks of a pitch deck</td><td>What to put on each slide</td></tr>
<tr><td>3</td><td>How big is the market: TAM, SAM, SOM</td><td>Your market in three numbers</td></tr>
<tr style="background:{LTEAL}"><td>4</td><td>How to give it</td><td>Six rules for the day</td></tr>
<tr style="background:{CREAM}"><td>5</td><td>Your turn</td><td>Your pitch, ready to rehearse</td></tr>
</table>
"""))

# ---------- Step 1 · What a pitch is ----------

S.append(section("what", f"""
{head("Step 1 · What a pitch is", "A short presentation to convince an investor")}
<div style="display:flex;gap:96px;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;gap:36px">
<p data-build-in="rise 1" style="font-size:40px;line-height:1.35">The word comes from Silicon Valley: <b>the presentation a founder gives to investors.</b></p>
<p data-build-in="rise 2" style="font-size:40px;line-height:1.35">The <b style="color:{TEAL}">elevator pitch</b> is the shortest form: you meet the investor in the elevator, and you have until the doors open.</p>
<p data-build-in="rise 3" style="font-size:40px;line-height:1.35">The goal is not the money. <b style="color:{RUST}">The goal is a second meeting.</b></p>
</div>
{elevator_icon(460)}
</div>
""", layout="center"))

AUDIENCE = [("Investors", "See hundreds of pitches every year"), ("CEOs", "Decide in minutes if a partner is worth it"),
            ("Managers", "Have twenty other things on the agenda today"), ("A jury", "Will hear ten teams in a row")]
S.append(section("audience", f"""
{head("Step 1 · Who listens", "The people you pitch to are always busy")}
{row(*[card(number(k + 1), n, t, WHITE if k else YELLOW, top_color=GREY, text_color=GREY if k else NAVY, size=44) for k, (n, t) in enumerate(AUDIENCE)])}
{lead(f"So your job is simple: <b style='color:{NAVY}'>make it easy for them.</b> Easy to follow, easy to remember, easy to repeat to a partner.")}
""", layout="between"))

S.append(section("anchor-structure", f"""
{kicker("Step 1 · The one rule", YELLOW)}
<p style="{RUBIK};font-size:96px;font-weight:700;line-height:1.1;width:1600px">There is no fixed structure.<br><span style="color:{YELLOW}">Show your strengths first.</span></p>
<p style="font-size:34px;color:#BFD0DD;width:1400px">The nine blocks that follow are a checklist, not a script. Strong traction? Open with it. Strong team? Say it early.</p>
""", bg="navy", layout="center"))

# ---------- Step 2 · Nine blocks ----------

BLOCKS = [
    ("name", "Name, logo and slogan", "Who are you, in one line?"),
    ("problem", "The problem", "What hurts, and who does it hurt?"),
    ("solution", "The solution", "What do you do about it?"),
    ("how", "How it works", "What does the customer actually do?"),
    ("traction", "Traction / MVP", "What have you proven so far?"),
    ("model", "Business model", "Who pays, and for what?"),
    ("competition", "Competition", "Who else does this, and why you?"),
    ("market", "Size of the opportunity", "How big can this get?"),
    ("team", "Team and roles", "Why are you the right people?"),
]


def block_cell(k, sid, name, q):
    return (f'<div data-build-in="rise {k + 1}" data-goto="b-{sid}" style="display:flex;gap:24px;align-items:center;padding:24px 28px;'
            f'background:{WHITE};border:2px solid {LINE};border-radius:14px">'
            f'{number(k + 1, TEAL, 52)}<div style="display:flex;flex-direction:column;gap:4px">'
            f'<h3 style="{RUBIK};font-size:34px;font-weight:700;line-height:1.1">{name}</h3>'
            f'<p style="font-size:24px;color:{GREY}">{q}</p></div></div>')


S.append(section("nine", f"""
{head("Step 2 · The pitch deck", "Nine blocks, one question each")}
{grid([block_cell(k, *b) for k, b in enumerate(BLOCKS)], 3, 20)}
<p style="font-size:22px;color:{GREY}">Based on {FIVE_HUNDRED}. Click a block to open it.</p>
"""))


def big_box(label, text, bg, border, label_color):
    return (f'<div style="display:flex;flex-direction:column;gap:14px;padding:36px 40px;background:{bg};'
            f'border:2px solid {border};border-radius:16px">'
            f'<p style="font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{label_color}">{label}</p>'
            f'<p style="font-size:31px;line-height:1.4">{text}</p></div>')


def block(k, title, ask, do, example, watch, extra="", ex_label="Example · Airbnb, 2008"):
    sid, name, _ = BLOCKS[k]
    dos = "".join(
        f'<div data-build-in="rise {j + 1}" style="display:flex;gap:20px;align-items:baseline;padding:16px 0;border-top:2px solid {LINE}">'
        f'<p style="{RUBIK};width:36px;flex:none;font-size:32px;font-weight:800;color:{TEAL}">✓</p>'
        f'<p style="flex:1;font-size:36px;line-height:1.3">{d}</p></div>' for j, d in enumerate(do))
    body = f"""
<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:32px">
{head(f"Block {k + 1} of 9 · {name}", title)}
{goto_pill("nine", "All blocks")}
</div>
<div style="flex:1;display:flex;gap:56px;min-height:0">
<div style="width:900px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="{CAVEAT};font-size:68px;line-height:1.1;color:{NAVY}">The investor asks: “{ask}”</p>
<div style="border-bottom:2px solid {LINE}">{dos}</div>
{extra}
</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px">
{big_box(ex_label, example, CREAM, CREAM, "#8A5A00")}
{big_box("Watch out", watch, WHITE, RUST, RUST)}
</div>
</div>"""
    return section(f"b-{sid}", body)


S.append(block(0, "A name people remember, a line that says what you do",
    "Who are you?",
    ["A name that is easy to say, spell and remember", "A simple logo: it must work small, in one colour",
     "A slogan: your mission in one sentence"],
    "<b>Airbnb</b> comes from “AirBed &amp; Breakfast”: the first guests slept on air mattresses. "
    "<b>MySQL</b> is named after My, the daughter of a co-founder. <b>Cabify</b>: a cab, as an app.",
    "A clever name you must explain. If you need a sentence to explain the name, the slogan has a problem too.",
    ex_label="Three names and where they come from"))

S.append(block(1, "Describe the pain so that everybody understands it",
    "Is this a real problem?",
    ["Say it in words your grandmother understands", "Show it is worth solving: how often, how bad, how many people",
     "Use what you heard in your customer interviews"],
    "Travellers care about price. Hotels keep you away from the real city. "
    "And there is no easy way to book a room in a local person’s home.",
    "A problem only you have. Or a problem that is really your solution in disguise: “there is no app for X”."))

S.append(block(2, "Say what you do, clearly and in few words",
    "So what do you do?",
    ["One sentence that answers the problem slide", "The benefit for the customer, not the technology",
     "No technical detail here: that comes later, if they ask"],
    "A website where people rent out a room to travellers. Travellers save money, hosts earn money, and both share the culture of the city.",
    "A list of features. The investor wants to know what changes for the customer."))

S.append(block(3, "Show how it works, step by step",
    "What does the customer actually do?",
    ["The customer’s path in three or four steps", "A screenshot, a prototype or a short demo is worth ten bullets",
     "Now you can add a little more detail"],
    "Three steps: search by city, see the room and the host, book and pay online.",
    "A live demo with no plan B. Record a video of the demo in case the Wi-Fi fails."))

S.append(block(4, "Show what you have proven so far",
    "Does anybody want it?",
    ["Customers or users, and how fast they grow", "Revenue, even if small", "Lessons from your interviews and experiments",
     "Other milestones: a pilot, a partner, a letter of intent"],
    "Before they had customers, they showed demand: thousands of people already looking for a room on Couchsurfing and Craigslist.",
    "Vanity numbers: page visits, likes, “people said they love it”. Show what people <b>did</b>, not what they said.",
    lead(f"No customers yet? Then your traction is <b style='color:{NAVY}'>what you learned:</b> interviews, experiments, results.", 26)))

S.append(block(5, "Explain how you make money",
    "Who pays, and for what?",
    ["Who pays, how much, and how often", "Use your Business Model Canvas as a guide, without showing all of it",
     "One simple calculation is better than a big table"],
    "Airbnb takes a commission on each booking. The calculation on the slide: number of trips × average price × commission.",
    "Showing the full canvas with nine boxes full of text. Pick the two or three boxes that matter."))

S.append(block(6, "Say who your competitors are, and how you are different",
    "Why you, and not them?",
    ["Name them: there is always competition, even if it is “doing nothing”",
     "Choose two criteria that matter to the customer", "Put everybody on a 2 × 2 map: you alone in one corner"],
    "Their map: cheap or expensive, and booking online or offline. Hotels, Couchsurfing, Craigslist and others on the map; Airbnb alone in the corner “cheap and online”.",
    "“We have no competitors.” To an investor it means: there is no market, or you have not looked."))

S.append(block(7, "Show how big the market is",
    "How big can this get?",
    ["Total market: everybody with the problem", "The part you can serve with your product",
     "The part you can realistically win in a few years"],
    "Two billion trips per year in the world. 560 million of them budget and booked online. Their target: 15% of that, 84 million trips.",
    "Starting with “the market is 500 billion euros, if we get 1%…”. Build it from the bottom: customers × price.",
    f'<div style="display:flex">{goto_pill("tam", "TAM, SAM, SOM →")}</div>'))

S.append(block(8, "Show why you are the right people",
    "Why should I trust you with this?",
    ["Who you are, with a photo", "What background makes you right for this problem",
     "Who takes care of what in the team"],
    "On the slide: the founders, with their roles and one line each about what they had built before.",
    "Titles with no content (“CEO, CTO, CMO” in a team of three students). Say what each person actually does."))

# ---------- Step 3 · Market size ----------

def rings():
    return f'''<svg viewBox="0 0 720 720" width="640" aria-label="Three nested circles: TAM, SAM, SOM">
<circle cx="360" cy="360" r="340" fill="{LTEAL}"/>
<circle cx="360" cy="460" r="230" fill="#CFE4EE"/>
<circle cx="360" cy="560" r="120" fill="{YELLOW}"/>
<text x="360" y="110" text-anchor="middle" font-family="Rubik, Arial" font-size="64" font-weight="800" fill="{TEAL}">TAM</text>
<text x="360" y="320" text-anchor="middle" font-family="Rubik, Arial" font-size="56" font-weight="800" fill="{TEAL}">SAM</text>
<text x="360" y="580" text-anchor="middle" font-family="Rubik, Arial" font-size="52" font-weight="800" fill="{NAVY}">SOM</text>
</svg>'''


TSS = [("TAM", "Total Available Market", "Everybody who has the problem, in the whole world.", "All LED lighting", LTEAL),
       ("SAM", "Serviceable Available Market", "The part you can reach with your product and your channels.", "Colour-changing LED for the home", "#CFE4EE"),
       ("SOM", "Serviceable Obtainable Market", "The part you can realistically win, with your competition, countries and sales team.", "Your sales goal for year 3", YELLOW)]


def tss_row(k, a, n, t, ex, bg):
    return (f'<div data-build-in="rise {k + 1}" style="display:flex;gap:28px;align-items:flex-start;padding:24px 28px;background:{bg};border-radius:14px">'
            f'<p style="{RUBIK};width:130px;flex:none;font-size:48px;font-weight:800;color:{NAVY}">{a}</p>'
            f'<div style="display:flex;flex-direction:column;gap:6px"><p style="font-size:24px;font-weight:700;color:{TEAL}">{n}</p>'
            f'<p style="font-size:28px;line-height:1.3">{t}</p>'
            f'<p style="font-size:22px;color:{GREY}"><b>Example:</b> {ex}</p></div></div>')


S.append(section("tam", f"""
{head("Step 3 · Size of the opportunity", "Three circles, from everybody to your customers")}
<div style="flex:1;display:flex;gap:64px;align-items:center">
{rings()}
<div style="flex:1;display:flex;flex-direction:column;gap:18px">{"".join(tss_row(k, *r) for k, r in enumerate(TSS))}</div>
</div>
"""))


def bubble(r, value, label, sub, k):
    return (f'<div data-build-in="rise {k}" style="display:flex;flex-direction:column;align-items:center;gap:20px;width:{max(2 * r, 380)}px">'
            f'<div style="width:{2 * r}px;height:{2 * r}px;border-radius:50%;background:{RUST if k == 3 else TEAL};display:flex;align-items:center;justify-content:center">'
            f'<p style="{RUBIK};font-size:{max(r // 2.6, 40):.0f}px;font-weight:800;color:{PAPER}">{value}</p></div>'
            f'<p style="{RUBIK};font-size:32px;font-weight:700;text-align:center">{label}</p>'
            f'<p style="font-size:24px;color:{GREY};text-align:center">{sub}</p></div>')


S.append(section("tam-airbnb", f"""
{head("Step 3 · Size of the opportunity", "How Airbnb sized its market in 2008")}
<div style="display:flex;gap:40px;align-items:flex-end;justify-content:center">
{bubble(230, "2 billion+", "Trips booked, worldwide", "TAM", 1)}
{bubble(130, "560 M", "Budget and online", "SAM", 2)}
{bubble(80, "84 M", "Trips with Airbnb", "SOM · 15% of the SAM", 3)}
</div>
{source(AIRBNB)}
""", layout="between"))

# ---------- Step 4 · How to give it ----------

TIPS = [
    ("Start with a question", "The first ten seconds decide if they listen. “How did you book your last trip?”"),
    ("Clear, brief, concise", "One idea per slide. If a slide needs a paragraph, it is two slides."),
    ("Plan the turns", "If you speak in turns, decide who says what, and how you pass the word."),
    ("Do not memorise", "Learn the order and the key sentences. A memorised text sounds like a recording."),
    ("Practise the time", "Rehearse with a timer, out loud, at least three times. You will be slower than you think."),
    ("Be convincing", "Believe in it, look at the audience, and finish with what you need from them."),
]
S.append(section("tips", f"""
{head("Step 4 · How to give it", "Six rules for the day of the pitch")}
{grid([f'<div data-build-in="rise {k + 1}" style="display:flex;flex-direction:column;gap:12px;padding:32px;background:{YELLOW if k == 4 else WHITE};'
       f'{"" if k == 4 else f"border:2px solid {LINE};"}border-radius:16px">{number(k + 1, NAVY if k == 4 else TEAL, 44)}'
       f'<h3 style="{RUBIK};font-size:38px;font-weight:700;line-height:1.1">{n}</h3>'
       f'<p style="font-size:26px;line-height:1.35;color:{NAVY if k == 4 else GREY}">{t}</p></div>'
       for k, (n, t) in enumerate(TIPS)], 3, 24)}
"""))

S.append(section("anchor-second", f"""
{kicker("Step 4 · Remember", YELLOW)}
<p style="{RUBIK};font-size:104px;font-weight:700;line-height:1.1;width:1600px">You do not need to tell everything.<br><span style="color:{YELLOW}">You need a second meeting.</span></p>
""", bg="navy", layout="center"))

# ---------- Step 5 · Your turn ----------

S.append(section("your-turn", f"""
{head("Your turn · This week", "Prepare your team’s pitch", kcolor="#8A5A00")}
{row(
    card(number(1), "Choose your blocks", "Go through the nine blocks. Put your strongest one early. Drop what you do not have yet.", PAPER),
    card(number(2), "One slide per block", "One idea per slide, big text, one picture or one number.", PAPER),
    card(number(3), "Split the voices", "Everybody in the team speaks. Decide who says what.", PAPER),
    card(number(4, YELLOW), "Rehearse with a timer", "Out loud, standing, at least three times. Cut until it fits.", NAVY, PAPER, "#DCE3EA", PAPER),
)}
{lead(f"Use everything from the last sessions: <b style='color:{NAVY}'>your hypotheses, your experiments and your interviews</b> are your traction.", 28)}
""", bg="cream", layout="between"))

S.append(section("close", f"""
<p style="{CAVEAT};font-size:120px;line-height:1.1;color:{YELLOW};text-align:center;width:1500px">Make it easy for them.</p>
<p style="{RUBIK};font-size:56px;font-weight:500;text-align:center">Then ask for the second meeting.</p>
<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#BFD0DD;text-align:center">ICAI · Innovation &amp; Entrepreneurship · The elevator pitch</p>
""", bg="navy", layout="center", extra=";align-items:center"))
