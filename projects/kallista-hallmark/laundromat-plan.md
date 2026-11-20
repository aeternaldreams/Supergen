# The real meet-cute: small-town laundromat (dialogue prep)

## Voices (the member's ElevenLabs account)
| Character | Voice | ID |
|---|---|---|
| Kallista | Kallista Vane (NS) | `MKqq8Z70lLyJj4W5AfgD` |
| Becca | Beth - Bold and Smooth Narrator | `y3UNfL9XC5Bb5htg8B0q` |
| Milly | Zoe - Playful and Arrogant Magician | `XdflFrQO8wbGpWMNZHFr` |
| Adrian | Adrian Vale | `kxfQeXXEoNcFggn2Ys06` |
| **Cal (proposed)** | **Will - Relaxed Optimist** (young American, chill, conversational). Alternative: Chris - Charming, Down-to-Earth | `bIHbv24MWmeRgasZH58o` / `iP95p4xoKVk53GoZ742B` |

## Dialogue (ElevenLabs Text to Dialogue, eleven_v3), one generation, split per clip afterwards
```
Kallista: [hesitant, awkward, quiet] Um... excuse me. [short pause] You have something.
Cal: [confused, friendly, a little alarmed] Where? [nervous laugh] Is it a bug?
Kallista: [mortified, flat, quiet] It's... mine.
Cal: [sheepish, trying very hard to be a gentleman] I'd like to say this has never happened to me before.
Kallista: [dry, suspicious] Has it?
Cal: [shy grin, sweetly awkward] Not with one this nice.
```
**Clip split** (max 4 lines per Supergen clip):
- **L1 (F6 frame):** lines 1–3. He pats his shoulders and turns in circles; she says it's hers. He peels it off and they freeze (silent).
- **L2 (F7 frame):** lines 4–6. She snatches it back; she almost smiles, catches herself, and leaves (silent).

## Cal's voice: designed via the API
"Cal Whitaker" `gxA3o4egfqrUI7soPxqX` (Voice Design, eleven_ttv_v3, preview 3 of 3), saved to the member's account.

## Take 1: `voices/holiday-reservations/laundromat_dialogue_take1.mp3` (21.8s, Text to Dialogue eleven_v3)
Speech blocks (pauses longer than 0.3s): 0–0.47 · 1.51–2.27 · 3.94–4.92 · 6.67–8.80 · 10.19–10.64 · 11.87–12.33 · 14.02–16.13 · 17.12–17.81 · 18.44–19.78. The pauses are long, so they'll be tightened when the clip tracks are built.

