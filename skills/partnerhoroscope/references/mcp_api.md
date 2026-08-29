# MCP API Reference – Welche Calls für welche Daten

Dieser Skill braucht zwei MCPs:

1. **MASCHA-MCP** – Astrologie- und Numerologie-API
   Server URL: `https://mcp.mascha-cosmos.com/mcp`
   Display Name: "MASCHA-MCP"

2. **KIMASTERMIND_IMAGES** – AI-Bildgenerierung (nur für Cover)
   Server URL: `https://mcp.kimastermind.net/image`
   Display Name: "KIMASTERMIND_IMAGES"

**Wenn die UUIDs/Tool-Präfixe in einer Installation anders heissen:** Nutze `tool_search`
zum Auffinden. Die Tool-Namen sind aber stabil:
- `MASCHA-MCP:natal_chart`
- `MASCHA-MCP:relationship_compatibility`
- `MASCHA-MCP:relationship_compatibility_score`
- `MASCHA-MCP:relationship_love_languages`
- `MASCHA-MCP:relationship_red_flags`
- `MASCHA-MCP:composite_chart`
- `MASCHA-MCP:numerology_core_numbers`
- `MASCHA-MCP:numerology_compatibility` (optional)
- `KIMASTERMIND_IMAGES:generate_image`

---

## ⚠️ ZENTRALE REGEL

**Halluzinationen sind verboten.** Alle astrologischen Fakten MÜSSEN aus den API-Antworten kommen.

Häufige Fehler, die Claude beim ersten Versuch macht:
- Aszendent erfunden (z.B. "Steinbock-Aszendent" weil Person geerdet wirkt)
- Mondzeichen falsch zugeordnet
- Orbs erfunden
- Häuser-Position falsch

**Lösung:** Nach jedem API-Call das Ergebnis in einem strukturierten Daten-Dict speichern und
beim Texte-Schreiben **nur aus diesem Dict zitieren**, nie aus dem Kopf.

---

## Schritt 1: Natal Charts für beide Personen

Pro Person ein Call. Liefert Sonnen-Zeichen, Mond, Aszendent, Häuser, alle Planeten.

```
MASCHA-MCP:natal_chart(
    day=6,                  # int 1-31
    month=2,                # int 1-12
    year=1973,              # int
    hour=9,                 # int 0-23
    minute=5,               # int 0-59
    city="Zürich",      # str
    country_code="CH",      # ISO-Code
    language="de",          # str (de | en | fr | it | es)
    name="Anna",            # optional
    house_system="P",       # P=Placidus (Standard für Mascha)
    zodiac_type="Tropic",   # Standard
)
```

**Relevante Felder im Response (`subject_data`):**

| API-Feld | Verwendung in Daten-Dict |
|---|---|
| `sun.sign` | `person.sun_sign` (englisch, z.B. "Lib" → mapping zu "Waage") |
| `moon.sign` | Mondzeichen für Charakterisierung |
| `moon.house` | Mond-Haus für Portrait |
| `ascendant.sign` | `person.ascendant_sign` |
| `mercury.sign`, `venus.sign`, `mars.sign` | Persönlichkeits-Texte |
| `jupiter.sign`, `saturn.sign` | Lebensthemen |
| `chiron.sign`, `chiron.house` | Heilung / Wunde |

**Sign-Abkürzungen → Deutsch:** Die Symbol-Bibliothek (`mascha_symbols.SIGN_DE`) hat das Mapping.

---

## Schritt 2: Relationship Compatibility Score

Liefert den Gesamt-Score und die Aufschlüsselung.

```
MASCHA-MCP:relationship_compatibility_score(
    person1_day=6, person1_month=2, person1_year=1973,
    person1_hour=9, person1_minute=5,
    person1_city="Zürich", person1_country_code="CH",
    person1_name="Anna",
    person2_day=7, person2_month=10, person2_year=1972,
    person2_hour=12, person2_minute=57,
    person2_city="Bern", person2_country_code="CH",
    person2_name="Lena",
    language="de",
)
```

**Mapping zu `data["compatibility"]`:**

