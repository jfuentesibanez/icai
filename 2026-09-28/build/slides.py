# -*- coding: utf-8 -*-
# Slide content, in order. Same engine as the CDP robotics keynote (Sept 2026).
# kind: cover | agenda | quote | bullets | anchor | data | compare | chart | video | breath | close
META = dict(
    title="Title of the class",
    foot="Course · topic",
    date="28 September 2026",
    author="Javier Fuentes Ibáñez",
    file="clase.html",
)

S = [
dict(kind="cover", title="Title of<br>the class", who="Javier Fuentes Ibáñez",
     org="University", date="28 September 2026"),

dict(kind="anchor", act="First act", text="One big sentence."),

dict(kind="bullets", act="First act", title="One idea per slide", items=[
  "four bullets at most",
  "about twelve words each",
  "every figure carries its source",
  "plain words, no idioms"],
  src="source line goes here"),

dict(kind="close", title="Thank you", mail="javier@ncompany.es", who="Javier Fuentes Ibáñez", org="NCompany"),
]
