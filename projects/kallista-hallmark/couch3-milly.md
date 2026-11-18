# Couch clip 3: "until the bossa nova" → Milly → "...The laundromat." → "My bra was stuck to his back."

## The background problem, and how we avoid it
Every time a model makes a new angle on its own (Supergen reference mode, or Omni Flash's angled close-ups), it invents a new room. So **every start frame for this scene comes from pixels we already have:**
- **Kallista and Becca's two-shot:** `couch2_front_v2.png`, the frame of couch clip 2 v2.
- **Close-ups:** crops of that same frame, like Becca's music-store close-up (`becca_mcu_crop.png`), which matched perfectly.
- **Milly:** she's the only new element. Her frame comes from **widening the existing frame** to reveal her armchair, not from building a new room. Her close-up is then a crop of that wider frame.
- **Supergen:** each clip uses **one start frame and no reference pictures** (Image to video), the setup that has held both faces and backgrounds every time.

## Geography (keep it consistent)
- Kallista sits on the left end of the sofa and Becca on the right. Milly is in an upright armchair **off to the left of the sofa** (screen-left), per the original F2 layout.
- When Kallista and Becca "turn and stare at Milly", they both look **screen-left**.
- In Milly's close-up she looks **screen-right**, toward them.

---

## 1. ElevenLabs: Text to Dialogue (same Kallista and Becca voices as clips 1 and 2)
**Milly's voice:** no custom design needed. Pick a stock library voice that's smooth, mid-pitched, pleasant and very even (American female, conversational), and save it to My Voices so her montage lines match later. Use high stability and low style, so the flatness comes from her delivery, not from a robotic voice. Choose one that sounds clearly different from Kallista (low, husky) and Becca (bright).

```
Kallista: [flat, deadpan] He was perfect... [short pause] until the bossa nova.
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

## 3. Clips (Supergen, Image to video, one start frame each, scene audio)

| Clip | Start frame | Length | What it covers |
|---|---|---|---|
| 3a | `couch2_front_v2.png` (two-shot) | 10s | Kallista's bossa nova line; Milly's line **off screen** while both women turn their heads screen-left and stare; then Becca's "Then where?!" and Kallista's "...The laundromat." |
| 3b | M2 (Milly close-up) | 5s | Milly says her line on camera |
| 3c | K1 (Kallista close-up) | 5s | "That's adorable!" (Becca off screen), then "My bra was stuck to his back." |

**Edit:** two-shot (Kallista's line) → **cut to Milly** (her line) → **cut back to the two-shot** as both women stare at her (the long beat) → Becca → Kallista → cut to Kallista's close-up for the bra line → white flash → laundromat.
**Cost:** 10s + 5s + 5s at Normal is about 120–140 XCE.

The Supergen prompts will be written once the dialogue is measured.
