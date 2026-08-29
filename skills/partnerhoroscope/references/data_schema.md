# Datenschema – `data.json` für `build_report.py`

Diese Datei beschreibt die JSON-Struktur, die das `build_report.py` erwartet. Alle 30
Sektionen sind in einem JSON-Dict zusammengefasst.

**Quelle der Daten:** API-Responses (siehe `data_collection.md`). Texte werden auf
Basis der echten API-Daten generiert nach den Regeln in `text_generation.md` und
`section_prompts.md`.

---

## Top-Level Felder

```json
{
  "person1": { ... },
  "person2": { ... },
  "intro_text": "...",

  "portraits": { ... },              // Sektion 2
  "score": { ... },                  // Sektion 3
  "life_priorities": { ... },        // Sektion 4 NEU
  "elements": { ... },               // Sektion 5 NEU
  "needs": { ... },                  // Sektion 6 NEU
  "feelings": { ... },               // Sektion 7 NEU
  "communication": { ... },          // Sektion 8 NEU
  "love_languages": { ... },         // Sektion 9 ERWEITERT
  "values": { ... },                 // Sektion 10 NEU
  "passion": { ... },                // Sektion 11 NEU
  "materiality": { ... },            // Sektion 12 NEU
  "type_profiles": { ... },          // Sektion 13 NEU
  "synastry": { ... },               // Sektion 14+15
  "dynamics": { ... },               // Sektion 16
  "composite": { ... },              // Sektion 17
  "numerology": { ... },             // Sektion 18 ERWEITERT
  "strengths": { ... },              // Sektion 19 ERWEITERT
  "shadows": { ... },                // Sektion 20 NEU
  "conflict_map": { ... },           // Sektion 21 ERWEITERT
  "masks": { ... },                  // Sektion 22 NEU
  "karma": { ... },                  // Sektion 23 NEU
  "crisis": { ... },                 // Sektion 24 NEU
  "sexual": { ... },                 // Sektion 25 NEU
  "energetic": { ... },              // Sektion 26 NEU
  "spiritual_mission": { ... },      // Sektion 27 NEU
  "profiles": { ... },               // Sektion 28
  "next_steps": { ... },             // Sektion 29
  "closing": { ... }                 // Sektion 30
}
```

---

## Personen-Header

```json
"person1": {
  "name": "Anna",
  "birth_date_de": "6. Februar 1973",
  "birth_time": "09:05 Uhr",
  "birth_place": "Zürich",
  "sun_sign_de": "Wassermann",
  "sun_sign_code": "Aqu"     // 3-Buchstaben-Code aus API
}
```

**Sun-Sign-Codes:** `Ari`, `Tau`, `Gem`, `Can`, `Leo`, `Vir`, `Lib`, `Sco`, `Sag`,
`Cap`, `Aqu`, `Pis`.

---

## Sektion 4 · life_priorities (NEU)

```json
"life_priorities": {
  "intro": "Was ist jedem von euch im Leben besonders wichtig?...",
  "person1": [
    ["Spiritualität, Rückzug", 22],
    ["Ich, Selbstentfaltung", 18],
    ...8 Bereiche absteigend nach Prozent
  ],
  "person2": [ ...8 Bereiche... ],
  "analysis_paragraphs": [
    "<strong>Wo seid ihr euch einig?</strong> ...",
    "<strong>Wo liegen die Unterschiede?</strong> ...",
    "<strong>Wer ist nach innen, wer nach aussen?</strong> ..."
  ],
  "golden_sentence": "Eure Lebenslandkarten überschneiden sich da, wo es zählt..."
}
```

**Werte:** Aus `calc_helpers.py::calc_life_priorities()`. Ganzzahlen.

---

## Sektion 5 · elements (NEU)

