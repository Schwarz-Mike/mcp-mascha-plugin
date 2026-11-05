# Datenerhebung – MCP-Calls

Dieses Dokument beschreibt **exakt**, welche MCP-Tool-Aufrufe gemacht werden müssen, um den
30-Sektion-Partnerhoroskop zu erstellen.

## ⚠️ Goldene Regel

**Halte dich strikt an die zurückgegebenen Daten. Keine Erfindungen. Keine
Halluzinationen.** Wenn ein Datenpunkt nicht in einer API-Response steht, darf er nicht
im Report stehen.

---

## Verwendete MCP-Server

1. **MASCHA-MCP** (`mcp.mascha-cosmos.com`) – Astrologie- und Numerologie-Daten
2. **KIMASTERMIND_IMAGES** (`mcp.kimastermind.net`) – Cover-Bild

Wenn Tools nicht direkt verfügbar sind, zuerst `tool_search` aufrufen:

```
tool_search(query="natal chart birth horoscope ascendant")
tool_search(query="numerology core numbers")
tool_search(query="relationship compatibility synastry")
tool_search(query="image generation gpt-image")
```

---

## Pflicht-API-Calls (zwingend für jeden Report)

### 1. Geburtshoroskope beider Personen (ZUERST!)

```
MASCHA-MCP:natal_chart(
    day=<TT>, month=<MM>, year=<YYYY>,
    hour=<HH>, minute=<MM>,
    city=<Stadt>, country_code=<ISO>,
    language="de", house_system="P",
    zodiac_type="Tropic", name=<Name>
)
```

**Pflicht-Extrakt aus jeder Response:**
- `subject_data.sun.sign` → Sonnenzeichen-Code (z.B. "Aqu")
- `subject_data.sun.position` → Grad
- `subject_data.sun.house` → "First_House" bis "Twelfth_House"
- Gleiche Struktur für: `moon`, `ascendant`, `mercury`, `venus`, `mars`, `jupiter`,
  `saturn`, `uranus`, `neptune`, `pluto`, `chiron`, `medium_coeli`, `mean_lilith`,
  `mean_node`
- `chart_data.aspects` → Liste aller Natal-Aspekte

### 2. Beziehungs-Kompatibilität

```
MASCHA-MCP:relationship_compatibility(
    person1=<dict mit day,month,year,hour,minute,city,country_code,name>,
    person2=<gleiche Struktur>,
    language="de"
)

MASCHA-MCP:relationship_compatibility_score(
    person1=..., person2=..., language="de"
)
```

Liefert: Gesamtwert, 6 Score-Dimensionen, Beziehungsdynamiken (Typ, Machtbalance,
Emotionale Verbindung, Kommunikation), Langzeitpotenzial.

### 3. Synastrie-Aspekte

```
MASCHA-MCP:synastry_chart(person1=..., person2=..., language="de")
```

Liefert: Liste aller Aspekte zwischen den Personen mit Orb-Werten.

**Auswahl der Top-Aspekte für den Report:**
- Alle Aspekte mit Orb < 1° → immer aufnehmen
- Personal-Planet-Aspekte (Sonne, Mond, Merkur, Venus, Mars) zwischen den Personen
- Achsen-Treffer (Aszendent, MC) zählen besonders
- Chiron-Sonne, Chiron-Mond, Mars-Pluto, Saturn-Venus als klassische Schlüssel-Aspekte
- Filtern auf 6 wichtigste Aspekte für ausführliche Erklärung, 8-12 für Tabelle

### 4. Liebessprachen

```
MASCHA-MCP:relationship_love_languages(person1=..., person2=..., language="de")
```

Liefert: pro Person Primary shown, Secondary shown, Primary received.

**Wichtige Sub-Logik:** Wenn sekundäre = empfangene Sprache (z.B. beide
"Qualitätszeit"), explizit als "kein Widerspruch" erklären.

### 5. Composite

```
MASCHA-MCP:relationship_davison(person1=..., person2=..., language="de")
```

Liefert die Composite-Hauptpunkte: Composite-Sonne, -Mond, -Venus, -Mars, -Aszendent,
-MC mit Sign und Haus.

### 6. Red Flags

```
MASCHA-MCP:relationship_red_flags(person1=..., person2=..., language="de")
```

Liefert grüne, gelbe und rote Signale.

### 7. Numerologie für beide Personen

```
MASCHA-MCP:numerology_core_numbers(
    day=..., month=..., year=...,
    name=<Vorname>, language="de"
)
```

Liefert: Lebenspfad-Zahl, Schicksalszahl, Seelendrang-Zahl, Persönlichkeitszahl,
persönliches Jahr.

### 8. Cover-Bild generieren

```
KIMASTERMIND_IMAGES:generate_image(
    model="gpt-image-2",
    aspect_ratio="21:9",
    quality="medium",
    prompt=<siehe references/image_prompts.md>
)
```

---

## Optionale API-Calls (empfohlen für tiefere Sektionen)

