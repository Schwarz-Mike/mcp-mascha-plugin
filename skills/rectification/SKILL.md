---
name: rectification-mascha
description: >
  Geburtszeit-Rektifikation via Mascha MCP. Berechnet die wahrscheinlichste
  Geburtszeit anhand bekannter Lebensereignisse. Trigger: Rektifikation,
  Geburtszeit rückrechnen, Geburtszeit berechnen, Geburtszeit unbekannt,
  Geburtszeit ermitteln, Geburtszeitkorrektur, birth time rectification,
  Geburtszeit herausfinden, ungenaue Geburtszeit, Geburtszeit korrigieren.
version: 1.0.0
---

# Rectification Mascha — Geburtszeit-Rektifikation

Berechne die wahrscheinlichste Geburtszeit einer Person anhand bekannter
Lebensereignisse über den `rectification_search` MCP-Endpoint.

---

## Schritt 1 — Basisdaten erfragen

Frage zuerst kompakt nach den Pflichtfeldern:

- **Name** der Person
- **Geburtsdatum** (Tag, Monat, Jahr)
- **Geburtsort** (Stadt + Land / ISO-Ländercode)
- **Ungefähres Zeitfenster** — z.B. "zwischen 8 und 14 Uhr", "Vormittag", "keine Ahnung"
  - Wenn "keine Ahnung" → Fenster 06:00–18:00 Uhr verwenden (Nachtgeburten selten)
  - Anchor = Mitte des Fensters, delta_minutes = halbe Fensterlänge in Minuten

---

## Schritt 2 — Ereignisse erfragen (priorisiert nach Gewichtung)

Präsentiere dem User die Kategorien **nach Wichtigkeit sortiert** und bitte ihn,
für jede bekannte Kategorie Datum + kurze Beschreibung anzugeben.

Stelle diese Frage strukturiert — zeige zuerst die hochgewichteten Kategorien:

```
Bitte nenne mir Lebensereignisse mit möglichst genauen Daten (je genauer, desto besser).
Mindestens 3–5 Ereignisse, ideal 8–12. Datumspräzision: exaktes Datum > Monat/Jahr > nur Jahr.

HÖCHSTE PRIORITÄT (Gewicht 9–10):
- Tod eines Familienmitglieds (Eltern, Geschwister, Grosseltern, nahe Verwandte)
- Heirat / Hochzeit
- Scheidung (rechtskräftig)
- Geburt eines Kindes

HOHE PRIORITÄT (Gewicht 7–8):
- Jobverlust / Kündigung (eigene oder Entlassung)
- Beruflicher Neustart / Karrierewechsel
- Unfall mit Verletzung (auch als Kind — Knochenbrüche, Autounfall etc.)
- Ende einer wichtigen Beziehung

MITTLERE PRIORITÄT (Gewicht 5–6):
- Start einer neuen Partnerschaft
- Operation / chirurgischer Eingriff
- Krankheitsdiagnose
- Umzug in andere Stadt/Region
- Erbschaft / grosse finanzielle Veränderung
- Ausbildungsabschluss / Studienabschluss

NIEDRIG (Gewicht 4–5):
- Spirituelle Erfahrung / religiöse Wende
- Sonstiges bedeutendes Ereignis (Beschreibung angeben)
```

---

## Schritt 3 — Parameter berechnen

Aus dem Zeitfenster:
- `hour` + `minute` = Mitte des Fensters
- `delta_minutes` = halbe Fensterlänge in Minuten
  - "8–14 Uhr" → 6h = 360 Min → anchor 11:00, delta 180
  - "Vormittag" → 6–12 Uhr → anchor 9:00, delta 180
  - "Keine Ahnung" → 6–18 Uhr → anchor 12:00, delta 360 mit step 15
- `step_minutes` = **8** (Standard — gutes Verhältnis Genauigkeit/Kosten)
  - Ausnahme: delta > 300 → step = 12 oder 15 verwenden

Für Jahresdaten ohne Monat: Monat "06" (Mitte des Jahres) einsetzen, date_precision: "month".

