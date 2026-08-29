---
name: partnerhoroscope
description: >
  Erstellt ein hochwertiges Premium-PDF-Beziehungshoroskop ("Partnerhoroskop") im Mascha
  Cosmos Brand-Stil (Navy, Gold, Cream) für ein Paar. Nutze diesen Skill wenn der User ein
  Beziehungshoroskop, einen Beziehungs-Report, ein Partnerhoroskop, einen Mascha Cosmos
  PDF für ein Paar, eine Synastrie-Auswertung als PDF, eine Astropsychologie-Analyse für
  zwei Personen oder eine vertiefte Paar-Analyse erstellen möchte. Trigger-Phrasen
  "erstelle Beziehungshoroskop", "Partnerhoroskop für", "Mascha Beziehungs-PDF",
  "Synastrie-Report", "Paar-Analyse als PDF", "Compatibility Report für Paar". Der Skill
  ermittelt zuerst einen Speicherort, holt dann alle Daten via MASCHA-MCP API, speichert
  sie in einer klienten_briefing.md (Rohdaten-Snapshot zur Reproduzierbarkeit), generiert
  ein Cover-Bild via KIMASTERMIND_IMAGES, schreibt die Texte in der Mascha-Stilistik
  (Deutsch, Du-Form, einfache Sprache, bedürfnis-orientiert, ohne Familien-Annahmen) und
  baut daraus ein ~50-seitiges A4-PDF mit 30 Sektionen.
version: 1.0.0
---

# Partnerhoroscope (Mascha Cosmos)

Dieser Skill erstellt ein ~50-seitiges Premium-PDF-Partnerhoroskop im Mascha Cosmos
Brand-Stil. Das PDF enthält 30 Sektionen von Cover über Portraits, Score, Lebensprioritäten,
Elemente-Mix, Bedürfnisse, Gefühlsebene, Kommunikation, Liebessprachen vertieft, Werte,
Leidenschaft, Materielles, Beziehungstyp, Synastrie, Aspekte, Dynamiken, Composite,
Numerologie, Stärken+Verantwortung, Schwächen+Schatten, Konfliktlandkarte, Authentizität,
Karma+Heilung, Krisenfähigkeit, sexueller Match, energetische Besonderheiten, spirituelle
Aufgabe, Profile, nächste Schritte bis Closing.

## Wann diesen Skill verwenden

Trigger-Phrasen:
- "erstelle ein Partnerhoroskop für [Person1] und [Person2]"
- "Mascha Cosmos Beziehungs-PDF"
- "Synastrie-Report für ..."
- "astrologische Beziehungsanalyse als PDF"
- "Premium-Compatibility-Report"

## Voraussetzungen

Zwei MCP-Server. Die UUIDs/Tool-Präfixe variieren je nach Claude-Installation, aber die
Tool-Namen sind stabil:

- **MASCHA-MCP** – Astrologie und Numerologie (`mcp.mascha-cosmos.com`).
  Pflicht-Tools: `natal_chart`, `relationship_compatibility`,
  `relationship_compatibility_score`, `relationship_love_languages`,
  `relationship_red_flags`, `relationship_davison` (oder `composite_chart`),
  `numerology_core_numbers`, `synastry_chart`.
  Optionale Tools für die Tiefen-Sektionen: `psychological_analysis`,
  `career_analysis`, `numerology_luck_analysis`, `enhanced_positions`,
  `enhanced_aspects`.

- **KIMASTERMIND_IMAGES** – Cover-Bild-Generation (`mcp.kimastermind.net`).
  Pflicht-Tool: `generate_image`.

Falls Tools nicht direkt verfügbar: `tool_search(query=...)` mit Keywords.

## ⚠️ ZENTRALE REGEL: Keine Halluzinationen

Alle astrologischen Fakten (Sternzeichen, Aszendent, Mondzeichen, Hauspositionen, Aspekte,
Orbs, Element-Verteilungen) und numerologischen Zahlen MÜSSEN aus den MCP-Calls kommen.
Niemals erfinden oder aus dem Sonnenzeichen ableiten.

**Häufige Fehler vermeiden:**
- Aszendent nicht aus Persönlichkeitseindruck "geraten" → IMMER aus `natal_chart.ascendant.sign`
- Mondzeichen nicht raten → IMMER aus `natal_chart.moon.sign`
- "Saturn am Aszendent" nur schreiben, wenn Saturn-Haus 1 im Chart steht
- "Erdfrau" / "Boden-Mensch" nur schreiben, wenn die Person tatsächlich Erd-Aszendent oder
  Erd-Mond hat – nicht aus dem Eindruck ableiten
- Element-Prozente: aus den echten Planetenpositionen rechnen, nicht schätzen

Nach jedem API-Call die Daten in `klienten_briefing.md` und `data.json` zwischenspeichern
und beim Schreiben **ausschliesslich** daraus zitieren.

## Workflow

### Schritt 1: Speicherort bestimmen (ZUERST!)

