# ICAI — class decks

One folder per class. A one-off class is named by date (`YYYY-MM-DD-topic`); a class taught
again every year is named by topic (`tech-trends/`) and shows the academic year instead of a day.
Each folder is self-contained: `build/slides.py` holds the content, `build/build.py` the engine
(the same one as the CDP robotics keynote, September 2026), and `python3 build.py` inside `build/`
writes the deck next to it.

```
icai/
  tech-trends/       Tech Trends (Entrepreneurship & Innovation), taught every year
    build/           slides.py, build.py, prepare-media.py, photos/, maps/, poster/, logos/
    img/  video/     animated illustrations and clips for that class
```

To start a new class, copy the most recent class folder, empty `build/slides.py` down to the
cover and close, and clear `img/`, `video/`, `build/poster/` and `build/photos/`.

## Publishing

The repo is public and served by GitHub Pages; the site root lists the classes.
Video files are **not** in the repo (`.gitignore`): they stay in each class's `video/`
folder on the local disk. Opened from disk or a local server, the deck plays them offline;
opened from GitHub Pages, it plays the same clip from YouTube, cut with `start`/`end`
from `slides.py`. Re-download a lost clip from its `vid` with the yt-dlp line in CLAUDE.md.