```json
"elements": {
  "image_caption": "Feuer, Erde, Luft, Wasser...",
  "person1": {"Feuer": 12, "Erde": 18, "Luft": 47, "Wasser": 23},
  "person2": {"Feuer": 28, "Erde": 20, "Luft": 38, "Wasser": 14},
  "mix": "Eure dominante Element-Achse ist...",
  "connection": "Wo ihr euch trefft...",
  "friction": "Wo es reibt...",
  "missing": "Was im Paar-System unterrepräsentiert ist...",
  "everyday": "<strong>Drei Alltagssituationen:</strong>...",
  "golden_sentence": "..."
}
```

**Werte:** Aus `calc_helpers.py::calc_element_distribution()`.

---

## Sektion 6 · needs (NEU)

```json
"needs": {
  "intro": "...",
  "person1": {
    "paragraphs": ["Para 1 mit Mond-Position...", "Para 2..."]
  },
  "person2": { "paragraphs": [...] },
  "meeting": "Wo eure Bedürfnisse sich treffen...",
  "colliding": "Wo es kollidiert: ...",
  "hard_to_understand": "Lena versteht schwer, dass...",
  "nervous_system": "<strong>Annas Nervensystem-Sprache</strong>...",
  "reflection": "Frage an euch beide: Was hat dir heute...",
  "golden_sentence": "..."
}
```

---

## Sektion 7 · feelings (NEU)

```json
"feelings": {
  "intro": "...",
  "person1": [
    "<strong>Anna, dein Fische-Mond</strong>...",
    "Was du brauchst...",
    "Wenn du frierst..."
  ],
  "person2": [3 Absätze analog],
  "synchron": "Wo ihr synchron schwingt...",
  "pass_by": "Wo ihr aneinander vorbei fühlt...",
  "emotional_load": "Wer trägt mehr emotionale Last...",
  "who_approaches": "Nach einem Streit: ...",
  "reflection": "Frage: ...",
  "golden_sentence": "..."
}
```

---

## Sektion 8 · communication (NEU)

```json
"communication": {
  "intro": "...",
  "person1": [2-3 Absätze],
  "person2": [2-3 Absätze],
  "examples": [
    "Wenn <strong>Anna</strong> sagt 'wir müssen reden', meint er...",
    "Wenn <strong>Lena</strong> sagt 'wir müssen reden', meint sie...",
    "Wenn Anna schweigt, bedeutet das...",
    "Wenn Lena schweigt, bedeutet das..."
  ],
  "in_fight": "Im Streit zieht Anna sich zurück...",
  "red_sentences": ["Bei Anna triggert: ...", "Bei Lena triggert: ..."],
  "green_sentences": ["Bei Anna: ...", "Bei Lena: ..."],
  "rituals": "<strong>Wochen-Reflektion (Sonntag, 20 Min):</strong>...",
  "golden_sentence": "..."
}
```

---

## Sektion 9 · love_languages (ERWEITERT)

```json
"love_languages": {
  "image_caption": "...",
  "intro": "...",
  "person1": {
    "primary": "Qualitätszeit",
    "secondary": "Körperliche Berührung",
    "receives": "Worte der Bestätigung",
    "paragraphs": [2 Absätze],
    "charges": ["3 Beispiele was den Akku lädt"],
    "drains": ["3 Beispiele was den Akku leert"]
  },
  "person2": { ...gleiche Struktur },
  "translation_table": [
    {
      "situation": "Sagt 'Ich brauche Zeit für mich'",
      "meaning_p1": "Ich muss meine Seele nähren...",
      "meaning_p2": "Selten gesagt..."
    },
    ...
  ],
  "mini_gestures": "<strong>Anna → Lena:</strong>...<br><strong>Lena → Anna:</strong>...",
  "overlap": "Eure Schnittmenge ist...",
  "golden_sentence": "..."
}
```

---

## Sektion 10 · values (NEU)

```json
"values": {
  "intro": "...",
  "person1": [2 Absätze: 2., 9., MC, Saturn, Nordknoten],
  "person2": [2 Absätze],
  "meeting": "Wo eure Missionen sich treffen...",
  "friction": "Wo sie sich reiben...",
  "common_mission": "Eure gemeinsame Mission (Composite-Sonne)...",
  "golden_sentence": "..."
}
```

---

## Sektion 11 · passion (NEU)

