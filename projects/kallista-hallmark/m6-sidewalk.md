# M6: sidewalk outside the laundromat, night (the "you could die?" scene)

**Lines** (eleven_v4; labeled variants per the skill's take rules, after the member's OK):
```
Kallista: [breathless, flustered] I don't do... falling.
Cal: [still holding her, softly] What's the worst that could happen?
Kallista: [deadpan, completely sincere] Uh... you could die?
Cal: [a stunned beat, then a smile] ...Okay. But besides that?
Kallista: [a real, surprised laugh]
```
A callback to the rink: this time she slips and he catches her.

## Shot plan (website Reference to video, 15s, like M5)
| Shot | Content | Source |
|---|---|---|
| 1 | The slip and the catch (a skid on ice, no lines) | @1 keyframe A |
| 2 | Held in his arms, faces close: the four lines | close angles from @2/@3 (+@4 B) |
| 3 | Her real laugh; he's smiling | @4 keyframe B |
Fallback if the catch looks bad: start on keyframe B (already caught) and add the skid sound off-screen.

## Keyframe A: the catch (Nano Banana Pro / Flow)
References: Kallista and Cal identity shots · `m7_door_D1.jpg` (wardrobe) · a laundromat frame (`laundromat_LM1_reveal_v2.png`) for the window look
> A cinematic night street shot on a small-town sidewalk in winter, outside a laundromat whose big front windows glow warm yellow, rows of washing machines visible inside. Old-fashioned street lamps, light snow falling, a glossy patch of ice on the sidewalk. Kallista, the woman from the Kallista references, has just slipped on the ice: she is tipped backward off balance, one foot skidding forward, her arms clutching at Cal's forearms. Cal, the man from the Cal references, has caught her by both arms and is holding her up, leaning over her, steady and calm. Both faces are visible in three-quarter view, close together, lit by the laundromat window glow: her eyes wide with surprise, lips parted; his expression gentle with a hint of amusement. Kallista: very pale cool platinum-blonde straight hair, almost white, with a center part, a longer face with defined cheekbones, large pale blue-grey eyes, a charcoal wool coat and a dark grey chunky knit scarf. Cal: tousled brown hair, light stubble, warm hazel eyes, a tan sherpa-collar canvas work jacket over a red-and-black buffalo-check flannel. Medium shot from the side at standing height, both full faces in frame, the laundromat window behind them. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm practical light against cool blue night, gentle highlight bloom, creamy shallow depth of field, light 35mm film grain, natural skin texture. 16:9. No text, no logos, no watermark.

Check: both faces lit and three-quarter or better; hands and arms read clearly (no extra limbs or fused fingers); the ice patch is visible; the wardrobe matches M5 and M7.

## Keyframe B: steadied, still in his arms (an EDIT of A)
> Keep this exact street, lighting and camera. Kallista is now back on her feet, still standing very close to Cal, her hands resting on his forearms; he still holds her lightly by the arms. They look at each other, faces close: she looks flustered and a little embarrassed, he looks soft and amused. Keep both faces exactly the same.

## Keyframes delivered
`m6_sidewalk_A_catch.jpg` · `m6_sidewalk_B_steady.jpg` (retouched locally: a dark cheek spot inpainted, a red cheek blotch toned to the surrounding skin; original kept as `_orig`).

## Line change (the member's): Cal: "In love? What's the worst that can happen?" (turns "falling" into the pun, so "you could die?" lands)

## Dialogue: one Text to Dialogue request per variant (Speaker 1 Kallista, Speaker 2 Cal, eleven_v4)
- **A deadpan sincere** (13.6s raw) · **B rattled, matter-of-fact** (15.2s raw; whisper start, "Umm...") · **C Cal leans in** (12.0s raw, "incredulous")
- The laugh line needs real text (the API rejects tag-only input): "Ha... haha." / "Ha... ha." / "Ha!"
- 15s tracks `m6_sidewalk_15s_<variant>.mp3`: `sfx_ice_skid_v3.mp3` (v3) at 0.15s, dialogue from 1.6s, `roomtone_night_street_v3.mp3` (v3) at about −47 dB.
**Member picked B.** Fixes: (1) the first skid sounded like a car skid. There is no v4 sound model (`eleven_text_to_sound_v4` and `eleven_sfx_v4` both return 422), so three new v3 takes were made with human-scale prompts (boot sole, coat rustle, "no vehicles"): `sfx_ice_slip_v3_take1–3.mp3`. (2) Kallista's laugh "Ha... ha.": the second burst is cut, so the dialogue is trimmed at 13.85s (`m6_sidewalk_dialogue_B_cut.mp3`). Tracks: `m6_sidewalk_15s_B_slip1–3.mp3`.

## FINAL track: `m6_sidewalk_15s_B_final.mp3` (15.0s)
Slip take 2 (trimmed to its main slide and catch) 0.06–1.46 → **love-hold silence ~1.5s** → Kallista 2.94–4.68 "I don't do... falling." → (Cal's soft amused breath 4.7–5.6) → Cal 5.74–8.02 "In love? What's the worst that can happen?" → Kallista 8.52–10.10 "Umm... you could die?" → Cal's stunned soft laugh 10.1–11.0 → Cal 11.12–12.92 "Okay... but besides that?" → Kallista's laugh 13.22–13.56 (ONE "hhuh" only; everything after the short pause is cut, so the track is room tone from 13.56 to 15.0). Pauses tightened: −0.25s at 3.95, −0.2s at 5.85, −0.17s at 6.85, −0.32s at 9.7.

## Website prompt (Reference to video, 15s): @1 A catch · @2 Kallista close face ref · @3 Cal face ref · @4 B steady · scene audio = the final track
```
The scene begins on @1 exactly as shown: night on a small-town sidewalk in winter, outside a laundromat whose big front windows glow warm yellow, old street lamps with wreaths, light snow falling, a glossy patch of ice on the pavement. Kallista @2, the platinum-blonde woman in the charcoal coat and grey knit scarf, has just slipped on the ice; Cal @3, the man in the tan sherpa-collar work jacket and buffalo-check flannel, has caught her by the arms.
SHOT 1 (about 3 seconds), the side two-shot from @1: her boot skids on the ice, she tips backward and Cal catches her. He steadies her and she comes back up onto her feet, ending close together as in @4, his hands still on her arms, hers on his forearms. Then they simply hold the moment: they look into each other's eyes, very close, perfectly still and silent, snow falling around them.
SHOT 2 (about 2 seconds), a close-up of Kallista over Cal's shoulder: flustered, breathless, she says softly: "I don't do... falling."
SHOT 3 (about 3 seconds), a close-up of Cal over her shoulder: an amused breath, then he says softly, half-smiling: "In love? What's the worst that can happen?"
SHOT 4 (about 2 seconds), back on Kallista: totally serious, matter-of-fact, she says: "Umm... you could die?"
SHOT 5 (about 3 seconds), on Cal: caught off guard, a soft laugh, then he says: "Okay... but besides that?"
SHOT 6 (about 2 seconds), the two-shot matching @4: Kallista breaks into a real, surprised laugh and covers her mouth with her hand; Cal grins at her.
Always cut to the person who is speaking so their face is on camera while they talk; only the person speaking moves their lips. The two of them only ever look at each other; nobody ever looks into the camera.
BACKGROUND LIFE: snow drifts down through the lamplight; inside the laundromat window a dryer drum slowly turns; far down the street a car's taillights pass.
SOUND: only the two voices, the skid on the ice and the quiet night street. There is no music.
```