Bevor irgendwelche Daten geholt werden, kläre mit dem User, **wo die Output-Dateien
gespeichert werden sollen**. Je nach Umgebung:

**Im Claude.ai-Projekt-Modus:**
Frage den User: "Ich kann das Partnerhoroskop für [Name1] & [Name2] erstellen. Wo soll der
Output hin?
- In einen neuen Unterordner in diesem Projekt (z.B. `clients/2026/name1_und_name2/`)
- In einen existierenden Ordner (bitte Namen nennen)
Ich werde dort folgende Dateien anlegen:
1. `klienten_briefing.md` – Rohdaten-Snapshot zur Reproduzierbarkeit
2. `data.json` – Strukturierte Daten für PDF-Generator
3. `cover.jpg` – Generiertes Cover-Bild
4. `partnerhoroscope.pdf` – Das fertige PDF"

**Mit Filesystem MCP (Claude Desktop, lokal):**
Frage den User welcher lokale Pfad gewünscht ist (z.B. `C:\...\clients\maria_und_tom\`).
Default-Vorschlag: ein neuer Unterordner unter dem aktuellen Arbeitsordner.

**Im reinen Web-Chat ohne Projekt:**
Output landet in `/mnt/user-data/outputs/`. Informiere den User: "Im Web-Chat-Modus speichere
ich die Dateien temporär in /mnt/user-data/outputs/. Lade die `klienten_briefing.md` und das
PDF nach Erstellung herunter, damit du sie behältst."

### Schritt 2: Geburtsdaten beim User abholen

Vom User die Geburtsdaten beider Personen erfragen, falls nicht bereits angegeben:
- Vorname (für Anrede im Report)
- Geburtsdatum (TT.MM.JJJJ)
- Geburtszeit (möglichst exakt – beeinflusst Aszendent)
- Geburtsort (Stadt + Land)

### Schritt 3: API-Calls durchführen

Detaillierte Anleitung siehe `references/data_collection.md`. Reihenfolge:

1. `natal_chart` für **beide** Personen (zwingend!)
2. `relationship_compatibility` und `relationship_compatibility_score`
3. `synastry_chart` (Aspekt-Tabelle)
4. `relationship_love_languages`
5. `composite_chart` oder `relationship_davison`
6. `relationship_red_flags`
7. `numerology_core_numbers` für **beide** Personen
8. (optional) `psychological_analysis` für tiefere Sektionen
9. (optional) `enhanced_positions` für Würden + Element-Stärken
10. Cover-Bild via `KIMASTERMIND_IMAGES:generate_image` (siehe `references/image_prompts.md`)

### Schritt 4: klienten_briefing.md schreiben (SOFORT nach API-Calls!)

Direkt nach den API-Calls in den gewählten Speicherort schreiben. Format siehe
`references/klienten_briefing_template.md`. Enthält:
- Beide Geburtsdaten strukturiert
- Astrologische Kernfakten pro Person (Sonne, Mond, Aszendent, Planeten mit Sign+Haus+Grad)
- Numerologische Kernzahlen
- Top 12 Synastrie-Aspekte mit Orbs
- Composite-Hauptpunkte
- Liebessprachen-Rohdaten
- Red-Flags-Rohdaten
- Persönliches Jahr
- Element-Prozente (aus den Planetenpositionen berechnet)
- Datum der Erstellung
- Genutzte Modell-/API-Versionen

**Diese Datei ist der "Goldstandard" für spätere Re-Runs.** Wenn der User das PDF nochmals
mit anderem Text oder Layout will, kann er später nur diese `.md` hochladen und der Skill
generiert ein neues PDF ohne weitere API-Credits.

### Schritt 5: Cover-Bild herunterladen

Bild von der KIMASTERMIND_IMAGES-URL herunterladen (z.B. `wget`/`curl` via `bash_tool`) und
lokal als `cover.jpg` im gewählten Output-Ordner speichern.

### Schritt 6: data.json erstellen

Die gesammelten Daten in die JSON-Struktur giessen, die `build_report.py` erwartet.
Komplette Schema-Definition siehe `references/data_schema.md`.

Bei der Text-Generierung die Vorgaben aus `references/text_generation.md` befolgen:
- Deutsche Du-Form, Swiss German (ss statt ß)
- Mascha-Cosmos-Persona: warm, direkt, modern, psychologisch fundiert. Kein esoterisches
  Geschwätz.
- Anti-Determinismus: "ihr neigt dazu" statt "ihr werdet immer"
- Astrologische Fachbegriffe **fett**: **Sonne im Skorpion**, **Mars Konjunktion Pluto**
- Goldener Satz pro Sektion (fett markiert)
- Selbstreflexionsfragen verteilt einbauen
- Keine Annahmen über Familie, Wohnsituation, Job, Hetero-Norm
- Inklusivität: "eure Kinder oder eure kreativen Projekte"
- Sehr behutsam bei Karma- und Sexual-Sektionen, niemals dramatisch oder reißerisch

### Schritt 7: PDF generieren

```bash
python3 /pfad/zum/skill/scripts/build_report.py \
    /pfad/zur/data.json \
    /pfad/zum/cover.jpg \
    /pfad/output/partnerhoroscope_<name1>_<name2>.pdf
```

Das Skript baut das HTML mit allen 30 Sektionen, embedded Assets, generiert das PDF mit
WeasyPrint.

Das fertige PDF mit `present_files` dem User zeigen, zusammen mit dem Hinweis auf die
gespeicherte `klienten_briefing.md`.

### Schritt 8: Re-Run-Logik

Wenn der User später kommt und sagt: "Generiere das PDF für [Name1] und [Name2] neu mit
folgenden Anpassungen..."

1. User lädt `klienten_briefing.md` hoch (oder gibt Pfad an)
2. Skill liest die `.md` und parst die Rohdaten
3. Skill baut eine neue `data.json` mit den angepassten Texten
4. Skill generiert nur das, was sich geändert hat (z.B. Cover-Bild bleibt, wenn nicht gewünscht)
5. Skill baut neues PDF

**KEINE neuen API-Calls nötig!** Das spart Credits und sorgt für Konsistenz.

## Sektionsstruktur des Reports (30 Sektionen)

1. Cover
2. Intro
3. Eure Kompatibilität auf einen Blick
4. Eure Lebens-Prioritäten im Vergleich (NEU)
5. Eure Elemente-Mischung (NEU)
6. Eure Bedürfnisse im Vergleich (NEU)
7. Eure Gefühlsebene (NEU)
8. Wie ihr miteinander sprecht (NEU)
9. Eure Liebessprachen vertieft (ERWEITERT)
10. Wertesystem und Lebensmission (NEU)
11. Eure Leidenschaftsbereiche (NEU)
12. Materielles, Stabilität, Erdung (NEU)
13. Welcher Typ ist sie, welcher Typ ist er (NEU)
14. Eure Synastrie
15. Die wichtigsten Aspekte zwischen euch
16. Eure Dynamiken
17. Composite
18. Numerologische Resonanz (ERWEITERT)
19. Eure Stärken und Verantwortungs-Verteilung (ERWEITERT)
20. Eure Schwächen und Schatten (NEU)
21. Eure Konfliktlandkarte (ERWEITERT)
22. Authentizität und Masken (NEU)
23. Karmische Wunden und gegenseitige Heilung (NEU)
24. Krisenfähigkeit (NEU)
25. Sexueller Match (NEU)
26. Energetische Besonderheiten (NEU)
27. Spirituelle Aufgabe als Paar (NEU)
28. Eure Beziehungs-Profile
29. Eure nächsten Schritte
30. Closing

## Bundled Resources

- **`scripts/symbols.py`** – SVG-Symbol-Bibliothek (Tierkreis, Planeten, Icons, Numerologie-
  Badges) im Mascha 3D-Gold-Stil.

- **`scripts/build_report.py`** – Hauptskript. Generiert das PDF.

- **`scripts/sections.py`** – Renders pro Sektion (30 Render-Funktionen).

- **`scripts/calc_helpers.py`** – Berechnet Element-Prozente, Haus-Betonungen, Modalitäten
  aus den natal_chart-Daten.

- **`assets/hero_*.webp`** – 12 generische Hero-Bilder (synastry, composite, love, steps,
  closing, strengths, triggers, essence, karma, elements, passion, spiritual).

- **`assets/logo.png`** – Mascha-Cosmos-Logo.

- **`references/data_collection.md`** – Welche MCP-Calls in welcher Reihenfolge.

- **`references/data_schema.md`** – Vollständiges JSON-Schema für `data.json`.

- **`references/text_generation.md`** – Sprach- und Stilrichtlinien.

- **`references/mcp_api.md`** – Detail-Doku der MCP-Endpunkte.

- **`references/image_prompts.md`** – Cover-Bild-Prompt-Template.

- **`references/klienten_briefing_template.md`** – Template für die `klienten_briefing.md`.

- **`references/section_prompts.md`** – KI-Prompts pro Sektion (Lisas Erweiterungen).

## Brand-Konstanten

| Farbe | Hex | Verwendung |
|-------|------|------------|
| Navy | `#0B1629` | Header-Bar, Cover-Boxen |
| Gold | `#EAC973` | Akzente, Symbol-Hauptfarbe |
| Cream | `#EBE7DC` | Seiten-Hintergrund |
| Dark Gold | `#7A4F0F` | 3D-Schatten in Symbolen |
| Highlight | `#FFE9A8` | 3D-Highlight in Symbolen |
| Burnt Gold | `#BA7517` | Sekundärtext, Tipp-Labels |

Schriften: Arial (Body), Cormorant Garamond (Kursivzitate, Numerologie-Zahlen).

## Erinnerung

Der Skill ist namensneutral und funktioniert für jedes Paar. Klientendaten landen NIEMALS
im Skill-Code, sondern werden pro Paar in den vom User gewählten Speicherort geschrieben.