```json
"passion": {
  "image_caption": "...",
  "intro": "...",
  "person1": [3 Absätze: was anmacht, Themen, Mars-Position],
  "person2": [3 Absätze],
  "common": "Eure gemeinsame Leidenschaft...",
  "different": "Wo eure Leidenschaften auseinander gehen...",
  "nourish": "Wie ihr eure Leidenschaften gegenseitig nähren könnt...",
  "golden_sentence": "..."
}
```

---

## Sektion 12 · materiality (NEU)

```json
"materiality": {
  "intro": "...",
  "person1": {
    "label": "Eher unmateriell, visionsorientiert",
    "position": 35,           // 0-100 für die Skala
    "paragraphs": [2 Absätze]
  },
  "person2": { ...gleiche Struktur },
  "who_carries": "Lena ist der Anker...",
  "risks": "Risiko: ...",
  "optimal_split": "Empfehlung: ...",
  "golden_sentence": "..."
}
```

---

## Sektion 13 · type_profiles (NEU)

```json
"type_profiles": {
  "intro": "...",
  "person1": {
    "archetype": "Der visionäre Heiler · der ruhige Tiefen-Denker",
    "description": [2 Absätze: Wirkung, was brodelt],
    "attracts": "Worauf er anspringt: DC, Venus, Mars-Resonanz..."
  },
  "person2": { ...gleiche Struktur },
  "resonance": "Die Resonanz zwischen euch ist hoch...",
  "golden_sentence": "..."
}
```

---

## Sektionen 14+15 · synastry

```json
"synastry": {
  "image_caption": "...",
  "intro_paragraphs": [3-4 Absätze],
  "reflection": "Frage an euch beide: ...",
  "aspect_table": [
    {"planet1": "Sonne", "planet2": "Mond", "aspect": "Trigon", "orb": "1,3°"},
    ... 8-12 Einträge
  ],
  "aspect_explanations": [
    "<strong>1. Mars Konjunktion Pluto (Orb 0,05°).</strong> ... <strong>Begegnungs-Tipp:</strong> ...",
    ... GENAU 6 Erklärungen
  ]
}
```

**Aspekt-Typen** (deutsch, für CSS-Farbe): `Konjunktion`, `Trigon`, `Sextil`,
`Quadrat`, `Opposition`.

---

## Sektion 16 · dynamics

```json
"dynamics": {
  "intro": "...",
  "relationship_type": {"value": "...", "desc": "..."},
  "power_balance": {"value": "...", "desc": "..."},
  "emotional": {"value": "...", "desc": "..."},
  "communication": {"value": "...", "desc": "..."},
  "long_term": {"value": "Hoch", "desc": "..."},
  "daily_tip": "..."
}
```

---

## Sektion 17 · composite

```json
"composite": {
  "image_caption": "...",
  "intro": "...",
  "bullets": ["<strong>Composite-X in Y.</strong> ...", "..."],  // 4 Bullets
  "deepening_tip": "3 Absätze durch <br><br> getrennt"
}
```

---

## Sektion 18 · numerology (ERWEITERT)

```json
"numerology": {
  "intro": "...",
  "person1": {
    "lifepath": 1, "lifepath_theme": "Der Pionier...", "lifepath_desc": "...",
    "soul": 5, "soul_theme": "...", "soul_desc": "...",
    "destiny": 2, "destiny_theme": "...", "destiny_desc": "..."
  },
  "person2": { ...gleiche Struktur },
  "combination": "Die 1 öffnet, die 9 vollendet...",
  "other_intro": "...",
  "resonance": {
    "number": 1,
    "theme": "Beziehungs-Resonanz",
    "desc": "Eure gemeinsame Frequenz (1+9 reduziert)..."
  },
  "personal_year": {
    "year": 2026, "number": 9,
    "theme": "Jahr des Loslassens",
    "text": "..."
  },
  "golden_sentence": "..."
}
```

---

## Sektion 19 · strengths (ERWEITERT)

