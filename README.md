# ICAI — class decks

One folder per class, named by date (`YYYY-MM-DD`, plus a topic once there is one).
Each folder is self-contained: `build/slides.py` holds the content, `build/build.py` the engine
(the same one as the CDP robotics keynote, September 2026), and `python3 build.py` inside `build/`
writes the deck next to it.

```
icai/
  2026-09-28/        first class
    build/           slides.py, build.py, prepare-media.py, photos/, maps/, poster/, logos/
    img/  video/     animated illustrations and clips for that class
```

To start a new class, copy the most recent class folder, empty `build/slides.py` down to the
cover and close, and clear `img/`, `video/`, `build/poster/` and `build/photos/`.
