---
name: supergen-video-prompting
description: Playbook for building supergen.video scenes (Super Animation and Super Live Action) — reference-image setup, dialogue pacing, prompt templates, styles (Super Seeds), direction mode and credit costs. Use whenever planning, prompting or generating Supergen pictures or videos, through the Supergen MCP tools or for pasting into the supergen.video website.
---

# Supergen video prompting

Rules learned from beta testing on supergen.video, plus prompt templates
taken from the member's own past videos. Apply them to every scene, whether
it is made through the Supergen MCP tools or written up for the member to
paste into the website.

## 0. Session start and credits

- Check the Supergen tool schemas: the owner is adding the website's missing
  options to the MCP, so section 6 may be out of date.
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
  right box." Untested idea: passing a hand-made sheet as `picture` with this
  note appended may reproduce multi-reference through the MCP — test with a
  cheap 5s 480p clip before relying on it.
- `reuse_video` keeps a past video's stitched sheet, so it is the reliable
  way to reuse a multi-reference setup through the MCP.
- **Physical continuity:** keep prop states identical across panels (e.g. the
  sleeping bag sealed at the bottom in panel 3 so it matches panel 4).
- **Spatial continuity:** isolate backgrounds with opposing eyelines
  (180-degree rule) so the model doesn't paste Character A into the
  background behind Character B.
- For character designs, start from a `character_sheet`, `cast_sheet` or
  `cast_and_place` picture.

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

Where `direction` isn't available, describe the camera in the scene text
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
| Direction | `direction` — `reuse_video` only |
| Style / Super Seed | `seed` — `reuse_video` only |
| + More Images (reference) | not in MCP — one picture per new video (see section 1) |
| + Add Scene Audio | not in MCP — `reuse_video` can keep a past video's audio (`keep_audio`) |

Other tools: `make_picture` (`kind`: plain, character_sheet, cast_sheet,
cast_and_place, background, storyboard; `look`: auto, photo, anime),
`make_live_action_video` (plans the scene ~1 min first, default 10s),
`reuse_video` (same picture, words, voices, audio and settings with any
changed; `keep_voices`, `keep_audio`), and `post_to_community` (only when
the member asks).

Until reference slots arrive in the MCP: build multi-shot scenes as pictures +
prompt blocks for the member to paste into the website, use `reuse_video` to
retake past multi-reference scenes, and run 5-second single-image pickups
directly through the MCP.
