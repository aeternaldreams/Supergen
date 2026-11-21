# Cast roll (5 hero shots, ~2–3s each over the song's chorus; name cards added in the edit)
Route: Supergen Image to video via MCP (I run these), 5s each, Normal. About 36 XCE each, about 180 XCE total. Medium close-ups so faces hold. In the cast roll, characters may look at the camera (the classic trailer cast-roll beat).

Shared camera line for all five keyframes:
`Shot on ARRI Alexa Mini LF with a 50mm Cooke S4 lens at T2, photorealistic film still, warm golden-hour backlight with gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.`

## 1. KALLISTA VANE: the snowy field, golden hour
Attach: Kallista identity shots 1 and 2, coat portrait, S10 field set.
> A medium close-up of Kallista, the woman from the Kallista references, standing in a quiet snowy field at the edge of a small town at golden hour, pine trees soft and out of focus behind her, light snow falling and glowing in the warm backlight. She is turned three-quarters away from the camera, glancing back over her shoulder toward the camera with the faintest half-smile she is trying to hide. Same face: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part, hair lit at the edges by the sun. A charcoal wool coat and a dark grey chunky knit scarf. [camera line]
**Motion:** she slowly turns her head to face the camera; the half-smile grows a little, then she catches it. Snow drifts. Locked camera, slow push-in.

## 2. CAL WHITAKER: woodchopping
Attach: Cal close-up, Cal full body, S10 field set.
> A medium shot of Cal, the man from the Cal references, at a chopping block in a snowy clearing at golden hour, pine trees behind him, a stack of split logs beside him. He wears a red-and-black buffalo-check flannel with the sleeves rolled up to the elbows over a grey thermal henley, work gloves, jeans. He has just split a log with an axe, the two halves falling away, and he looks up toward the camera with a warm, boyish, slightly bashful grin. Same face: tousled brown hair, light stubble, warm hazel eyes. His breath fogs in the cold. [camera line]
**Motion:** the axe comes down and splits the log; he looks up at the camera and grins. Wood chips fly; snow sparkles in the backlight.

## 3. BECCA HARTLEY: the cocoa swoon
Attach: Becca indoor portrait, S1 sitting-room set (evening).
> A medium close-up of Becca, the woman from the Becca reference, curled up on the cozy bed-and-breakfast sofa at night by the Christmas tree, holding a huge mug of hot cocoa piled high with marshmallows in both hands, gazing dreamily off to the side with a lovestruck, swooning smile. Same face: long wavy auburn hair, light freckles, warm green-brown eyes, a burgundy cable-knit sweater. Warm firelight and soft tree-light bokeh behind her. [camera line, but "warm firelight" instead of golden-hour backlight]
**Motion:** she sighs dreamily and clutches the mug to her chest; marshmallows tumble over the rim and she scrambles to catch them, laughing.

## 4. MARCUS BELL: the hammer
Attach: Marcus close-up, Marcus full body, S9 side-yard set.
> A medium close-up of Marcus, the man from the Marcus references, in the snowy side yard of the bed-and-breakfast by the sawhorses at golden hour, pointing a hammer straight at the camera with a knowing, wry smirk and one raised eyebrow. Same face: a handsome light-skinned Black man around thirty, short tapered dark hair, a neatly trimmed beard, warm brown eyes, a carpenter's pencil behind his ear, an olive-green canvas work jacket over a navy henley. [camera line]
**Line (needs ElevenLabs):** `Marcus: [smirking, to camera] 'Subsequential Consequences.' Total banger.` *(song easter egg)*, or `Marcus: [smirking, to camera] Don't overthink it, Cal.`

## 5. "and introducing" MILLY ALWOOD: the snow
Attach: Milly portrait, S10 field set (or the B&B front yard).
> A medium close-up of Milly, the woman from the Milly reference, standing perfectly still and upright in gently falling snow in front of the bed-and-breakfast at golden hour. Same face: a sleek glossy chestnut-brown bob, flawless, very symmetrical features, large calm brown eyes, a perfectly pressed camel wool coat over a cream turtleneck. Snowflakes fall all around her, but not a single flake has landed on her hair or coat; she is spotless. She looks straight at the camera with a pleasant, completely neutral expression. [camera line]
**Motion:** snow falls around her and never touches her; after a beat she smiles one beat too late, and holds the smile far too long without blinking.

