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
dict(kind="anchor", act="Opening", text="In 2021 this class had nine trends. Some of them are dead."),

# II. Intelligence
dict(kind="anchor", act="Intelligence", kicker="Trend 1 · Generative AI and agents",
     text="Software that writes, talks and acts for you."),
dict(kind="anchor", act="Intelligence", kicker="Trend 2 · Smart devices",
     text="The AI moves from the cloud into the object."),
dict(kind="anchor", act="Intelligence", kicker="Trend 3 · Spatial computing",
     text="The screen moves from your hand to your eyes."),
dict(kind="anchor", act="Intelligence", kicker="Trend 4 · Hyper-personalization",
     text="One product, made for one person."),
dict(kind="anchor", act="Intelligence", kicker="Trend 5 · Quantum computing",
     text="A new kind of computer for a few very hard problems."),

# III. Machines
dict(kind="anchor", act="Machines", kicker="Trend 6 · Robotics and humanoids",
     text="Robots leave the factory cage."),
dict(kind="anchor", act="Machines", kicker="Trend 7 · Autonomous mobility",
     text="Cars with nobody in the driver's seat."),
dict(kind="anchor", act="Machines", kicker="Trend 8 · Additive manufacturing",
     text="From printed prototypes to printed parts."),

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
