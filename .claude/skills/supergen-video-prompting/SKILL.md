---
name: supergen-video-prompting
description: Playbook for building supergen.video scenes (Super Animation and Super Live Action) — reference-image setup, dialogue pacing, prompt structure, direction mode and credit costs. Use whenever planning, prompting or generating Supergen pictures or videos, through the Supergen MCP tools or for pasting into the supergen.video website.
---

# Supergen video prompting

Rules learned from beta testing on supergen.video. Apply them to every scene,
whether it is made through the Supergen MCP tools or written up for the
member to paste into the website.

## 0. Before spending credits

- Call `my_account` (free) to get the balance and current prices.
- Tell the member the cost and get a yes before `make_picture` or any video.
- Price note: the MCP reports Normal (480p) at 6 XCE/s (5s = 30 XCE), but the
  website showed 5s Normal at 36 XCE. Quote the higher figure until this is
  confirmed.
- Videos take a few minutes: poll with `check_video`. Watch links last
  30 minutes; videos stay in the member's library.
- If a picture is slow, resume it with `picture_job` — never start a new one.

## 1. Reference images and slot mechanics

- **Never put a multi-panel grid in the first frame.** The first frame locks
  the literal pixels of frame 0, so a 2x2 grid plays as split-screen for the
  first 4–5 seconds.
- Instead: make a 2x2 sheet in the target shape (16:9 or 9:16) for visual
  consistency, then split it into 4 full-bleed images:
  - @1 → first frame (Image to Video / `picture`)
  - @2, @3, @4 → extra reference images (+ More Images)
- **Physical continuity:** keep prop states identical across panels (e.g. the
  sleeping bag sealed at the bottom in panel 3 so it matches panel 4).
- **Spatial continuity:** isolate backgrounds with opposing eyelines
  (180-degree rule) so the model doesn't paste Character A into the
  background behind Character B.
- For character consistency without reference slots, start from a
  `character_sheet`, `cast_sheet` or `cast_and_place` picture.

## 2. Dialogue and pacing

There is no separate dialogue box. Spoken lines go inside the scene
description in quotation marks, wrapped in physical and emotive cues:

> Walt leans in, voice barely a whisper: "You heard it too... didn't you?"

- **Max 4 spoken lines per clip.** A 5th line makes the audio collide lines
  early or invent dialogue.
- **2.5 words per second.** A 4-second shot gets under 10–12 words.
- Use ellipses (...) inside the quoted line to force slow, dramatic pauses
  instead of rushed delivery.
- **Speech queue quirk:** if shot 4 (12–16s) is silent and shot 5 (16–20s)
  has the 4th line, the line fires early at 12s and the silent shot is pushed
  to 16s. Keep the final reaction shot non-verbal, or swap the two segments
  in post.

## 3. Prompt structure

- Write multi-shot scenes as timestamp blocks (e.g. 0–4s, 4–8s, ...).
- **No negative character placement.** "X is absent from the opening shot"
  puts X into frame 1. Only mention a character inside the block where they
  appear.
- **Physical verbs over emotion adjectives.** In multi-character action cuts,
  secondary characters sit idle unless given a verb ("throws hands up to
  block the impact").
- **5-second standalone pickups** for intense facial acting and vocal texture
  (e.g. a slow push-in whisper): 1 image + 1 spoken line gets the model's
  full attention.

## 4. Direction mode

| Mode | Behaviour | Use for |
|---|---|---|
| Auto (default) | One steady move per shot, picked for the scene | Most scenes, dialogue, single-character shots |
| Super | Wild camera, more cuts and angles | Chases, fights, sudden scares, intense moments |
| Off | Camera holds still | CCTV / found-footage looks, static wides holding on something unsettling |

If the MCP tools don't expose direction yet, describe the camera in the scene
text instead ("static shot", "slow push-in") — it is a request, not a
guaranteed setting.

## 5. MCP tools vs website

Check the Supergen tool schemas at the start of a session; the owner is
adding the website's missing options to the MCP.

| Website | MCP parameter |
|---|---|
| Image to Video | `picture` (picture_id or https link) / `picture_file` |
| Describe the scene and dialogue | `description` |
| 5s / 10s / 15s / 20s | `seconds` |
| Normal | `quality: "480p"` (made at 576p) |
| HD / Upscale to 1080p | `quality: "720p"` (made at Normal, upscaled to 1080p) |
| 16:9 etc. | `shape` (videos also allow 21:9) |
| Direction | not yet in MCP |
| + More Images (reference) | not yet in MCP — one picture per video |
| + Add Scene Audio | not yet in MCP |

Other tools: `make_picture` (`kind`: plain, character_sheet, cast_sheet,
cast_and_place, background, storyboard; `look`: auto, photo, anime),
`make_live_action_video` (plans the scene ~1 min first, default 10s), and
`post_to_community` (only when the member asks).

Until reference slots arrive in the MCP: build multi-shot scenes as pictures +
prompt blocks for the member to paste into the website, and run 5-second
single-image pickups directly through the MCP.
