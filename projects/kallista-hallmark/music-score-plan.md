# HOLIDAY RESERVATIONS: trailer score plan (ElevenLabs Music, timed to the AG preview cut)

Measured from `HolidayReservationsAG.mp4` (65.8s, 24 fps).

## Cut map
| Time | Picture |
|---|---|
| 0.0–4.5 | DPC "Presents" card, then "This winter..." |
| 4.5–18.3 | Couch clip 1 (wide, then a Kallista close-up at 10.0 and Becca at 14.3) |
| 18.33 | **White flash** → rink, "Hey..." |
| 22.12 | **White flash** → couch, "The coffee shop!" |
| 27.92 | **White flash** → barista (28.1), then Kallista's stare (30.0) |
| 31.92 | **White flash** → couch, "Nobody does that." |
| 33.42 | Card: "She came for a quiet getaway..." |
| 35.8 | Becca: "Ooh, the music store!" → Kallista closes her eyes (39.9) |
| 41.12 | **White flash** → music store (Adrian at 47.1; the bossa nova is in the scene) |
| 51.6 | Kallista laughs behind her hand |
| 52.75 | **White flash** → card: "...love was in the last place she'd look." |
| 55.0 | Title: *Holiday Reservations* |
| 59.5 | "Premieres December 12" / DPC |
| 62.9 | Black → stinger: Adrian alone at the keyboard (63.4–65.3) |

## Why Video to Music came out flat
It scores the overall mood of the video, so it never changes direction. A comedy trailer needs the music to **stop on the jokes**. The score drops out for the music store, because the bossa nova is the joke, and comes back big on the title.

## ElevenLabs Music: sections
**Global style (every section):** a warm, whimsical holiday romantic-comedy trailer score, instrumental, 92 BPM, F major, with fingerpicked acoustic guitar, pizzicato strings, celesta, sleigh bells and a light orchestra. **Global negative:** vocals, choir, EDM, heavy drums, dark, minor key.

| # | Section name | Duration | Positive styles | Negative styles |
|---|---|---|---|---|
| 1 | Ident and "This winter" | 4.5s | celesta and glockenspiel shimmer, two-note sleigh-bell ident, soft string swell, magical, cozy | percussion, guitar |
| 2 | Cozy couch setup | 13.8s | soft fingerpicked acoustic guitar, light pizzicato bass, very sparse and low, leaves room for dialogue, a small plucky pickup into the end | drums, brass, busy melody |
| 3 | Flashback run | 15.1s | bouncy, playful staccato pizzicato strings and celesta, stop-start comedic phrasing, light tambourine, short string flourishes, quirky and mischievous | heavy drums, long legato melody |
| 4 | Quiet getaway, then the music store | 7.7s | starts as a held, warm string pad with a single celesta note (a breath), then a coy, curious tiptoeing pizzicato that rises and ends on an abrupt cut-off | drums, brass |
| 5 | Dropout | 11.65s | near silence: one faint sustained low string note that fades to nothing within 2 seconds, then silence | melody, rhythm, percussion, any instrument after the fade |
| 6 | Love in the last place, then the title | 10.15s | starts tender, with solo felt piano and soft strings, then blooms into the full warm holiday orchestra: sleigh bells, a celesta sparkle on the title, a soaring string resolve, ending on one bright, punchy brass and timpani button | minor key, sad, vocals |

Total 62.9s. After the button, leave silence: the stinger (62.9–65.8) plays with no score, just the bossa nova in the scene.

## In the edit (done here, after the cue is generated)
- **Flash hits:** add a soft string swell or chime into each white flash at 18.33, 22.12, 27.92, 31.92, 41.12 and 52.75, on top of the whoosh.
- **Ducking:** lower the score about 10 dB under every line of dialogue.
- **Dropout:** hard-mute the score from about 43s to 52.75s, whatever the generator does there.
- **The button:** line it up to land on the black at 62.9s.
- **Fitting the sections:** if a section comes out a little long or short, I'll trim or stretch it to the cut.

## Suno alternative (for the acoustic song bed / cast roll)
Suno can't follow timestamps. Use it for a full song with lyrics, then I'll cut it to the edit the same way. Style prompt:
`warm acoustic holiday indie-folk, female breathy vocal, fingerpicked guitar, celesta, sleigh bells, soft strings, 92 BPM, F major, cozy, hopeful, Hallmark Christmas movie`

