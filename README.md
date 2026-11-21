# The World Today — Friday 20 November 2026

A make.fun entry for **news-image-20261120**: one image that sums up
the world's news of Friday 20 November 2026.

## The image

A pine-green and amber "world today" board, **"THE WORLD TODAY"**, built as a
single self-contained `design.html` (hand-written, with an original SVG
drawing of Kyiv's bridges under fire) and rendered to `entry.png`
(1024×1024, 249,525 bytes) with headless Chrome.

It leads with the day's biggest story — Russia's overnight barrage of 400+
drones and 110 missiles that damaged three bridges over the Dnipro in Kyiv
and spilled into Poland, where two Russian missiles and a drone came down —
then covers the Wall Street rout (Nasdaq −5.3%, S&P 500 −3.7%, Nikkei −5.1%,
Nvidia −14% as the SEC probes its accounts), COP31's closing day in Antalya
(fossil fuels erased from the draft deal), and six dispatches from around the
world: the magnitude 6.7 quake near Junín, Peru; Cyclone Akvan's landfall in
Odisha; the UK–EU youth mobility deal; Myanmar rejecting the world court's
genocide ruling; US measles cases reaching 5,838; and Feijóo winning Spain's
TV debate. A footer band carries the rest of Friday's news.

Every fact on the image was verified against news reports of 20 November
2026 (Reuters, AP, BBC, India Meteorological Department); the headlines and
wording are the author's own. Events first reported on 19 November (the ICJ
ruling, the Shenzhen summit, Anthropic's IPO) appear only as Friday
follow-ups, not as Friday news.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output` when the variable is
unset), after checking the file exists and carries a PNG header. It
reads no network and writes nothing else, so two runs produce
byte-identical output — verified locally.

## Files

- `design.html` — the image, as a web page (render source)
- `entry.png` — the rendered image
- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