## Kallista cast clip: `a24225960583` (5s, Image to video from `castroll/cast_kallista.png`)
Clean, no cuts. Use 0–3.1s (the turn and the smile; after about 4s she starts to part her lips as if speaking). Name test `cast_kallista_name_test.mp4`: "KALLISTA  VANE" in letter-spaced cream serif with a gold rule, left third; fades in at 0.6s over 0.45s, drifts 3 px/s, fades out from 2.75s.

## Cal: `4e1352575a32` (swing) + `6737c0456ece` (grin), both 5s Image to video
Cut `cast_cal_v1.mp4` (4.6s): swing 0–1.1 (impact at about 0.52, the log splits, chips fly) → hard cut → grin 0.2–3.7 (breath, grin, bashful duck, looks back up). v2: only the soft thunk of `sfx_axe_split.mp3` (first 0.26s, lowpass 2.5 kHz, −16 dB) at 0.5s; the crack was too loud, winter tone. Name "CAL / WHITAKER" fades in at 0.5s into the grin, same template as Kallista (top-left over the trees).
- v3 cut (`cast_cal_v3.mp4`): `sfx_axe_thunk_v3.mp3` (ElevenLabs sound **v3**, "soft, muffled thunk"), −14 dB, hit aligned to 0.52s. **Use model `eleven_text_to_sound_v3` for all SFX from now on.**
- v4 cut (`cast_cal_v4.mp4`): v3 thunk at 0.52s (−14 dB) + `sfx_wood_crack_v3.mp3` (v3, crack onset 0.12s in the file) placed so the crack hits at 0.58s, as the log visibly splits (−15 dB), with the halves landing after.

**LOCKED:** Cal = `cast_cal_v4.mp4` (v3 thunk + v3 crack).

## Becca: `5d018dff48b2` (5s Image to video from `castroll/cast_becca.png`)
Cut `cast_becca_v1.mp4` (3.9s, clip 1.0–4.9): dreamy smile → hugs the mug → catches a marshmallow and pops it in, laughing. Name "BECCA / HARTLEY" over the tree bokeh with a stronger left shade (alpha 165). B&B tone at −4 dB.

## Marcus (idea agreed): secret fan
Earbuds in, eyes closed, earnestly vibing to Kallista's song on the sawhorse; senses the camera, freezes mid-nod, plays it cool with a slow nod and a smirk. Silent. Escalates the M2 joke instead of repeating the apple.
**Marcus props:** small white wireless earbuds (generic, no logo), plus a phone in one hand with a dark, moody album cover on screen (a pale platinum-haired woman in shadow, i.e. Kallista's album) and no readable text, so the gag reads at a glance.
- Becca v2 (`cast_becca_v2.mp4`, 2.7s): clip 0–2.7 only (dreamy swoon and sigh); the marshmallow catch from 2.75s on looked AI/uncanny, so it is cut.
- Becca v3 (`cast_becca_v3.mp4`, 4.1s): reroll `cf89e06f0166` (sip version), clip 0.5–4.6: raises the mug, sips, lowers it, a contented sigh, starts to lean back. No flying marshmallows.

## Marcus: `b5efdfd34b21` (5s Image to video from `castroll/cast_marcus.png`)
Cut `cast_marcus_v1.mp4` (3.6s, clip 0.8–4.4): smiling at his phone with a little bob → looks up at the camera with a sly, knowing smirk. The "eyes closed, vibing" part did not really happen. A small Carhartt patch is on his chest pocket (blurry at 576p); remove it with a Nano Banana edit if he is rerolled.
- Marcus v2 (`cast_marcus_v2.mp4`, 4.2s): reroll `22a356b50e87` from the logo-free `cast_marcus_v2.png`, clip 0.3–4.5: eyes shut, vibing → eyes open, caught, a little "oh" → slow grin. Name fades in late (2.0s) so the vibing reads first.

## Milly: interior concept chosen ("the perfect present")
The outdoor snow gag is dropped (she has no reason to be outside, and the snow landed on her in the test frame). Instead: at the B&B dining table, finishing a gift with a flawless bow next to a stack of identically wrapped boxes in perfect alignment; she trims both ribbon tails to exactly the same length, looks up at the camera, smiles a beat too late and holds it too long. Base: Nano Banana edit of `castroll/cast_milly_outdoor_ref.png` (her face, bob and turtleneck).
