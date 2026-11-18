# Flash 3: the music store (Adrian and the bossa nova)

## Sequence in the edit (about 6–7s)
1. **WHITE FLASH** out of couch clip 2 (Becca: "...Some broody musician.").
1b. **Shot E, entrance (~1.5s, muted):** a wide, front-on shot. Kallista studies the SX920 panel; Adrian glides in from the right edge and plants his elbow on the panel. *tick... tick...* starts.
2. **Shot A, Adrian (~4.5s, lip-synced):** Kallista's point of view. Adrian leans on the PSR-SX920, chin on hand: "You play? ...Perhaps we could make something... beautifully dark—". A quiet count-in *tick... tick...* runs under the line (added in the edit).
3. **Hard cut on "dark—"**, and the bossa nova **BOOM**s in (added in the edit).
4. **Shot B, panic (~2s, muted):** Adrian jerks upright and stabs at buttons.
5. **Shot C, Kallista (~1.2s):** a flat, unblinking stare. The tempo speeds up and the horns join in.
6. Optional: a final 0.5s of Shot B, then the **"WOO!"** lands right on the white flash.
7. **WHITE FLASH** into couch clip 3: "He was perfect... until the bossa nova."

Total about 9s: E 1.5s + A 4.5s + B 2s + C 1.2s.
Cost: E, A and B are 5s Normal clips at 30–36 XCE each, **90–108 XCE in total** out of the 120 left. If credits run short, drop E and open on Shot A; the entrance is then implied. Shot C is a still with a slow push-in in the edit, so it costs nothing in Supergen.

---

## 1. Start frames (Nano Banana, 16:9)
Before you start: check that the PSR-SX920 product photo isn't mirrored. "YAMAHA" should read correctly.