- `total` → API-Feld `overall_score` oder `total`
- `rating` → API-Feld `rating` oder `category` (z.B. "Solide Grundlage")
- `items` → Aufschlüsselung in Kategorien; falls API keine ausführliche Liste liefert, manuell
  konstruieren aus `score_breakdown`:
  - Aspekte zwischen euch (aspects_score)
  - Sonne und Mond (sun_moon_score)
  - Anziehung (attraction_score)
  - Saturn / Verbindlichkeit (saturn_score)
  - Elemente (elements_score)
  - Merkur / Kommunikation (mercury_score)

**`percent` für Balken:** `value / max_value * 100`, max ca. 25 für Aspekte.

---

## Schritt 3: Relationship Compatibility (Detail)

Liefert ausführliche Beziehungs-Dynamiken und Aspekt-Tabelle.

```
MASCHA-MCP:relationship_compatibility(
    # Same params as score
)
```

**Mapping zu `data["synastry"]["aspect_table"]`:**

Aus dem Response `aspects` oder `synastry_aspects`:
```python
[
    {
        "p1": <deutsche Bezeichnung von aspect.point1>,
        "aspect": <deutsche Bezeichnung, z.B. "Trigon", "Konjunktion", "Quadrat">,
        "p2": <deutsche Bezeichnung von aspect.point2>,
        "orb": <formatiert als "1,3°" – Komma!>
    }
]
```

**Englisch → Deutsch Aspekt-Mapping:**
- `conjunction` → Konjunktion
- `opposition` → Opposition
- `trine` → Trigon
- `square` → Quadrat
- `sextile` → Sextil
- `quintile` → Quintil (selten verwendet)

**Mapping zu `data["dynamics"]`:**

Aus `relationship_dynamics` oder `summary`:
- `relationship_type` → grid_items[0]
- `power_balance` → grid_items[1]
- `emotional_bond` → grid_items[2]
- `communication` → grid_items[3]
- `long_term_potential` → wide_item

---

## Schritt 4: Composite Chart

```
MASCHA-MCP:composite_chart(
    # Same params as compatibility
)
```

**Mapping zu `data["composite"]`:**

Die wichtigsten Composite-Aspekte werden zu Bullets:
- Composite Sonne + Position/Haus → "Sonne und Merkur im X, Y. Haus"
- Venus-Mars-Aspekt im Composite → "Venus Konjunktion Mars"
- Sonne-Saturn-Aspekt → "Sonne Opposition Saturn"
- Composite-Aszendent → Aussenwirkung

---

## Schritt 5: Love Languages

```
MASCHA-MCP:relationship_love_languages(
    # Same params as compatibility
)
```

**Response-Struktur (vereinfacht):**

```json
{
    "person1": {
        "primary_love_language_shown": "Quality Time",
        "secondary_love_language_shown": "Physical Touch",
        "primary_love_language_received": "Words of Affirmation",
        "analysis": "..."
    },
    "person2": {...}
}
```

**Achtung Edge-Case:** Wenn `secondary_shown` == `primary_received`, dann im Text EXPLIZIT
erklären, dass das KEIN Widerspruch ist:
> Du *zeigst* Liebe primär durch Taten + sekundär durch Zeit; *fühlst* dich aber primär
> durch ungeteilte Zeit geliebt.

**Englisch → Deutsch Love-Language-Mapping:**
- Quality Time → Qualitätszeit
- Physical Touch → Körperliche Berührung
- Words of Affirmation → Worte der Bestätigung
- Acts of Service → Taten der Dienstbarkeit
- Receiving Gifts → Geschenke

---

## Schritt 6: Numerology

Pro Person ein Call:

```
MASCHA-MCP:numerology_core_numbers(
    day=6, month=2, year=1973,
    name="Anna Muster",     # Vollständiger Name (Vor- + Nachname falls bekannt, sonst Vorname)
    language="de",
)
```

**Relevante Response-Felder:**

| API-Feld | Mapping |
|---|---|
| `life_path_number` | `lifepath_person.number` |
| `life_path_theme` | `lifepath_person.theme` |
| `life_path_description` | Basis für `lifepath_person.desc_html` |
| `soul_urge_number` | `second_numbers.soul_person.number` |
| `soul_urge_theme` | `second_numbers.soul_person.theme` |
| `destiny_number` (oder `expression_number`) | `second_numbers.destiny_person.number` |
| `destiny_theme` | `second_numbers.destiny_person.theme` |
| `personal_year_number` (für aktuelles Jahr) | `year_resonance.number` |