Diese sind nicht zwingend, machen aber die neuen Sektionen (Karma, Schatten, Authentizität)
sauberer und reduzieren Halluzinations-Risiko.

### 9. Psychologische Analyse (optional, für Sektionen 6, 7, 20, 22)

```
MASCHA-MCP:psychological_analysis(
    day=..., month=..., year=...,
    hour=..., minute=...,
    city=..., country_code=...,
    language="de",
    tradition="psychological",
    detail_level="full"
)
```

Liefert: Persönlichkeitsstruktur, Entwicklungspotential, Schatten-Themen.

### 10. Karriere-Analyse (optional, für Sektion 10 Wertesystem/Mission)

```
MASCHA-MCP:career_analysis(
    day=..., month=..., year=...,
    hour=..., minute=...,
    city=..., country_code=...,
    language="de"
)
```

Liefert: Berufung, MC-Themen, Saturn-Position, Lebens-Mission.

### 11. Numerologie-Timing (optional, für Sektion 18 erweitert)

```
MASCHA-MCP:numerology_luck_analysis(
    day=..., month=..., year=...,
    name=<Vorname>,
    target_date="2026-01-01",
    language="de"
)
```

Liefert: günstige Zahlen, Farben, Tage, Zeitfenster.

### 12. Enhanced Positions (optional, für Element-Berechnungen)

Falls Natal-Chart-Response keine Würden-Daten enthält:

```
MASCHA-MCP:enhanced_positions(
    day=..., month=..., year=...,
    hour=..., minute=...,
    ...
)
```

---

## Was selbst berechnet werden muss (kein API-Call nötig)

Diese Werte werden aus den `natal_chart`-Daten in `scripts/calc_helpers.py` berechnet:

| Wert | Funktion | Verwendet in Sektion |
|------|----------|----------------------|
| Element-Verteilung in % | `calc_element_distribution(natal_data)` | 5 Elemente-Mischung |
| Modalitäten-Verteilung | `calc_modality_distribution(natal_data)` | 5 Elemente-Mischung |
| Haus-Betonungen | `calc_house_emphasis(natal_data)` | 4 Lebens-Prioritäten |
| Lebens-Prioritäten in % | `calc_life_priorities(natal_data)` | 4 Lebens-Prioritäten |

Die Gewichtung der Planeten ist in `PLANET_WEIGHTS` definiert. Sonne und Mond zählen am
stärksten (×4), gefolgt von Aszendent (×3), persönlichen Planeten (×2), äußeren
Planeten (×1).

---

## Was niemals erfunden werden darf

- **Aszendent** – muss aus `natal_chart.ascendant.sign` kommen
- **Mondzeichen + Mondhaus** – aus `natal_chart.moon`
- **Planetenpositionen** (Sign + Haus + Grad) – aus den natal_chart-Feldern
- **Aspekte und Orbs** – aus `synastry_chart.aspects` und `natal_chart.aspects`
- **Numerologische Zahlen** – aus `numerology_core_numbers`
- **Liebessprachen** – aus `relationship_love_languages`
- **Composite-Punkte** – aus `relationship_davison`
- **Score-Werte** – aus `relationship_compatibility_score`
- **Element-Prozente** – berechnet aus echten natal_chart-Positionen, nicht geschätzt

---

## Was geschrieben werden darf (Text auf Basis der echten Daten)

- Interpretation des Charakters basierend auf den **echten** Positionen
- Beziehungs-Tipps abgeleitet aus den **echten** Aspekten
- Metaphorische Sprache zur Erklärung der Konstellationen
- Bedürfnis-orientierte Empfehlungen
- Goldene Sätze (verdichtende Aphorismen)
- Selbstreflexionsfragen

---

## Datenfluss-Checkliste

Vor dem PDF-Bau sicherstellen, dass folgende Felder befüllt sind:

```
✓ Beide vollständigen Natal-Charts geholt
✓ Sonnenzeichen + Aszendent + Mondzeichen für beide verifiziert
✓ Kompatibilitäts-Score (Total + 6 Dimensionen)
✓ Synastrie-Aspekte (mind. 8 Aspekte mit Orbs)
✓ Liebessprachen für beide
✓ Composite (Davison) Hauptpunkte
✓ Red Flags (grün/gelb/rot)
✓ Numerologie für beide Personen
✓ Element-Verteilung beider Personen berechnet
✓ Lebens-Prioritäten-Verteilung beider Personen berechnet
✓ Cover-Bild generiert und lokal gespeichert
✓ klienten_briefing.md geschrieben (im gewählten Output-Ordner!)
```

---

## Re-Run-Modus (ohne API-Calls)

Wenn ein bestehendes Paar wiederkommt und nur das PDF neu generiert werden soll:

1. User lädt vorhandene `klienten_briefing.md` hoch oder verweist auf Pfad
2. Skill parst die `.md`-Datei (Markdown-Tabellen, Listen, Felder)
3. Skill baut neue `data.json` mit angepassten Texten
4. PDF wird generiert ohne neue API-Calls

**Vorteil:** Schneller, billiger, konsistente Datenbasis.
