---
name: astrology-mascha
description: >
  Astrology tools via remote MCP at mcp.mascha-cosmos.com (OAuth via Mascha).
  130 tools: natal/transit/synastry/composite/progression/solar-return/draconic/antiscia/saturn-return/local-space
  charts, horoscopes (daily/weekly/monthly/yearly), relationship compatibility
  & love languages, natal/transit/career/psychological reports, planetary
  positions, fixed stars, Human Design, numerology, profections,
  astrocartography, eclipses, Arabic parts, wellness, Jung archetypes,
  business insights, electional astrology, horary, birth time rectification
  (Rektifikation). Ptolemaic + non-Ptolemaic aspects (Semisextil, Quincunx,
  Quintil, Biquintil). Media: generate_image,
  render_html_to_pdf. Skills: list_skills, get_skill, install_skill (Skill
  installieren/hinzufügen — Partnerhoroskop, Mutter-Kind-Horoskop,
  Rektifikation). German: Geburtshoroskop, Synastrie, Kompatibilität,
  Numerologie, Profektionen, Stundenastrologie, Fixsterne, Rektifikation,
  Geburtszeit-Rückrechnung.
version: 1.15.0
---

# Astrology Mascha — MCP Skill

Remote-MCP-Server für umfassende Astrologie-Tools, angebunden an deinen
Mascha-Account (`app.mascha-cosmos.com`). Berechnet Geburtshoroskope,
Transite, Synastrie, Horoskope, Human Design, Numerologie und
Beziehungs-Insights über [astrology-api.io](https://astrology-api.io).

## Verbinden

**Server-URL**: `https://mcp.mascha-cosmos.com/mcp`

In claude.ai: Settings → Connectors → Add custom connector → URL oben
eintragen. OAuth läuft automatisch; Login mit denselben Credentials wie
auf app.mascha-cosmos.com. Ein Admin muss den MCP-Zugriff einmalig
freischalten (`is_enabled = true` + Credits in Hub-Admin).

## Wie Credits funktionieren

Jeder Tool-Call zieht Credits. Überblick:

| Kategorie | Preis (= 1:1 Upstream) |
|---|---|
| Einfache Daten, Numerologie, Horoskop-Texte, Glossare | 1 Credit |
| `planetary_positions`, `enhanced_positions` | 2 Credits (inkl. house-cusps für Selena/PoF) |
| `aspects` (Ptolemäisch + Nebenaspekte), `non_ptolemaic_aspects` | 2 Credits |
| Charts, Scores, Profektionen, Eklipsen, Horary (Daten) | 2 Credits |
| Reports, Wellness, Fixed Stars, Electional (einfach) | 2–3 Credits |
| Human Design (alle Tools inkl. Glossare) | 5 Credits |
| Astrocartography (alle Tools inkl. Glossare) | 5 Credits |
| Horary (ask, analyze, fertility) | 2–4 Credits |
| SVG-Renderings (Natal/Synastry/Transit/Draconic etc.) | **10 Credits** |
| Profektions-Renders (Rad, Doppelrad) | **10 Credits** |
| Electional Search | 5 Credits |
| Rektifikation Search (delta=60/step=4) | **15 Credits** ⚠️ |
| rectification_event_categories (Glossar) | 1 Credit (0 upstream) |
| generate_image (Evolink GPT-Image-2, medium/1K) | 2 Credits |
| render_html_to_pdf (Puppeteer, A4) | 5 Credits |

Bei zu wenig Credits liefert das Tool `isError: true` mit einer
freundlichen Hinweismeldung ("Nicht genug Credits…" / "Dein Account ist
für MCP nicht freigeschaltet…"). Dann User bitten, sich an die
Mascha-Admin zu wenden.

## Pflicht-Eingaben (Geburtsdaten)

Fast alle Tools brauchen ein Geburtsdaten-Objekt. Typische Felder (flach
als Tool-Parameter, nicht nested):

| Feld | Pflicht | Beispiel |
|---|---|---|
| `year`, `month`, `day`, `hour`, `minute` | **ja** | `1987, 3, 15, 14, 30` |
| `second` | nein | `0` |
| `city` + `country_code` **oder** `latitude` + `longitude` | einer von beiden | `"Zurich", "CH"` |
| `timezone` (IANA) | nein (wird sonst geschätzt) | `"Europe/Zurich"` |
| `name` | nein | `"Anna"` |

Für Zwei-Personen-Tools (Synastrie, Composite, Compatibility, Davison,
Timing): zweite Person mit Suffix `2`: `year2`, `month2`, …, `city2`,
`country_code2`.

Allgemeine Optionen (überall gültig): `language` (`"de"` default,
`"en"`, `"fr"`, `"it"`, `"es"`), `house_system` (`"P"`=Placidus default,
`"W"`=Whole Sign, `"K"`=Koch, `"E"`=Equal), `zodiac_type` (`"Tropic"`
default, `"Sidereal"`), `tradition` (`"universal"` default,
`"classical"`, `"psychological"`), `detail_level` (`"full"` default,
`"standard"`).

## Tools (134 insgesamt)

### Charts (17) — Berechnung · `/api/v3/charts/*`

- **`natal_chart`** (2 Cr) — Volles Geburtshoroskop (Positionen, Häuser, Aspekte)
- **`transit_chart`** (2 Cr) — Aktuelle/spezifische Transite zum Natal. Pflicht: `transit_year/month/day` (+ Stunde/Minute optional). Für den Transit-Ort gilt: `transit_city`+`transit_country` **oder** `transit_latitude`+`transit_longitude`. Wenn nichts angegeben → Fallback auf den Natal-Geburtsort des Subjects (sinnvoll für "Transit bei mir zuhause heute"). Explizit setzen wenn der User woanders ist (Urlaub, Umzug).
- **`synastry_chart`** (2 Cr) — Inter-Aspekte zwischen zwei Charts (technische Beziehungs-Analyse)
- **`composite_chart`** (2 Cr) — Positions-Mittelpunkt zweier Charts (verschmolzenes Beziehungs-Chart)
- **`solar_return_chart`** (2 Cr) — Jahres-Horoskop für das Geburts-Jubiläum (braucht `return_year`, optional Aufenthaltsort)
- **`lunar_return_chart`** (2 Cr) — **Monatliches** Mini-Horoskop: Chart für die nächste Mondrückkehr nach `return_date` (alle ~27,3 Tage). Optional `return_city`/`return_country` für den Aufenthaltsort.
- **`solar_return_transits`** (2 Cr) — Liste der Transit-Ereignisse während des Solar-Return-Jahres (sowohl zu Natal als auch zu SR-Positionen). Default-Zeitraum = das Jubiläumsjahr.
- **`lunar_return_transits`** (2 Cr) — Liste der Transit-Ereignisse während einer Lunar-Return-Periode (~28 Tage). Braucht `return_date`.
- **`progressions_chart`** (2 Cr) — Sekundärprogressionen — symbolische Planetenbewegung (braucht `target_date`, optional `progression_type`)
- **`directions_chart`** (2 Cr) — Klassische Direktionen (default `solar_arc` mit ~0.9856°/Jahr; alternativ `naibod`). Braucht `target_date`. Prognose-Werkzeug für **große Lebenswenden** (jeder Direktion entspricht ~1 Jahr). **Hinweis:** Lisa's Wunsch "solar-arc-planets" ist genau das — keine separates Tool nötig.
- **`natal_transits`** (2 Cr) — Liste kommender Transit-Ereignisse in einem Zeitraum. `start_date`/`end_date` im Format `YYYY-MM-DD`. Beide optional — Default ist heute bis +30 Tage. `orb` optional (default 1°).
- **`venus_return_chart`** (2 Cr) — **Venus-Rückkehr-Chart** (~alle 10 Monate). DER Liebes-/Werte-/Finanzen-Zyklus. Pflicht: `return_date` (ISO `YYYY-MM-DD`). Bei Venus-Retrograde (selten) → Triple-Return, dann `preferred_pass` setzen. Optional `return_city`/`return_country` für Aufenthaltsort.
- **`venus_return_transits`** (2 Cr) — Transit-Trigger innerhalb des Venus-Zyklus. Pflicht: `return_date` + `start_date` + `end_date`.
- **`draconic_chart`** (4 Cr) — **Drakonisches Horoskop**: Natal-Planeten werden um den Mondknoten rotiert (Mondknoten=0°Widder). Zeigt **Seelenmuster und karmische Themen** hinter dem Persönlichkeitshoroskop. Response: `chart_data.planetary_positions` (drakon. Positionen), `draconic_metadata`. `node_type`: Mean_Node (default) oder True_Node (±1.5°). Ideal als Pendant zum Natal für **Seelen-Arbeit, Reinkarnations-Astrologie**.
- **`antiscia_chart`** (4 Cr) — **Antiszie-Chart**: Spiegelung der Natal-Planeten an Sonnenwende-Achse (solstitial 0°Krebs/0°Steinbock, Lilly-Tradition) oder Äquinoktium-Achse (equinoctial = Contra-Antiszie). Response: `natal_chart`, `solstitial_antiscia`, `equinoctial_antiscia`, `antiscia_aspects`. Für **verborgene Aspekte und Spiegelkorrespondenzen**. `include` Default = BEIDE Familien.
- **`saturn_return_chart`** (4 Cr) — **Saturn-Rückkehr-Chart** (~alle 29,5 Jahre). Pflicht: `return_number` (1/2/3 für 1./2./3. Return) ODER `target_date` (ISO YYYY-MM-DD) — genau eines davon. Response: vollständiger Chart + Saturn-spezifische Interpretationshinweise. 1. Saturn-Return (Ende 20er): Erwachsen-werden, Verantwortung; 2. Saturn-Return (Ende 50er): Ernte + Weisheit.
- **`local_space_chart`** (4 Cr) — **Local-Space-Chart**: azimutale Planetenlinien vom Geburtsort. Zeigt Himmelsrichtungen (Azimut) aller Natal-Planeten als Kompassrose. Response: Azimutwerte pro Planet + kardinale Ausrichtungen (N/S/O/W). Optimal kombinierbar mit `render_local_space_chart` für visuelle Darstellung.

### Data (11) — Reine Berechnungsdaten · `/api/v3/data/*`

- **`planetary_positions`** (2 Cr) — Planetenstellungen inkl. Uranus, Neptun, Pluto, Chiron, Lilith, True Node/South Node + **Mean_Selena** (Weißer Mond, astronomische Formel) + **Part_of_Fortune** (Glückspunkt) mit korrektem Haus. Alle 18 Punkte automatisch, kein `active_points`-Parameter nötig.
- **`enhanced_positions`** (2 Cr) — + traditionelle Würden (Domizil, Exaltation, Triplizität)
- **`aspects`** (2 Cr) — **Vollständige Aspekttabelle** in einem Call: Ptolemäische Aspekte (Konjunktion 0°, Sextil 60°, Quadrat 90°, Trigon 120°, Opposition 180°) via API + nicht-ptolemäische Nebenaspekte (Semisextil 30°, Quintil 72°, Biquintil 144°, Quincunx 150°) berechnet aus Positionen. Ergebnis-Feld `non_ptolemaic_aspects` enthält die Nebenaspekte. **Verwende dieses Tool wenn du alle Aspekte auf einmal brauchst** (Aspekttabellen, Huber-Analyse, vollständige Natal-Analyse).
- **`non_ptolemaic_aspects`** (2 Cr) — **Nur nicht-ptolemäische Nebenaspekte**: Semisextil (30°, Orb 2°), Quintil (72°, Orb 2°), Biquintil (144°, Orb 2°), Quincunx (150°, Orb 3°). **Verwende dieses Tool wenn du bereits Ptolemäische Aspekte hast** (aus `aspects`, `natal_chart` o.ä.) und nur die Nebenaspekte ergänzen möchtest. Liefert: `planet1`, `planet2`, `aspect`, `target_angle`, `orb`.
- **`enhanced_aspects`** (1 Cr) — + Rezeptionen, gegenseitige Rezeptionen, Aspekt-Stärke
- **`house_cusps`** (1 Cr) — 12 Häuserspitzen mit Zeichen und Grad
- **`global_positions`** (1 Cr) — geozentrische Positionen für einen Zeitpunkt in **UTC**, ohne Geburtsdaten und **ohne Ort**. Nur `year`/`month`/`day` (+ optional `hour`/`minute`). Für Häuser oder Aszendent stattdessen `planetary_positions` oder `current_moment` mit `city`.
- **`lunar_metrics`** (1 Cr) — Mondphase, Beleuchtung, Void-of-Course
- **`enhanced_lunar_metrics`** (1 Cr) — + lunare Würden, Mansion-Analyse, elektionale Hinweise (`favorable_for`), kommende Timing-Fenster — gut für **Wahl-Astrologie** ("Wann ist ein guter Zeitpunkt für …?")
- **`current_moment`** (2 Cr) — Aktuelle Planetenpositionen + Mondphase für **jetzt**. Ohne Parameter aufrufbar (Positionen für UTC/Greenwich — Zeichen und Grad sind ortsunabhängig). Optional `city` + `country_code`, wenn Häuser oder Aszendent gebraucht werden. Antwort: `moment_utc`, `positions`, `lunar`.
- **`sabian_symbols`** (1 Cr) — Sabian Symbols (1°-Symbolik nach Rudhyar) für alle Natal-Planeten + ASC/MC; pro Punkt: Symbol-Text, Keynote, Keyword. Ideal für **tiefenpsychologische, meditative oder spirituelle Deutungen** der einzelnen Planeten-Stellungen.

### Analysis (8) — Reports mit Interpretationstext (v2 Analysis-Client) · `/api/v3/analysis/*`

- **`natal_report`** (5 Cr) — Natal-Report mit Text-Interpretationen aller Planeten, Aspekte, Häuser
- **`synastry_report`** (5 Cr) — Klassischer Synastrie-Report (älter; für reichere Beziehungs-Analyse `relationship_compatibility` nehmen)
- **`compatibility_score`** (5 Cr) — Numerische Kompatibilität (Gesamt + Kategorien, v2; günstiger via `relationship_compatibility_score`)
- **`transit_report`** (5 Cr) — Transit-Interpretationen für einen Zeitraum
- **`progression_report`** (5 Cr) — Progressions-Interpretationen für ein Zieldatum
- **`solar_return_report`** (5 Cr) — Jahresthemen + Prognosen aus dem Solar Return
- **`career_analysis`** (5 Cr) — Berufung, Karriere-Stärken, Timing
- **`psychological_analysis`** (5 Cr) — Persönlichkeitsstruktur, Entwicklungspotential
- **`jung_archetypes`** (3 Cr) — **12 Jungsche Archetypen** aus dem Natal. Liefert `profile_name` (z.B. "Sovereign-Alchemist"), Top-3 dominante Archetypen mit Texten, `shadow_archetype` (verdrängtes Muster + Integrations-Hinweise), alle 12 Scores in %. Auch nützlich für Berufungs-Hinweise (dominanter Archetyp = natürliche Rolle).

### Relationship Insights (6) — v3 Insights-Client (neu) · `/api/v3/insights/relationship/*`

Reichere Strukturen als die `analysis.*`-Variante. Bei
Beziehungsfragen zuerst diese hier anbieten:

- **`relationship_compatibility`** (5 Cr) — Umfassender v3-Kompatibilitäts-Report (Dynamiken, Stärken, Herausforderungen)
- **`relationship_compatibility_score`** (2 Cr) — Nur numerischer Score (günstig — wenn nur die Zahl gebraucht wird)
- **`relationship_love_languages`** (3 Cr) — Liebessprachen aus **einem** Geburtshoroskop (Single-Subject)
- **`relationship_davison`** (5 Cr) — Davison-Chart: Zeit-/Ort-Mittelpunkt-Chart als Beziehungs-Entität (anders als Composite, das Positions-Mittelpunkte nutzt)
- **`relationship_timing`** (5 Cr) — Optimale Zeitfenster für Beziehungs-Ereignisse (Zusammenziehen, Heirat, Kind, heikle Gespräche)
- **`relationship_red_flags`** (3 Cr) — Warnsignale, Trigger, Schattenthemen aus **einem** Geburtshoroskop (Single-Subject)

### Eclipses (3) — Sonnen-/Mondfinsternisse, Saros-Zyklen · `/api/v3/eclipses/*`

Finsternisse sind die mächtigsten Transit-Ereignisse — Lisa: "MUSS HABEN für Jahresprognosen". Drei Tools mit unterschiedlicher Granularität.

- **`eclipses_upcoming`** (1 Cr) — **Global**, parameterlos: kommende Finsternisse mit NASA-Format-IDs (z.B. `2026Aug12T`), Saros-Series, Pfad. Ideal als Lookup-Quelle für die anderen 2 Eclipses-Tools.
- **`eclipses_natal_check`** (3 Cr) — Personalisiert: welche kommenden Finsternisse aktivieren mein Natal? `impact_score` 0–10 pro Finsternis + aktivierte Punkte. Optional `max_orb` (default 3°).
- **`eclipses_interpretation`** (3 Cr) — Detail-Interpretation einer spezifischen Finsternis. Pflicht: `eclipse_id` (aus `eclipses_upcoming`). Optional Geburtsdaten für personalisierte statt kollektive Themen.

**Typischer Workflow "Was bedeutet die nächste Finsternis für mich?":**
1. `eclipses_upcoming` → Liste, User wählt eine (z.B. höchster Impact)
2. `eclipses_interpretation` mit `eclipse_id` + Geburtsdaten → Saros-Kontext + persönliche Themen

### Traditional (1) — Hellenistische/klassische Techniken · `/api/v3/traditional/*`

- **`arabic_parts`** (3 Cr) — **Arabische Teile / Lots**: Glückspunkt, Geistespunkt, Liebespunkt, **Reichtumspunkt**, **Erfolgspunkt**, Karmapunkt, Sexualitätspunkt etc. Mit Position (Sign + Grad), traditionellen Bedeutungen und sect-basierten Formeln (Tag- vs. Nachtgeburt). Direkter Einsatz in **Geld-Sektion** (Reichtumspunkt) und **Beziehungs-Analysen** (Liebespunkt).

### Astrocartography (13) — Karten-Astrologie, Relocation, Power-Zonen · `/api/v3/astrocartography/*`

Geo-Astrologie für Standort-Entscheidungen, Reise-Planung, Auswanderungs-Beratung.
Geo-Input: `location_city`+`location_country_code` ODER `location_latitude`+`location_longitude`.
Multi-Location-Tools brauchen `locations: [{city, country_code} | {latitude, longitude}]` mit 2-10 Einträgen.

- **`astrocartography_map`** (4 Cr) — SVG-Weltkarte mit Planetenlinien (AC/MC/DS/IC). Klassisches Relocation-Werkzeug, zeigt wo welcher Planet angular wirkt
- **`astrocartography_render`** (4 Cr) — Wie `_map`, aber Format-flexibel: `format=svg|png|jpg|webp`. PNG für E-Mail-Reports, JPG für Social Media
- **`astrocartography_lines`** (3 Cr) — Rohe Linien-Koordinaten (kein SVG) — für Custom-Map-Implementierungen, Mobile-Apps
- **`astrocartography_location_analysis`** (3 Cr) — Detail-Analyse eines Ortes (Pflicht: `location_*`): nearby_lines, relocated_chart, life_area_ratings, overall_score
- **`astrocartography_line_meanings`** (1 Cr) — **Glossar**, keine Geburtsdaten. Was bedeutet Sun-AC? Mars-IC? etc.
- **`astrocartography_supported_features`** (1 Cr) — System-Info: welche Linientypen/Planeten/Formate sind verfügbar
- **`astrocartography_search_locations`** (5 Cr) — Weltweite Suche nach `life_area`: `career | love | creativity | wealth | spiritual | health | family | overall`. Liefert geranktes Städte-Ranking
- **`astrocartography_compare_locations`** (5 Cr) — Side-by-side Vergleich von 2-10 Städten (Pflicht: `locations`). "Soll ich nach Paris, NYC oder Tokyo?"
- **`astrocartography_relocation_chart`** (3 Cr) — Relocated-Natal-Chart (Pflicht: `location_*`). Geburtshoroskop "umsortiert" für einen anderen Ort — Häuser-Cusps verschieben sich, Planeten landen in anderen Häusern
- **`astrocartography_power_zones`** (4 Cr) — Schnittpunkte mehrerer Planetenlinien (z.B. Sun-Jupiter für Karriere, Venus-Jupiter für Liebe, Moon-Venus für Harmonie). Liefert Koordinaten + Stärke-Score
- **`astrocartography_paran_map`** (4 Cr) — Paran-Karte: horizontale Latitude-Bänder mit gleichzeitig angularen Planeten (komplementär zu vertikalen Standard-Linien)
- **`astrocartography_astrodynes`** (4 Cr) — Church-of-Light **Astrodynes**: Power + Harmony numerisch pro Planet. Optional `location_*` für relocated Vergleich. **Quantitatives** System.
- **`astrocartography_astrodynes_compare`** (5 Cr) — Astrodynes-Vergleich mehrerer Städte (Pflicht: `locations`). Datengetriebenes Relocation-Ranking.

**Typischer Workflow "Wohin soll ich auswandern?":**
1. `astrocartography_map` → Überblick aller Linien weltweit (visuell)
2. `astrocartography_search_locations` mit `life_area="overall"` → top 10 Städte
3. `astrocartography_compare_locations` mit den 3-5 vielversprechendsten → detail-Vergleich
4. `astrocartography_location_analysis` für die Top-1-Wahl → tiefere Analyse

### Wellness Insights (6) — Astro-Wellness, Self-Care, Energie · `/api/v3/insights/wellness/*`

Single-Subject (nur Geburtsdaten). Alle Responses enthalten einen Disclaimer
("entertainment purposes only, consult healthcare provider") — Tools ersetzen
keine medizinische Beratung; das in der Antwort an User mitkommunizieren wenn
sinnvoll.

- **`wellness_body_mapping`** (3 Cr) — Körperareale ↔ Tierkreis/Planeten-Herrschaft. Liefert `element_balance` (% Fire/Earth/Air/Water), `sensitive_systems`, `strong_systems`, `sixth_house_sign` (klassisches Gesundheits-Haus), `wellness_focus`, `preventive_care`
- **`wellness_biorhythms`** (2 Cr) — **Klassische Biorhythmen** (physisch/emotional/intellektuell als mathematische Zyklen — *nicht* astrologisch, aber traditionsverbunden) für heute, plus astrologische Anreicherung mit aktueller Mondphase. Werte -1…+1, plus `critical_days`, `overall_vitality`, `recommendations`
- **`wellness_timing`** (3 Cr) — Optimale Zeitfenster für Wellness-Aktivitäten + Mond-Kalender mit Empfehlungen pro Phase. Gut kombinierbar mit `enhanced_lunar_metrics` für **Wahl-Astrologie** ("Wann sollte ich mit Yoga anfangen?")
- **`wellness_energy_patterns`** (3 Cr) — Persönliches Energie-Profil: `chronotype`, `peak_hours`/`low_energy_hours`, `monthly_cycle`, `seasonal_energy` (in welcher Jahreszeit man Hochenergie hat), `exercise_style` (strukturiert/freeform, aus Mars), `recovery_needs` (aus Mond), 3 konkrete `energy_management`-Tipps
- **`wellness_score`** (3 Cr) — **Tagesaktueller Wellness-Score** 0–100 mit 4 Subkategorien (physical_vitality, emotional_balance, mental_clarity, spiritual_connection); aktuelle Transit-Bewertung + Biorhythmus + 1–3 Recommendations + Focus-Areas. Schneller Daily-Check
- **`wellness_moon`** (3 Cr) — 30-Tage-Mond-Wellness-Kalender ab heute: aktuelle Mondphase + Illumination + Mond-Zeichen + Perigäum/Apogäum, plus generische `wellness_guidance` pro Phase (focus / activities / avoid). Brücke zwischen Mond-Astrologie und konkretem Selbstpflege-Verhalten

### Horoscopes (5) — fertig interpretierte Texte · `/api/v3/horoscope/*`

Personalisiert (mit Geburtsdaten):
- **`personal_daily_horoscope`** (1 Cr) — Tageshoroskop **nur für heute**. Ein `date`-Parameter wird vom Endpoint ignoriert. Für andere Tage: `transit_chart` (Chart eines bestimmten Tages) oder `natal_transits` (Transit-Ereignisse im Zeitraum). Für eine **Woche im Voraus**: `natal_transits` mit `start_date`/`end_date`.

Per Sternzeichen (ohne Geburtsdaten, braucht `sign`: Aries, Taurus, Gemini, …):
- **`sign_daily_horoscope`** (1 Cr) — Tageshoroskop pro Sternzeichen
- **`sign_weekly_horoscope`** (1 Cr) — Wochenhoroskop pro Sternzeichen
- **`sign_monthly_horoscope`** (1 Cr) — Monatshoroskop pro Sternzeichen
- **`sign_yearly_horoscope`** (1 Cr) — Jahreshoroskop pro Sternzeichen

### Profections (9) — Jahresherr-Technik · `/api/v3/timing/profections/*` (NEW v1.4.0)

Hellenistische Jahresherr-Astrologie (Vettius Valens): jedes Lebensjahr aktiviert ein Haus. Der Herr dieses Hauses ("Lord of the Year") prägt das Jahr. **anchor** (Standard: `asc`) wählbar: `asc`, `fortune`, `sun`, `moon`, `mc`, `spirit`.

- **`profections_annual`** (2 Cr) — **Jahresprofektionen**: aktiviertes Haus + Lord of the Year für Lebensalter-Range. `start_age`/`end_age` optional (default: 0 bis aktuelles Alter+2). **Einstiegs-Tool** — immer zuerst aufrufen.
- **`profections_monthly`** (2 Cr) — **Monatsprofektionen**: 12 Monate des `age`-Jahres mit Haus + Lord of the Month. Braucht `age`. `include_loy_details` optional.
- **`profections_daily`** (2 Cr) — **Tagesprofektionen**: alle Tage eines Monats im Profektionsjahr. Braucht `age` + `month_index` (0=Geburtsmonat, 11=letzter Monat).
- **`profections_continuous`** (2 Cr) — Exakte Zodiak-Longitude für Dezimal-Alter (z.B. 35.75). Feingranulare Timing-Analyse.
- **`profections_aspects`** (3 Cr) — Aspekte des profektierten Punktes zu Natal-Planeten an `target_date` (default heute). Zeigt welche Natal-Planeten aktiviert werden.
- **`profections_biwheel`** (3 Cr) — Doppelrad-Daten: profektierter Chart (aussen) ↔ Natal (innen). `aspect_types`, `aspect_orb` optional.
- **`profections_wheel_render`** (3 Cr) — **Profektions-Rad als SVG**: Natal mit hervorgehobener Jahresposition + Lord of the Year. `highlight_age` optional (default=aktuelles Alter).
- **`profections_biwheel_render`** (3 Cr) — **Profektions-Doppelrad als SVG**: visuell mit Aspektlinien. `target_date` optional.
- **`profections_house_glossary`** (1 Cr) — Glossar aller 12 Profektions-Häuser mit Themen und Schlüsselwörtern. Parameterlos.

**Typischer Workflow:** `profections_annual` → aktuelles Lebensjahr + Lord → `profections_monthly` → Monat des Ereignisses → `profections_aspects` für Auslöser.

### Render (6) — SVG/PNG-Grafiken · `/api/v3/svg/*` + `/api/v3/render/*`

Liefern Chart als SVG-Text (oder PNG/JPG/WebP/PDF mit `format`-Option):
- **`render_natal_chart`** (3 Cr) — Geburtshoroskop als Grafik
- **`render_synastry_chart`** (3 Cr) — Synastrie zweier Personen als Grafik
- **`render_transit_chart`** (3 Cr) — Transit gegen Natal als Grafik
- **`render_draconic_chart`** (3 Cr) — Drakonisches Horoskop als Grafik
- **`render_antiscia_chart`** (3 Cr) — Antiszie-Chart als Grafik
- **`render_local_space_chart`** (3 Cr) — Local-Space-Chart als SVG: Kompassrose mit azimutalen Planetenlinien. Optional `azimuth_orb` für Kardinalpunkt-Ausrichtungen.

Zusatz-Optionen: `theme` (`light|dark|classic`), `size` (default 800px), `format` (`svg|png|jpg|webp|pdf`).

### Human Design (10) · `/api/v3/human-design/*`

- **`hd_bodygraph`** (3 Cr) — Vollständiges Bodygraph: Typ, Strategie, Autorität, Profil, Definition, 9 Zentren, Tore, Kanäle
- **`hd_type`** (2 Cr) — Nur Type + Strategy + Authority (kompakt, ressourcenschonend)
- **`hd_design_date`** (1 Cr) — Designdatum (88° Sonne vor Geburt, infos-only)
- **`hd_transits`** (3 Cr) — Aktueller (oder bestimmter) HD-Transit-Overlay
- **`hd_compatibility`** (4 Cr) — HD-Kompatibilität zweier Personen: gemeinsame Kanäle, Zentren, elektromagnetische Verbindungen
- **`hd_bodygraph_svg`** (4 Cr) — Bodygraph als SVG / PNG / JPEG / WebP (default PNG, direkt anzeigbar)
- **`hd_compatibility_svg`** (5 Cr) — Kompatibilitäts-Bodygraph zweier Personen als Grafik
- **`hd_glossary_gates`** (1 Cr) — Lexikon: alle 64 Tore (oder einzelnes via `gate=N`)
- **`hd_glossary_channels`** (1 Cr) — Lexikon: alle 36 Kanäle mit Schaltkreis-Zuordnung
- **`hd_glossary_types`** (1 Cr) — Lexikon: 5 HD-Typen mit Strategie und Signatur

### Numerology (5) · `/api/v3/numerology/*`

- **`numerology_core_numbers`** (1 Cr) — Lebenspfad, Ausdruckszahl, Seelendrang, Persönlichkeit, Geburtstag, Reife (braucht `name` + Geburtsdatum)
  - **Wichtig — nur den `pythagorean`-Block verwenden.** Der `chaldean`-Block ist upstream unvollständig: bei `destiny`, `soul_urge` und `personality` sind `raw_total` und `calculation_breakdown` immer `null`, und die Interpretationstexte kommen auch bei `language: "de"` auf Englisch. Nur `chaldean.life_path` ist vollständig (er stammt aus dem Geburtsdatum, nicht aus dem Namen). Chaldean-Zahlen also höchstens als Zusatz nennen, niemals als Grundlage einer Deutung — und keine englischen Passagen ungefragt einbauen.
- **`numerology_comprehensive`** (3 Cr) — Vollständig: Kernnummern, Herausforderungen, Gipfel, Persönliches Jahr/Monat/Tag, karmische Lektionen + Texte
- **`numerology_compatibility`** (3 Cr) — Numerologische Kompatibilität zweier Personen (0–100 + Detail-Zahlen beider)
- **`numerology_zodiac_planet`** (2 Cr) — Hybrid: Numerologie ↔ Planeteneinflüsse + Tierkreis-Resonanzen
- **`numerology_luck_analysis`** (2 Cr) — Glücks-Zahlen, -Farben, -Tage; Timing-Analyse zum optionalen `target_date`

### Email — **derzeit deaktiviert**

Das Tool `email_send` ist auf diesem Server **abgeschaltet** und wird nicht mehr
angeboten. Grund: Der SMTP-Absender ist serverseitig fest und wird von allen
MCP-Nutzern geteilt — Versand würde also unter Mascha-Identität erfolgen.

**Wenn ein Nutzer nach E-Mail-Versand fragt:** freundlich sagen, dass der Versand
über Mascha derzeit nicht verfügbar ist. Den Text stattdessen direkt im Chat
ausgeben, damit er kopiert werden kann — oder bei längeren Auswertungen
`render_html_to_pdf` nutzen und den PDF-Link weitergeben.

Nicht versuchen, den Versand über andere Tools zu umgehen.

### Fixed Stars (5) — Fixsterne im Natal · `/api/v3/fixed-stars/*` (NEW v1.5.0)

Klassische Astrologie: Fixsterne gelten als mächtige Einzelpunkte, besonders bei Konjunktion zu Planeten/ASC/MC (enge Orbs, meist 1-2°). Preset-Auswahl: `essential` (~15 wichtigste, default), `traditional` (~50), `behenian` (15 Behenian Stars), `extended` (>100).

- **`fixed_stars_positions`** (2 Cr) — Positionen aller Fixsterne im Natal: Zodiak-Länge, Deklinierung, Magnitude, Natur (Planeten-Analogie), Natal-Aspekte. Ausgangspunkt für Fixstern-Arbeit.
- **`fixed_stars_conjunctions`** (2 Cr) — **Konjunktionen** (Klassik: nur Konjunktionen!) der Fixsterne zu Natal-Planeten + optional Oppositionen. Pro Konjunktion: Orb, Natur des Sterns, Kurzinterpretation. **Beachte:** Konjunktionen zu ASC und MC sind besonders bedeutsam.
- **`fixed_stars_report`** (4 Cr) — Vollständiger Fixstern-Report mit ausführlichen Interpretationstexten + `summary` (dominant_themes, key_fixed_stars, recommendations). Teurer als `_conjunctions`, dafür mit mehr Text.
- **`fixed_stars_presets`** (1 Cr) — Welche Sterne sind in welchem Preset? Parameterlos. Nutzen um das richtige Preset zu wählen.
- **`fixed_stars_glossary`** (1 Cr) — Lexikon aller bekannten Fixsterne: Name, Konstellation, Planeten-Analogie, Magnitude, traditionelle Bedeutung. Parameterlos.

**Typischer Workflow:** `fixed_stars_conjunctions` (essential preset) → Konjunktionen prüfen → bei Bedarf `fixed_stars_report` für Texte.

### Business Insights (6) — Astro-Business-Coaching · `/api/v3/insights/business/*` (NEW v1.5.0)

Astrologisch fundierte Business-Tools für Führungsstil, Team-Dynamiken, Hiring und Timing. **Kein Ersatz für professionelle Unternehmensberatung.**

Single-Person: `business_leadership_style`. Multi-Person (min. 2): alle anderen. Sonder-Tool: `business_timing` (kein Natal, nur Datum + Aktivitäten).

- **`business_leadership_style`** (4 Cr) — **Führungsstil-Report**: primärer Stil (z.B. "Strategic Visionary"), `action_approach`, `leadership_potential`, `decision_making`, `team_management`, `stress_response`. Ideal für Coaching + Karriere-Beratung.
- **`business_timing`** (4 Cr) — **Günstiges Business-Timing**: `activities` wählen aus `product_launch`, `meetings`, `negotiations`, `hiring`, `restructuring`. `start_date`/`end_date` optional (default: heute + 30 Tage). Optionale `company_data` (Gründungsdatum/-ort) für Corporate-Chart-Analyse.
- **`business_team_dynamics`** (5 Cr) — Team-Dynamiken zwischen 2 Personen: synergies, tensions, communication_styles, collaboration_recommendations, risk_areas.
- **`business_hiring_compatibility`** (5 Cr) — Kandidat (Person 1) vs. Hiring Manager (Person 2): compatibility_score, working_style_match, onboarding_recommendations, role_fit_factors.
- **`business_department_compatibility`** (5 Cr) — Abteilungsübergreifend: cross_department_dynamics, collaboration_potential, synergy_areas, friction_points, structural_recommendations.
- **`business_succession_planning`** (5 Cr) — Person 2 als Nachfolger von Person 1: succession_fit, leadership_transition, continuity_factors, development_areas, handover_strategy.

**Multi-Person-Schema:** Person 1 = normale Felder (`year`, `month`, …), Person 2 = Suffix `2` (`year2`, `month2`, …, `city2`, `country_code2`).

### Electional Astrology (4) — Wahl-Astrologie · `/api/v3/electional/*` (NEW v1.5.0)

Wahl-Astrologie: optimale Zeitpunkte für Aktivitäten finden und bewerten. Valide Aktivitätsnamen via `electional_activities_glossary` ermitteln.

- **`electional_activities_glossary`** (1 Cr) — **Zuerst aufrufen**: Lexikon aller unterstützten Aktivitätstypen (wedding, surgery, business_launch, travel, signing_contract …). Parameterlos.
- **`electional_planetary_hours`** (2 Cr) — **Planetenstunden**: welcher Planet die aktuelle Stunde regiert (chaldäische Reihenfolge: Saturn-Jupiter-Mars-Sonne-Venus-Merkur-Mond). `include_full_day=true` für alle 24 Stunden. Ideal als schneller Check: "Ist jetzt eine gute Stunde für X?"
- **`electional_evaluate`** (2 Cr) — **Moment-Bewertung**: konkreten Zeitpunkt für Aktivität bewerten → Score 0-100, Stärken/Schwächen, Planetenstunde, Mondphase. Optionaler Natal-Kontext für personalisierte Auswertung.
- **`electional_search`** (8 Cr ⚠️) — **Zeitraum-Suche**: beste Zeitfenster für Aktivität in Datumsbereich suchen → optimal_windows mit Score + Begründung, best_moment, avoid_periods. **Teuer** (5 Cr upstream) — nur wenn echte Suche nötig ist; für einfache Bewertung stattdessen `electional_evaluate`.

**Typischer Workflow:** `electional_activities_glossary` → valide activity-Werte → `electional_evaluate` für konkrete Termine → `electional_search` nur wenn Optimalzeit unbekannt.

### Horary — Stundenastrologie (7) · `/api/v3/horary/*` (NEW v1.6.0)

Stundenastrologie beantwortet konkrete Fragen aus dem Chart des **Fragemomentes** (nicht des Geburtsmomentes). Klassische Technik (Lilly, al-Qabisi). **Alle 2 Cr upstream.**

**Wichtigste Regel:** `question_time` = Datum+Zeit+Ort **wann die Frage verstanden wurde** (nicht wann sie gestellt wurde — der Moment des "Verstehens" zählt). Exakte Uhrzeit ist entscheidend.

- **`horary_ask`** (4 Cr) — ⭐ **Einfachster Einstieg**: natürlichsprachige Frage ("Werde ich den Job bekommen?") + Fragemomen → AI klassifiziert Kategorie + vollständige Analyse + `ai_answer` (Ja/Nein/Vielleicht mit Begründung + `radicality` (Chartfitness-Check). Empfohlener Startpunkt.
- **`horary_analyze`** (4 Cr) — Strukturierter als `horary_ask`, mit expliziter `category`. Gibt `significators` (Fragesteller + Befragtes), `aspect_perfections`, `judgment`. `include_timing=true` für Zeitvorhersagen. Kategorien: pregnancy|fertility|love|marriage|career|job|money|health|missing_item|travel|general.
- **`horary_chart`** (3 Cr) — Roher Chart ohne Urteil (Positionen, Häuser, Würden). Für manuelle Interpretation.
- **`horary_aspects`** (3 Cr) — Anwendende Aspekte sortiert nach Graden-zur-Perfektion + Zeichen-Eintritte + Stationen. Kern der Horary-Technik ("Was wird sich verbinden?").
- **`horary_fertility`** (4 Cr) — Spezialisiert für Fruchtbarkeit/Schwangerschaft: Mondsequenz + 5. Haus + Konzeptionsfenster (`include_timing=true` empfohlen). ⚠️ Kein Ersatz für Medizin.
- **`horary_considerations_glossary`** (2 Cr) — Die 8 klassischen Raikalitäts-Tests: Void of Course Moon, Saturn in 7th, Early/Late Degrees, Via Combusta, etc. Parameterlos.
- **`horary_categories_glossary`** (2 Cr) — Alle Fragekategorien mit Significatoren + validen subcategory-Werten. Parameterlos. Vor `horary_analyze` aufrufen um richtige Kategorie zu wählen.

**Typischer Workflow "Ja/Nein-Frage stellen":**
1. `horary_ask` mit `question` + aktuellem Zeitpunkt+Ort → vollständige Antwort
2. Falls `radicality` Warnungen: `horary_considerations_glossary` für Erklärung der Tests
3. Für tiefere Aspekt-Analyse: `horary_aspects` zusätzlich aufrufen

**Subject Role** (für `horary_analyze`): `self` (standard), `spouse_partner`, `third_party_employer`, `third_party_friend`, `third_party_parent`, `third_party_child`, `third_party_sibling`, `third_party_enemy`, `third_party_other` — für "Fragen über andere Personen".

### Account (4) — eigene Daten aus der Mascha-App (NEW v1.25.0)

Diese vier Tools lesen **direkt aus der Mascha-Datenbank** — kein Upstream-Call, keine
Neuberechnung, je 1 Credit. Sie funktionieren ohne Parameter, weil die Identität aus der
OAuth-Anmeldung stammt.

- **`my_account`** (1 Cr) — eigenes Konto: Name, **Sterne-Guthaben**, hinterlegte
  Geburtsdaten, Anzahl der angelegten Personen. **Guter Einstiegspunkt**: Sind die
  Geburtsdaten hinterlegt, müssen sie nicht erfragt werden.
- **`my_radix`** (1 Cr) — das eigene, bereits gespeicherte Geburtshoroskop: Big Three,
  Planeten mit Zeichen und Haus, zwölf Häuserspitzen, Elemente- und Qualitätenbilanz,
  engste Aspekte. **Schneller und günstiger als `natal_chart`**, wenn es um die eigene
  Person geht. Liegt nichts vor, meldet die Antwort `kein_gespeichertes_radix`.
- **`list_sub_users`** (1 Cr) — die Personen des Kontos (Familie, Klientinnen, Partner) mit
  Name, Geburtsdatum, -zeit, -ort und `sub_user_id`.
- **`sub_user_radix`** (1 Cr) — gespeichertes Radix einer dieser Personen. `sub_user_id`
  vorher via `list_sub_users` ermitteln. Es sind ausschliesslich Personen des eigenen
  Kontos abrufbar.

**Typischer Ablauf:** `my_account` → Guthaben und Geburtsdaten prüfen → `my_radix` für die
eigene Analyse, oder `list_sub_users` + `sub_user_radix` für eine andere Person. Erst wenn
kein gespeichertes Radix vorliegt, auf `natal_chart` mit expliziten Geburtsdaten ausweichen.

### Skills Marketplace (3) (NEW v1.6.0 · `install_skill` seit v1.11.0)

Meta-Tools zum Entdecken, Laden und Installieren von Skill-Definitionen (SKILL.md-Dateien) auf diesem Server:

- **`list_skills`** (1 Cr) — Listet alle verfügbaren Skills mit Name, Version, Beschreibung.
- **`get_skill`** (1 Cr) — Gibt vollständigen SKILL.md-Inhalt zurück. `name` aus `list_skills`. **Nur für die laufende Session.**
- **`install_skill`** (1 Cr) — **Dauerhafte Installation.** Liefert Zielpfad + vollständigen Inhalt; der Client legt die Datei an. Parameter: `name`, optional `scope` (`user` = `~/.claude/skills/`, Standard · `project` = `.claude/skills/`).

**Wann was?** Einmalig etwas nachschlagen → `get_skill`. Der User will den Skill behalten
("installier mir das", "hätte ich gern dauerhaft") → `install_skill`.

Öffentlicher HTTP-Endpoint: `GET https://mcp.mascha-cosmos.com/skills/index.json`

**Verfügbare Skills auf diesem Server:**

| Name | Laden (Session) | Installieren (dauerhaft) |
|---|---|---|
| `astrology-mascha` | `get_skill name: "astrology-mascha"` | `install_skill name: "astrology-mascha"` |
| `rectification-mascha` | `get_skill name: "rectification"` | `install_skill name: "rectification"` |
| `partnerhoroscope` | `get_skill name: "partnerhoroscope"` | `install_skill name: "partnerhoroscope"` |
| `mutter-kind-horoskop` | `get_skill name: "mutter-kind-horoskop"` | `install_skill name: "mutter-kind-horoskop"` |

**`rectification-mascha`** (v1.0.0) — Vollständiger Workflow für Geburtszeit-Rektifikation: Basisdaten erfragen, Ereignisse priorisieren, Parameter berechnen, API-Call ausführen, Response per Grep auslesen, Ergebnis strukturiert präsentieren. **Vor einer Rektifikation immer diesen Skill laden!**

**`partnerhoroscope`** (v1.0.0) — Erstellt ein ~50-seitiges Premium-PDF-Beziehungshoroskop im Mascha Cosmos Brand-Stil für ein Paar (30 Sektionen: Portraits, Synastrie, Composite, Liebessprachen, Konfliktlandkarte …). **Bei jedem Partner-/Beziehungs-PDF diesen Skill laden.**

**`mutter-kind-horoskop`** (v1.0.0) — Erstellt ein ~35-seitiges Premium-PDF Mutter-Kind- bzw. Eltern-Kind-Horoskop: ein Elternteil versteht sein Kind in der Tiefe (Wesen, Gefühle, Kommunikation, Herausforderungen, Eltern-Kind-Synastrie, Selbstfürsorge). Funktioniert für Mutter/Vater × Sohn/Tochter. **Bei jedem Kind-Report für Eltern diesen Skill laden.**

> **Hinweis für dich als Assistent:** Wenn eine Anfrage klar zu einem dieser Spezial-Skills
> gehört (Partner-PDF, Kind-Report, Rektifikation), lade ihn **bevor** du mit der Arbeit
> beginnst — er enthält den vollständigen Workflow, das PDF-Layout und die Brand-Regeln.
> Baue solche Reports niemals frei aus diesem Skill heraus.

### Rectification (2) — Geburtszeit-Rektifikation · `/api/v3/rectification/*` (NEW v1.8.0)

Rektifikation = Rückrechnung der genauen Geburtszeit anhand bekannter Lebensereignisse (Heirat, Todesfall, Jobwechsel, Umzug, Unfall, …). Wenn die Geburtszeit unbekannt oder ungenau ist, liefert dieser Ansatz gerankete Kandidaten-Zeiten mit Wahrscheinlichkeits-Score.

**Pflicht:** Mindestens 1 Lebensereignis mit Datum + Kategorie. `hour`/`minute` = ungefähre Geburtszeit als Suchankerpunkt.

- **`rectification_event_categories`** (1 Cr, 0 upstream) — **Zuerst aufrufen**: Lexikon aller unterstützten Ereignis-Kategorien (`marriage`, `death_family`, `career_change`, …). Optional `language`-Parameter. Liefert `key` (für `rectification_search`), `label`, `description`.
- **`rectification_search`** (**15 Cr ⚠️** bei delta=60/step=4) — **Rektifikations-Suche**: prüft alle Geburtszeiten im Suchfenster (`delta_minutes`) in `step_minutes`-Schritten und berechnet für jede Zeit den astrologischen Score gegen die Ereignisse. Kosten skalieren mit Anzahl geprüfter Zeitpunkte (`2 × delta_minutes / step_minutes`). Response: `candidates` — gerankete Kandidaten mit `rank`, Score, Aszendent-Grad/-Zeichen + vollständigem Chart; **bester Match = Kandidat mit `rank: 1`** (kein separater `best_match`-Key). Drei Modi:
  - `around_anchor` (Standard): Suchfenster ±`delta_minutes` um Ankerpunkt
  - `explicit_range_with_asc_constraint`: Suche mit bekanntem Aszendent-Zeichen als Constraint
  - `single_moment`: Nur genau einen Zeitpunkt prüfen (zur Validierung, günstig)

**Typischer Workflow "Geburtszeit unbekannt":**
1. `rectification_event_categories` → valide `category`-Werte ermitteln
2. Ereignisse sammeln: Datum + Kategorie (mind. 3–5 Ereignisse für bessere Genauigkeit)
3. `rectification_search` mit `delta_minutes: 60`, `step_minutes: 4` → Kandidaten-Liste (15 Cr)
4. Bester Match = Kandidat mit `rank: 1` → mit `natal_chart` verifizieren — passt Aszendent zur Person?

**Kostenkontrolle:** Kleineres Suchfenster (`delta_minutes`) und größere Schrittweite (`step_minutes`) sparen Credits. Für erste grobe Suche: `delta_minutes: 30`, `step_minutes: 10` (günstig). Für Feinabstimmung: `delta_minutes: 15`, `step_minutes: 2`.

**Hinweis:** Wenn nur Monat bekannt: `date_precision: "month"` setzen. Je mehr Ereignisse, desto präziser das Ergebnis.

### Media (2) — server-seitige Generierung (NEW v1.7.0)

- **`generate_image`** (2 Cr) — KI-Bildgenerierung via Evolink/GPT-Image-2 (medium, 1K). Async (max ~100s). Bild 24h abrufbar unter `mcp.mascha-cosmos.com/generated-images/<uuid>.webp`. Parameter: `prompt` (Pflicht), `size` (optional, z.B. `"16:9"`, `"1024x1024"`).
- **`render_html_to_pdf`** (5 Cr) — HTML-String → A4-PDF via Puppeteer/Chromium. PDF 24h unter `mcp.mascha-cosmos.com/generated/<filename>.pdf`. Bilder im HTML als absolute URLs einbinden (werden beim Rendering geladen). Parameter: `html` (Pflicht), `filename` (optional).

## Parameter-Fallstricke (aus dem Vollaudit 2026-08-25)

Diese Punkte führen sonst zu Fehlern:

- **`sign` immer englisch und grossgeschrieben**: `Aries`, `Taurus`, … `Pisces`.
  Kleinschreibung wird abgelehnt.
- **`saturn_return_chart`**: entweder `return_number` ODER `target_date` — niemals beides,
  das gibt sonst einen Fehler.
- **`global_positions`** kennt keinen Ort (siehe oben).
- **Numerologie** braucht `name` (der vollständige Geburtsname), nicht `full_name`.
- **Zeiträume** (`transit_report`, `electional_search`): `start_date`/`end_date` als
  ISO-String `YYYY-MM-DD` übergeben — die Umwandlung ins API-Format macht der Server.
- **Render-Tools** liefern bei `format: svg` reines SVG, bei `png`/`jpg`/`webp`/`pdf`
  einen Base64-Data-URI. `hd_bodygraph_svg` gibt PNG direkt als Bild zurück.

## Typische Workflows

### "Erzähl mir über mein Geburtshoroskop"
1. Fehlt etwas: nach Geburtsdatum/Zeit/Ort fragen
2. `natal_chart` — rohe Daten (Positionen, Häuser, Aspekte)
3. `natal_report` — Textinterpretation in Prosa zusammenfassen

### "Wie passen wir zusammen?" (zwei Geburtsdaten)
1. `relationship_compatibility` — v3-Report (reichster Output)
2. Optional `relationship_compatibility_score` für die harte Zahl
3. Optional `synastry_chart` wenn technische Details gefragt

### "Wie wirst du heute mit den Sternen stehen?"
1. Bei Geburtsdaten → `personal_daily_horoscope` (nur heute!)
2. Ohne Daten, nur Sternzeichen → `sign_daily_horoscope`

### "Horoskop für morgen / einen bestimmten Tag"
`personal_daily_horoscope` funktioniert hier **nicht**. Stattdessen:
1. `transit_chart` mit `transit_day/month/year` und optional `transit_hour/minute` → rohe Transit-Daten für den Tag
2. Interpretation durch Claude (deterministische Fakten + Stilisierung)
3. Alternativ `natal_transits` mit `start_date`/`end_date` für eine Liste kommender Transit-Ereignisse

### "Was sind meine Liebessprachen?"
→ `relationship_love_languages` (Single-Subject)

### "Mein Human Design"
1. `hd_bodygraph` — vollständig
2. Optional `hd_bodygraph_svg` für Grafik
3. Bei Begriffen ("Was ist das 7. Gate?") → `hd_glossary_gates`

### "Wann ist ein guter Moment für einen wichtigen Schritt in unserer Beziehung?"
→ `relationship_timing`

### "Volle Numerologie" (braucht `name`!)
1. `numerology_core_numbers` — wichtigste 4 Zahlen
2. Oder `numerology_comprehensive` für alles auf einmal

### Huber-Methode (Bruno & Louise Huber) — Koch + Farb-Aspekte

Die Huber-Schule arbeitet mit **Koch-Häusern** und einem Drei-Farben-Aspektsystem. Bei jeder Huber-Analyse `house_system: "K"` bei ALLEN Tool-Calls mitgeben!

**Farb-Klassifikation der Aspekte:**

| Farbe | Aspekte | Charakter |
|---|---|---|
| 🔴 Rot (Spannungsaspekte) | Quadrat (90°), Opposition (180°) | dynamisch, treibend, konfliktiv |
| 🔵 Blau (Harmoniaspekte) | Trigon (120°), Sextil (60°) | stabil, fließend, unterstützend |
| 🟢 Grün (Sensitiv-Aspekte) | Semisextil (30°), Quintil (72°), Biquintil (144°), Quincunx (150°) | sensibel, lernend, ambivalent |
| ⚪ Neutral | Konjunktion (0°) | Wirkung abhängig von beteiligten Planeten |

**Workflow Huber-Analyse:**
1. `natal_chart` mit `house_system: "K"` — Koch-Häuser, Positionen, Ptolemäische Aspekte
2. `aspects` mit `house_system: "K"` — liefert zwei Felder im Response:
   - Ptolemäische Aspekte (Hauptfeld) → nach Rot/Blau klassifizieren (siehe Tabelle oben)
   - **`non_ptolemaic_aspects`** (separates Array im Response) → **das sind ALLE grünen Aspekte (Sensitiv-Aspekte)**. Dieses Feld vollständig auslesen und als grüne Aspekte verwenden — es enthält Semisextil, Quintil, Biquintil, Quincunx mit exaktem Orb.
3. Aspekte nach Farbe gruppieren: Rot-Aspekte / Blau-Aspekte / Grün-Aspekte (= `non_ptolemaic_aspects`)
4. Übergewichte analysieren (viele Rot = Spannung dominiert; viele Grün = Über-Sensibilität; wenig Blau = fehlende Stabilität)
5. Optional: `natal_report` mit `house_system: "K"` für Interpretationstexte
6. Optional: `enhanced_aspects` mit `house_system: "K"` für Aspekt-Stärke-Bewertung

**Orbs im Tool:** Semisextil/Quintil/Biquintil 2°, Quincunx 3° — entspricht Standard-Huber-Toleranzen. Den `orb`-Wert im Response für Feinbewertung verwenden (enger Orb = stärkerer Aspekt).

**Häuser nach Huber:** Koch-Häuser (nicht Placidus!) zeigen die psychologische Thematik der Häuser nach Huber-Schule anders als Placidus. Das Koch-System ist zwingend für eine authentische Huber-Auswertung.

### "Schicke mir mein Tageshoroskop per Mail"
E-Mail-Versand ist derzeit deaktiviert (siehe Abschnitt *Email*). Stattdessen:
1. `personal_daily_horoscope` — Horoskop-Text holen
2. Text direkt im Chat ausgeben, damit der User ihn kopieren kann
3. Bei längeren Auswertungen: HTML bauen + `render_html_to_pdf` → PDF-Link weitergeben

## Sprach-Handling

Default ist Deutsch (`language: "de"`). Wenn der User in einer anderen
Sprache schreibt oder explizit wünscht: `language`-Parameter setzen
(`"en"`, `"fr"`, `"it"`, `"es"`, auch `"pt"`, `"ru"`, `"nl"`, `"pl"`
verfügbar).

## Error-Handling

- **MCP-Server nicht erreichbar / "down"**: Dem User erklären, dass
  der MCP-Connector kurz neu verbunden werden muss:
  - **Claude Desktop**: Einstellungen → Entwickler → MCP-Server →
    Server neu starten oder App neu starten
  - **claude.ai**: Einstellungen → Anpassen → Konnektoren →
    `mcp.mascha-cosmos.com` → Verbindung neu laden / Tools neu laden
  - Dies ist nötig nach Server-Updates oder kurzer Inaktivität
- **"Die Astrology-API ist momentan nicht erreichbar" (HTTP 502/503/504)**:
  Upstream-Ausfall bei astrology-api.io — ausserhalb unserer Kontrolle.
  Dem User sagen, er soll es in einigen Minuten erneut versuchen.
  Kein Retry sofort — der Ausfall dauert typisch 5–60 Minuten.
- **401 / OAuth**: Connector muss neu verbunden werden (siehe oben)
- **`isError: true` mit "nicht freigeschaltet"**: User wendet sich an
  Admin von `app.mascha-cosmos.com`
- **`isError: true` mit "Nicht genug Credits"**: dito, Aufladung
  nötig — nicht einfach weiterklicken mit niedrigeren Kosten
- **Unplausible Geburtsdaten**: Daten mit User verifizieren (Jahr vor
  1900? Zeit > 23:59? Ort unbekannt?) bevor Tool erneut aufgerufen wird
- **Lange Wartezeiten** (>10s): normal bei Reports, besonders
  `..._report`, `relationship_*` und `psychological_analysis` — nicht
  vorschnell retryen

## Tipps für gute Resultate

1. **Präzise Geburtszeit** zählt — ohne Minutengenauigkeit ist
   Ascendent/Häuser-Analyse ungenau. Bei "circa Nachmittag": ehrlich
   erwähnen, dass Häuser unsicher sind
2. **Ort wichtig**: `city` + `country_code` meistens ausreichend, bei
   kleinen Orten notfalls `latitude`/`longitude` direkt
3. Bei **mehreren Personen**: Nach jeder zweiten Person einzeln fragen
   statt alle auf einmal — verhindert Verwechslungen bei den `*2`-Feldern
4. Für **Reports** erstmal kurze Zusammenfassung + Frage, was der User
   vertiefen will — nicht 10.000 Zeichen Output auf einmal
5. Bei **Horoskop-Texten** (Sign-Horoscopes): Das sind generische
   Interpretationen per Zeichen, keine Natal-Analyse
