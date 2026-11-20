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
- Count-in: `intro_clicks.mp3` (4 ticks at 120 BPM, 0.5s apart) placed at 6.08s (−8 dB). The ticks fall at 6.26, 6.76, 7.26 and 7.75s, so the next beat is the bossa nova hit at 8.25s.
- Flash whoosh: `flash_whoosh.mp3` (0.53s). It goes on every white flash.

## v2 (44.2s): built by `scratchpad/tools/assemble.py`
- **Flashes:** a 9-frame dip through white (2 frames fading up to white, 2 frames of solid white, 5 frames fading down), with `flash_whoosh.mp3` (−4 dB) starting 0.15s before the white frames. Barista → stare stays a hard cut.
- **Room tones:** `roomtone_bnb.mp3` (−4 dB) under the couch clips, `roomtone_rink.mp3` (−4 dB), `roomtone_cafe.mp3` (−10 dB), and `roomtone_music_store.mp3` (already in the music edit).
- **Music store:** the bossa nova #1 version.
- **Becca's L-cut line** starts 29.53s.

## v3 (46.7s): Becca's line now lip-synced
- Becca pickup `bbc362eba079` (5s from `becca_mcu_crop.png` + `becca_musicstore_5s.mp3`, about 36 XCE): her face matches and the lip-sync is good.
- Couch 2 ending is now: couch 2 v2 5.7–7.0 ("Nobody does that.") → **Becca 0–4.4** ("Ooh, the music store! Some broody musician.") → couch 2 v2 8.9–10.1 (Kallista closes her eyes) → white flash → music store. Hard cuts within the couch; the B&B room tone runs across all three.
- Becca's L-cut line from the old track has been removed.
- Flashes at 14.3, 18.08, 23.87, 27.85, 34.83 and 46.58s.

## v4: barista clip audio muted (its sniff cut off abruptly); the café room tone carries the shot.

**Export fix (v4, rebuilt):** v2–v4 played badly in some players. The `fade=...:color=white` filter had switched the video to yuv444p (H.264 High 4:4:4), mixed with yuv420p white frames, and the index (moov) was at the end of the file. The script now forces `format=yuv420p` after the fades and `-profile:v high`, and the final pass re-encodes at constant 24 fps with `-movflags +faststart`. Always check exports with `ffprobe` for yuv420p, High profile and 24/1.

## v5 (66.4s): couch 3 added
- The music store (bossa nova #1 mix) → white flash → **couch 3 v3** (`couch3_assembled_v3.mp4`, 19.5s, its own B&B room tone) → white flash (ready for the laundromat).
- Flashes at 14.3, 18.08, 23.87, 27.85, 34.83, 46.58 and 66.21s.
- Exported as H.264 High, yuv420p, constant 24 fps, faststart.

## v6 (66.4s): audio clean-up
- **Café bed:** now one continuous `roomtone_cafe.mp3` overlay (−10 dB) laid across the barista and stare shots after the join. Per-shot tone slices left a small gap at the cut. The stare's own clip audio is muted too.
- **Music store:** Kallista's cough at the flash is muted (music edit dialogue from 10.97s). The two laugh bursts before it stay. Rebuilt `music_v3` and the bossa nova #1 mix.
- **Couch 3:** the first sigh (Supergen's scene audio 9.35–9.65s) is muted; the close-up's sigh before "...The laundromat." stays (`couch3_assembled_v4.mp4`).

## v7 (81.5s): laundromat added: COLD OPEN COMPLETE
- Laundromat one-beat `Scene7fix` (the member's website reference-mode render with `laundromat_oneshot_15s.mp3`): wide 0–2.83 ("Oh my god") · Kallista close-up 2.83–8.0 · over-the-shoulder on Cal 8.0–15 ("What?", the peel-off, "...break the ice", she snatches it back). Identities hold. Its audio is dry (no laundromat room tone yet).
- Flashes at 14.3, 18.08, 23.87, 27.85, 34.83, 46.58, 66.21 and 81.38s.

## v8: laundromat room tone (`roomtone_laundromat.mp3`, ElevenLabs Sound Effects, 15s, mixed at −15 dB to match the other locations).
- v9: laundromat ends at 14.4s (her hand on the bra), cutting the tug where Cal seems to yank it back.
