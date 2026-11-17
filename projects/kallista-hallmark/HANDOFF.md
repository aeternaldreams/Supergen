# HOLIDAY RESERVATIONS: handoff brief

## 1. Premise
- **Format:** spoof Hallmark-style romcom trailer, about 1:30–2:00. Reads as genuine, with subtle "if you know, you know" jabs.
- **No narrator.** The story is told through dialogue, Claude title cards and an acoustic song bed (added later).
- **Story:** Kallista Vane, a gloomy dark dream-pop singer and Ryan's AI avatar, is on a winter girls' trip at a small-town bed and breakfast. She meets Cal, a carpenter, when her bra sticks to his back at the laundromat. His crew is fixing up the B&B, so they keep running into each other. She's guarded ("What's the worst that could happen?" / "Uh... you could die?").
- **Title:** HOLIDAY RESERVATIONS. Tagline: "She made a reservation. She has several."
- **Network card:** "DPC: the Deep Prompt Channel."
- **Cold open:** on the B&B couch, Becca guesses where Kallista met someone, and each guess is a white-flash fake meet-cute:
  - rink (Chase)
  - café (man-bun barista, "CALLISTUH")
  - music store (Adrian Vale and the bossa nova)

  Then the real meet-cute at the laundromat.
- **Full script:** `holiday-reservations-script.md`, including the montage, cast roll and Adrian stinger.

## 2. Cast (identity blocks in `supergen-character-blocks.md`)
- **Kallista Vane:** pronounced kah-LEE-stah.
  - **Look:** pale skin; a longer face with defined cheekbones; large pale blue-grey eyes; sad, slightly down-turned brows; straight sleek pale platinum hair (never golden) with a center part.
  - **Manner:** reserved and deadpan. Never bubbly or loud.
- **Becca Hartley:** best friend and hopeless romantic.
  - **Look:** long wavy auburn hair, freckles, green-brown eyes, burgundy cable-knit.
  - **Manner:** warm and teasing, with small gestures. Never theatrical.
- **Milly Alwood:** subtle Tilly Norwood jab.
  - **Look:** sleek chestnut bob, too-perfect.
  - **Manner:** flat, unblinking, reacts a beat late (the "Ha. Ha." late laugh).
- **Cal Whitaker:** carpenter at Hearthstone Carpentry; sweet and awkward.
- **Marcus Bell** (was Dusty): Cal's coworker. Light-skinned Black man, handsome, opinions about everything.
- **Adrian Vale:** cameo; Ryan's other avatar.
  - **Look:** spiky black hair, smoky eyeliner, cross earrings.
  - **Outfit (locked):** black double-breasted greatcoat over a black turtleneck, no scarf.
- **One-offs (no reference picture needed):** Chase the hockey player, the man-bun barista.

## 3. Wardrobe
- **Couch (now):** Kallista in an oversized charcoal knit and leggings; Becca in burgundy.
- **Flashes and laundromat:** Kallista in a black ribbed mock-neck plus a charcoal wool coat and dark grey chunky scarf.
- **No slip dresses.**

## 4. Workflow and constraints (details in `.claude/skills/supergen-video-prompting/SKILL.md`)
- **Start frames:** made in Nano Banana or GPT. Supergen Live Action renders at 576p Normal.
  - **Couch start frame:** `pic_1619a74c7520` (the corrected two-shot).
- **Frame 0 sets identity.** Fix the face in the start frame first; front-facing, close faces hold best.
- **Every prompt includes the full identity block,** plus "keep her face exactly as in the first frame."
- **Dialogue:** made in ElevenLabs v3 Text to Dialogue, padded to 15s with room tone, used as scene audio via a raw GitHub link (`voices/holiday-reservations/`, public repo).
  - Write the prompt with measured timestamps.
  - Say "if you cut, always cut to the woman who is speaking."
  - Tie each voice to a character ("softer, lower" / "brighter, higher").
- **No style seeds.** Max 4 lines per clip. One tiny action per 5s clip; use only about 2–3s of it.
- **Supergen invents chatter after the scripted action.** Trim before it and mute.
- **Avoid in prompts:** "static", "spark", "crackle", "flash", "bright". The white flashes are added in the edit.
- **Nano Banana:** has no context, so describe camera position and the physical scene literally. The first attached image sets the layout. Never use shorthand tags like "trailer look". Use the full camera line instead (ARRI Alexa Mini LF, 35mm Cooke S4 at T2...).
- **"Failed" jobs:** if a job reports failed, check the library before retrying; one "failed" job still finished.
- **Editing style:** white flashes 3 frames; J/L-cuts between couch and flashes. If lip-sync fails, play the line over a reaction shot.
- **Shimmer and upscale:** small faces shimmer. Topaz Starlight Precise 2.6 helps partly. A developer report is at https://claude.ai/artifact/TmJvhfTsRAfi5NwhepRfxC.
- **Not yet:** score and final sound design come later (fire/room tone bed, flash whooshes, café ambience).

## 5. Done (Supergen library IDs)
- **Couch clip 1:** `e283454221e7`. "So... something weird happened today" through "Hockey player." Keeper.
- **Rink flash:** `2878e67cdf3e`. Trim 0–3.7s, ending after "Hey..." (he says "think, then move" after that).
- **Couch clip 2:** `a23f07fcb321`. Head shake, coffee-shop line, "Nobody does that.", "Ooh, the music store! Some broody musician."
  - Becca isn't lip-synced on the music-store line, so it plays over Kallista's reaction shot (12.2–15s).
- **Barista:** `aaebefa67da6`. Use 0–1.9s (the wink).
- **Kallista café stare:** `79e0726cbb61`. Use 0–2.0s (the blink); her lips part after 2.4s.
- **Rough cut v3** (couch 2 + café flash, 14.5s) was sent in chat. Download it, since session scratch files don't persist.
- **Credits:** about 186 XCE left.

## 6. Next step
**Adrian music store flash** (beat in the script):
- Kallista at the PSR-SX920 in the keyboard department.
- Adrian leans in on his elbow: "You play? ...Perhaps we could make something... beautifully dark—"
- His elbow hits the keyboard's start button and a cheesy bossa nova blasts. He panics, jabbing buttons; it gets worse, and a "WOO!" fires. Kallista just watches.
- Back to the couch: "He was perfect... until the bossa nova."

**Plan:**
- **Start frame:** Nano Banana, music store set, front-facing faces. The set prompt and the F5 prompt are in `nano-banana-keyframes.md`.
- **Adrian's line:** voice it in ElevenLabs (British, low, velvety).
- **Bossa nova and "WOO!":** add in the edit, not generated.
- **Then:** the couch line "He was perfect... until the bossa nova." / Milly's "Statistically, most people meet at work." / the laundromat.