**Wenn beide Personen das gleiche persönliche Jahr haben (z.B. beide im Jahr 9):**
Eigene Sektion `year_resonance` füllen mit Hinweis auf gemeinsame Resonanz.

---

## Schritt 7: Red Flags / Compatibility Warnings

```
MASCHA-MCP:relationship_red_flags(
    # Same params as compatibility
)
```

**Mapping zu `data["profiles"]["flags_*"]`:**

Response hat typischerweise drei Kategorien:
- `green_flags` → `flags_green.items`
- `yellow_flags` → `flags_yellow.items`
- `red_flags` → `flags_red.items` (oft leer / "keine ernsthaften")

---

## Schritt 8: Cover-Bild generieren

**NUR das Cover wird pro Klient neu generiert** (mit den richtigen Sternzeichen-Symbolen).
Alle anderen Bilder kommen aus `/assets`.

```
KIMASTERMIND_IMAGES:generate_image(
    model="gpt-image-2",
    aspect_ratio="21:9",
    quality="medium",       # 1K, reicht für PDF, spart Credits
    prompt=<siehe unten>
)
```

**Cover-Prompt-Template** (Variablen-Platzhalter mit echten Sternzeichen ersetzen):

```
Mystical cosmic artwork on warm cream beige background (#EBE7DC). Two glowing astral figures
embracing forehead to forehead in the center, made of golden stardust and starlight. Their
hair flows as golden cosmic energy. Between them in their hearts a radiant golden sacred
geometry star pulses with light. {SIGN1_ENGLISH} zodiac symbol on the left side,
{SIGN2_ENGLISH} zodiac symbol on the right side, both glowing in deep gold within elegant
circular gold medallions. The background transitions seamlessly from rich gold and warm amber
at the center to soft cream beige at the edges, with golden mist and starlight particles
fading to nothing. Soft vignette edges that blend into cream background. Premium luxury
aesthetic, painterly digital art, no text, no hard edges, vintage astrology poster style.
Warm cream beige (#EBE7DC) dominates the outer 30% of the image.
```

**SIGN-Englisch-Namen für den Prompt:**
Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn,
Aquarius, Pisces (zodiac symbol ♈♉♊♋♌♍♎♏♐♑♒♓)

**Wichtig:** Quality `medium` (= ca. 1K Auflösung) reicht völlig. `4K` würde 4x mehr Credits
kosten ohne sichtbaren Nutzen im PDF.

**Bildgrösse Credits:**
- `gpt-image-2` medium: ~4 Credits pro Bild
- `nano-banana-pro` 1K: ~5 Credits

Für gpt-image-2 sprechen die besseren Text/Symbol-Rendering-Fähigkeiten. Verwende immer
**gpt-image-2** für das Cover.

---

## Komplettes Daten-Sammeln-Pattern (Pseudocode)

```python
# 1. Beide Natal Charts holen
chart1 = mascha_natal_chart(person1_data)
chart2 = mascha_natal_chart(person2_data)

# 2. Beziehungs-Daten
score = mascha_relationship_compatibility_score(p1, p2)
compat = mascha_relationship_compatibility(p1, p2)
composite = mascha_composite_chart(p1, p2)
loves = mascha_relationship_love_languages(p1, p2)
flags = mascha_relationship_red_flags(p1, p2)

# 3. Numerologie pro Person
num1 = mascha_numerology_core_numbers(p1)
num2 = mascha_numerology_core_numbers(p2)

# 4. Daten in strukturiertes Dict packen (siehe data_schema.md)
data = build_data_dict(chart1, chart2, score, compat, composite, loves, flags, num1, num2)

# 5. Cover-Bild generieren
cover_url = kimastermind_generate_image(
    prompt=cover_prompt.format(
        SIGN1_ENGLISH=de_to_en(chart1["sun.sign"]),
        SIGN2_ENGLISH=de_to_en(chart2["sun.sign"]),
    )
)
cover_path = download_image(cover_url, "cover_generated.jpg")

# 6. Texte vom LLM generieren basierend auf data-dict (siehe text_generation.md)
data = enrich_with_llm_texts(data, all_facts)

# 7. PDF bauen
build_pdf(data, output_path="report.pdf", cover_image=cover_path)
```
