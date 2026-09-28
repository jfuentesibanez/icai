# ICAI — Javier's university class decks

Javier Fuentes Ibáñez (NCompany) teaches at ICAI (Universidad Pontificia Comillas). Every class
deck lives here, one subfolder per class (`YYYY-MM-DD-topic/`; a class taught every year, like `tech-trends/`,
is named by topic and shows the academic year), all in
one git repo. Each subfolder is self-contained, with its own copy of the engine, so an old class
still builds exactly as it was taught.

The engine comes from the CDP / Headspring robotics keynote (Madrid, 24 September 2026, repo
`jfuentesibanez/robotics-2026`, folder `~/Documents/Desarrollo/Headspring Robots/deck`). That talk
is delivered and public; never edit it to build a class.

## Working with Javier

- He writes in Spanish, fast and with typos. Answer in Spanish. Slide text language depends on
  the class; ask if unclear.
- He reviews slide by slide from screenshots and asks "¿qué significa esto?". Explain, offer
  two or three rewrites with a recommendation, and change only when he picks one.
- When the audience is not native in the slide language, write literally: no idioms, no
  unexplained metaphors ("the other column", "rounding error", "yardstick" all had to go).
- Verify every figure at the primary source before it goes on a slide, and put the source in
  `src`. Twice in the keynote a widely quoted number turned out to be from a different study.

## The one rule

Never hand-edit the generated HTML. Content is `build/slides.py`, engine is `build/build.py`:

```bash
cd <class>/build && python3 build.py     # stdlib only
```

`META` at the top of `slides.py` sets title, footer, date, author and output file name.

## Slide kinds (build.py)

`cover · agenda · quote · bullets · anchor · data · compare · chart · video · breath · close`

- One idea per slide, four bullets at most, ~12 words each, lower case after the first word.
- `anchor`: one big sentence, no illustration; `wide=True` for a three-line anchor.
- `compare`: two figures that are not the same thing measured twice. Never an arrow between them.
- `chart`: SVG line chart from numbers in slides.py, one highlighted series.
- `data` with `map="KOR"`: country outline from `build/maps/<code>.geo.json` (Natural Earth 10m).
- `bullets` with `polaroids=[...]`: photos drop one per click and pile up; `pin=` pins one
  polaroid over an illustration's corner. Credits come from `build/photos/credits.json`.
- The act rail across the top and the `agenda` slide build themselves from each slide's `act`.
- Logos are optional: `build/logos/left.png`, `right.png`, `right-dark.png`.

## Illustrations (animated WebP)

Each piece ships twice: the first frame embedded in the HTML, the loop in `img/`, fetched when
its slide comes up and prefetched in the background. Always go through `prepare-media.py`:

- Pillow's `convert('RGB')` keeps only the first frame of an animated WebP. It destroyed the
  animations once.
- The originals have irregular per-frame timing (80–560 ms). `prepare-media.py` reads it from the
  ANMF chunks; a fixed frame rate plays them at the wrong speed.
- It also shifts each file's background to the paper colour #F7F4EE, or the image edge shows.

## Photos

Only CC BY, CC BY-SA, CC0 or public domain, from Wikimedia Commons, credited on the slide. Check
the licence first: a museum's own photo is often NC (non-commercial), and Commons usually has a
free one of the same object. Cut-outs: the macOS Vision subject mask via PyObjC works well
(the command-line Swift SDK here is too old for the API).

## Videos

Play from a local file, not from YouTube: download with yt-dlp at 720p H.264
(`-f "bv*[height<=720][vcodec^=avc1]+ba[acodec^=mp4a]"`), remux with `-movflags +faststart`,
put it in `video/<slug>.mp4`. Use the official channel's upload, not a re-upload. Long videos:
cut an excerpt with ffmpeg and say "excerpt" on the slide. A clip with no audio track needs a
silent one added, or some browsers pause it. GitHub rejects files over 100 MiB.

## Publishing

GitHub Pages serves a repo's `main` branch. A cached old version is the browser, not the
deploy: Cmd+Shift+R. The repo must be public for free Pages, and it would carry the video copies.
