# -*- coding: utf-8 -*-
# Slide content, in order. Same engine as the CDP robotics keynote (Sept 2026).
# kind: cover | agenda | quote | bullets | anchor | data | compare | chart | video | breath | close
# Taught more than once a year: the date is the academic year, not a day.
META = dict(
    title="Tech Trends",
    foot="Entrepreneurship & Innovation · Tech Trends",
    date="2026–27",
    author="Javier Fuentes Ibáñez",
    file="tech-trends.html",
)

S = [
dict(kind="cover", title="Tech<br>Trends", who="Javier Fuentes Ibáñez",
     org="ICAI", date="Entrepreneurship & Innovation · 2026–27"),

dict(kind="agenda", act="Opening", title="Today"),

# I. Opening: the 2021 map, and what is still alive
dict(kind="bullets", act="Opening", title="My 2021 map: nine trends", art="map2021", items=[
  "IoT, augmented reality, blockchain",
  "hyper-personalization, AI, big data",
  "fintech, 3D printing, robotics",
  "five years later: which examples are still alive?"],
  src="Tech Trends class, ICAI, 2021"),

dict(kind="bullets", act="Opening", title="Two 2021 examples that did not survive", items=[
  "Amazon Dash buttons: sales stopped in February 2019",
  "Amazon Go: all stores in the US and UK closed in 2026",
  "Amazon: no &ldquo;right economic model&rdquo; for large-scale expansion",
  "the technology worked; the business did not"],
  src="Engadget, 1 Mar 2019 (Dash); aboutamazon.com, 27 Jan 2026 (Fresh and Go)"),

dict(kind="anchor", act="Opening", wide=True,
     text="A trend is not a business.<br>For each trend today, we look for the business."),

# II. Intelligence
dict(kind="anchor", act="Intelligence", kicker="Trend 1 · Generative AI and agents",
     text="Software that writes, talks and acts for you."),
dict(kind="video", act="Intelligence", slug="lovable", vid="xhW9up0Gi2E",
     title="Lovable: an app from one sentence", label="Lovable · official video · 2024"),
dict(kind="video", act="Intelligence", slug="claude-code", vid="AJpK3YTTKZ4",
     title="Claude Code: an agent that changes the code itself",
     label="Anthropic · official video · 2025 · excerpt"),
dict(kind="data", act="Intelligence", figure="$500M",
     cap="Lovable's annual revenue rate, less than three years after it started",
     src="TechCrunch, 9 June 2026 (figures from Lovable)"),
dict(kind="bullets", act="Intelligence", title="From answers to actions", items=[
  "2023: the AI answers your question",
  "2026: the agent does the task, step by step",
  "startup: Lovable (Stockholm) builds whole apps",
  "your question: which task in your field can an agent do?"]),

dict(kind="anchor", act="Intelligence", kicker="Trend 2 · Smart devices",
     text="The AI moves from the cloud into the object."),
dict(kind="video", act="Intelligence", slug="humane-ai-pin", vid="9lNIwOOMVHk",
     title="Humane Ai Pin: a phone with no screen",
     label="Humane · official video · 2023 · excerpt"),
dict(kind="data", act="Intelligence", figure="$116M",
     cap="what HP paid for Humane in 2025. The Ai Pin stopped working that month.",
     src="TechCrunch, 18 Feb 2025"),
dict(kind="video", act="Intelligence", slug="airpods-pro-3", vid="EMmKs8vMKhU",
     title="AirPods Pro 3: live translation in your ears", label="Apple · official video · 2025"),
dict(kind="bullets", act="Intelligence", title="Same idea, two results", items=[
  "Humane: a new device and new habits",
  "price: $699, plus $24 every month",
  "Apple: the AI goes into earphones people already wear",
  "a good technology needs a product people already want"],
  src="Humane launch video, Nov 2023; Apple, Sep 2025"),

dict(kind="anchor", act="Intelligence", kicker="Trend 3 · Spatial computing",
     text="The screen moves from your hand to your eyes."),
dict(kind="video", act="Intelligence", slug="meta-ray-ban-display", vid="hrj4NQuE93M",
     title="Meta Ray-Ban Display", label="Ray-Ban | Meta · official video · 2025"),
dict(kind="bullets", act="Intelligence", title="Glasses, not a headset", items=[
  "a small screen inside the right lens",
  "a wristband reads muscle signals to control it",
  "$799, on sale in the US since 30 September 2025",
  "your question: what do you want to see without your phone?"],
  src="Meta, Connect 2025 announcement"),

dict(kind="anchor", act="Intelligence", kicker="Trend 4 · Hyper-personalization",
     text="One product, made for one person."),
dict(kind="video", act="Intelligence", slug="loreal-cell-bioprint", vid="JDbEUQ13nGw",
     title="L'Oréal Cell BioPrint", label="L'Oréal Groupe · official video · 2025"),
dict(kind="bullets", act="Intelligence", title="A laboratory on the counter", items=[
  "skin analysis in five minutes, from proteins in the skin",
  "it predicts which ingredients will work on your skin",
  "the lab-on-a-chip comes from NanoEnTek, a Korean startup",
  "a big brand plus a startup: a common model"],
  src="L'Oréal Groupe press release, CES, 6 Jan 2025"),

dict(kind="anchor", act="Intelligence", kicker="Trend 5 · Quantum computing",
     text="A new kind of computer for a few very hard problems."),
dict(kind="video", act="Intelligence", slug="google-willow", vid="W7ppd_RY-UE",
     title="Google Willow", label="Google Quantum AI · official video · 2024 · excerpt"),
dict(kind="data", act="Intelligence", figure="10<sup>25</sup> years",
     cap="what a supercomputer would need for a test Willow did in under five minutes",
     src="Google, 9 Dec 2024"),
dict(kind="bullets", act="Intelligence", title="Real progress, few uses yet", items=[
  "Willow: 105 qubits, fewer errors as the chip grows",
  "the test in the video has no practical use yet",
  "startup: Multiverse Computing (San Sebastián)",
  "quantum-inspired maths to make AI models smaller: $215M raised in 2025"],
  src="Google, 9 Dec 2024; Multiverse Computing, 12 Jun 2025"),

# III. Machines
dict(kind="anchor", act="Machines", kicker="Trend 6 · Robotics and humanoids",
     text="Robots leave the factory cage."),
dict(kind="video", act="Machines", slug="unitree-h2", vid="eUdBIFkMh-M",
     title="Unitree H2: a humanoid you can order", label="Unitree Robotics · official video · October 2025"),
dict(kind="compare", act="Machines",
     fig_a="$90,000", lbl_a="Unitree H1 · April 2024",
     notes_a=["full-size humanoid, about 1.8 m", "no hands as standard"],
     fig_b="$29,900", lbl_b="Unitree H2 · October 2025",
     notes_b=["full-size humanoid, about 1.8 m", "31 joints, hands as an option"],
     cap="two different robots. the price to buy a full-size humanoid fell by two thirds in eighteen months",
     src="Unitree list prices, H1 and H2"),
dict(kind="data", act="Machines", figure="22,000",
     cap="humanoid robots shipped in the first half of 2026: more than in all of 2025. 86% came from Chinese companies.",
     src="Counterpoint Research, 20 Aug 2026"),
dict(kind="video", act="Machines", slug="bmw-figure", vid="xLVm-QKEZSI",
     title="Figure 02 at BMW: one task, one factory", label="BMW Group · official video · August 2024"),
dict(kind="bullets", act="Machines", title="The Roomba from my 2021 map", items=[
  "iRobot, maker of the Roomba, filed for bankruptcy in December 2025",
  "cheaper Chinese competitors, plus US import taxes",
  "its own Chinese manufacturer, Picea, takes over the company",
  "being first in a market is not enough"],
  src="Manufacturing Dive, 15 Dec 2025"),

dict(kind="anchor", act="Machines", kicker="Trend 7 · Autonomous mobility",
     text="Cars with nobody in the driver's seat."),
dict(kind="video", act="Machines", slug="waymo-sensors", vid="Vwrz1hfVeSM",
     title="Waymo: cameras, radar and lidar together", label="Waymo · official video · September 2026"),
dict(kind="data", act="Machines", figure="500,000",
     cap="paid Waymo rides every week in 10 US cities: ten times more than in May 2024",
     src="TechCrunch, 27 Mar 2026 (figures from Waymo)"),
dict(kind="bullets", act="Machines", title="Two countries, two leaders", items=[
  "Waymo (Alphabet): target of one million rides a week in 2026",
  "Baidu Apollo Go: 3.4 million driverless rides in the last quarter of 2025",
  "Apollo Go: 26 cities, including Dubai and Abu Dhabi",
  "your question: what changes in a city with no drivers?"],
  src="Automotive World, Feb 2026 (Waymo co-CEO); Baidu Q4 2025 results, 26 Feb 2026"),

dict(kind="anchor", act="Machines", kicker="Trend 8 · Additive manufacturing",
     text="From printed prototypes to printed parts."),
dict(kind="video", act="Machines", slug="divergent-daps", vid="iTrc7Z2Av4Q",
     title="Divergent: car frames made by printers and robots", label="Divergent · official video · 2025"),
dict(kind="data", act="Machines", figure="20 &rarr; 1",
     cap="parts in the fuel nozzle tip of a GE jet engine, once it is 3D printed. It is also about 25% lighter.",
     src="GE Aerospace, 4 Oct 2018"),
dict(kind="video", act="Machines", slug="icon-wolf-ranch", vid="k0REJf3rv44",
     title="ICON: 100 printed houses in Texas", label="ICON · official video · 2023"),
dict(kind="bullets", act="Machines", title="From prototype to production", items=[
  "2021 in this class: printed trainers and prototypes",
  "today: engine parts, car frames and houses",
  "startups: Divergent (cars, aerospace) and ICON (houses)",
  "your question: which part in your project has too many pieces?"],
  src="GE Aerospace; Divergent; ICON and Lennar, July 2023"),

# IV. Infrastructure
dict(kind="anchor", act="Infrastructure", kicker="Trend 9 · Chips",
     text="Every trend in this class runs on a chip."),
dict(kind="anchor", act="Infrastructure", kicker="Trend 10 · Space and satellites",
     text="Your phone talks directly to a satellite."),
dict(kind="anchor", act="Infrastructure", kicker="Trend 11 · Energy and climate",
     text="Cheaper batteries change what we can electrify."),

# V. Money and life
dict(kind="anchor", act="Money and life", kicker="Trend 12 · Fintech and stablecoins",
     text="Money that moves like a message."),
dict(kind="anchor", act="Money and life", kicker="Trend 13 · Biotech",
     text="Biology becomes an engineering problem."),

# VI. Your turn
dict(kind="anchor", act="Your turn", text="A trend is not a business. Where is the opportunity?"),

dict(kind="close", title="Thank you", mail="javier@ncompany.es", who="Javier Fuentes Ibáñez", org="NCompany"),
]
