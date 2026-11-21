# Finale cards (concept)
Fonts (OFL, from google/fonts): Great Vibes (script), Cinzel (caps), Playfair Display (+ Italic). Palette: cream #FAF4E8, gold #E2C076, berry red #962828, evergreen #0E201C.
- **Main title:** "Holiday" script in gold over "RESERVATIONS" caps in cream, gold rule, tagline in Playfair italic. Motion: snow falling, gold shimmer sweep across "Holiday", slow push-in, a service-bell "ding" on the reveal.
- **Tune-in "reservation card":** a cream guest-reservation card on evergreen bokeh: "Check-in: Saturday, December 12 · 8/7c · DPC". Motion: the card slides/settles in, then a red CONFIRMED rubber stamp slams down with a thunk and a tiny camera shake.
- Fully original (DPC network); no Hallmark marks.

**Locked:** "Holiday" in **Playball** (gold) over "RESERVATIONS" in Cinzel (cream). Tagline: **"Some reservations are meant to be cancelled."** (Playfair Display Italic, 50 px at 1080p). The tune-in card uses the same fonts.
Title background: a B&B exterior at dusk (prompt in chat / below).
```
An empty white Victorian bed-and-breakfast at blue-hour dusk in winter, seen from across a snowy front yard at standing height, wide shot. The wraparound porch glows with warm lights; every window is lit warm amber from inside; green wreaths with red bows on the doors and garland along the porch rail; a small decorated Christmas tree twinkles in the front window. Fresh snow blankets the yard, roof and porch railings, and soft snow is gently falling. The deep blue sky fades to a faint pink glow at the horizon. The house sits in the lower two-thirds of the frame, slightly soft, with generous dark-blue sky and open snowy space in the upper-middle of the frame, where title text will go. No people, no vehicles. Shot on ARRI Alexa Mini LF with a 35mm Cooke S4 lens at T2, photorealistic film still, warm practical lights against a cool blue dusk, gentle highlight bloom, creamy shallow depth of field, light 35mm film grain. No text, no logos, no watermark.
```

## Built (finale v1, `finale_v1.mp4`, 37.2s, scratchpad)
- `title_card_sfx.mp4` (4.6s): B&B night frame (`keyframes/.../title_bnb_night.jpg`), centre darkened, slow push-in 1.08→1.02, 260 snowflakes, fade-ins Holiday 0.35s / RESERVATIONS 0.75s / rule + tagline 1.6s, gold glint across "Holiday" 1.3–2.3s, fade out from 4.15s. `sfx_bell_v3.mp3` (ElevenLabs SFX v3) at 0.45s, −6 dB.
- `tunein_card_sfx.mp4` (4.6s): evergreen bokeh + snow; the card slides up 0–0.8s; the CONFIRMED stamp slams at 1.6s (scale 1.7→1, shake 0.18s), top-right corner; `sfx_stamp_v3.mp3` (v3, hit at 0.35s into the file) placed at 1.25s, −3 dB.
- Order: Kallista 3.1 → Cal 4.6 → Becca 4.1 → Marcus 4.2 → Milly 5.6 → title 4.6 → tune-in 4.6 → black 0.6 → stinger 5.7.
- Generator script: `cards.py` (copy in this folder).