```json
"strengths": {
  "intro": "...",
  "items": [
    {"title": "Stärke 1", "body": "..."},
    ... GENAU 5 Items
  ],
  "image_caption": "...",
  "complement": "Wo ihr euch ergänzt...",
  "responsibility_intro": "Diese Empfehlungen basieren auf...",
  "responsibility": [
    "<strong>Finanz-Überblick:</strong> Lena ...",
    "<strong>Vision:</strong> Anna...",
    ... 5-6 konkrete Bereiche
  ],
  "tandem": "Wo ihr gemeinsam stärker seid...",
  "golden_sentence": "..."
}
```

---

## Sektion 20 · shadows (NEU)

```json
"shadows": {
  "intro": "...",
  "person1": ["Schwäche 1", "Schwäche 2", "...", "..."],  // 3-4 Items
  "person2": ["...", "...", "..."],
  "trigger": "Wo eure Schwächen sich gegenseitig triggern...",
  "catch": "Wo sie sich auffangen...",
  "awareness": "Warum es leichter wird, wenn beide kennen...",
  "golden_sentence": "..."
}
```

---

## Sektion 21 · conflict_map (ERWEITERT)

```json
"conflict_map": {
  "image_caption": "...",
  "intro": "...",
  "fields": [
    {
      "title": "Bedürftigkeit vs. Unabhängigkeit",
      "anchor": "Mond Quadrat Saturn, ...",
      "body": "...mit <strong>Tipp:</strong>..."
    },
    ... GENAU 5-6 Felder
  ],
  "golden_sentence": "..."
}
```

---

## Sektion 22 · masks (NEU)

```json
"masks": {
  "intro": "...",
  "person1": [3 Absätze: Spalt AC-Sonne, 12. Haus, Saturn],
  "person2": [3 Absätze],
  "meeting": "Wo eure Masken aufeinandertreffen...",
  "when_falls": "Wann die Maske fällt...",
  "invitation": "Wie ihr euch einladet...",
  "reflection": "Frage: ...",
  "golden_sentence": "..."
}
```

---

## Sektion 23 · karma (NEU)

```json
"karma": {
  "image_caption": "...",
  "intro": "...",
  "person1": [3 Absätze: Wunde, wie sich zeigt, wie getriggert],
  "person2": [3 Absätze],
  "trigger_loop": "Wie ihr euch unbewusst triggert...",
  "healing_axis": "Eure Heilungs-Achse über Chiron-Aspekte...",
  "rituals": [
    "<strong>Ehrliche-Worte-Ritual.</strong> ...",
    ... 3-4 konkrete Rituale
  ],
  "golden_sentence": "..."
}
```

---

## Sektion 24 · crisis (NEU)

```json
"crisis": {
  "intro": "...",
  "resources": "Ressourcen im Chart...",
  "vulnerability": "Wo eure Gefahr liegt...",
  "hints": [
    "<strong>Krise nicht alleine durchstehen.</strong> ...",
    ... 3-4 konkrete Hinweise
  ],
  "golden_sentence": "..."
}
```

---

## Sektion 25 · sexual (NEU)

```json
"sexual": {
  "image_caption": "...",
  "intro": "...",
  "person1": [3 Absätze: Antrieb, was anmacht, wann schliesst],
  "person2": [3 Absätze],
  "body_resonance": "Mit Mars-Pluto-Konjunktion (Orb 0,05°)...",
  "needs_compare": "Frequenz: ähnlich. Stil: ... Initiierung: ...",
  "lust_sleeps": "Wenn die Lust einschläft...",
  "body_resource": "Körperkontakt als Ressource...",
  "growth_spaces": "Sexuelle Tabus und Wachstumsräume...",
  "golden_sentence": "..."
}
```

---

## Sektion 26 · energetic (NEU)

```json
"energetic": {
  "intro": "...",
  "aura": "Eure Aura-Resonanz...",
  "medial": "Mediale Verbindung...",
  "magnetic": "Karmische Magnetik...",
  "leaks": "Energetische Lecks...",
  "charging": "Was lädt eure gemeinsame Energie auf...",
  "golden_sentence": "..."
}
```

---

