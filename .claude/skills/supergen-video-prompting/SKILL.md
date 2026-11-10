---
name: supergen-video-prompting
description: Playbook for building supergen.video scenes (Super Animation and Super Live Action) — reference-image setup, character sheets, character voices and own audio, dialogue pacing, prompt templates, styles (Super Seeds), direction mode and credit costs. Use whenever planning, prompting or generating Supergen pictures or videos, through the Supergen MCP tools or for pasting into the supergen.video website.
---

# Supergen video prompting

Rules learned from beta testing on supergen.video, plus prompt templates
taken from the member's own past videos. Apply them to every scene, whether
it is made through the Supergen MCP tools or written up for the member to
paste into the website.

## 0. Session start and credits

- Check the Supergen tool schemas: the owner is adding the website's missing
  options to the MCP, so section 6 may be out of date (last checked 2026-11-09).
- `my_account` (free): balance and prices. `my_videos` (free): past prompts
  and settings — read them for continuity before writing a sequel or retake.
- Tell the member the cost and get a yes before `make_picture`,
  `make_*_video` or `reuse_video`.
- Price note: the MCP reports Normal (480p) at 6 XCE/s (5s = 30 XCE), but the
  website showed 5s Normal at 36 XCE. Quote the higher figure until this is
  confirmed.
- Videos take a few minutes: poll with `check_video`. Watch links last
  30 minutes; videos stay in the member's library.
- If a picture is slow, resume it with `picture_job` — never start a new one.
- **The id `make_*_video` returns (`vid_...`) is not the library id.** If
  `check_video` says it "can't find" the video (this happens after the MCP
  reconnects), get the 12-character id from `my_videos` and call
  `check_video` with that. Watch links are direct MP4s. From a cloud session
  you can `curl` them and pull frames with ffmpeg to review the beats (use
  `silencedetect` for dialogue timing).
