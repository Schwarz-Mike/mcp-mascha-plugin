# Klienten-Briefing Template

Dieses Template wird verwendet, um nach den API-Calls eine `klienten_briefing.md` zu
schreiben. Diese Datei dient als **Goldstandard-Snapshot der Rohdaten** und ermöglicht
Re-Runs ohne erneute API-Calls.

## Format der `klienten_briefing.md`

```markdown
# Klienten-Briefing · [Name1] & [Name2]

**Erstellt am:** [YYYY-MM-DD HH:MM]
**Skill-Version:** partnerhoroscope v1.0
**Datenquelle:** MASCHA-MCP (mcp.mascha-cosmos.com)
**Status:** ✅ Vollständiger Datenabruf

---

## 👤 Person 1: [Name1]

### Stammdaten
- **Vorname:** [Name1]
- **Geburtsdatum:** TT.MM.JJJJ
- **Geburtszeit:** HH:MM
- **Geburtsort:** [Stadt], [Land]
- **Koordinaten:** Lat [X], Lng [Y]
- **Timezone:** [IANA]

### Astrologische Kernfakten (aus natal_chart API)
| Position | Sign | Grad | Haus | Element | Modalität |
|----------|------|------|------|---------|-----------|
| Sonne | [Sign_de] | [X.X°] | [N] | [El] | [Mod] |
| Mond | ... | ... | ... | ... | ... |
| Aszendent | ... | ... | 1 | ... | ... |
| Merkur | ... | ... | ... | ... | ... |
| Venus | ... | ... | ... | ... | ... |
| Mars | ... | ... | ... | ... | ... |
| Jupiter | ... | ... | ... | ... | ... |
| Saturn | ... | ... | ... | ... | ... |
| Uranus | ... | ... | ... | ... | ... |
| Neptun | ... | ... | ... | ... | ... |
| Pluto | ... | ... | ... | ... | ... |
| Chiron | ... | ... | ... | ... | ... |
| MC | ... | ... | 10 | ... | ... |
| Lilith (Mean) | ... | ... | ... | ... | ... |
| Nordknoten | ... | ... | ... | ... | ... |

### Element-Verteilung (berechnet)
- 🔥 Feuer: X%
- 🌍 Erde: X%
- 💨 Luft: X%
- 💧 Wasser: X%

### Modalitäten-Verteilung (berechnet)
- ⚡ Kardinal: X%
- 🔒 Fix: X%
- 🌀 Veränderlich: X%

### Haus-Betonungen (Anzahl Planeten pro Haus, Top 3)
- Haus [N]: [N] Planeten ([Liste])
- Haus [N]: [N] Planeten ([Liste])
- Haus [N]: [N] Planeten ([Liste])

### Natal-Aspekte (wichtigste, Top 10)
| Planet 1 | Aspekt | Planet 2 | Orb |
|----------|--------|----------|-----|
| ... | ... | ... | ... |

### Numerologie (aus numerology_core_numbers)
- **Lebenspfad:** [N]
- **Schicksalszahl:** [N]
- **Seelendrang:** [N]
- **Persönlichkeitszahl:** [N]
- **Persönliches Jahr 2026:** [N]

---

## 👤 Person 2: [Name2]

[Gleiche Struktur wie Person 1]

---

## 💞 Beziehungs-Daten

### Kompatibilitäts-Score (aus relationship_compatibility_score)
- **Gesamt:** [X / 100]
- **Rating:** [Text]

### Score-Dimensionen
- Aspekte zwischen euch: [X]
- Sonne und Mond: [X]
- Anziehung: [X]
- Saturn / Verbindlichkeit: [X]
- Elemente: [X]
- Merkur / Kommunikation: [X]

### Synastrie-Aspekte (aus synastry_chart, Top 12 sortiert nach Wichtigkeit)
| Person1 | Aspekt | Person2 | Orb |
|---------|--------|---------|-----|
| ... | ... | ... | ... |
| ... | ... | ... | ... |

### Beziehungs-Dynamiken (aus relationship_compatibility)
- **Beziehungstyp:** [z.B. "Romantische Partnerschaft"]
- **Machtbalance:** [z.B. "Gleichberechtigt"]
- **Emotionale Verbindung:** [z.B. "Stark"]
- **Kommunikation:** [z.B. "Harmonisch"]
- **Langzeitpotenzial:** [z.B. "Hoch"]

### Composite (aus relationship_davison oder composite_chart)
- **Composite-Sonne:** [Sign], Haus [N]
- **Composite-Mond:** [Sign], Haus [N]
- **Composite-Venus:** [Sign], Haus [N]
- **Composite-Mars:** [Sign], Haus [N]
- **Composite-Aszendent:** [Sign]
- **Composite-MC:** [Sign]
- **Wichtigste Composite-Aspekte:** [Liste]

### Liebessprachen (aus relationship_love_languages)
- **[Name1]:**
  - Primary shown: [Sprache]
  - Secondary shown: [Sprache]
  - Primary received: [Sprache]
- **[Name2]:**
  - Primary shown: [Sprache]
  - Secondary shown: [Sprache]
  - Primary received: [Sprache]
- **Schnittmenge:** [Sprache(n)]

### Red Flags (aus relationship_red_flags)
- **Grüne Signale:** [Liste]
- **Gelbe Signale:** [Liste]
- **Rote Signale:** [Liste]

### Numerologie-Resonanz
- Persönliches Jahr beider Personen: [Same / Different]
- Lebenspfad-Kombination: [N1 + N2]
- Beziehungs-Resonanz-Zahl (Summe reduziert): [N]

---

## 🛠️ Technische Informationen

### MCP-Endpunkte verwendet
- ✅ MASCHA-MCP:natal_chart (Person 1)
- ✅ MASCHA-MCP:natal_chart (Person 2)
- ✅ MASCHA-MCP:relationship_compatibility
- ✅ MASCHA-MCP:relationship_compatibility_score
- ✅ MASCHA-MCP:synastry_chart
- ✅ MASCHA-MCP:relationship_love_languages
- ✅ MASCHA-MCP:relationship_davison
- ✅ MASCHA-MCP:relationship_red_flags
- ✅ MASCHA-MCP:numerology_core_numbers (Person 1)
- ✅ MASCHA-MCP:numerology_core_numbers (Person 2)
- (optional) MASCHA-MCP:psychological_analysis
- (optional) MASCHA-MCP:enhanced_positions
- (optional) MASCHA-MCP:enhanced_aspects

### Cover-Bild
- **Generiert mit:** KIMASTERMIND_IMAGES:generate_image
- **Modell:** gpt-image-2
- **Quality:** medium
- **Aspect ratio:** 21:9
- **Pfad:** [cover.jpg]
- **Generierungs-Datum:** [YYYY-MM-DD]

### Hinweise zur Reproduzierbarkeit
Diese Datei enthält **alle** Rohdaten, die für eine erneute Generierung des Reports nötig
sind. Bei Re-Run mit dieser Datei:
- Keine erneuten API-Calls nötig
- Konsistente Datenbasis (API-Werte können sich geringfügig ändern)
- Schneller (~30 Sekunden statt mehrere Minuten)
- Kein API-Credit-Verbrauch

### Datenschutz-Hinweis
Diese Datei enthält personenbezogene Daten (Geburtsdaten, Klarnamen). Sie gehört NICHT in
ein öffentliches Repository, sondern bleibt im privaten Klienten-Ordner.
```

## Nutzung im Code

Das Skript `scripts/calc_helpers.py` enthält die Funktion `write_klienten_briefing()` die
diese Datei aus den API-Responses erzeugt.

Beim Re-Run kann `scripts/parse_klienten_briefing.py` (TODO) die Datei wieder einlesen.