### Frame E: wide entrance master, without Adrian
Adrian's face has to come from somewhere when he walks in from out of frame, so it comes from **reference pictures** (Supergen's `more_pictures`), not from frame 0. The shot is wide, so his face is small and moving and any drift barely shows. The next cut (Shot A) puts him in frame 0, which locks his face for the close-up.
Make the music store set (S6 in `nano-banana-keyframes.md`) first if you don't have it yet. Then edit it, attaching **the S6 set picture first**, then Kallista identity shots 1 and 2 and the PSR-SX920 photo:
> Keep this store, lighting and style. Reframe as a wide, eye-level shot facing straight into the keyboard department. In the center of the frame, the Yamaha PSR-SX920 stands on a black X-stand, seen from the front of the instrument (its back toward the camera, the player's side facing away), with a row of other arranger keyboards on stands receding behind it. Kallista, the woman from the Kallista references, stands behind the keyboard on its left half, facing the camera, looking down at the control panel with one finger hovering over a key. Same face: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) worn down with a center part. She wears a fitted black ribbed mock-neck sweater under an open charcoal wool coat and a dark grey chunky knit scarf. The right half of the keyboard and the open floor to its right are clear, with plenty of room for someone to step in. Warm afternoon light through tall windows with snow outside. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.

Shot A is the reverse angle from her side of the keyboard. Adrian stays on screen-right in both, so the cut matches.

### Frame A: Adrian, Kallista's point of view
Attach, in this order: **Adrian's front close-up identity shot first** (it sets a front-facing layout), then his full-body shot, then the PSR-SX920 photo.
> A medium close-up in 16:9 from the point of view of someone standing at an arranger keyboard in a music store. Camera at standing eye height, looking slightly down across the keyboard. In the lower foreground, the Yamaha PSR-SX920 runs across the bottom of the frame on a black X-stand: the keys nearest the camera and the control panel with its screen and buttons just beyond them, matching the attached product photo exactly, softly in focus. Adrian, the man from the Adrian reference, stands at the right end of the keyboard and leans down toward the camera: one elbow rests on the right end of the control panel, his chin on his hand, his face turned almost straight to the camera at eye level, filling the right-center of the frame. Same face as the reference: pale skin, spiky black hair with a choppy fringe, subtle smoky eyeliner, small gold cross earrings. He wears a long black wool double-breasted greatcoat with silver buttons, open over a black fine-knit turtleneck. No scarf. His expression is brooding and velvety, with heavy-lidded eyes and the faintest knowing smile, mouth closed. Behind him, softly out of focus: a row of arranger keyboards on stands receding diagonally, a wall of guitars, pressed-tin ceiling, tall windows with snow outside and garland across the top. Warm afternoon light. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text other than the brand name on the keyboard, no other logos, no watermark.

Check: his face should be large, sharp and nearly front-on; the panel should read correctly; there should be no scarf.

### Frame C: Kallista's stare (an edit of the café stare frame)
Attach, in this order: **the café stare frame `pic_1e5dc4fea01a` first** (it sets the exact framing, face and outfit), then Kallista identity shots 1 and 2.
> Keep this woman's face, expression, hair, pose, clothes and the camera framing exactly the same. Replace only the background: she now stands in the keyboard department of a spacious small-town music store, with a row of arranger keyboards on black stands softly out of focus behind her, a wall of guitars, a pressed-tin ceiling and tall windows with snow outside and garland across the top. Her face stays exactly as in the first image: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) worn down with a center part. Her expression is completely flat and unimpressed: a dead, unblinking stare with her mouth closed. Warm afternoon light. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.

(If Nano Banana redraws her face, run the "Kallista pass" from `nano-banana-keyframes.md` on the result.)

Upload both frames with the Supergen upload box and send me the `pic_` ids.

---

## 2. Adrian's line (ElevenLabs v3)
One voice: British male, low, velvety, unhurried (Text to Speech v3, or Text to Dialogue with one speaker).
```
[low, velvety, slow] You play? [pause] Perhaps we could make something... [intimate, breathy] beautifully dark—
```
- Make 3–4 takes. Pick one where "dark" stays up and unfinished rather than landing with a falling tone, and cut it just after the "k".
- Target about 4.0–4.5s of speech. If it runs past 4.7s, tell me: Shot A would then have to be a 10s clip (60–72 XCE instead of 30–36).

Send the file and I'll measure it, add 0.3s of room tone at the start, pad it to 5.0s, commit it to `voices/holiday-reservations/` and fill in the timestamps below.

---

## 2b. Shot E: Supergen prompt (5s, Normal, 16:9, no seed, no audio)
First frame: Frame E. More pictures: Adrian's front close-up identity shot and his full-body greatcoat shot (uploaded to Supergen, as `pic_` ids).
> Create a 5-second cinematic live-action romantic comedy shot in 16:9, beginning directly from the supplied first frame: a woman with platinum-blonde hair studying an arranger keyboard in a small-town music store. One continuous wide shot, locked camera, no cuts. Keep her face, the keyboard and the store exactly as in the first frame. Animate the scene naturally; do not interpolate or morph between the reference pictures. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon window light, shallow depth of field and organic film grain.
> KALLISTA is the woman behind the keyboard: reserved and deadpan; she moves very little.
> 0–1.5 seconds: ADRIAN, the man from the reference pictures (pale skin, spiky black hair with a choppy fringe, subtle smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat open over a black turtleneck, no scarf), glides in from the right edge of the frame with slow, self-important strides, his coat swinging, and smoothly sets one elbow down on the right end of the keyboard's panel, chin on his hand, gazing at her with a brooding look.
> 1.5–5 seconds: He holds the pose, perfectly still and very pleased with himself. Kallista keeps looking down at the panel, unimpressed, and does not look up.
> Sound: quiet music store ambience. No dialogue, no music, no other people, no subtitles, no watermarks.
Use 0 to the moment his elbow lands (about 1.5–2s), then cut to Shot A.

## 3. Shot A: Supergen prompt (5s, Normal, 16:9, no seed, scene audio = padded line)
Timestamps are placeholders until the audio is measured.
> Create a 5-second cinematic live-action romantic comedy close-up in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a brooding British musician leaning on an arranger keyboard in a small-town music store, seen from the point of view of the woman he is talking to. One continuous shot, locked camera, no cuts. Keep the keyboard, its panel and the store exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon window light, shallow depth of field and organic film grain.
> CHARACTER: ADRIAN (Speaker 1) is the only person in the shot, with a low, velvety British voice. Keep his face exactly as in the first frame: pale skin, spiky black hair with a choppy fringe, subtle smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat open over a black turtleneck, no scarf. A self-serious frontman: brooding and velvety, with slow, deliberate movements. He believes every word.
> 0–0.3 seconds: Complete silence. He holds the look, chin on his hand, mouth closed.
> 0.3–[t1] seconds: He raises his eyebrows slightly and speaks low and slow, looking straight into the lens: "You play?"
> [t2]–[t3] seconds: He leans a little closer, his elbow still resting on the panel, and lowers his voice to an intimate murmur: "Perhaps we could make something... beautifully dark—"
> [t3]–5 seconds: He holds the heavy-lidded look, mouth slightly open, completely still.
> Throughout: keep the supplied audio unchanged; add no voices, music or sound effects. His elbow stays on the panel the whole time. No extra people, no subtitles, no watermarks.

Use 0 to the end of "dark—". Discard the tail.

## 4. Shot B: Supergen prompt (5s, Normal, 16:9, no seed, no audio, from Frame A)
> Create a 5-second cinematic live-action comedy shot in 16:9, beginning directly from the supplied first frame: a brooding British musician leaning on an arranger keyboard in a music store. One continuous shot, locked camera, no cuts. Keep his face exactly as in the first frame: pale skin, spiky black hair with a choppy fringe, subtle smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat open over a black turtleneck, no scarf. Keep the keyboard and the store exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon window light, shallow depth of field and organic film grain.
> 0–1 second: He jerks upright off his elbow in alarm, eyes suddenly wide, staring down at the keyboard.
> 1–5 seconds: Panicking, he jabs at the buttons on the panel with both hands, quick and clumsy, his eyes darting across the panel, mouth tight.
> Sound: a busy music store. No dialogue, no other people, no subtitles, no watermarks.

Use about 0.3–2.5s, muted. The bossa nova and the "WOO!" go on top in the edit.

---

## 5. Then
Couch clip 3 (F1/F2 framing): "He was perfect... until the bossa nova." → Milly: "Statistically, most people meet at work." → both of them stare at Milly → Becca: "Then where?!" → "...The laundromat." These are 4 lines, so they fit in one 15s clip. Set up the ElevenLabs dialogue the same way as couch clip 2, with Milly as a third voice: flat, even, a beat late.

---

## Revision: fixing the GPT store frames (geography)
The three GPT frames all show the same front windows, but they are shot from opposite sides of the keyboard. In the wide shot (camera in front of the keyboard, looking at its back), the windows are behind Kallista and Adrian. In a reverse angle from the player's side, the camera looks the other way, into the store, so the windows must not appear. Rule: **the windows appear only in the wide shot.** The close shots play against the store interior: the brick wall, the guitar wall, the upright pianos and the sheet music counter. This also means faces are lit from the front by the windows behind the camera instead of backlit.

Edit each GPT frame (attach the frame being edited **first**, so it keeps the layout, faces and pose).

### E. Wide entrance master: edit of the GPT two-shot (Kallista and Adrian behind the keyboard)
Attach: the GPT two-shot, then Kallista identity shot 1.
> Keep this exact image: the same camera position, framing, lens, lighting, store, windows and keyboard, and the woman's face, hair, coat and scarf exactly as they are. Make only these changes: remove the man in the black coat completely, and fill the space where he was with the store behind him (the brick wall, the guitar wall and the piano), so the right half of the keyboard and the floor beside it are clear and empty. The woman now looks down at the keyboard's control panel, studying it, with one finger resting on a key, and her expression is calm and absorbed. Keep everything else exactly the same. Photorealistic film still, light 35mm film grain. No text other than the existing brand name on the keyboard, no logos, no watermark.
This is the waist-up opening shot of Kallista at the keyboard. Adrian enters from the right in Shot E.

### A. Adrian's point-of-view close-up: edit of the GPT Adrian frame
Attach: the GPT Adrian frame only.
> Keep the man, his face, hair, eyeliner, cross earrings, greatcoat, pose and hand on his chin, the keyboard in the foreground and the camera framing exactly the same. Replace only the background: we are now looking toward the back of the store, away from the front windows, so no windows are visible anywhere. Behind him, softly out of focus: an exposed red-brick wall with a long row of acoustic and electric guitars on wall hangers, an upright piano, a wooden sheet music counter with a small brass lamp, and warm pendant lights below a pressed-tin ceiling. Soft daylight falls on his face from in front of him (from the windows behind the camera). Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, creamy shallow depth of field, light 35mm film grain, natural skin texture. No text other than the existing brand name on the keyboard, no logos, no watermark.

### C. Kallista's stare: edit of the GPT Kallista close-up
Attach: the GPT Kallista close-up, then Kallista identity shot 1.
> Keep this woman's face, hair, coat, scarf, head angle and the camera framing exactly the same. Replace only the background: no windows anywhere. Behind her, softly out of focus: an exposed red-brick wall with acoustic guitars on wall hangers, a row of arranger keyboards on black stands, and warm pendant lights. Soft daylight falls on her face from in front of her. Change her expression to completely flat and unimpressed: a dead, unblinking stare, her brows level, her mouth closed and relaxed. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, creamy shallow depth of field, light 35mm film grain, natural skin texture. No text, no logos, no watermark.

### References for Shot E (Supergen `more_pictures`)
- **Face:** the corrected Frame A, not the old music-video headshot. The headshot's ruffled white shirt and vinyl jacket could pull the wrong wardrobe in, and Frame A has his face front-on, in costume and in this store's light.
- **Wardrobe:** the full-body greatcoat shot.

---

## FINAL PLAN: one 10s directed clip (replaces separate Shots E, A, B and C)
Supergen directs the cuts from 3 references and the line, at about 66 XCE instead of 90–108.
- First frame @1: `keyframes/holiday-reservations/music_E_kallista_wide.png`
- More pictures: @2 `music_A_adrian_pov.png` (Adrian's close-up, his face and wardrobe), @3 `music_C_kallista_stare.png`
- Audio: `voices/holiday-reservations/music_adrian_10s.mp3` (raw take: `adrian_line_raw.mp3`, ElevenLabs v4). 1.4s of silence at the start, padded to 10.0s.
- Measured: "You play?" 1.62–2.30s, "Perhaps we could make something..." 3.20–4.76s, "beautifully dark—" 5.26–6.20s, silence 6.4–10s.
- 10s, Normal, 16:9, no seed.

> Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame (@1): a woman with platinum-blonde hair studying an arranger keyboard in a small-town music store. Exactly THREE shots with two clean HARD CUTS. References define each shot's composition, faces, wardrobe and setting. Animate the scenes naturally; do not interpolate or morph between the reference images. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon window light, shallow depth of field and organic film grain.
> CHARACTERS: KALLISTA is the woman at the keyboard (@1, @3): pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part, a charcoal wool coat and a dark grey chunky knit scarf. Reserved and deadpan; she moves very little and never speaks. ADRIAN (Speaker 1, @2) has a low, velvety British voice: pale skin, spiky black hair with a choppy fringe, smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat over a black turtleneck, no scarf. A self-serious, brooding frontman, until things go wrong. Keep both faces exactly as in the references.
> 0–1.5 seconds, SHOT 1, match @1: wide shot, locked camera. Kallista looks down at the keyboard panel. Adrian glides in from the right edge of the frame with slow, self-important strides, his coat swinging, and smoothly sets one elbow down on the right end of the keyboard, chin on his hand. Silence.
> AT EXACTLY 1.5 SECONDS: HARD CUT to the close-up composition in @2.
> 1.5–8.0 seconds, SHOT 2, match @2: close-up of Adrian leaning on the keyboard, elbow on the panel, chin on his hand, gazing straight into the lens. He raises his eyebrows slightly and speaks low and slow: "You play?" He leans a little closer and lowers his voice to an intimate murmur: "Perhaps we could make something... beautifully dark—" At 6.3 seconds he jerks upright off his elbow in alarm, eyes suddenly wide, and jabs at the buttons on the panel with both hands, quick and clumsy, his eyes darting across the panel, mouth tight.
> AT EXACTLY 8.0 SECONDS: HARD CUT to the close-up composition in @3.
> 8.0–10 seconds, SHOT 3, match @3: close-up of Kallista, completely still, watching him with a flat, unimpressed, unblinking stare, mouth closed. Hold this shot to the end without a fade.
> Throughout: keep the supplied audio unchanged; add no other voices, music or dialogue. Only Adrian speaks. No additional cuts, dissolves, slow motion, subtitles or watermarks.

**Edit:** white flash → 0–1.5 entrance (*tick... tick...* starts under it) → line → bossa nova **BOOM** at 6.2 on "dark—" → panic → Kallista → **"WOO!"** → white flash. Mute the clip's audio after 6.4s.
**Fallback:** if Supergen ignores the cuts or drifts a face, retake only the weak shot as a 5s pickup from its own frame (the Shot A, B and E prompts above).

**Result:** `ae52c5fdb83d` (vid_41acc8b3ae6d4214), about 66 XCE.
- Shot 1, entrance (0–1.25s): good. Adrian glides in, his hair and coat read right at this size, and Kallista holds.
- Shot 2, close-up (1.25–8.2s): **Adrian's identity failed.** Supergen did not use @2's composition (windows behind him, arms folded instead of chin on hand) and drew a different man: tanned skin, brown eyes, flatter hair, light eyeliner, two earrings per ear. The line is lip-synced. The panic hands come at about 7.4–8.2s.
- Shot 3, Kallista (8.2–9.9s): usable. Her face is a little more mature than Frame C, but she's recognisable.
- Supergen moved the audio about 0.25s earlier (speech starts at 1.37s) and trimmed the end to 9.875s.
- Lesson: **reference pictures (`more_pictures`) don't hold a face in a close-up; only the first frame does.** Use references for wide shots and quick entrances only.

---

## PLAN v3: every shot from its own keyframe (no reference pictures)
Adding `more_pictures` turns Supergen into reference-to-video mode: frame 0 is no longer locked, and faces are redrawn. So every shot now starts from its own first frame, with no extra pictures. With 54 XCE left, only Adrian's line gets a clip; everything else plays as a still or uses audio in the edit.

**Edit (about 7s):**
1. White flash, then **Frame E as a still** (~1.2s, slow push-in). Kallista at the keyboard; *tick... tick...* starts.
2. Hard cut to **the Adrian clip** (Frame A first frame, ~5s): he is suddenly just *there*, chin on hand. "You play? ...Perhaps we could make something... beautifully dark—"
3. **BOOM** on "dark—": he jerks upright (4.4–5.0s). The bossa nova blasts, with button beeps and the tempo speeding up, all in audio.
4. **Frame C as a still** (~1.5s, slow push-in): Kallista's flat stare as the horns pile on, then **"WOO!"** and the white flash.

### Adrian pickup: Supergen prompt (5s, Normal, 16:9, no seed, no more_pictures)
- First frame: `keyframes/holiday-reservations/music_A_adrian_pov.png`
- Audio: `voices/holiday-reservations/music_adrian_5s.mp3` (raw take with the long pause shortened by 0.4s)
- Measured: "You play?" 0.22–0.90s, "Perhaps we could make something..." 1.40–2.96s, "beautifully dark—" 3.46–4.40s, silence 4.4–5.0s.

> Create a 5-second cinematic live-action romantic comedy close-up in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a brooding British musician leaning on an arranger keyboard in a small-town music store, seen from the point of view of the woman he is talking to. One continuous shot, locked camera, no cuts. Keep his face exactly as in the first frame, and keep the keyboard, its panel and the store behind him exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon light, shallow depth of field and organic film grain.
> CHARACTER: ADRIAN (Speaker 1) is the only person who speaks, with a low, velvety British voice. Keep his face exactly as in the first frame: pale skin, spiky black hair with a choppy fringe, smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat open over a black turtleneck. A self-serious frontman: brooding, with slow, deliberate movements. He believes every word.
> 0.2–0.9 seconds: Chin on his hand, he raises his eyebrows slightly and speaks low and slow, looking straight into the lens: "You play?"
> 1.4–4.4 seconds: He leans a little closer, his elbow still on the panel, and lowers his voice to an intimate murmur: "Perhaps we could make something... beautifully dark—"
> 4.4–5 seconds: Silence. He jerks upright off his elbow in alarm, eyes suddenly wide, staring down at the keyboard.
> Throughout: keep the supplied audio unchanged; add no voices, music or sound effects. The people in the background stay small and out of focus and never speak. No extra cuts, no subtitles, no watermarks.

---

## PLAN v4: website multi-reference scene (10s), shot by the member in the web UI
**References:** @1 `music_E_kallista_wide.png` (first frame), @2 `music_A_adrian_pov.png`, @3 `music_C_kallista_stare.png`, @4 Adrian's full-body greatcoat shot (gives the back of the coat for the entrance).
**Scene audio (compiled once the SFX and the laugh arrive):** Adrian's raw take placed at +2.0s, then the button mashing, then Kallista's laugh, padded to 10.0s.

| Time | Shot | Audio |
|---|---|---|
| 0–2.0 | @1 wide, held: Kallista presses a button; Adrian enters from bottom right, back to camera, elbow on keyboard | silence |
| 2.0 | HARD CUT to @2 | |
| 2.2–2.9 | @2 Adrian | "You play?" |
| 3.7 | CUT to @3 (L-cut) | |
| 3.8–4.66 | @3 Kallista furrows her brow | "Perhaps we could make" (Adrian, off screen) |
| 4.66 | CUT back to @2 | |
| 4.66–6.8 | @2 Adrian | "something... beautifully dark—" |
| 7.0–8.4 | @2 Adrian jolts upright and prods the panel buttons | button mashing SFX (≤1.4s) |
| 8.4 | CUT to Kallista, closer than @3 | |
| 8.6–9.4 | Kallista, hand to mouth | her short stifled laugh |
| 9.4–10 | hold, then the white flash in the edit | |

"Something" starts at about 2.66s in the raw take (4.66s in the scene), measured from a level dip. Nudge the cut if it lands a syllable early or late.

### ElevenLabs: button mashing (Sound Effects, 1.5s, prompt influence high)
```
Flustered fingertips jabbing small hard plastic buttons on an electronic keyboard's control panel: quick uneven clicks and clacks, two soft electronic beeps, one knob twist, close-up, dry indoor room, no music, no piano notes.
```
### ElevenLabs: Kallista's stifled laugh (v4, her voice)
```
[stifling a laugh behind her hand] Hm— [short, quiet, breathy laugh through her nose] hm.
```
Alternates: `[trying not to laugh] Pfft— [soft, muffled giggle]` or `[a single surprised, muffled laugh behind her hand] Hah.` Keep it under 1s: dry, private, a crack in the deadpan, never a giggle fit.

### Website prompt (Image to Video + More Images, 10s, Normal, 16:9, no seed, scene audio = the compiled track)
See the chat copy, or below.
```
Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame (@1): a woman with platinum-blonde hair at an arranger keyboard in a small-town music store. Clean hard cuts between camera setups, exactly as timed below. References define each shot's composition, faces, wardrobe and setting. Animate the scenes naturally; do not interpolate or morph between the reference images. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon window light, shallow depth of field and organic film grain.

CHARACTERS: KALLISTA (@1, @3) is the woman at the keyboard: pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part, a charcoal wool coat and a dark grey chunky knit scarf. Reserved and deadpan; she moves very little. Keep her face exactly as in @1 and @3. ADRIAN (Speaker 1, @2, @4) has a low, velvety British voice: pale skin, spiky black hair with a choppy fringe, smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat with silver buttons over a black turtleneck. A self-serious, brooding frontman, until things go wrong. Keep his face exactly as in @2.

0–2.0 seconds, SHOT 1, match @1, locked wide shot: Kallista looks down at the keyboard and presses a button with one finger, absorbed. Adrian walks into frame from the bottom-right corner, close to the camera, with his back to the camera: we see only the back of his long black greatcoat and his spiky black hair. He steps up to the right half of the keyboard on the side facing the camera, opposite her, and leans forward to rest one elbow on top of the keyboard. Silence.
AT EXACTLY 2.0 SECONDS: HARD CUT to the reverse angle, matching @2.
2.0–3.7 seconds, SHOT 2, match @2: close-up of Adrian, already leaning with his elbow on the panel and his chin on his hand, gazing straight into the lens. He speaks low and slow: "You play?"
AT EXACTLY 3.7 SECONDS: HARD CUT to @3.
3.7–4.7 seconds, SHOT 3, match @3: close-up of Kallista listening, mouth closed. She subtly furrows her brow, puzzled and unconvinced. She does not speak; his voice continues off screen: "Perhaps we could make..."
AT EXACTLY 4.7 SECONDS: HARD CUT back to @2.
4.7–8.4 seconds, SHOT 4, match @2: Adrian leans a little closer and lowers his voice to an intimate murmur: "...something... beautifully dark—" At 7.0 seconds he jolts upright in alarm, eyes wide, and hunts for the off switch: quick, flustered prods with his fingertips on the small buttons of the control panel above the keys, one hand then the other, his eyes darting across the screen. His fingers stay on the panel buttons and never play the piano keys.
AT EXACTLY 8.4 SECONDS: HARD CUT to a closer framing of Kallista from @3.
8.4–10 seconds, SHOT 5: close-up of Kallista. She raises a hand to cover her mouth and lets out one short, quiet, stifled laugh, her eyes crinkling for a moment, then keeps her hand there, trying to stay deadpan. Hold this shot to the end without a fade.

Throughout: keep the supplied audio unchanged; add no music or extra voices. Only Adrian speaks words. No additional cuts, dissolves, slow motion, subtitles or watermarks.
```

### v4 scene audio: compiled (12s, final); these timings replace the 10s table above
`voices/holiday-reservations/music_scene_12s.mp3`, built from `adrian_line_raw.mp3` (+2.3s), `buttons_sfx_raw.mp3` (+15 dB, at 8.0s) and `kallista_laugh_raw.mp3` (first 1.25s only, at 9.8s).
Measured: "You play?" 2.52–3.20s · "Perhaps we could make" 4.10–4.96s · "something... beautifully dark—" 4.96–7.10s · **a 0.85s beat** (the bossa nova hits here in the edit) · buttons 8.14–9.3s · laugh 9.9–11.0s · silence to 12.0s.

**Website prompt (12s):**
```
Create a 12-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame (@1): a woman with platinum-blonde hair at an arranger keyboard in a small-town music store. Clean hard cuts between camera setups, exactly as timed below. References define each shot's composition, faces, wardrobe and setting. Animate the scenes naturally; do not interpolate or morph between the reference images. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm afternoon window light, shallow depth of field and organic film grain.

CHARACTERS: KALLISTA (@1, @3) is the woman at the keyboard: pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part, a charcoal wool coat and a dark grey chunky knit scarf. Reserved and deadpan; she moves very little. Keep her face exactly as in @1 and @3. ADRIAN (Speaker 1, @2, @4) has a low, velvety British voice: pale skin, spiky black hair with a choppy fringe, smoky eyeliner, small gold cross earrings, a long black double-breasted greatcoat with silver buttons over a black turtleneck. A self-serious, brooding frontman, until things go wrong. Keep his face exactly as in @2.

0–2.3 seconds, SHOT 1, match @1, locked wide shot: Kallista looks down at the keyboard and presses a button with one finger, absorbed. Adrian walks into frame from the bottom-right corner, close to the camera, with his back to the camera: we see only the back of his long black greatcoat and his spiky black hair. He steps up to the right half of the keyboard on the side facing the camera, opposite her, and leans forward to rest one elbow on top of the keyboard. Silence.
AT EXACTLY 2.3 SECONDS: HARD CUT to the reverse angle, matching @2.
2.3–4.0 seconds, SHOT 2, match @2: close-up of Adrian, already leaning with his elbow on the panel and his chin on his hand, gazing straight into the lens. He speaks low and slow: "You play?"
AT EXACTLY 4.0 SECONDS: HARD CUT to @3.
4.0–5.0 seconds, SHOT 3, match @3: close-up of Kallista listening, mouth closed. She subtly furrows her brow, puzzled and unconvinced. She does not speak; his voice continues off screen: "Perhaps we could make..."
AT EXACTLY 5.0 SECONDS: HARD CUT back to @2.
5.0–9.4 seconds, SHOT 4, match @2: Adrian leans a little closer and lowers his voice to an intimate murmur: "...something... beautifully dark—" At 7.2 seconds he freezes mid-word, startled, and slowly looks down at the keyboard under his elbow, his eyes widening in horror. At 8.1 seconds he straightens up and hunts for the off switch: quick, flustered prods with his fingertips on the small buttons of the control panel above the keys, one hand then the other, his eyes darting across the screen, in time with the button clicks. His fingers stay on the panel buttons and never play the piano keys.
AT EXACTLY 9.4 SECONDS: HARD CUT to a closer framing of Kallista from @3.
9.4–12 seconds, SHOT 5: close-up of Kallista. At 9.9 seconds she raises a hand to cover her mouth and lets out one short, quiet, stifled laugh, her eyes crinkling for a moment, then keeps her hand there, trying to stay deadpan. Hold this shot to the end without a fade.

Throughout: keep the supplied audio unchanged; add no music or extra voices. Only Adrian speaks words. No additional cuts, dissolves, slow motion, subtitles or watermarks.
```
