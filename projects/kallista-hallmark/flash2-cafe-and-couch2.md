# Flash 2 (café) and couch clip 2

## Sequence in the edit
1. White flash back from the rink, then **couch clip 2, part 1:** Kallista's slow, dead-eyed head shake, then Becca: "The coffee shop! He spelled your name wrong on purpose... so you'd have to talk to him."
2. **WHITE FLASH, café:** barista POV shot (~2s), then Kallista's dead stare at the cup (~1–1.5s). **WHITE FLASH.**
3. **Couch clip 2, part 2:** Kallista sips wine: "Nobody does that." Becca: "Ooh, the music store! Some broody musician." Then the Adrian flash.

Couch clip 2 is one 15s render that gets split in the edit around the café flash.

---

## A. Barista start frame (Nano Banana, 16:9)
No reference needed; he's a one-off character.
> A cozy small-town café counter in the morning, seen from the customer's point of view across the counter. A charming barista in his late twenties with a dark brown man bun, a groomed full beard and a rolled-sleeve olive flannel shirt under a dark brown canvas apron faces the camera from behind the counter. He holds a white paper coffee cup up beside his face at shoulder height, turned so its side faces the camera. Written on the cup in thick black marker, large and clearly legible: "CALLISTUH" with a small hand-drawn heart after it. He gives a flirty, self-satisfied half-smile, one eyebrow raised. Behind him: an espresso machine, a chalkboard menu, hanging Edison bulbs and Christmas garland, softly out of focus. Warm morning window light. The cup and his face are both in sharp focus. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No other text, no logos, no watermark.

## B. Kallista stare (a still; push in slowly in the edit)
Attach: Kallista identity shots 1 and 2 (and the rink front-facing frame, if it helps hold her face).
> A medium close-up of Kallista, the woman from the Kallista references, standing at the same cozy café counter in warm morning window light, facing the camera straight on as if looking at the barista. Same face: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair worn down with a center part. She wears an open charcoal wool coat over a black ribbed mock-neck sweater and a dark grey chunky knit scarf. Her expression is completely flat and unimpressed: a dead, unblinking stare, mouth closed, not amused. Behind her, the café is softly out of focus: wooden tables, a window with snow outside, Christmas garland. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.
(Optional, if a still feels too frozen: a 5s Supergen clip from this frame with "She blinks once, slowly, and keeps staring. Her mouth stays closed. Nothing else moves." About 36 XCE.)

## C. Barista clip (Supergen, 5s, Normal, 16:9, no seed; use about 2s)
> Create a 5-second cinematic live-action romantic comedy shot in 16:9, beginning directly from the supplied first frame: a barista behind a cozy café counter, seen from the customer's point of view. One continuous shot, locked camera, no cuts. Keep the cup and the handwritten "CALLISTUH" with its heart exactly as in the first frame, sharp and legible; the writing never changes. THE BARISTA is the only person in the shot: late twenties, dark brown man bun, groomed full beard, olive flannel shirt and brown canvas apron, flirty and very pleased with himself.
> 0–2 seconds: Holding the cup still beside his face with the writing facing the camera, he gives one slow, flirty wink and a smug little nod, mouth closed in a half-smile.
> 2–5 seconds: He keeps holding the cup up, eyebrows raised expectantly, waiting for a reaction, mouth closed.
> Sound: quiet café ambience, the hiss of an espresso machine, soft clinking cups. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm morning window light, shallow depth of field and organic film grain. No dialogue, no music, no other people, no subtitles, no watermarks.

---

## D. Couch clip 2: ElevenLabs Text to Dialogue (same voices as clip 1)
Leave about 1.5s of silence at the start for the head shake; I'll add it when I pad the track.
```
Becca: [excited, rapid] The coffee shop! [conspiratorial] He spelled your name wrong on purpose... so you'd have to talk to him.
Kallista: [flat, deadpan] Nobody does that.
Becca: [lighting up, delighted] Ooh, the music shop! [dreamy] Some broody musician.
```
Send the file and I'll measure the timings, pad it to 15s and finish the prompt below.

## E. Couch clip 2: Supergen prompt
Audio: `voices/holiday-reservations/couch2_dialogue_15s.mp3` (1.5s of room tone added at the start, padded to 15.0s).
Measured: Becca 1.5–6.6s, Kallista "Nobody does that." 6.8–8.0s, Becca 8.3–12.2s, silence 12.2–15s.
Start frame: the corrected couch two-shot `pic_1619a74c7520`. 15s, Normal, 16:9, no seed, scene audio = padded dialogue track.
> Create a 15-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: two best friends sharing a quiet, intimate late-night conversation on a sofa in a cozy bed-and-breakfast sitting room. It should feel real and unperformed: relaxed, close, easy eye contact. Preserve their faces, hair, sweaters, the sofa, the Christmas tree, the frosted windows and the warm lamp and firelight exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm practical light, soft halation on the tree lights, shallow depth of field and organic film grain.
> CHARACTERS: [Kallista block from clip1-v2-prompt.md, unchanged] BECCA (Speaker 2) is the woman on the right, with the brighter, higher voice. Keep her face exactly as in the first frame: late twenties, long wavy auburn hair, light freckles across her nose and cheeks, warm green-brown eyes, a burgundy cable-knit sweater and jeans, holding a bottle of red wine by its neck. Kallista's best friend: warm, playful and teasing; her energy shows in her eyes and smile, with relaxed body language and small, loose gestures. Never theatrical, never performing for the camera.
> Camera: keep the two-shot, or if you cut, always cut to the woman who is speaking so her face is on camera while she talks. Only the woman who is speaking moves her lips.
> 0–1.5 seconds: Complete silence, no one speaks. Kallista looks at Becca and gives a slow, dead-eyed shake of her head, mouth closed.
> 1.5–6.6 seconds: Becca perks up, points at Kallista with the bottle hand and leans in, conspiratorial and delighted: "The coffee shop! He spelled your name wrong on purpose... so you'd have to talk to him."
> 6.8–8.0 seconds: Kallista takes a slow sip of wine, lowers the glass and says, flat and deadpan: "Nobody does that."
> 8.3–12.2 seconds: Becca's face lights up and she sits up straight: "Ooh, the music store! Some broody musician."
> 12.2–15 seconds: Complete silence, no one speaks. Kallista closes her eyes and sinks slightly into the sofa, mouth closed.
> Throughout: keep the supplied audio unchanged and add no voices or music. No extra people, no subtitles, no watermarks.

