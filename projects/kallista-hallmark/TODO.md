# Holiday Reservations: to-do list

## Locked
- [x] Cold open (v9)
- [x] Montage M1–M3
- [x] Finale **v8** (cast roll → title → tune-in → stinger), with the music, chime and timing in `music-score-plan.md`

## Remaining clips: easiest → hardest
- [ ] 0. Text cards: "She came for a quiet getaway…" / "…not a thaw." (no render, no credits; I build them in code)
- [ ] 1. **M7 half-open door** (MCP, 5s, silent): one face, Cal tiny in the distance. Needs the member's keyframe; I run it here (confirm cost first).
- [ ] 2. **M5 town-square piano** (10s): 2 people, 2 lines. Safest as single-speaker pickups (Cal line, then Kallista line), with the piano notes added in post.
- [ ] 3. **M6 icy sidewalk** (15s): 2 people, 4 lines and a laugh, plus a slip-and-catch (body contact and physics). Split it: catch shot (no lines), then single-speaker pickups.
- [ ] 4. **M4 cocoa break** (10s): five faces, a group laugh, comic timing. Wide establishing shot, then singles (Marcus line, Milly's "Ha. Ha."); expect face passes.
- [ ] Omni Flash guide: add the new scenes

## Music
- [ ] Montage score (separate from the finale song). Plan a clean join into the finale: end on a hard stop or held chord, then smash-cut to the sleigh bells. If it's in C / ~100 BPM, a seamless transition is possible.
- [ ] Cut the cast roll on the beat of the finale song (optional polish)

## Assembly
- [ ] Full trailer assembly (cold open → montage → cards → finale v8)

## Finishing / post (in this order)
1. [ ] **Upscale** all footage first (planned elsewhere)
2. [ ] **Re-render all text at final resolution** (name cards, title, tune-in): from `cards.py` and the name-card overlays, composited over the upscaled footage
3. [ ] **Light unifying grade:** warm Marcus's cast shot to sit with the others. Optional gentle glow on practical lights, slightly lifted warm blacks. Leave the stinger cold and dark.
4. [ ] **Fine 35mm grain** over the whole trailer (lighter on the cards). Watch for banding on the tune-in background and the night title.
5. [ ] **Dialogue placement pass** (not muffling):
   - [ ] First, a before/after test on one scene (couch 3 or the laundromat) for approval
   - [ ] Every line: high-pass ~80–100 Hz, gentle de-ess
   - [ ] Interiors: subtle short room reverb sized to the space
   - [ ] Snowy exteriors: nearly dry, slight high-end softening for distance
   - [ ] Wide shots: a little less low end and a touch more room than close-ups
   - [ ] Keep Adrian's stinger line and Marcus dry and close
   - [ ] Judge each scene by ear (some Supergen renders already processed the audio)
6. [ ] **Audio master** on the full trailer: gentle compression and a limiter at −1 dBTP, ~−14 LUFS for online delivery; keep the stinger's quiet beat
7. [ ] Final export: yuv420p, High profile, CFR 24, `+faststart`