---

## Schritt 4 — API-Call

Rufe `rectification_search` mit allen Daten auf. Kein vorheriger
`rectification_event_categories`-Call nötig — die Kategorien sind bekannt.

**Bekannte Kategorie-Keys:**
`marriage`, `divorce`, `child_birth`, `death_family`, `career_change`,
`career_promotion`, `job_loss`, `move`, `accident`, `surgery`,
`health_diagnosis`, `education`, `relationship_start`, `relationship_end`,
`financial_gain`, `financial_loss`, `spiritual`, `other`

---

## Schritt 5 — Ergebnis auslesen (IMMER mit Grep, nie mit Subagent!)

Die Response ist zu gross für den Context und wird in eine Datei gespeichert.
**WICHTIG: Immer Grep verwenden — das ist 10x schneller als ein Subagent.**

### Grep-Calls für alle nötigen Daten:

**Call 1 — Kandidaten + Confidence:**
```
pattern: "rank"|"time"|"aggregate_score"|"grade"|"peak_time"|"level"|"explanation"|"credits_used"|"quality_advisory"|"total_candidates"
output_mode: content
head_limit: 100
```

**Call 2 — ASC des besten Kandidaten (rank 1):**
Lese mit Read offset=100, limit=30 aus der Datei → enthält house_cusps mit ASC.

**Call 3 — Event-Scores des besten Kandidaten:**
```
pattern: "total_score"|"event_category"|"event_date"
output_mode: content
head_limit: 60
```
(Zeigt nur Rank 1 und Rank 2 Event-Scores — reicht für Analyse)

---

## Schritt 6 — Ergebnis präsentieren

Strukturiere die Ausgabe so:

```
## Rektifikation [Name] — Ergebnis

**Bester Kandidat: HH:MM Uhr — ASC [Zeichen] [Grad]° — Grade: [good/fair/excellent]**
Confidence: [low/medium/high]

### Top 5 Geburtszeiten
[Tabelle: Rang | Zeit | Score | Grade | ASC]

### Stärkste Ereignis-Belege (Rang 1)
[Tabelle: Ereignis | Datum | Score | Stärkster Check]

### Interpretation
- Welche Ereignisse haben das Ergebnis am stärksten geprägt?
- Welche Events haben Score 0 → Warnsignal
- Empfehlung: weitere Ereignisse falls Confidence LOW
```

---

## Qualitäts-Regeln

**Confidence LOW** → dem User erklären dass mehr/genauere Ereignisse nötig sind.
Wichtigste Massnahmen:
1. Exacte Daten statt Monat/Jahr
2. Todesfälle in der Familie (höchstes Gewicht = 10)
3. Zeitfenster einengen wenn möglich

**Score 0 bei einem Ereignis** → erwähnen, dass dieses Ereignis für diese Geburtszeit
astrologisch keine Entsprechung findet — kann Hinweis sein, dass Geburtszeit nicht stimmt.

**Confidence MEDIUM/HIGH** → Ergebnis als Empfehlung formulieren, nicht als Gewissheit.
Astrologie ist kein Beweis — Rektifikation ist eine fundierte Einschätzung.

---

## Kosten-Hinweis

- `rectification_event_categories`: 0 Credits (nur bei Bedarf aufrufen — die Keys oben reichen)
- `rectification_search`: **15 Credits pro Call** (fix, unabhängig von Eventanzahl/Schrittgrösse)
- Typisch 1 Call pro Person = 15 Credits
- Bei Nachberechnung mit mehr Events = nochmals 15 Credits

---

## Schnell-Referenz Event-Keys nach Gewicht

| Gewicht | Keys |
|---------|------|
| 10 | `death_family` |
| 9 | `marriage`, `divorce`, `child_birth` |
| 8 | `job_loss`, `career_change` |
| 7 | `accident`, `relationship_end`, `career_promotion` |
| 6 | `surgery`, `health_diagnosis`, `move`, `financial_loss`, `relationship_start` |
| 5 | `financial_gain`, `other`, `education` |
| 4 | `spiritual` |
