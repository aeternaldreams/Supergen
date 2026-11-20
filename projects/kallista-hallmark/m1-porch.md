# M1: B&B front porch, morning (the classic setup)

Kallista opens the front door with her morning coffee. Cal, the guy from the laundromat, is kneeling on the porch steps in a tool belt, replacing a rotted board. A "Hearthstone Carpentry" pickup is parked out front.

## Dialogue (ElevenLabs Text to Dialogue, eleven_v4)
Voices: Kallista Vane (NS) `MKqq8Z70lLyJj4W5AfgD`, Cal Whitaker `gxA3o4egfqrUI7soPxqX`.
```
Kallista: [stops short, dry and suspicious] Are you following me?
Cal: [caught off guard, then sheepish, a small grin] I was hired... [beat] in August.
```
Clip: about 8–10s. A silent beat at the start (she opens the door and sees him), the two lines, then a silent reaction at the end (she narrows her eyes and sips her coffee; he goes back to hammering, still grinning).

## Wardrobe
- **Kallista:** charcoal turtleneck (identity shot 2), charcoal wool coat worn open over it, dark grey chunky scarf, holding a white ceramic coffee mug. Hair as always.
- **Cal:** red-and-black buffalo-check flannel under a tan canvas work jacket with a sherpa collar, worn leather tool belt, jeans, work boots (Cal "work look", `nano-banana-keyframes.md` 2b).

## Keyframes
**Rule (from the laundromat):** close-ups that need a held face are crops of the master frame, and dialogue clips run in Reference to video mode with @2/@3 face references plus full scene audio.

### P0: the set (S2 in `nano-banana-keyframes.md`)
Use the existing B&B exterior set, or make it now (the prompt is in S2).

### P1: master two-shot (edit the S2 set, attached FIRST, plus Kallista identity shot 2, the coat portrait, Cal's work-look portrait)
> Keep this exact Victorian bed-and-breakfast, porch, snow and morning light. Reframe as a medium-wide shot from the front walk at standing height, looking up the porch steps at the front door, so both people's faces are clearly visible. In the open front doorway at the top of the steps, Kallista, the woman from the Kallista references, has just stepped out, holding a white ceramic coffee mug in both hands, stopped mid-step, looking down at the man on the steps with a dry, suspicious expression. Same face: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part. She wears a charcoal turtleneck under an open charcoal wool coat and a dark grey chunky knit scarf. On the porch steps in the lower right of the frame, Cal, the man from the Cal references, kneels on one knee beside a missing step board, a hammer in his hand and a new board beside him, looking up at her over his shoulder with a startled, sheepish half-smile, his face in three-quarter view toward the camera: tousled brown hair, light stubble, warm hazel eyes, a red-and-black buffalo-check flannel under a tan canvas work jacket with a sherpa collar, a worn leather tool belt. Green wreaths with red bows on the doors, garland along the porch rail, fresh snow. In the soft-focus background on the left, a pickup truck at the curb. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm soft practical lighting, gentle highlight bloom, creamy shallow depth of field, rich soft colors (warm reds, evergreen, cream, wood tones), light 35mm film grain, natural skin texture. No text, no logos, no watermark.

Check: both faces sharp and three-quarter or better; the steps, door and truck consistent with the S2 set. If a face drifts, run the one-person face pass from `nano-banana-keyframes.md`.

### P2 / P3: close-ups (crops of P1, done by me)
Kallista in the doorway, and Cal on the steps. These are the @2/@3 face references.

## Supergen (website, Reference to video, @1 = P1, @2 = Kallista crop, @3 = Cal crop, scene audio = the M1 track)
Written once the audio is measured (named speakers on every line).

## Audio: take 1 (`m1_porch_take1_v4.mp3`, 4.75s) → `m1_porch_10s.mp3`
Opening beat 0–1.5 (silent: door opens, she sees him) · Kallista "Are you following me?" 1.5–2.85 · Cal "I was hired..." 3.2–5.0 · "...in August." 5.4–6.25 · silent reaction 6.25–10.

## P1 delivered: `keyframes/holiday-reservations/m1_porch_P1.png`
Kallista stands on the porch steps (not in the doorway) in her coat and scarf with a white mug; Cal kneels at the steps with a hammer and a new board, looking up at her with a grin. The Hearthstone Carpentry truck is on the left. Face refs: the member's headshots, not crops (faces too small for crops).

## Audio v2: `m1_porch_10s_v2.mp3` (more breathing room before Cal)
Opening 0–1.67 · Kallista "Are you following me?" 1.67–2.83 · **gap 2.83–4.55** · Cal "I was hired..." 4.55–6.33 · "...in August." 6.71–7.42 · reaction 7.42–10.

