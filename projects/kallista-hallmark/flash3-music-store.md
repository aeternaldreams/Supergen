# Flash 3: the music store (Adrian and the bossa nova)

## Sequence in the edit (about 6–7s)
1. **WHITE FLASH** out of couch clip 2 (Becca: "...Some broody musician.").
2. **Shot A, Adrian (~4.5s, lip-synced):** Kallista's point of view. Adrian leans on the PSR-SX920, chin on hand: "You play? ...Perhaps we could make something... beautifully dark—". A quiet count-in *tick... tick...* runs under the line (added in the edit).
3. **Hard cut on "dark—"**, and the bossa nova **BOOM**s in (added in the edit).
4. **Shot B, panic (~2s, muted):** Adrian jerks upright and stabs at buttons.
5. **Shot C, Kallista (~1.2s):** a flat, unblinking stare. The tempo speeds up and the horns join in.
6. Optional: a final 0.5s of Shot B, then the **"WOO!"** lands right on the white flash.
7. **WHITE FLASH** into couch clip 3: "He was perfect... until the bossa nova."

Cost: Shot A and Shot B are 5s Normal clips at 30–36 XCE each, **60–72 XCE in total**, which leaves about 115–125 XCE. Shot C is a still with a slow push-in in the edit, so it costs nothing in Supergen.

---

## 1. Start frames (Nano Banana, 16:9)
Before you start: check that the PSR-SX920 product photo isn't mirrored. "YAMAHA" should read correctly.

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
