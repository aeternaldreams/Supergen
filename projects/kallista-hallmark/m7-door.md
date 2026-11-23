# M7: half-open door (MCP Image to video, 5s, silent)

## Keyframe (member makes it in Nano Banana / Flow)
**References to attach:** Kallista identity shots · Cal identity shots · `keyframes/holiday-reservations/title_bnb_night.jpg` (same house, yard and porch lights at night) · `m1_porch_P1.png` (porch architecture: rail, steps, door)

**Prompt:**
> A cinematic night interior shot from inside the dark front hallway of a Victorian bed-and-breakfast, looking toward the front door, which stands half open. Kallista, the woman from the Kallista references, stands just inside the doorway with one hand resting on the edge of the door, her body angled toward the gap and her face turned in three-quarter profile toward the camera side as she looks out through the opening. Same face: a longer face with defined cheekbones, large pale blue-grey eyes, sad slightly down-turned brows, straight sleek pale platinum-blonde hair (never golden) with a center part, worn down just past the shoulders. She still wears her charcoal wool coat and dark grey chunky knit scarf. Her expression is soft and unguarded: the very beginning of a smile she hasn't decided to allow. Warm golden porch light spills through the gap across her face and onto the hallway floorboards; the hallway behind her is dim, with only a faint warm lamp glow and a hint of a garland on the banister. Through the gap in the door: the snowy front path and yard at night, softly falling snow, the porch rail with green garland, and further down the path, small in the frame, Cal, the man from the Cal references, in a brown canvas work jacket over his red-and-black buffalo-check flannel, walking away but glancing back over his shoulder toward the door. Cal is in soft focus; Kallista's face is sharp. Shot on ARRI Alexa Mini LF with a 50mm Cooke S4 lens at T2, photorealistic film still, warm practical light against cool blue night, gentle highlight bloom, creamy shallow depth of field, light 35mm film grain, natural skin texture. 16:9. No text, no logos, no watermark.

**Checklist for the frame:**
- Her face is large enough (about a quarter of the frame height or more), lit by the porch light, in three-quarter view, **not** her back to the camera.
- The door is clearly *half* open: we can see Cal through the gap, but the door isn't wide open.
- Cal is small and soft. His face doesn't need to be perfect.
- Platinum hair, not golden. Coat and scarf match M6.

## Motion prompt (I run it via MCP once the frame exists; confirm the cost first)
Drafted once the frame is in, so it matches what's actually in the picture. Plan: locked camera; she begins to ease the door closed, then stops with it half open; far down the path Cal looks back; her almost-smile. Silent; the sound (night wind, a distant wind chime) is added in post.

## Chosen keyframe: `keyframes/holiday-reservations/m7_door_D1.jpg` (Nano Banana Pro)
Platinum hair, soft almost-smile, door half open, stairs, lamp and garland. Cal has stopped on the path and is looking back (larger than planned). The motion is rewritten around that: a shared look, then he goes.

## Motion prompt (Image to video, 5s, 480p: 30 XCE)
> A 5-second cinematic live-action romantic comedy shot in 16:9, continuing directly from the supplied first frame. One continuous shot, locked camera, no cuts, no camera movement. Night, inside the dim front hallway of the bed-and-breakfast. Kallista, the platinum-blonde woman in the charcoal coat and grey knit scarf, stands at the half-open front door with her hand on its edge, watching Cal through the gap. Outside in the softly falling snow, Cal, the man in the tan work jacket, holds her gaze for a moment, gives a small shy nod, then turns and walks slowly away down the snowy path, glancing back once over his shoulder. Kallista's fingers tighten on the door's edge as if she is about to close it, but she hesitates and doesn't; the door stays half open. Her small closed-lip almost-smile slowly deepens, just slightly, and she lowers her eyes for a second, then looks back out after him. Subtle, restrained performance. No one speaks. Keep both faces, the door, the hallway, the lamp and the lighting exactly as in the first frame. Snow keeps falling gently outside.

## Render v1: `cf2092546f94` (5s at 480p, ~36 XCE; output 6.58s, no audio)
- 0–2s: face visible; her almost-smile, then she lowers her eyes (as prompted). Cal nods and turns.
- ~2.5s on: she turns into pure profile toward the gap, watching him go; a slight smile in profile at the end. Cal walks away down the path. Locked camera held; the door stays put.
- Mix (`m7_door_v1.mp4`, scratchpad): `roomtone_porch_winter.mp3` −6 dB + `sfx_windchime_night_v3.mp3` (v3) −10 dB.
