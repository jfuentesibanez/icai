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
dict(kind="video", act="Infrastructure", slug="asml-high-na", vid="h_zgURwr6nA",
     title="ASML: the machine that prints chips", label="ASML · official video · June 2024"),
dict(kind="data", act="Infrastructure", figure="13.5 nm",
     cap="the wavelength of the light in ASML's EUV machines: almost x-rays. The technology is unique to ASML.",
     src="ASML, EUV lithography systems"),
dict(kind="bullets", act="Infrastructure", title="One machine, one company", items=[
  "ASML is Dutch: 2025 sales of €32.7 billion",
  "the most advanced chips are made with its EUV machines",
  "one supplier means a risk for every chip maker",
  "your question: what can a startup build around this machine?"],
  src="ASML, Q4 2025 results, 28 Jan 2026; ASML website"),

dict(kind="anchor", act="Infrastructure", kicker="Trend 10 · Space and satellites",
     text="Your phone talks directly to a satellite."),
dict(kind="video", act="Infrastructure", slug="t-satellite", vid="HLw6ZovMpLI",
     title="T-Satellite: no signal, no problem", label="T-Mobile · official video · February 2025"),
dict(kind="data", act="Infrastructure", figure="657",
     cap="Starlink satellites that work as mobile phone towers in space. Normal phones connect with no extra equipment.",
     src="T-Mobile Newsroom, July 2025"),
dict(kind="video", act="Infrastructure", slug="sateliot", vid="hVC-1yhzmbk",
     title="Sateliot: 5G satellites from Barcelona", label="Sateliot · official video · November 2025"),
dict(kind="bullets", act="Infrastructure", title="Two ways into space", items=[
  "SpaceX and T-Mobile: text messages and apps for people",
  "Sateliot (Barcelona): 5G satellites for sensors and machines",
  "Sateliot opened Europe's first 5G satellite centre in November 2025",
  "your question: what needs a connection where there is no mobile tower?"],
  src="T-Mobile Newsroom, 2025; Sateliot, 2025"),

dict(kind="anchor", act="Infrastructure", kicker="Trend 11 · Energy and climate",
     text="Cheaper batteries change what we can electrify."),
dict(kind="video", act="Infrastructure", slug="catl-shenxing", vid="Z75mVvU7MPQ",
     title="CATL: a full charge in six minutes",
     label="CATL · official video · April 2026 · excerpt · figures from CATL"),
dict(kind="data", act="Infrastructure", figure="$108",
     cap="average price of one kWh of lithium-ion battery pack in 2025, 8% lower than in 2024. For grid storage: $70.",
     src="BloombergNEF battery price survey, Dec 2025"),
dict(kind="bullets", act="Infrastructure", title="28 April 2025: Spain and Portugal go dark", items=[
  "continental Spain and Portugal lost all electric power",
  "cause: problems with voltage control, not renewables as such",
  "more solar power needs more control and more storage",
  "an opportunity for engineers: batteries, inverters, grid software"],
  src="ENTSO-E expert panel, final report, 20 Mar 2026"),

# V. Money and life
dict(kind="anchor", act="Money and life", kicker="Trend 12 · Fintech and stablecoins",
     text="Money that moves like a message."),
dict(kind="video", act="Money and life", slug="stripe-stablecoins", vid="H4eWjC_nXcw",
     title="Stripe: what is a stablecoin?", label="Stripe Developers · official video · September 2025 · excerpt"),
dict(kind="chart", act="Money and life", title="Dollar stablecoins in circulation, $ billion",
     years=list(range(2020, 2027)), highlight="Stablecoins", round=50, grid=100,
     series={"Stablecoins": [4.2, 27.4, 161.9, 137.4, 129.8, 204.8, 305.9]},
     note="$306 billion in January 2026, eleven times January 2021",
     src="DefiLlama, stablecoins in circulation pegged to the US dollar, 1 January of each year"),
dict(kind="bullets", act="Money and life", title="Blockchain, without the hype", items=[
  "2021 in this class: NFTs and DeFi",
  "2025: first US law for stablecoins, the GENIUS Act",
  "Stripe paid $1.1 billion for Bridge, a stablecoin startup from 2022",
  "your question: which payment is still slow and expensive?"],
  src="White House, 18 Jul 2025; TechCrunch, 5 Feb 2025"),

dict(kind="anchor", act="Money and life", kicker="Trend 13 · Biotech",
     text="Biology becomes an engineering problem."),
dict(kind="video", act="Money and life", slug="alphafold", vid="r4-hXO7MLVU",
     title="AlphaFold: a 50-year problem solved by AI", label="Google DeepMind · official video · 2025"),
dict(kind="data", act="Money and life", figure="200 million",
     cap="protein structures AlphaFold2 predicted: almost all known proteins. Nobel Prize in Chemistry, 2024.",
     src="Nobel Prize press release, 9 Oct 2024"),
dict(kind="video", act="Money and life", slug="vertex-casgevy", vid="NL6iYtyI7Vw",
     title="Casgevy: the first medicine made with CRISPR",
     label="Vertex Pharmaceuticals · official video · December 2025"),
dict(kind="bullets", act="Money and life", title="From the laboratory to the patient", items=[
  "Casgevy: first CRISPR therapy, approved in the UK in November 2023",
  "it edits the patient's own cells to treat sickle cell disease",
  "startup: Isomorphic Labs, DeepMind's spin-off, raised $600M in 2025",
  "your question: which other hard problem could AI make faster?"],
  src="Vertex, 16 Nov 2023; Isomorphic Labs, 31 Mar 2025"),

# VI. Your turn
dict(kind="bullets", act="Your turn", title="What the failures teach us", items=[
  "Dash and Amazon Go: the technology worked, the numbers did not",
  "Humane: a new device needs a strong reason to change habits",
  "iRobot: being first did not protect it from cheaper competitors",
  "a trend gives you the timing, not the business model"]),
dict(kind="bullets", act="Your turn", title="Your turn: 15 minutes, groups of four", items=[
  "choose one of the thirteen trends",
  "choose one problem you know well from your own field",
  "write it down: who pays, and why now?",
  "two minutes per group to present it"]),
dict(kind="anchor", act="Your turn", wide=True,
     text="In five years, some of today's examples will be dead too.<br>Build one that is not."),

dict(kind="close", title="Thank you", mail="javier@ncompany.es", who="Javier Fuentes Ibáñez", org="NCompany"),
]
