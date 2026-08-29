# Cover-Bild Prompt-Vorlage

Dieser Skill generiert **nur das Cover-Bild** neu für jedes Paar. Die anderen 7 Bilder
(`hero_synastry.webp`, `hero_composite.webp`, `hero_love.webp`, `hero_steps.webp`,
`hero_closing.webp`, `hero_strengths.webp`, `hero_triggers.webp`) sind generisch und liegen
im `assets/`-Ordner.

## Cover-Bild API-Call

```
KIMASTERMIND_IMAGES:generate_image(
    model="gpt-image-2",
    aspect_ratio="21:9",
    quality="medium",
    prompt=<siehe unten>
)
```

**Parameter-Erklärung:**
- `model="gpt-image-2"` → bestes Modell für stylisierte Astrologie-Kunst
- `aspect_ratio="21:9"` → passt für die Cover-Position oberhalb der dunklen Namens-Box
- `quality="medium"` → reicht aus, low kostet 1 Credit, medium 4 Credits, high 16 Credits

## Prompt-Vorlage

Die zwei Sternzeichen der Personen werden mit ihren Unicode-Glyphen + englischem Namen
eingesetzt. Bei manchen Paaren ist es das gleiche Sternzeichen – dann nur ein Symbol mit dem
Hinweis "twice the energy" oder gleiches Symbol auf beiden Seiten.

```
Mystical cosmic artwork on warm cream beige background (#EBE7DC). Two glowing astral figures
embracing forehead to forehead in the center, made of golden stardust and starlight. Their
hair flows as golden cosmic energy. Between them in their hearts a radiant golden sacred
geometry star pulses with light. {SIGN1_GLYPH} {SIGN1_NAME} zodiac symbol on the left side,
{SIGN2_GLYPH} {SIGN2_NAME} zodiac symbol on the right side, both glowing in deep gold within
elegant circular gold medallions. The background transitions seamlessly from rich gold and
warm amber at the center to soft cream beige at the edges, with golden mist and starlight
particles fading to nothing. Soft vignette edges that blend into cream background. Premium
luxury aesthetic, painterly digital art, no text, no hard edges, vintage astrology poster
style. Warm cream beige (#EBE7DC) dominates the outer 30% of the image.
```

## Sternzeichen-Glyph- und Name-Mapping

| Code | Glyph | English Name |
|------|-------|--------------|
| Ari | ♈ | Aries |
| Tau | ♉ | Taurus |
| Gem | ♊ | Gemini |
| Can | ♋ | Cancer |
| Leo | ♌ | Leo |
| Vir | ♍ | Virgo |
| Lib | ♎ | Libra |
| Sco | ♏ | Scorpio |
| Sag | ♐ | Sagittarius |
| Cap | ♑ | Capricorn |
| Aqu | ♒ | Aquarius |
| Pis | ♓ | Pisces |

## Wichtig

- **Cream-Fade-Edges sind ESSENTIELL**: Das Bild muss sich in den `#EBE7DC`-Hintergrund des PDFs
  einbetten, nicht als rechteckige Box auf der Seite stehen.
- **NO TEXT** im Prompt explizit erwähnen, sonst kann GPT-image Buchstaben in die Sternzeichen
  hineinhalluzinieren.
- **Beide Personen als androgyne Lichtwesen** dargestellt – keine Gender-Annahmen, keine
  bestimmten Ethnien.
- Wenn die Generation merkwürdig wird (z.B. unscharfe Symbole), kann der Prompt vereinfacht
  werden auf "two glowing astral figures embracing", und die Symbole werden notfalls als
  SVG-Overlay im PDF gezeichnet (Fallback).

## Beispiel: Wassermann + Waage

```
... Aquarius zodiac symbol ♒ on the left side, Libra zodiac symbol ♎ on the right side, both
glowing in deep gold ...
```

## Bild-Pfad nach Generation

Die KIMASTERMIND_IMAGES API gibt eine URL zurück (z.B. `https://mcp.kimastermind.net/img/<uuid>.jpg`).

**Schritte zum Einbinden ins PDF:**
1. Bild von der URL herunterladen (z.B. mit `wget` oder `requests`)
2. Lokal speichern als z.B. `/tmp/cover_<paar>.jpg`
3. Optional: zu WebP konvertieren (spart Speicherplatz)
4. Pfad an `build_report.py` übergeben:
   ```
   python3 scripts/build_report.py data.json /tmp/cover_<paar>.webp output.pdf
   ```