## Result: `score_mistletoe_v1.mp3` (63.0s, ElevenLabs)
Measured loudness: steady 0–33s. Section 4 became a fade (33–40s), 41–54s is near silence (the dropout worked), the last section bursts in at 54.5s and fades out by about 61.5s. There's no hard button at the end, and section 6 began about 1.7s later than planned, so there's no tender piano under the "...love was in the last place" card.
**Mix v1 (`preview_with_score_v1.mp4`, scratchpad):**
- Score 0–43s at −11 dB, ducked under the preview's own audio (sidechain: threshold 0.025, ratio 8, attack 15 ms, release 450 ms), then a fade 40.5–43s.
- Hard silence through the music store.
- Score 54.0–63.0s placed at 54.5s, so the burst lands on the title card (55.0s), at −5 dB with no ducking.

## Finale score options (ElevenLabs Music, composition plan, instrumental, 30.8s)
Sections map to `finale_v2`: Cast Roll Chorus 21.6s · Title Swell 4.6s (bell ~22.05) · Confirmed Button 4.6s (stamp ~27.8, ring-out).
- **A acoustic folk-pop** (`score_finale_A_acoustic_folkpop.mp3`): 110 BPM D major, strummed/fingerpicked guitars, glockenspiel hook, sleigh bells, claps, upright bass.
- **B orchestral Hallmark** (`score_finale_B_orchestral_hallmark.mp3`): 96 BPM E-flat major, soaring strings, horn countermelody, celesta, harp, sleigh bells.
- **C dream-pop holiday** (`score_finale_C_dreampop_holiday.mp3`): 100 BPM A major, chiming reverb guitars, analog pads, glockenspiel, soft drums.
Mix: music −5 dB, dipped to 60% under the bell (21.95–22.7) and stamp (27.7–28.4), fade 30.1–30.8, silent for the stinger. Plan JSONs kept in the session scratchpad (`el/music_*.json`).

## Suno: "Snow on Every Conversation" (member's render, 43s, ~99.4 BPM)
Song map (from speech-to-text): vocals 1.92–20.3 ("I made holiday reservations… never planned on you, no.") · ooh section 22.3 · **Hey! 25.82** · oohs · Hey! 30.62 · instrumental 31–38.1 · final hit 38.13 with a ring-out to ~41.5.
**Finale fit (`finale_v3_suno.mp4`):** song 0–26.76 placed at +1.98s, so the first **Hey! lands on the stamp (27.8)** and "...on you, no." lands on the title (22.08). Spliced on the beat at finale 28.71 to the song's ending (38.10 on). Ring-out fades out by 31.3, black stays silent, then the stinger. Song −3 dB, dipped to 65% under the bell.
**v4 (`finale_v4_suno.mp4`):** removed the silent opening. The song's own instrumental bars (song 31.59–35.20, full band and sleigh bells) pre-roll at finale 0, crossfading on the beat into the song intro (1.50) at finale 3.48. Everything after that is unchanged: "no." on the title, Hey! on the stamp.
**v5:** the whole song moved up (song 1.50 = finale 0), so the bells start on frame one and "I made holiday reservations" lands on Kallista.
**v6 (`finale_v6_suno.mp4`, the current pick):** v5 timing. Title-card bell removed (finale audio muted 21.6–26.2). The song ends after the first Hey! (finale 24.32–24.88) with a fade 24.9–25.7. At 25.23 (on the beat) a solitary glockenspiel note plays: v3 SFX `sfx_glock_note_v3_take2` (G5) pitched to C6 to match the song (key of C, tuned ~12 cents flat), plus a 4s synthetic hall reverb, giving `sfx_glock_C6_reverb.wav` at −4 dB. It rings out under the stamp (27.8) and is gone by ~29.5.
**v7 (`finale_v7.mp4`, LOCKED chime):** same as v6, but the glock is replaced by the member's ElevenLabs chime `sfx_chime_crystal_final.mp3` (a crystal ting at C7 plus E6), tuned −16 cents to the song, onset at 25.23, −4 dB, no extra reverb.
**v8 (`finale_v8.mp4`):** the chime is **untuned** (original pitch) with a slight hall reverb (dry 0.9 / wet 0.22, 4s IR), giving `sfx_chime_crystal_final_verb.wav`. Onset 25.23, −4 dB.
