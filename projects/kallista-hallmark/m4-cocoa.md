# M4: front-yard cocoa break (all five), the hardest scene

**Beat:** a sunny winter morning on the B&B porch. Becca hands out cocoa. Marcus ribs Cal about how long the porch step is taking (he's obviously stretching the job to be near Kallista). Everyone laughs; the laugh dies completely; a beat of silence; then Milly, a full beat late: "Ha. Ha." She stops instantly, and everyone turns and looks at her.

## Dialogue (eleven_v4 Text to Dialogue; variants after the member's OK)
```
Marcus: [nodding at Cal, dry, deadpan] Four days. [beat] Same porch step.
(group laugh: Becca, Cal, Marcus; Kallista only a small smirk) → dies out → ~1.2s silence
Milly: [flat, polite, perfectly even, a full beat late] Ha. Ha.
(silence: everyone stares at her)
```
Voices: Marcus `escr2235adlWNmBRQ4Ay` · Becca `y3UNfL9XC5Bb5htg8B0q` · Cal `gxA3o4egfqrUI7soPxqX` · Milly `XdflFrQO8wbGpWMNZHFr`.

## Shot plan (website Reference to video, 10s; pickups as the fallback)
| Shot | Frame | Content |
|---|---|---|
| 1 | @1 W (wide) | Becca hands out mugs; Marcus nods at Cal: "Four days. Same porch step." |
| 2 | @1 W | Everyone laughs (Cal sheepish, rubbing the back of his neck; Kallista hides a smirk behind her mug) |
| 3 | @3 Milly MCU | Silence, then "Ha. Ha.", perfectly flat |
| 4 | @4 TURN | Everyone turns and stares at Milly; she sips her cocoa, unbothered |
@2 = Marcus MCU. Only three face slots, so the wide carries Becca, Cal and Kallista.
**Fallback:** single-speaker Image to video pickups (MCP) from the Marcus and Milly MCUs; the laugh goes on the wide in post.

## Keyframe W: the wide (Nano Banana Pro / Flow)
References: `m1_porch_P1.png` (porch, steps, door, truck) · Kallista, Cal, Becca (outdoor), Milly, Marcus identity shots. With five faces, generate the scene first, then do **face passes one person at a time** ("match this person's face exactly to the reference, keep everything else").
> A cinematic medium-wide shot on the front porch steps of a white Victorian bed-and-breakfast on a crisp, sunny winter morning, fresh snow on the yard and railings, wreaths and garland on the porch. One porch step is still unfinished, a bare new pine tread with a hammer and a few nails beside it. Five friends stand in a loose semicircle on and below the steps, all facing roughly toward the camera, every face clearly visible and lit by soft morning sun. Center: Becca, the woman from the Becca reference, holding a wooden tray of steaming mugs of cocoa, handing one to Cal: long wavy auburn hair, freckles, a warm winter coat as in her reference. Left of her: Cal, the man from the Cal references, in a tan sherpa-collar canvas work jacket over a red-and-black buffalo-check flannel, a tool belt, taking the mug. Next to Cal: Marcus, the man from the Marcus references, in an olive-green canvas work jacket over a navy henley, holding a mug, smirking sideways at Cal. Right of Becca: Kallista, the woman from the Kallista references, very pale cool platinum-blonde straight hair with a center part, a long charcoal wool coat and a dark grey chunky knit scarf, holding a mug near her chin, a guarded half-smile. Far right, standing perfectly upright and apart: Milly, the woman from the Milly reference, a sleek glossy chestnut-brown bob, a perfectly pressed camel wool coat over a cream turtleneck, holding her mug with both hands, expression pleasant and blank. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2.8, photorealistic film still, soft winter sunlight, gentle highlight bloom, light 35mm film grain, natural skin texture. 16:9. No text, no logos, no watermark.

Check: all five faces visible and front or three-quarter, about 1/6 of the frame height or more; no extra people; the same wardrobe as earlier scenes; the unfinished step visible.

## Keyframe Marcus MCU (an edit or crop of W)
> Keep this exact scene and lighting. Change to a medium close-up of Marcus, with Cal partly visible at the edge of frame beside him: Marcus holds his mug, nods toward Cal with a dry, deadpan smirk. Keep his face exactly the same.

## Keyframe Milly MCU (an edit or crop of W)
> Keep this exact scene and lighting. Change to a medium close-up of Milly standing apart near the porch rail, mug held in both hands at her chest, perfectly upright, pleasant blank expression, eyes slightly unfocused. Keep her face exactly the same.

## Keyframe TURN (an edit of W)
> Keep this exact scene, camera and lighting. Becca, Cal, Marcus and Kallista have all turned their heads to stare at Milly, frozen mid-moment with puzzled, slightly alarmed expressions; Milly calmly takes a sip of her cocoa, unbothered. Keep all five faces exactly the same.

## Wide delivered: `m4_cocoa_W_wide.jpg` (member's). All five faces clear, the Hearthstone truck, platinum Kallista, Milly apart at the rail. The new pine treads are the ones Cal hammered in M1 (raw, unpainted), so "Four days. Same porch step." still reads. Retouch: a brand-style patch on Marcus's chest pocket cloned out locally (original kept as `_orig`).
## Dialogue (eleven_v4 Text to Dialogue)
- A dry: Milly said "Ha." four times; only the first two are used. B smug: the first run duplicated Marcus's line and garbled the laughs; re-run without "sipping his cocoa" (the tag made a slurp and a repeat).
- 10s tracks `m4_cocoa_10s_A_dry.mp3` / `_B_smug.mp3`: Marcus 0.1–2.6 → group laugh (Cal's "Okay, okay" / "Yeah, yeah" overlapped onto the tail) to ~6.0 → **~1.1s silence** → Milly "Ha. Ha." A 7.0–8.3 / B 7.5–8.6 → silent stare to 10s; porch winter tone underneath.
**Milly pick: squeal 3** ("[high-pitched, perky, way too cheerful, quick] Ha ha!") → scene audio `m4_cocoa_10s_B_squeal3.mp3`.

## Wide v2: `m4_cocoa_W2_wide.jpg` (member's, built on the M1 porch plate), the chosen base
New raw-pine treads and risers installed, unpainted, with a hammer left on a step (still not finished); the same porch, doors and wreaths as M1; Marcus's jacket is clean (no patch). Cal is in three-quarter profile toward Becca (fine, he has no spoken line). **Milly's bob reads coppery-auburn in the sun** against her glossy chestnut elsewhere: a hair-only pass suggested.
**Wide v3 (`m4_cocoa_W3_wide.jpg`): W2 with Milly's hair corrected to a darker chestnut. This is @1 for M4.**

## Edit prompts (Nano Banana Pro / Flow; attach W3 FIRST each time)
**E1 Marcus MCU** (refs: W3, Marcus identity headshot)
> Keep this exact scene, porch, lighting and wardrobe. Reframe as a medium close-up of Marcus, the man from the Marcus reference, from the chest up, the camera at the same angle as the wide, the white porch door and wreath softly out of focus behind him. Cal's tan sherpa-collar shoulder and the back of his head are just visible at the left edge of frame. Marcus holds his glass mug of cocoa at chest height and looks toward Cal at frame left with a dry, deadpan smirk, one eyebrow slightly raised. Same face exactly as in the reference: short tapered dark hair, neatly trimmed beard, warm brown eyes; the plain olive-green canvas jacket with no patches or logos over a navy henley. 16:9. No text, no logos, no watermark.

**E2 Milly MCU** (refs: W3, Milly portrait)
> Keep this exact scene, porch, lighting and wardrobe. Reframe as a medium close-up of Milly, the woman from the Milly reference, from the chest up, the white porch railing with green garland softly out of focus behind her. She stands perfectly upright holding her glass mug of cocoa in both hands at her chest, her body angled slightly toward the group at frame left, her eyes on them (not on the camera), with a polite, pleasant, perfectly composed blank expression. Same face exactly as in the reference: a sleek glossy dark chestnut-brown bob, flawless symmetrical features, large calm brown eyes; the pressed camel wool coat over a cream turtleneck. 16:9. No text, no logos, no watermark.

**E3 TURN** (refs: W3 only; face passes afterwards if anyone drifts)
> Keep this exact scene, framing, porch, lighting and wardrobe, and all five people in the same places. Becca, Cal, Marcus and Kallista have all turned their heads toward Milly at the far right and stare at her, frozen mid-moment, with puzzled, slightly alarmed expressions; Cal at the far left now faces more toward the camera as he turns, so his face is clearly visible. Milly, at the far right, calmly takes a sip of her cocoa, eyes down, completely unbothered. Keep all five faces exactly the same. No text, no logos, no watermark.

## Edits delivered: `m4_cocoa_E1_marcus.jpg` (Marcus MCU, Cal's shoulder at frame left, door and wreath behind) · `m4_cocoa_E2_milly.jpg` (Milly MCU, porch rail and bows behind, eyes to frame left). E3 TURN pending (GPT Images).
## FINAL scene audio `m4_cocoa_10s_final.mp3` (retimed so the stare has room)
Marcus "Four days... same porch step." 0.1–2.45 → group laugh 2.45–~5.1 (Cal's chuckle and one "Yeah." overlapped at 3.9) → **silence ~5.15–6.45** → Milly squeal 3 "Ha ha!" ~6.6–8.2 → **silent stare 8.2–10.0**.
**E3 TURN delivered: `m4_cocoa_E3_turn.jpg` (GPT Images; Cal holds his own mug, Becca both hands on the tray). Member is fine with Kallista as is. Render: ONE 10s website Reference to video, 4 scripted shots (@1 W3, @2 E1, @3 E2, @4 E3) + `m4_cocoa_10s_final.mp3`.**

## Supergen version fix (member makes two versions: Omni Flash and Supergen)
The member's Supergen render `4a7882915c7c` fell apart (Marcus's MCU ran 6s; in the wide, Kallista wandered off and vanished; no Milly shot; snow at the end). Omni Flash's Scene 11 nailed it and stays the Omni Flash version.
- **Group laugh rebuilt with our voices:** separate eleven_v4 TTS laughs (`m4_laugh_becca/cal/marcus/kallista.mp3`), layered and staggered → `m4_group_laugh_v2.wav` (3.05s; Becca's tail burst trimmed so nothing reads as a late Milly). Member: Milly squeals ~0.3–0.4s after the laugh dies; anything longer feels forced.
- MCP pickups (5s, 480p): laugh `864fae96757f` (from W3, laugh audio) · Milly `6bf94bd6382b` (from E2, squeal 3 at 1.0s) · stare `522ef00093db` (from E3, silent). All held faces and positions, with no snow.
- **Edit `m4_cocoa_sg_v1.mp4` (10.7s):** Supergen render 0–2.5 (Marcus line) → laugh pickup 0.25–3.45 → Milly pickup 0.7–3.3 → stare pickup 0.3–2.7. Audio: clean Marcus line, group laugh at 2.55, squeal 3 at 6.0 (~0.4s after the laugh), porch tone; Supergen audio muted.