- **The content check is not consistent.** The same picture and words failed
  once ("didn't pass our content check... outfit or a moment that reads as
  too intimate", no charge) and then passed on an identical retry. A failed
  check costs nothing, so retry once before rewriting. Shirtless characters
  and innuendo (fertility sample, shoulder-length glove, "buy me dinner
  first") did pass.
- A Super Seed passed through the MCP shows as `style: null` in
  `my_videos`; it's unclear whether it was applied.

## 1. Reference images and slot mechanics

- **Never put a multi-panel grid in FIRST FRAME by hand.** The first frame
  locks the literal pixels of frame 0, so a 2x2 grid plays as split-screen
  for the first 4–5 seconds.
- Instead: make a 2x2 sheet in the target shape (16:9 or 9:16) for visual
  consistency, then split it into 4 full-bleed images:
  - @1 → FIRST FRAME (Image to Video)
  - @2, @3, @4 → + MORE IMAGES (reference)
- **How Supergen handles extra images:** the website stitches the first
  frame and reference images into one "reference sheet" picture (so
  `my_videos` reports `pictures: 1`) and appends this note to the prompt:
  > (Reference sheet: the starting picture is 4 separate reference pictures
  > laid out side by side, each in its own box. @1 (image 1) = the top-left
  > box. @2 (image 2) = the top-right box. @3 (image 3) = the bottom-left box.
  > @4 (image 4) = the bottom-right box. Each box is its own reference - a
  > character, a place or an object. Bring them together into ONE scene in
  > one world; the boxes, borders and the grid are never shown in the video.)

  For 2 images it reads "@1 (image 1) = the left box. @2 (image 2) = the
  right box."
- **Hand-made sheets don't work.** Tested: passing a 2x2 sheet as the first
  frame renders the grid for several seconds and animates each cell. Always
  use individual full-bleed keyframes — they work well.
- **⚠️ MCP `more_pictures` bug (tested Nov 2026):** the MCP stitches the
  first frame and `more_pictures` into one 2x2 reference sheet, the same as
  the website, but then **uses the sheet itself as the opening frame**. The
  video opens on the 2x2 grid for about 2 seconds, zooms blurrily into one
  cell, and the opening line plays over the grid. Until Supergen fixes this,
  make multi-reference scenes on the website (+ More Images), or use a
  single `picture` with no `more_pictures`. `my_videos` also showed
  `voices: []` for a render whose result said `voices: 1`.
- **Reference slots in the MCP:** both video tools take `picture` (@1, the
  first frame) plus `more_pictures` (up to 3 more: picture_ids, `pic_` ids or
  https links) for @2–@4. Use these for new multi-reference scenes.
  `reuse_video` still keeps a past video's stitched sheet for retakes.
- **Getting keyframes to the MCP:** `picture` and `more_pictures` take a
  `make_picture` id (`img_...`), an uploaded id (`pic_...`) or an https link.
  - Preferred (private): `upload_pictures` (free) returns one-time upload
    addresses (valid 20 minutes). **Tested and working from Claude Code:**
    POST the raw image bytes, not a multipart form:
    `curl -sS -X POST -H "Content-Type: image/jpeg" --data-binary @frame.jpg "<url>"`
    → `{"picture_id": "pic_...", ...}`. Gotchas:
    - The cloud session's network must allow `api.supergen.video`. Use
      the personal "Supergen" environment, which allows it.
    - A multipart (`-F file=@...`) POST fails with "isn't a picture" AND
      uses up the address. Call `upload_pictures` again for a new one.
    - `my_pictures` lists uploaded `pic_` ids.
  - Fallback (public): commit the file to `keyframes/<project>/` in this
    public repo, push, and pass
    `https://raw.githubusercontent.com/aeternaldreams/Supergen/main/keyframes/<project>/<file>`.
    Anything committed here is publicly visible.
- **Letterbox bars:** Gemini/Nano Banana edits often add thin black bars
  (about 12–17px) top and bottom, even when told not to. Crop them locally
  with PIL (find rows whose mean brightness is near 0, then crop to 16:9)
  instead of re-editing. A crop costs nothing and can't change faces.
- **Plan the first frame's hands around the script:** check what each hand
  must do (hold a prop, pick something up, swap gloves) and pose the frame
  so the first action is free. Don't add props like pens that the scene
  doesn't need; the model may drop, duplicate or morph them.
- **Physical continuity:** keep prop states identical across panels (e.g. the
  sleeping bag sealed at the bottom in panel 3 so it matches panel 4).
- **Spatial continuity:** isolate backgrounds with opposing eyelines
  (180-degree rule) so the model doesn't paste Character A into the
  background behind Character B.
- **Character and set design with `make_picture`** (5 XCE each). `kind`:
  - `character_sheet`: design sheet for one character
  - `cast_sheet`: several characters together
  - `cast_and_place`: the cast plus their setting
  - `background`: a place with no people (good for @2–@4 location refs)
  - `storyboard`: a shot-by-shot board for planning
  - `plain` (default): one picture, e.g. a clean full-bleed keyframe

  `look`: auto, photo (live action) or anime. `shape`: match the video.
  Sheets are multi-panel, so never use one as the first frame (see above).
  Make the sheet first, then a clean `plain` keyframe of the same character
  for @1. Passing the sheet in `more_pictures` as an identity reference
  should work but is *untested*.

## 1b. Voices and own audio (both video tools)

- **`voices`**: up to 3 entries `{name, audio}`. `audio` is an https link to
  2–20 seconds of that character talking. Each character speaks in the voice
  from their sample.
  - `name` must match the character's name as written in `description`
    (e.g. `Walt` → "Walt (Speaker 1) whispers: ...").
  - Samples attached in a chat go in `voice_file_1..3`, in the same order as
    `voices`.
  - From Claude Code, a sample needs a link: commit it to
    `voices/<project>/` in this public repo and pass the raw GitHub link.
    Only use voices the member is happy to make public and has the right to
    use.
- **`audio` / `audio_file`**: the member's own track (MP3, WAV, M4A, AAC,
  OGG, FLAC or MP4). The video follows it (music, voices). Up to 20 seconds.
  **Own audio overrides `voices`.** Don't send both.
- `reuse_video` can keep a past video's voices and audio (`keep_voices`,
  `keep_audio`, both default true).