---

## F. Couch clip 2, v2 retake (10s): fixing Becca's face drift
**Why:** the v1 start frame had Becca turned in three-quarter profile toward Kallista, so Supergen had to invent the hidden half of her face. It drifted away from couch clip 1, worst in its Becca close-up. The v2 frame shows both women front-on and fully lit.

**Shortened to 10s (60–72 XCE instead of 90–108):** Becca's music-store line was never lip-synced in v1, and the rough cut already plays it over Kallista's reaction. v2 renders only the two synced lines plus a 3s silent reaction. In the edit, Becca's "Ooh, the music store! Some broody musician." (8.3–12.2s of `couch2_dialogue_15s.mp3`) goes over that reaction.

- Start frame: `keyframes/holiday-reservations/couch2_front_v2.png`
- Audio: `voices/holiday-reservations/couch2_dialogue_v2_10s.mp3`, cut from the v1 track (1.0–8.1s) and padded to 10.0s.
- Measured: Becca 0.56–5.62s, Kallista 5.83–6.95s, silence 6.95–10s.
- 10s, Normal, 16:9, no seed.

> Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: two best friends sharing a quiet late-night conversation on a sofa in a cozy bed-and-breakfast sitting room. It should feel real and unperformed. Preserve their faces, hair, sweaters, the sofa, the Christmas tree, the frosted windows and the warm lamp and firelight exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm practical light, soft halation on the tree lights, shallow depth of field and organic film grain.
> CHARACTERS: KALLISTA (Speaker 1) is the woman on the left, with the softer, lower voice. Keep her face exactly as in the first frame: early-to-mid twenties, pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) worn down past the shoulders with a center part. She wears an oversized charcoal knit sweater and black leggings, sits cross-legged and holds a glass of red wine. A dark dream-pop songwriter: reserved, deadpan, emotionally restrained; she moves little and deliberately, and her emotions show in her eyes. Never bubbly, never loud, no big gestures. BECCA (Speaker 2) is the woman on the right, with the brighter, higher voice. Keep her face exactly as in the first frame: late twenties, long wavy auburn hair, light freckles across her nose and cheeks, warm green-brown eyes, a burgundy cable-knit sweater and jeans, holding a bottle of red wine by its neck. Kallista's best friend: warm, playful and teasing; her energy shows in her eyes and smile, with small, loose gestures. Never theatrical.
> Camera: hold the frontal two-shot with a very slow push-in. Both women stay facing mostly toward the camera, turning only their heads slightly toward each other, so both full faces stay visible the whole time. If you cut, always cut to the woman who is speaking, straight-on, so her face is on camera while she talks. Only the woman who is speaking moves her lips.
> 0–0.5 seconds: Silence. Becca turns her head slightly toward Kallista with a sly smile.
> 0.5–5.6 seconds: Becca leans in a little, points the bottle toward Kallista and says, conspiratorial and delighted: "The coffee shop! He spelled your name wrong on purpose... so you'd have to talk to him."
> 5.8–7.0 seconds: Kallista takes a small sip of wine, lowers the glass and says, flat and deadpan: "Nobody does that."
> 7.0–10 seconds: Complete silence, no one speaks. Kallista closes her eyes and sinks slightly into the sofa, mouth closed. Becca grins at her, mouth closed.
> Throughout: keep the supplied audio unchanged and add no voices or music. No extra people, no subtitles, no watermarks.

**Edit:** couch 0–5.6 (Becca) → café flash (barista + stare) → couch 5.8–7.0 ("Nobody does that.") → couch 7.0–10 under Becca's music-store line from the v1 track → white flash → Adrian.

**Result:** `87c6f21670aa` (vid_992f1cfbb8fe4e57), about 66 XCE.
- 0–~5.7s: wide two-shot from the frame. Becca's face holds (freckles, eyes, hair) and her line is lip-synced. She turns toward Kallista mid-line, which is fine at this size.
- ~5.7–10s: Supergen cut to a closer two-shot on Kallista for "Nobody does that.", lip-synced, then her silent reaction (side-eye, closes her eyes). Her face is slightly rounder and younger in this shot than in the frame. Check it against clip 1.
- The audio came back unchanged; the timings match the track.
