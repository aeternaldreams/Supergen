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