## Take 2: Eleven v4 (`eleven_v4`), `laundromat_dialogue_take2_v4.mp3` (16.0s)
The same script and voices. Tighter pacing than v3 (21.8s). Pauses longer than 0.3s: 0.66–1.21 · 2.08–2.73 · 3.99–4.35 · 4.81–5.16 · 8.09–8.61 · 9.31–9.76.
**Use `eleven_v4` for all dialogue from now on** (the member's request). Also available: `eleven_v4_turbo`.

## Clip tracks (from take 2, v4)
- `laundromat_L1_10s.mp3`: Kallista 0.5–4.3 ("Um... excuse me. You have something.") · Cal 4.65–8.4 ("Where? [laugh] Is it a bug?") · silence to 10.0 (he turns in circles).
- `laundromat_L2_10s.mp3`: Kallista 0.3–0.8 ("It's... mine.") · **silent freeze 0.8–2.3** (he peels it off and holds it up) · Cal 2.5–6.2 ("I'd like to say...") · Kallista about 6.5 ("Has it?") · Cal 7.3–8.8 ("Not with one this nice.") · silence to 10.0 (her almost-smile).

## Keyframes needed (none exist yet)
Rules: one start frame per clip, both faces visible, and **every close-up is a crop of a master frame** so the room never changes. Kallista wears Outfit A (black ribbed mock-neck, open charcoal wool coat, dark grey chunky scarf). Cal wears a red-and-black buffalo-check flannel over a grey thermal henley.
**Geography:** dryers along the left wall, a wooden folding counter on the right, front windows with snow behind the counter. Kallista works the dryers (screen-left); Cal folds at the counter (screen-right).

| # | Frame | Use |
|---|---|---|
| S3 | Empty laundromat set (prompt in `nano-banana-keyframes.md`) | Base for L1 |
| CAL | Cal cast portraits (front close-up + full body; `nano-banana-keyframes.md` #2 / #2b) | Identity reference |
| **LM1** | L1 start frame: edit of S3 | Clip L1 |
| **LM2** | L2 start frame: edit of LM1 (same room, same camera) | Clip L2 |
| LM3 | Cal close-up: crop of LM2 | Towel gag, and Omni Flash |
| LM4 | Kallista close-up: crop of LM2 | Omni Flash, reactions |

### LM1: the reveal (edit S3, attach the set FIRST, then Kallista identity shot 1 + coat portrait, then Cal's portraits)
> Keep this exact laundromat, camera and lighting. Add two people. In the left foreground, Kallista, the woman from the Kallista references, stands at an open front-loading dryer holding a basket of warm laundry, her body and face turned toward the camera at three-quarters as she looks across the room at Cal with an awkward, uncertain expression. Same face: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part. She wears a fitted black ribbed mock-neck sweater, an open charcoal wool coat and a dark grey chunky knit scarf. In the mid-ground right, Cal, the man from the Cal references, stands at the wooden folding counter folding a towel, his back half turned to the camera, with his head turned over his shoulder toward her so his face shows in three-quarter profile: tousled brown hair, light stubble, warm hazel eyes. He wears a red-and-black buffalo-check flannel shirt over a grey thermal henley. A black lace bra clings flat to the back of his flannel between his shoulder blades, clearly visible. Warm winter daylight through the front windows, snow outside. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.

### LM2: holding it up (edit LM1, attached FIRST, plus Cal's front close-up)
> Keep this exact laundromat, camera position, lighting, and both people's faces, hair and clothes. Change only their poses: they now stand facing each other in the middle of the room near the folding counter, both turned at three-quarters toward the camera so both faces are clearly visible: Kallista on the left, Cal on the right. Cal holds the black lace bra up between them by one strap at arm's length, his face frozen in polite, mortified gentleman mode. Kallista stares at it, deadpan, cheeks slightly flushed, one hand starting to reach for it. Her laundry basket sits on the counter. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, creamy shallow depth of field, light 35mm film grain, natural skin texture. No text, no logos, no watermark.

## Supergen prompts (Image to video, single start frame, scene audio, 10s, Normal, 16:9)

### L1: start frame LM1, audio `laundromat_L1_10s.mp3`
```
Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a charming small-town laundromat on a snowy winter day. Keep both faces, the clothes, the black lace bra on his back and the room exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm winter daylight, shallow depth of field and organic film grain.
KALLISTA (left, by the dryer) has a soft, low, dry voice: pale skin, a longer face, large pale blue-grey eyes, straight sleek pale platinum-blonde hair, a black mock-neck, a charcoal coat and a grey knit scarf. Reserved and mortified. CAL (right, at the folding counter) has a warm, boyish voice with a slight rasp: tousled brown hair, light stubble, a red-and-black buffalo-check flannel. Sweet, earnest and a little awkward.
If you cut, always cut to whoever is speaking so their face is on camera; only the person speaking moves their lips. Nobody looks into the camera.
0.5–4.3 seconds: Kallista hesitates, then says awkwardly: "Um... excuse me. You have something."
4.6–8.4 seconds: Cal turns toward her, confused and friendly: "Where?" He gives a nervous laugh and pats his own shoulders: "Is it a bug?"
8.4–10 seconds: silence. Cal turns in a slow circle trying to see his own back, like a dog chasing its tail, while Kallista watches, mouth closed.
Throughout: keep the supplied audio unchanged; add no music or voices. No other people, no subtitles, no watermarks.
```

### L2: start frame LM2, audio `laundromat_L2_10s.mp3`
```
Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a man and a woman facing each other in a small-town laundromat on a snowy day, the man holding up a black lace bra between them. Keep both faces, the clothes and the room exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm winter daylight, shallow depth of field and organic film grain.
KALLISTA (left) has a soft, low, dry voice: pale skin, a longer face, large pale blue-grey eyes, straight sleek pale platinum-blonde hair, a black mock-neck, a charcoal coat and a grey knit scarf. Reserved and deadpan. CAL (right) has a warm, boyish voice with a slight rasp: tousled brown hair, light stubble, a red-and-black buffalo-check flannel. Sweet, earnest, trying very hard to be a gentleman.
If you cut, always cut to whoever is speaking so their face is on camera; only the person speaking moves their lips. Nobody looks into the camera.
0.3–0.8 seconds: Kallista, mortified and flat: "It's... mine."
0.8–2.3 seconds: silence. Both freeze, staring at the bra he is holding up.
2.5–6.2 seconds: Cal, sheepish and earnest: "I'd like to say this has never happened to me before."
6.3–7.0 seconds: Kallista snatches the bra out of his hand and says, dry and suspicious: "Has it?"
7.3–8.8 seconds: Cal, with a shy grin: "Not with one this nice."
8.8–10 seconds: silence. Kallista almost smiles, catches herself, mouth closed.
Throughout: keep the supplied audio unchanged; add no music or voices. No other people, no subtitles, no watermarks.
```

## LM1 delivered: `keyframes/holiday-reservations/laundromat_LM1_reveal.png`
Kallista is at the left dryers in her black mock-neck, without the coat (fine indoors). Cal is at the counter, looking down at his towel. The bra is clearly on his back, and pastel dryers line the right wall behind him.

## LM0: setting up the gag (2–3s used from a 5s clip, silent)
**The joke:** Cal pulls his flannel fresh out of a dryer (the one Kallista used, where her bra got left behind) and shrugs it on; the bra stays clinging to the back. (Never write "static" in Supergen prompts; use "fresh out of the dryer".)
**Frame LM0** (edit LM1, attached first, plus Cal's front close-up):
> Keep this exact laundromat, camera, lighting, and Kallista exactly as she is on the left. Change only the man: he now stands at the pastel-green dryer on the right wall with its round door open, facing it at three-quarters toward the camera so his face is visible, in a grey thermal henley and jeans. He is pulling a red-and-black buffalo-check flannel shirt out of the dryer drum with both hands, about to shake it out. A black lace bra is caught on the back of the flannel, partly visible. The towels sit folded on the wooden counter beside him. Same face as the Cal reference: tousled brown hair, light stubble, warm hazel eyes. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, creamy shallow depth of field, light 35mm film grain, natural skin texture. No text, no logos, no watermark.
(Optional: crop to a medium shot of Cal afterwards, so he fills the frame.)

**Supergen (Image to video, start frame LM0, 5s, Normal, 16:9, no audio):**
```
Create a 5-second cinematic live-action romantic comedy shot in 16:9, beginning directly from the supplied first frame: a small-town laundromat on a snowy day. One continuous shot, locked camera, no cuts. Keep his face, the room and the woman in the background exactly as in the first frame. CAL is a sweet, easygoing young man with tousled brown hair and light stubble, in a grey thermal henley.
0–1.5 seconds: He pulls the warm red-and-black buffalo-check flannel out of the dryer and gives it one quick shake.
1.5–3.5 seconds: He shrugs it on over his henley, one arm then the other, completely unaware that a black lace bra is stuck flat to the back of the flannel, between his shoulder blades. He turns toward the folding counter.
3.5–5 seconds: He starts folding a towel, oblivious.
Sound: dryers tumbling, a soft machine hum. No dialogue, no music, no subtitles, no watermarks.
```
**Edit:** LM0 (about 2.5s) → L1. The cut lands on him at the counter with the bra on his back, which matches LM1.

### LM0 revision (the member's notes)
- **Cal is alone** in the setup shot; Kallista first appears in LM1, already noticing.
- **The logic:** Kallista is on her second load. Her bra stayed stuck inside the dryer drum when she emptied her first load. Cal used that dryer next, and his flannel comes out with her bra clinging to it. In LM1 she's *unloading* her second load from another dryer.
- **The fix** (edit the first LM0 result, attached first): "Keep this exact image... Remove the blonde woman and her laundry basket completely, and fill the space where she stood with the same row of dryers, the window and the checkered floor behind her, so the man is the only person in the room. Change nothing else." Then crop to a medium shot of Cal.

## Take 3 (revised lines, eleven_v4): `laundromat_dialogue_take3_v4.mp3` (18.8s)
Script: "Oh my god." (whisper) / "Um... excuse me. You have something." / Cal: "Where?" / "It's... mine." / Cal: "[embarrassed laugh] Guess we used the same dryer. ... I'd like to say this has never happened to me before." / "Has it?" / Cal: "Not with one this nice."
Approximate map: whisper 0.3–1.3 · "Um... excuse me. You have something." 2.0–5.75 · "Where?" 6.1–6.6 · "It's... mine." 7.0–about 8.4 · laugh + "Guess we used the same dryer." about 8.8–11.4 · "I'd like to say..." 12.3–15.4 · "Has it?" 15.8–16.4 · "Not with one this nice." 16.7–18.75.
The setup frame LM0 is now Cal alone (the member's image; he glances off toward Kallista, then puts the shirt on).

## FINAL (take 3) Supergen setup: three clips
Frames: `laundromat_LM0_setup.png`, `laundromat_LM1_reveal.png`, `laundromat_LM2_holdup.png` (the member's). Crops for close-ups: `laundromat_LM3_cal_cu.png`, `laundromat_LM4_kallista_cu.png`.

### C0: setup (LM0, 5s, no audio)
```
Create a 5-second cinematic live-action romantic comedy shot in 16:9, beginning directly from the supplied first frame: a young man alone in a small-town laundromat on a snowy day, holding a red-and-black buffalo-check flannel shirt fresh out of the dryer. One continuous shot, locked camera, no cuts. Keep his face, the room and the black lace bra stuck to the back of the flannel exactly as in the first frame. CAL is sweet and easygoing: tousled brown hair, light stubble, a grey thermal henley and jeans.
0–1 second: He gives a polite little glance across the room to the left, off screen, then looks back at his shirt.
1–3.5 seconds: He gives the warm flannel one quick shake and shrugs it on over his henley, one arm then the other, completely unaware that the black lace bra stays stuck flat to the back of it, between his shoulder blades.
3.5–5 seconds: He turns to the wooden folding counter and starts folding a towel, oblivious.
Sound: dryers tumbling, a soft machine hum. No dialogue, no music, no other people, no subtitles, no watermarks.
```

### C1: L1 (LM1, 10s, `laundromat_L1_v3_10s.mp3`)
Map: double-take 0–1.4 · "Oh my god." (whisper) 1.4–2.5 · "Um... excuse me. You have something." 3.2–6.95 · Cal "Where?" 7.3–7.8 · he circles 7.8–10.
```
Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a small-town laundromat on a snowy winter day. Keep both faces, the clothes, the black lace bra stuck to the back of his flannel, and the room exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm winter daylight, shallow depth of field and organic film grain.
KALLISTA (left, at the dryer with her laundry basket) has a soft, low, dry voice: pale skin, a longer face, large pale blue-grey eyes, straight sleek pale platinum-blonde hair, a black mock-neck. Reserved and mortified. CAL (right, at the folding counter, his back half turned) has a warm, boyish voice with a slight rasp: tousled brown hair, light stubble, a red-and-black buffalo-check flannel. Sweet, earnest, a little awkward, completely oblivious.
If you cut, always cut to whoever is speaking so their face is on camera; only the person speaking moves their lips. Nobody looks into the camera.
0–1.4 seconds: silence. Kallista glances at Cal's back, looks away, then does a double-take, her eyes going wide as she recognizes the bra.
1.4–2.5 seconds: she whispers to herself, mortified: "Oh my god."
3.2–7.0 seconds: she gathers herself and says awkwardly: "Um... excuse me. You have something."
7.3–7.8 seconds: Cal turns toward her, confused and friendly: "Where?"
7.8–10 seconds: silence. He pats his own shoulders and turns in a slow circle trying to see his back, like a dog chasing its tail, while Kallista watches, mouth closed.
Throughout: keep the supplied audio unchanged; add no music or voices. No other people, no subtitles, no watermarks.
```

### C2: L2 (LM2, 15s, `laundromat_L2_v3_15s.mp3`)
Map: "It's... mine." 0.3–1.55 · **silent freeze 1.55–3.3** · Cal [embarrassed laugh] "Guess we used the same dryer." 3.3–5.95 · "I'd like to say this has never happened to me before." 6.85–10.0 · "Has it?" 10.35–10.95 · "Not with one this nice." 11.25–13.3 · her almost-smile, then she leaves, 13.3–15.
```
Create a 15-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio, beginning directly from the supplied first frame: a man and a woman facing each other in a small-town laundromat on a snowy day, the man holding up a black lace bra by one strap between them. Keep both faces, the clothes and the room exactly as in the first frame. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, warm winter daylight, shallow depth of field and organic film grain.
KALLISTA (left) has a soft, low, dry voice: pale skin, a longer face, large pale blue-grey eyes, straight sleek pale platinum-blonde hair, a black mock-neck, cheeks slightly flushed. Reserved and deadpan. CAL (right) has a warm, boyish voice with a slight rasp: tousled brown hair, light stubble, a red-and-black buffalo-check flannel. Sweet, earnest, trying very hard to be a gentleman.
If you cut, always cut to whoever is speaking so their face is on camera; only the person speaking moves their lips. Nobody looks into the camera.
0.3–1.6 seconds: Kallista, mortified and flat: "It's... mine."
1.6–3.3 seconds: silence. Both freeze, staring at the bra between them.
3.3–6.0 seconds: Cal realizes, with an embarrassed laugh: "Guess we used the same dryer."
6.8–10.0 seconds: Cal, sheepish and earnest: "I'd like to say this has never happened to me before."
10.3–11.0 seconds: Kallista snatches the bra out of his hand and says, dry and suspicious: "Has it?"
11.2–13.3 seconds: Cal, with a shy grin: "Not with one this nice."
13.3–15 seconds: silence. Kallista almost smiles, catches herself, picks up her laundry basket and walks out past the camera, leaving him smiling at the counter.
Throughout: keep the supplied audio unchanged; add no music or voices. No other people, no subtitles, no watermarks.
```
Costs: C0 about 36 XCE, C1 about 66, C2 about 99 (about 200 in total).

## Prop toned down (Supergen content check)
Every laundromat job with the sheer black lace bra was refused, twice, even after the developer said he would relax the setting. **Fix:** the member re-edits LM0, LM1 and LM2: "replace the black lace bra with a plain matte black cotton sports bra, solid opaque fabric, no lace or sheer parts; change nothing else." Then resubmit C0–C2 with "black sports bra" in the prompts. The dialogue and audio are unchanged.

## Resubmit after the developer dropped the guardrail (original lace-bra frames)
- **C0 setup: done, `839d446d074f`** (5s → 6.58s, about 36 XCE). The cape-swing direction worked: he turns his back to the camera, swings the flannel over his head and threads his arms, and the bra ends up on his back (slightly high, by his left shoulder blade). Then he folds a towel.
- **C1 (L1) `vid_671083527b0e4ec8` and C2 (L2) `vid_95fb2ee928bc48a5`: still refused immediately.** Whatever still blocks them is specific to the dialogue clips (Kallista in frame with the bra, plus the dialogue audio). Reported to the member for the developer.
- **Prompt lesson (Supergen and Omni Flash):** for putting on a shirt, write "turns his back to the camera and swings the shirt up and over his head and down behind his shoulders like a cape... the shirt never passes in front of his chest."