## Sektion 27 · spiritual_mission (NEU)

```json
"spiritual_mission": {
  "image_caption": "...",
  "intro": "...",
  "composite_sun": "Eure Composite-Sonne im Schützen...",
  "nodes": "Eure Composite-Mondknoten...",
  "learning": "Was lernt ihr durcheinander...",
  "agreement": "Eure Verabredung (in Sacred-Box)...",
  "golden_sentence": "..."
}
```

---

## Sektion 28 · profiles

```json
"profiles": {
  "intro": "...",
  "person1": {
    "Bereitschaft": "43,8 / 100",
    "Emotionale Reife": "8,5 / 10",
    "Kommunikation": "...",
    "Im Konflikt": "...",
    "Stärke": "...",
    "Wachstum": "..."
  },
  "person2": { ...gleiche Struktur },
  "note": "Eine Bemerkung zur Bereitschaft-Zahl...",
  "green": ["...", "...", "..."],
  "yellow": ["...", "..."],
  "red": ["..."]
}
```

---

## Sektion 29 · next_steps

```json
"next_steps": {
  "image_caption": "...",
  "intro": "...",
  "items": [
    {"title": "Qualitätszeit ohne Funktion", "body": "..."},
    ... GENAU 5 Schritte
  ]
}
```

---

## Sektion 30 · closing

```json
"closing": {
  "quote": "Wir sind kein Zufall. Wir sind eine Wahl, die sich jeden Tag neu trifft.",
  "signoff": "Anna und Lena – was zwischen euch ist..."
}
```

---

## Sun-Sign-Codes Mapping

| Code | Deutsch    |
|------|------------|
| Ari  | Widder     |
| Tau  | Stier      |
| Gem  | Zwilling   |
| Can  | Krebs      |
| Leo  | Löwe       |
| Vir  | Jungfrau   |
| Lib  | Waage      |
| Sco  | Skorpion   |
| Sag  | Schütze    |
| Cap  | Steinbock  |
| Aqu  | Wassermann |
| Pis  | Fische     |

---

## Aspekt-Typen für CSS-Farbe

| Begriff      | Farbe   |
|--------------|---------|
| Konjunktion  | blau    |
| Trigon       | grün    |
| Sextil       | grün    |
| Quadrat      | rot     |
| Opposition   | rot     |

---

## Pflicht-Anzahlen pro Sektion (Validation)

| Sektion | Mindest-/Fix-Anzahl |
|---------|----------------------|
| `score.dimensions` | 6 |
| `life_priorities.person1/person2` | 8 Bereiche |
| `elements.person1/person2` | 4 Elemente (Feuer/Erde/Luft/Wasser) |
| `synastry.aspect_table` | 8-12 Aspekte |
| `synastry.aspect_explanations` | **GENAU 6** Erklärungen |
| `composite.bullets` | 4 Bullets |
| `strengths.items` | **GENAU 5** |
| `conflict_map.fields` | 5-6 Felder |
| `karma.rituals` | 3-4 Rituale |
| `crisis.hints` | 3-4 Hinweise |
| `next_steps.items` | **GENAU 5** Schritte |
| `numerology.person1/person2` | je 3 Zahlen (lifepath, soul, destiny) |

---

## Validation-Checkliste vor PDF-Bau

- [ ] Alle Sternzeichen aus echtem API-Call?
- [ ] Aszendent korrekt, NICHT aus Sonnenzeichen abgeleitet?
- [ ] Alle 8+ Aspekte aus echter Synastrie-API?
- [ ] Element-Prozente per `calc_helpers` berechnet, nicht geschätzt?
- [ ] Lebens-Prioritäten per `calc_helpers` berechnet?
- [ ] Goldene Sätze pro Sektion vorhanden?
- [ ] Selbstreflexionsfragen verteilt?
- [ ] Karma-Sektion behutsam, keine "voriges Leben"-Dramatik?
- [ ] Sex-Sektion respektvoll, keine Vulgarität?
- [ ] Keine Familien-/Wohn-/Job-Annahmen?
- [ ] Keine Hetero-Norm?
