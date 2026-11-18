# Cold open assembly: edit decision list

## v1 (44.4s, 1024x576, 24 fps)
White flashes are 3 frames (0.125s) of white with silence.

| # | Source | In–out | Notes |
|---|---|---|---|
| 1 | couch 1 `e283454221e7` | 0–14.3 | through "Hockey player." |
| – | white | 3 frames | |
| 2 | rink `2878e67cdf3e` | 0–3.7 | ends after "Hey..." |
| – | white | 3 frames | |
| 3 | couch 2 v2 `87c6f21670aa` | 0–5.7 | Becca: "The coffee shop!..." |
| – | white | 3 frames | |
| 4 | barista `aaebefa67da6` | 0–1.9 | wink |
| 5 | café stare `79e0726cbb61` | 0–2.0 | blink |
| – | white | 3 frames | |
| 6 | couch 2 v2 `87c6f21670aa` | 5.7–end | "Nobody does that." + reaction. Becca's "Ooh, the music store! Some broody musician." (`couch2_dialogue_15s.mp3` 8.2–12.3) starts 0.35s after Kallista's line and runs as an L-cut about 0.9s into the music store entrance |
| – | white | 3 frames | |
| 7 | music store edit v3 (website render, trimmed) | 11.67s | garble muted; render 3.6–5.6 cut out at the existing cut; no button SFX; `roomtone_music_store.mp3` at -6 dB; 3-frame fade to white |

## To do
- Bossa nova + "WOO!" in the music store: BOOM at about 8.25s into the music store edit (the end of "dark—"); WOO around 10.6s.
- Room tones for the B&B sitting room, the rink and the café (the couch clips are dry).
- Couch clip 3: "He was perfect... until the bossa nova." → Milly → "...The laundromat."

## Bossa nova tests (music store edit v3)
`bossa1–4.mp3` and `woo.mp3` are in `voices/holiday-reservations/`. Each bossa nova is about 3.95s of music.
- Bossa nova starts at 8.25s (the end of "dark—"). The first 1.5s plays at normal speed, the rest at 1.15x ("gets worse").
- It drops 5 dB under Kallista's close-up (10.375s on) and fades out 11.45–11.67 with the white flash.
- WOO at 9.85s (−1 dB), just before the cut to her laugh.
- Gains for a matched mean of about −20 dB in the mix: bossa1 0, bossa2 +4.1, bossa3 +3.5, bossa4 +3.0 dB. A limiter at −0.4 dBFS on the mix.
- Count-in: `intro_clicks.mp3` (two ticks, 0.53s) at 7.76s (−3 dB), so the second tick lands just before the hit at 8.25s.
