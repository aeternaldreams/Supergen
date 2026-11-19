# Couch clip 3: "You watch way too many of these movies." → Milly → "...The laundromat." → "My bra was stuck to his back."

## The background problem, and how we avoid it
Every time a model makes a new angle on its own (Supergen reference mode, or Omni Flash's angled close-ups), it invents a new room. So **every start frame for this scene comes from pixels we already have:**
- **Kallista and Becca's two-shot:** `couch2_front_v2.png`, the frame of couch clip 2 v2.
- **Close-ups:** crops of that same frame, like Becca's music-store close-up (`becca_mcu_crop.png`), which matched perfectly.
- **Milly:** she's the only new element. Her frame comes from **widening the existing frame** to reveal her armchair, not from building a new room. Her close-up is then a crop of that wider frame.
- **Supergen:** each clip uses **one start frame and no reference pictures** (Image to video), the setup that has held both faces and backgrounds every time.

## Why the line changed
Becca's guesses (the rink, the café, the music store) are her **imaginings**, not things that happened. So Kallista doesn't remember them; she **scoffs** at Becca's fantasy. That also sets up the real answer, the laundromat, as the unglamorous truth. Alternatives considered: "[scoffs] Where do you come up with these?" and "[scoffs] That's not a guy. That's a playlist."

## Geography (keep it consistent)
- Kallista sits on the left end of the sofa and Becca on the right. Milly is in an upright armchair **off to the left of the sofa** (screen-left), per the original F2 layout.
- When Kallista and Becca "turn and stare at Milly", they both look **screen-left**.
- In Milly's close-up she looks **screen-right**, toward them.

---

## 1. ElevenLabs: Text to Dialogue (same Kallista and Becca voices as clips 1 and 2)
**Milly's voice:** no custom design needed. Pick a stock library voice that's smooth, mid-pitched, pleasant and very even (American female, conversational), and save it to My Voices so her montage lines match later. Use high stability and low style, so the flatness comes from her delivery, not from a robotic voice. Choose one that sounds clearly different from Kallista (low, husky) and Becca (bright).

```
Kallista: [scoffs, dry, unimpressed] You watch way too many of these movies.
Milly: [pleasant, perfectly even, no emotion at all] Statistically, most people meet at work.
Becca: [snapping back to Kallista, eager, exasperated] Then where?!
Kallista: [reluctant, quiet, sinking] ...The laundromat.
Becca: [delighted, gushing] That's adorable!
Kallista: [dry, flat] My bra was stuck to his back.
```
- **Takes:** make 2–3 takes and send the best one (or several). I'll measure it and split it into the clip tracks.
- **The stare:** the long silent beat where they stare at Milly is added in the edit (about 1.5s after Milly's line). ElevenLabs won't hold a pause that long.
- **Milly's timing:** she answers "a beat late", so leave a short gap before her line. I can lengthen it in the edit too.

---

## 2. Start frames

### M1. Wider three-shot (Nano Banana / GPT: **edit** `couch2_front_v2.png`, attached FIRST)
Attach: `couch2_front_v2.png` first, then your Milly portrait.
> Keep this exact image: the same room, lighting, sofa, Christmas tree, windows, lamp, and both women's faces, hair, clothes and poses, exactly as they are. Widen the view: zoom the camera out slightly and extend the scene to the left, so the existing picture sits in the right two-thirds of the new frame. In the newly revealed space on the left, continue the same room (the same wall, the same window frames and the same warm lamp and Christmas-tree light) and add an upright upholstered armchair angled toward the sofa. In it sits Milly, the woman from the Milly reference, with the same face: mid twenties, a sleek glossy chestnut-brown bob, flawless, very symmetrical features, large calm brown eyes. She wears a perfectly pressed cream turtleneck and tailored taupe trousers, sits perfectly upright with her knees together, and holds a full glass of red wine she hasn't touched. Her expression is pleasant, polite and neutral, and she is looking toward the two women. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.

Check: the right two-thirds should be pixel-identical to `couch2_front_v2.png`. If the women's faces drift, run the one-person-at-a-time face passes from `nano-banana-keyframes.md`.

### M2. Milly close-up (a crop of M1)
1. Crop M1 to 16:9 around Milly (head and shoulders, with the room behind her). The crop keeps the background identical.
2. If it looks soft, run one edit pass: "Keep the composition, background and lighting exactly the same; add fine detail and sharpness. Make her face match the Milly reference exactly; she looks screen-right toward the sofa, pleasant and neutral, eyes wide open."

### K1. Kallista close-up (a crop of `couch2_front_v2.png`, done by me)
The same way as Becca's crop. It's for "My bra was stuck to his back.", with Becca's "That's adorable!" off screen.

---

## 3. Clips (revised): one Reference to video scene + one locked pickup

**Dialogue** (`couch3_dialogue_raw.mp3`, 13.4s): Kallista scoff and line 0–2.8 · Milly 2.95–5.9 · Becca "Then where?!" 6.0–7.15 · Kallista "...The laundromat." 8.15–9.35 · Becca "That's adorable!" 9.5–11.15 · Kallista "My bra was stuck to his back." 11.55–13.3.
**Voice samples for Reference to video** (in `voices/holiday-reservations/`): `voice_kallista_c3.mp3` (her two lines), `voice_milly_c3.mp3`, `voice_becca_c3.mp3`.

### Clip 3a: Supergen website, Reference to video, 12s, Normal, 16:9 (lines 1–4)
| Ref | Image | Camera setup it defines |
|---|---|---|
| @1 | `couch3_wide_three.png` | Establishing wide; the stare at Milly |
| @2 | `couch2_front_v2.png` | Frontal two-shot of Kallista and Becca |
| @3 | `milly_mcu_crop.png` (crop of the wide, upscaled and lightly sharpened) | Milly's close-up |
| @4 | `kallista_mcu_crop.png` | Kallista's close-up |
Voice 1 = Kallista, Voice 2 = Milly, Voice 3 = Becca.

```
Create a 12-second cinematic live-action romantic comedy scene in 16:9, late at night in a cozy bed-and-breakfast sitting room, told in five shots joined by clean hard cuts. Use ONLY the four camera setups shown in the references: @1 is the wide shot of the whole room, @2 the frontal two-shot of the sofa, @3 Milly's close-up, @4 Kallista's close-up. Every shot matches its reference's camera angle, framing and background exactly; invent no other angles, no profile shots and no over-the-shoulder shots. Keep every face exactly as in the references. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm lamp and firelight, soft halation on the Christmas tree lights, shallow depth of field and organic film grain.

CHARACTERS: KALLISTA (@1, @2, @4), who speaks with Voice 1, sits on the left end of the sofa in an oversized charcoal knit sweater with a glass of red wine: pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part. Deadpan and dry. BECCA (@1, @2), who speaks with Voice 3, sits on the right end of the sofa in a burgundy cable-knit sweater, holding a bottle of red wine: long wavy auburn hair, freckles, warm green-brown eyes. Warm, playful and teasing. MILLY (@1, @3), who speaks with Voice 2, sits perfectly upright in an armchair to the left of the sofa in a pressed cream turtleneck, holding an untouched glass of red wine: a sleek glossy chestnut-brown bob, flawless symmetrical features, large calm brown eyes; pleasant, polite, rarely blinks, reacts a beat late. Nobody ever looks into the camera.

THE ROOM: the sofa faces the camera with the Christmas tree and frosted windows behind it and a lamp at its right end. Milly's armchair is to the left of the sofa, angled toward it, so when Kallista and Becca look at Milly they turn their heads to the left of the frame.

SHOT 1 (about 3 seconds), the two-shot matching @2: Kallista scoffs, sets her wine glass down on her knee and says, dry and unimpressed: "You watch way too many of these movies."
SHOT 2 (about 3 seconds), Milly's close-up matching @3: perfectly still and upright, she says pleasantly and evenly, looking toward the sofa: "Statistically, most people meet at work."
SHOT 3 (about 2 seconds), the wide shot matching @1: silence. Kallista and Becca slowly turn their heads and stare at Milly. Milly holds a polite, unblinking smile.
SHOT 4 (about 2 seconds), back to the two-shot matching @2: Becca snaps back to Kallista, eager and exasperated: "Then where?!"
SHOT 5 (about 2 seconds), Kallista's close-up matching @4: she sinks slightly into the sofa and says, reluctant and quiet: "...The laundromat." Hold to the end.

SOUND: only the three voices, a gentle crackling fireplace and soft room hum. No music, no other voices, no subtitles, no watermarks.
```

### Clip 3b: Supergen, Image to video (MCP or website), 5s, Normal (lines 5–6)
First frame: `keyframes/holiday-reservations/kallista_mcu_crop.png` (the same framing as shot 5 of 3a, so the cut matches). Scene audio: `couch3b_5s.mp3` (Becca off screen 0.3–1.95, Kallista 2.4–4.15).
```
Create a 5-second cinematic live-action romantic comedy close-up in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a woman on a sofa in a cozy bed-and-breakfast sitting room at night, a Christmas tree and frosted windows behind her. One continuous shot, locked camera, no cuts. Keep her face exactly as in the first frame: pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair with a center part, an oversized charcoal knit sweater, a glass of red wine. KALLISTA is deadpan and dry; she looks to the right of the camera at her friend, never into the lens.
0.3–2.0 seconds: her friend's delighted voice comes from off screen ("That's adorable!"); Kallista's mouth stays closed and she gives a small, pained look.
2.4–4.2 seconds: Kallista says, dry and flat: "My bra was stuck to his back."
4.2–5 seconds: she takes a slow sip of wine, mouth closed.
Throughout: keep the supplied audio unchanged; add no voices or music. No other people, no subtitles, no watermarks. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm lamp and Christmas-tree light, shallow depth of field and organic film grain.
```
**Cost:** about 78 XCE for 3a (12s on the website) and about 36 XCE for 3b.
**Edit:** 3a → 3b (the same Kallista framing) → white flash → laundromat. Clean up any garbled duplicate lines in 3a the same way as in the music store.

**Frames delivered:** `couch3_wide_three.png` (the member's wide, 1376x768) and `milly_mcu_crop.png`.
- The wide's camera is further left than the two-shot, so the tree moves between Kallista and Becca and a second floor lamp stands by Milly. The geometry is consistent. Kallista and Becca are already looking at Milly, which suits shot 3.
- Milly's crop is a three-quarter view looking screen-right. It's soft from the 2.3x upscale; a Nano Banana detail pass is optional.

## Clip 3a result (`supergen-15c2fececddb`, website Reference to video, 13.6s)
**Visuals: good.** The shot order matches the plan: two-shot 0–4.0 · Milly close-up 4.0–7.5 · wide stare 7.5–9.62 · two-shot 9.62–11.04 · Kallista close-up 11.04–13.63. Backgrounds match the references.
**Audio: unusable.** Supergen re-voiced all three characters in near-identical voices (all about 160–216 Hz, ignoring the samples) and repeated lines, including speech during the silent stare.
**Fix (`couch3a_redub_v1.mp4`):** muted the Supergen audio and placed the ElevenLabs takes shot by shot, plus the B&B room tone at −4 dB:
- Kallista 0.1s (her scoff and line)
- Milly 4.6s (atempo 1.15 to match her lip movement)
- Becca 9.85s
- Kallista 11.35s (breath + "...The laundromat.")
- The stare (7.5–9.62) stays silent.
**Lesson:** in Reference to video mode, Character Voice samples don't reliably carry the voice. Plan to re-dub every multi-character scene in post with the real takes.