- **Tested (Nov 2026):** a 5.6s clip of a character's lines, cut from an
  earlier Supergen render, was accepted (`voices: 1` in the result). The
  render took about 17 minutes, against about 5–10 without a voice sample,
  so expect longer waits. Also say the accent in the text ("deep, raspy
  American accent"): without it, one take gave the character a British
  accent.
- **Props that appear later:** keep them out of sight in a closed container
  that is in the frame (a cart drawer), then write "pulls open its top
  drawer and takes out X". Tested: the poncho and goggles came out of the
  drawer cleanly, with no morphing. A prop pulled "from his coat pocket" or
  from off-frame gets made up or morphs.
- **Silent beats turn into gibberish (tested Nov 2026).** Both renders that
  used a voice sample filled their dialogue-free stretch with fast,
  unintelligible pseudo-English: 8s of prop business in one, and a 3s stare
  in the other, even though that one described the beat as "only the hum of
  the fluorescent lights". The two renders without a voice sample held a
  3.4s silence cleanly. **Untested idea:** voice-sample mode makes the audio
  model fill gaps. Until that's confirmed:
  - keep dialogue-free stretches to about 1.5–2s;
  - or fill them with a specific, non-verbal sound made by a character in
    the frame (a snort, a sigh, a cough);
  - and test the same prompt without `voices` to compare.
- **A line must be spoken by a character in the frame.** When the last shot
  showed only the doctor, Gary's line was lip-synced onto the doctor. Make
  sure whoever speaks is visible in that shot.

## 2. Dialogue and pacing

There is no separate dialogue box. Spoken lines go inside the scene
description in quotation marks, wrapped in physical and emotive cues and
tagged with the speaker number:

> Walt (Speaker 1) leans slowly toward the lens and speaks in a slow, raspy,
> ominous whisper: "The forest spirit... turns a boy... into a giant...
> green... worm."

- **Max 4 spoken lines per clip.** A 5th line makes the audio collide lines
  early or invent dialogue.
- **2.5 words per second.** A 4-second shot gets under 10–12 words.
- Use ellipses (...) inside the quoted line to force slow, dramatic pauses.
- An em dash at the end of a line ("that's the dumbest—") makes a clean
  interruption.
- **Speech queue quirk:** if shot 4 (12–16s) is silent and shot 5 (16–20s)
  has the 4th line, the line fires early at 12s and the silent shot is pushed
  to 16s. Keep the final reaction shot non-verbal, or swap the two segments
  in post.
- **Confirmed fix (Nov 2026):** give the silent beat its own timestamp
  block that says "Complete silence, no one speaks", and tie the last line
  to a physical cue ("Right after the snap, Gary says..."). In a 20s single
  locked-off shot this held the silence from about 12.4 to 15.8s and the
  last line landed at about 19–20s. Clips come out about 21.5s long.
- Music videos with own audio: "singing in precise synchronization with the
  supplied vocal: '<lyric>'", plus "Keep the original audio unchanged" and
  "no added voices".

## 3. Prompt structure rules

- Write multi-shot scenes as timestamp blocks, one physical camera setup per
  block, joined by "Hard cut to ...". Give exact cut times
  ("AT EXACTLY 5.5 SECONDS: HARD CUT ...").
- **No negative character placement.** "X is absent from the opening shot"
  puts X into frame 1. Only mention a character inside the block where they
  appear.
- **Physical verbs over emotion adjectives.** In multi-character action cuts,
  secondary characters sit idle unless given a verb ("throws hands up to
  block the impact").
- **5-second standalone pickups** for intense facial acting and vocal texture
  (e.g. a slow push-in whisper): 1 image + 1 spoken line gets the model's
  full attention.
- To stop morphing between references: "Animate the scenes naturally; do not
  interpolate or morph between the reference images."
- End with a "Throughout:" or "No ..." line listing what must not happen
  (extra cuts, dissolves, slow motion, extra people, subtitles, watermarks).

- **Mentioning something off-screen brings it on-screen.** "Looking at
  someone off-screen" plus "a poncho rustling off-screen" made a stranger
  in a poncho walk into a 5s close-up. Instead write "X is the only person
  in the shot" and give an eyeline ("eyes fixed slightly downward toward
  the left edge of the frame").
- **Write reactions as face movements, not emotion words.** "Smug half-smile"
  came out as a warm, charmed grin. "One eyebrow lifts high, one corner of
  his mouth curls into a lopsided smirk, mouth stays closed, one slow nod"
  gave exactly the smug button.
- **Assemble the master edit from several takes.** Keep the best take, swap
  in shots from other takes for weak moments (mute their audio and lay
  room tone under them), and render cheap 5s single-picture pickups for
  missing beats. To make a pickup match on the cut, start it from the
  previous shot's last frame: crop it, enhance it in GPT Images ("keep
  everything identical"), and use that as its first picture. ffmpeg handles
  the rest: whip pans (slideleft xfade plus horizontal blur and a filtered
  noise whoosh), slowing a shot down instead of freezing it, and sound
  stings.

- **5s Live Action pickups stay on script for about 2.5s (tested Nov 2026,
  Top Tier Reality, four pickups).** Each came back 6.6s long, and after
  about 2.7s cut to unrelated content: a person on the hood, a second
  driver, even the seed's own example scene (a hunter and a giant beast).
  Plan each pickup around one action that finishes inside 2.5s, and trim
  the rest.
- **Small faces smear.** Normal quality renders at 1024x576; a face about
  60px tall in a wide shot is redrawn badly from frame 0 and doesn't act.
  Put acting in a close-up pickup where the face fills a third of the
  frame, and keep wide shots of that character short.
- **Do camera tricks in the edit.** A snap zoom out from a close-up to a
  wide is two separate clips joined with ffmpeg `zoompan` (4x to 1x over 6
  frames, centred on the face) plus a whoosh. The model never has to
  invent what is outside the close-up.
- **Chase scenes:** state where the pursuers are in every shot ("the yellow
  car leads, the cruisers follow behind"), and prefer cameras looking back
  at the lead car. Avoid "flash", "bright" or "explosive" for sparks (they
  cause full-frame white flashes) and "flies through the air in slow
  motion" (the car hovers). The model ignores engine-sound requests, so
  add engine, screech and a low rumble bed in the mix.

## 4. Prompt templates

These follow the member's proven structure. Fill the <angle brackets>.

### 4a. Multi-shot scene (15–20s)

```
Create a complete <N>-second cinematic <genre> short in <16:9 | 9:16>, beginning directly from the supplied first frame of <character>. Preserve the established faces, clothing, <location>, and <key lighting> across all <n> supplied reference images. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist diffusion filter, <lighting>, soft halation around <light source>, <atmosphere>, shallow depth of field, and organic film grain.

CHARACTERS: <NAME> (Speaker 1, Image @1) is <look, wardrobe, defining trait>. <NAME> (Speaker 2, Image @2) is <...>.

0–4 seconds: Begin on the first frame (@1). <Physical action>. <Name> (Speaker 1) <delivery cue>: "<line, ≤10 words, ellipses for pauses>"
4–8 seconds: Hard cut to <shot type> of <who/where> (@2). <Physical action with verbs for every character>. <Name> (Speaker 2) <delivery cue>: "<line>"
8–12 seconds: Hard cut to <shot> (@3). <...>
12–16 seconds: Hard cut to <shot> (@4). <Action — keep silent shots before the last spoken line in mind (speech queue quirk)>
16–20 seconds: Hard cut back to <shot> (@1). <Reaction / button>. Cut to black.

Sound: <dialogue texture>, shifting at <t> seconds into <sound effects>. Clean hard cuts between physical camera setups. No subtitles or watermarks.
```

### 4b. 5-second pickup (one image, one line)

```
Create a 5-second cinematic <genre> close-up in <shape>, beginning directly from the supplied first frame of <character>. Shot on 35mm Kodak Vision3 500T film with a 1/4 Pro-Mist filter, <lighting>, and organic film grain. 0–5 seconds: <Shot type and angle> of <Name> (Speaker 1) <physical action / camera move>, and speaks in a <delivery>: "<line with ... pauses>" Sound: <delivery> over <ambience>. No subtitles or watermarks.
```

### 4c. Two-shot music video with own audio

```
Create a <N>-second cinematic <shape> music video using the supplied song audio. Exactly TWO shots, with one clean instantaneous HARD CUT at <t> seconds. References define each shot's composition, character identity, wardrobe and setting. Animate the scenes naturally; do not interpolate or morph between the reference images.

0.0–<t> seconds — SHOT 1, match @1: <Action>, singing in precise synchronization with the supplied vocal: "<lyric>". <Camera move>. <Performance notes>. <Background characters with discrete, staggered verbs>.
AT EXACTLY <t> SECONDS: HARD CUT directly to the composition and room in @2.
<t>–<N> seconds — SHOT 2, match @2: <Action>, singing: "<lyric>". <Locked camera / framing>. Hold this shot through the end without a fade.

Throughout: synchronize visible singing to the actual supplied audio, preserving its timing and melody. Preserve <identity details>. Keep the original audio unchanged. No additional cuts, transitions, dissolves, morphing, slow motion, subtitles, added voices or extra people.
```

## 5. Direction mode and styles

### Direction

| Mode | Behaviour | Use for |
|---|---|---|
| auto (default) | One steady move per shot, picked for the scene | Most scenes, dialogue, single-character shots |
| super | Wild camera, more cuts and angles | Chases, fights, sudden scares, intense moments |
| off | Camera holds still | CCTV / found-footage looks, static wides holding on something unsettling |

`direction` is on `make_animation_video` and `reuse_video` only. For Live
Action, or wherever it isn't available, describe the camera in the scene text
("static shot", "slow push-in") — a request, not a guaranteed setting.

### Styles (Super Seeds, from `list_styles`)

A seed sets the room: an anime seed only works for animation, a live seed
only for live action.

| Style | Code | Room | Good for |
|---|---|---|---|
| Readable Sakuga | SEED-FBPG-678X | anime | Fast fights you can follow |
| Living Characters | SEED-T8XP-9G3G | anime | Realistic acting, pauses, attitude |
| Expressive Anime | SEED-CKNT-MSNY | anime | Camera-driven storytelling |
| Realistic Anime | SEED-T537-PB4H | anime | Wide curved lens, street energy |
| Sky Sakuga | SEED-JYNE-7XK2 | anime | Big aerial action |
| Royal Seed | SEED-SQJU-U7PD | live | Real-movie look, hard sunset light, story stays in order |
| Titan Clash | SEED-DKTT-TZRT | live | Small hero vs something enormous |
| Deadpan Comedy | SEED-BR69-7QFZ | live | Two people, rising tension, comic timing |
| Shockwave | SEED-3ZPF-79XZ | live | One move that shakes the room |
| Raw Performance | SEED-TPV5-UB5R | live | One actor, full emotion |
| Golden Hour | SEED-RN4C-SCGK | live | Quiet, warm, real moments |
| Top Tier Reality | SEED-SWXM-Y7GN | live | Camera stays in the danger |
| Raw Merge | SEED-NG6R-6REK | live | Heavy, hard-lit fighting |

Codes may change — re-check `list_styles` if one is refused. Older styles in
the member's history (Mini Story, Keep My Face, The Complete One, Cinematic
Likability, Cinematic Reinvention Reality, Title & Logo, Big Cinematic
Moment) are not in the current list.

Starting points: Walt-style horror-comedy dialogue → Deadpan Comedy or Raw
Performance; 5s whisper pickup → Raw Performance; fight/chase with
direction super → Raw Merge, Top Tier Reality or Readable Sakuga.

## 6. MCP tools vs website

| Website | MCP |
|---|---|
| Image to Video | `picture` (picture_id or https link) / `picture_file` |
| Describe the scene and dialogue | `description` |
| 5s / 10s / 15s / 20s | `seconds` (website history also shows 6s and 25s) |
| Normal | `quality: "480p"` (made at 576p) |
| HD / Upscale to 1080p | `quality: "720p"` (made at Normal, upscaled to 1080p) |
| 16:9 etc. | `shape` (videos also allow 21:9) |
| Direction | `direction`: `make_animation_video` and `reuse_video` (not Live Action) |
| Style / Super Seed | `seed`: all video tools (code or style name) |
| + More Images (reference) | `more_pictures` (up to 3) / `picture_file_2..4` |
| + Add Scene Audio | `audio` (https link) / `audio_file` |
| Character voices | `voices` (up to 3) / `voice_file_1..3` |

Other tools:
- `make_picture`: see section 1. `picture_job` resumes a slow picture.
- `make_live_action_video`: plans the scene for about a minute first.
  Default 10s. `make_animation_video` defaults to 5s.
- `reuse_video`: same picture, words, voices, audio and settings with any of
  them changed (`keep_voices`, `keep_audio`).
- `upload_pictures` and `my_pictures`: the member's own photos (free).
- `my_videos` and `my_account`: history, balance and prices (free).
- `list_styles`: current Super Seeds (free).
- `post_to_community`: only when the member asks.

Multi-shot, multi-reference scenes with voices or audio can now be made
entirely through the MCP; the website is no longer required. Confirm the
cost first.
