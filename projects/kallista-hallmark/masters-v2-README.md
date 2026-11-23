# HOLIDAY RESERVATIONS: approved masters v2 (Supergen version)

Everything approved, **without edit treatments** (no white flashes, no dips, no score in the scene clips), so another editor (e.g. Antigravity / Gemini) can build its own cut.
All video is 1024×576, 24 fps (M1 also at 1080p). Scene clips carry their approved dialogue, room tone and SFX.

## final/ (edit-ready, trimmed, in story order)
| # | File | What it is |
|---|---|---|
| 01–08 | couch1 · rink flash · couch2 coffee shop · café flash · couch2 music-store line · music store · couch3 (Milly) · laundromat | **Cold open** |
| 09 | M1_porch_576p / _1080p | "Are you following me?" / "I was hired... in August." (truck lettering fixed to CARPENTRY) |
| 10 | M2_sideyard | Marcus: dream-pop / Cal: "You looked her up." / "She's got style." |
| 11 | M3_sittingroom | "You're watching him again." / "Textbook denial..." |
| 12 | M4_cocoa | "Four days... same porch step." → group laugh (our voices) → Milly "Ha ha!" → the stare |
| 13 | M5_piano | "I could fix that." / "Some things are supposed to sound... a little broken." (out-of-tune piano bed) |
| 14 | M6_sidewalk | the slip → "I don't do... falling." / "In love? What's the worst that can happen?" / "Umm... you could die?" / "Okay... but besides that?" |
| 15 | M7_door | the half-open door, silent (night tone and wind chime) |
| 16 | card_pair1_this_winter | "This winter…" / "…**love** was in the last place she'd look." (4.58s, silent) |
| 17 | card_pair2_reservations | "She came for a quiet getaway…" / "…but she had her **reservations**." (4.58s, silent) |
| 18–22 | cast_kallista · cal · becca · marcus · milly | cast-roll shots with name cards |
| 23 | title_card_nosfx | HOLIDAY RESERVATIONS title (bell removed, as in finale v8) |
| 24 | tunein_card_stamp | reservation card + CONFIRMED stamp SFX |
| 25 | stinger | Adrian: bossa → WOO! → "...Beautifully dark." → smash to black |

## originals/
Untouched Supergen downloads, named by library ID, for re-cutting from scratch (scenes, pickups and cast raws).

## audio/
- **score/**: `score_suno_snow_on_every_conversation.m4a` (finale song, the member's Suno track) · `sfx_chime_crystal_final_verb.wav` (finale chime) · `montage_score_A/B.mp3` (ElevenLabs Music, 80.98s, timed to cards + montage, below)
- **sfx/**: approved v3 SFX (axe thunk, wood crack, stamp, bell +7, ice slip take 2, out-of-tune piano, wind chime) + hammer, flash whoosh, WOO, intro clicks, bossa #1
- **dialogue/**: approved scene tracks (M1–M6, couch 3, laundromat, stinger line, M4 laughs and squeal)
- **roomtone/**: all room tones
## keyframes/ (all start frames and references)
## reference/
`cold_open_assembly_v9.mp4` · `finale_v8.mp4` (locked) · `HolidayReservations_Supergen_rough_v1_scoreA.mp4` (full rough cut) · `OmniFlash_Scene11_M4.mp4`

## Rough cut v1 EDL (198.8s)
| Time | Section | Source |
|---|---|---|
| 0:00.0–1:20.9 | Cold open | reference/cold_open_assembly_v9 (finals 01–08 with 2-frame white flashes + whooshes) |
| 1:20.9–1:25.5 | Card pair 1 | final/16 |
| 1:25.5–1:35.6 | M1 | final/09 (576p) |
| 1:35.6–1:45.7 | M2 | final/10 |
| 1:45.7–1:57.1 | M3 | final/11 |
| 1:57.1–2:06.8 | M4 | final/12 (0–9.75) |
| 2:06.8–2:16.0 | M5 | final/13 (0–9.125) |
| 2:16.0–2:31.1 | M6 | final/14 (0–15.125) |
| 2:31.1–2:37.1 | M7 | final/15 (0–6.0) |
| 2:37.1–2:41.7 | Card pair 2 | final/17 |
| 2:41.7–3:18.8 | Finale | reference/finale_v8 (cast roll → title → tune-in → black → stinger; Suno song + chime) |
Montage score: `montage_score_A.mp3` from the start of card pair 1, −11 dB, sidechain-ducked under the clip audio (threshold 0.015, ratio 5, 25/400 ms). Sections: card 4.58 · montage bounce 41.42 (M1–M4) · the turn 9.17 (M5) · falling 15.17 (M6) · half-open door 6.0 (M7) · reservations lift 4.58 (card 2, ends on a held chord that cuts into the finale's sleigh bells).