## Supergen (website, Reference to video, 10s): @1 P1, @2 Kallista headshot, @3 Cal headshot, scene audio `m1_porch_10s_v2.mp3`
```
Create a 10-second cinematic live-action romantic comedy scene in 16:9 using the supplied dialogue audio. The scene begins on @1 exactly as shown: the front porch of a white Victorian bed-and-breakfast on a snowy winter morning, a green "Hearthstone Carpentry" pickup truck parked on the left. Keep both faces, the clothes, the porch, the truck and the snow exactly as in @1. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, soft winter morning light, shallow depth of field and organic film grain.
Kallista @2 stands on the porch steps holding a white coffee mug: pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad down-turned brows, straight sleek pale platinum-blonde hair with a center part, a long charcoal wool coat, a black turtleneck and a dark grey chunky knit scarf. Dry, deadpan, suspicious; she has a soft, low, dry voice. Cal @3 kneels in front of the steps, nailing a new pine tread board flat into the gap where a step is missing, a hammer in his hand: tousled brown hair, light stubble, warm hazel eyes, a tan canvas work jacket with a sherpa collar over a red-and-black flannel, a leather tool belt. Sweet, a little sheepish, quick to grin; he has a warm, boyish voice with a slight rasp.
Only the character named for each line speaks it; when Kallista speaks only Kallista's lips move, and when Cal speaks only Cal's lips move. Use only clean hard cuts between shots; never zoom or swing the camera. Nobody looks into the camera.
0–1.7 seconds: Kallista stops on the steps, coffee in both hands, and stares down at Cal. Cal is busy lining up the new tread board in the gap in the step and tapping it with his hammer.
1.7–2.8 seconds: Kallista says, dry and suspicious: "Are you following me?"
2.8–4.5 seconds: silence. Cal stops hammering mid-swing, freezes, and slowly looks up at Kallista.
4.5–7.4 seconds: Cal holds up the hammer as evidence and says, sheepish with a small grin: "I was hired... in August."
7.4–10 seconds: silence. Kallista narrows her eyes and takes a slow sip of coffee. Cal goes back to nailing the new tread into the step, still grinning to himself.
Throughout: keep the supplied audio unchanged; add no music or voices. No other people, no subtitles, no watermarks.
```

## Omni Flash (Ingredients, simplified, **10s**; attach P1 and both headshots)
```
A 10-second cinematic live-action romantic comedy scene in 16:9 on the front porch of a white Victorian bed-and-breakfast on a snowy winter morning, wreaths on the doors, garland on the porch rail, a green "Hearthstone Carpentry" pickup truck parked by the house.

Kallista stands on the porch steps holding a white coffee mug: pale skin, a longer face with defined cheekbones, large pale blue-grey eyes, sad down-turned brows, straight sleek pale platinum-blonde hair with a center part, a long charcoal wool coat, a black turtleneck and a dark grey chunky knit scarf. Dry, deadpan, suspicious; a soft, low, dry American voice, a little husky. Cal kneels in front of the steps, nailing a new pine tread board flat into the gap where a step is missing, a hammer in his hand: tousled brown hair, light stubble, warm hazel eyes, a tan canvas work jacket with a sherpa collar over a red-and-black flannel, a leather tool belt. Sweet, a little sheepish, quick to grin; a warm, boyish American voice with a slight rasp.

Kallista stops on the steps and stares down at Cal, who is busy nailing the new tread into the step. Kallista says, dry and suspicious: "Are you following me?" Cal stops mid-swing, freezes, and slowly looks up at Kallista. After a beat, Cal holds up the hammer as evidence and says, sheepish with a small grin: "I was hired... in August." Kallista narrows her eyes and takes a slow sip of coffee; Cal goes back to nailing the new tread into the step, still grinning.

Only the character named for each line speaks it. Nobody looks into the camera. Keep both faces and the porch consistent in every shot. Sound: a hammer tapping wood, a soft winter breeze, distant birds. No music, no subtitles, no text, no watermark, no extra people.
```

## Fix after the Omni Flash test (`Woman_and_man_on_porch`, 15s)
The P1 board leans diagonally against the railing, so he hammers an impractical plank. **Fix:** a Nano Banana edit of P1 (the second step is missing its tread; Cal lays a new pine tread flat across the gap, holding it with his left hand). Both prompts above now say "nailing a new pine tread board flat into the gap where a step is missing". Run Omni Flash at 10s.
