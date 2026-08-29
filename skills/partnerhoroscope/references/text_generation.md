# Text-Generation Guidelines

Wie Claude die ~20'000 Wörter Premium-Texte für jeden Bericht schreibt.

## Sprache & Stil

- **Deutsch**, Du-Form
- **Swiss German Rechtschreibung**: "ss" statt "ß" (also "ausserdem", "Schluss", "muss")
- **Kollegial, freundlich, leicht humorvoll**, dennoch professionell und tiefgründig
- **Einfache Sprache**, kein Astrologen-Jargon ohne Erklärung
- **Metaphorisch und bildhaft**, aber keine Esoterik-Floskeln ("Schwingungen", "Energien
  aktivieren" etc. sparsam dosieren)
- **Konkret im Alltag**: Jeder Block sollte mindestens eine umsetzbare Anregung enthalten
- **Bedürfnis-Orientierung**: "Was kann Person A der Person B geben? Was sind die Bedürfnisse?"

## ⚠️ Verbotene Formulierungen / Annahmen

**Niemals annehmen**:
- Dass das Paar Kinder hat ("euer Sohn", "die Kinder", "unser Kind")
- Eine bestimmte Wohnsituation ("der Garten", "die Nachbarn", "die Wohnung")
- Genaue Familienkonstellation ("Schwiegermutter", "Cousine")
- Berufliche Situation ("im Büro", "nach der Arbeit")
- Sexuelle Orientierung / Gender-Rollen-Annahmen
- Beziehungsstatus (verheiratet/verlobt/zusammenwohnend)

**Stattdessen banale, universelle Alltagsszenen**:
- "kommt müde nach Hause"
- "am Morgen", "am Abend"
- "ruhig in den Tag starten"
- "ein Tee zubereiten"
- "spazieren gehen"
- "einen Moment innehalten"

## ⚠️ Faktenintegrität

**Kein einziges astrologisches Faktum darf erfunden werden.** Wenn etwas nicht aus den API-Daten
hervorgeht, lass es weg oder mache es vorsichtig konditional ("Falls ihr ...", "Vermutlich ...").

**Konkret zu prüfen vor jedem Faktum-Satz**:
- Sternzeichen → aus `natal_chart.sun.sign` (mapped)?
- Aszendent → aus `natal_chart.ascendant.sign`? (NICHT raten oder ableiten!)
- Mond → aus `natal_chart.moon.sign`?
- Häuser-Position → aus `natal_chart.<planet>.house`?
- Aspekt + Orb → aus API-Aspect-Liste?

**Common Mistakes (gesammelt aus echten Fehlern)**:
- Aszendent aus Persönlichkeitseindruck "geraten" → IMMER aus API
- "Saturn am Aszendent" geschrieben, obwohl Saturn ganz woanders steht
- "Erdfrau" geschrieben, obwohl Person Feuer-Aszendent hat
- Composite-Aszendent erfunden

## Wer-ist-X Portrait-Sektion

**Aufbau pro Portrait (Anna + Lena bekommen jeder eine eigene Seite)**:

1. **Header** mit Sternzeichen-Symbol + Name + Subtitle
   Subtitle-Format: `"{Sternzeichen} mit {Aszendent}-Aszendent · {Archetyp-Bezeichnung}"`
   Beispiel: "Wassermann mit Fische-Aszendent · Der visionäre Heiler"

2. **2 Absätze Fliesstext** (jeweils 4-6 Zeilen):
   - Absatz 1: Sonne + Aszendent kombinieren, Charakter-Mischung beschreiben
   - Absatz 2: Mond-Position + ein weiterer prägender Planet (Venus, Mars)

3. **Stärken-Liste in Beziehung** (3-5 Bullets mit ✦-Symbol)
   Konkrete Verhaltens-Eigenschaften, KEIN Esoterik-Geschwafel

4. **"Was das für den Partner bedeutet"-Box**:
   - Was die Partner-Person an dieser Person hat (positiv)
   - "Achtung:" — ein konkreter Reibungspunkt mit Tipp

**Sprachregel**: Ich-Du-Form. Person wird direkt angesprochen, nicht in dritter Person.

## Score-Erklärungen

Für jede der 6 Score-Zeilen: **2-3 Sätze**, einfache Sprache, kursiv.

**Format**:
- Was misst der Wert? (1 Satz)
- Wie sieht es bei diesem Paar konkret aus? (1-2 Sätze)

**Beispiel**:
> Eure Planeten reden viel miteinander – und meistens auf gute Art. Hier zählen die direkten
> Verbindungen zwischen euren Geburtshoroskopen. Bei euch überwiegen harmonische Aspekte
> (Trigone, Sextile). Das heisst: Wenn ihr im Raum seid, fliesst es.

## Synastrie-Sektion

**Intro-Text** (3 Absätze):
1. Was ist Synastrie überhaupt? Metapher mit Folien-Übereinanderlegen.
2. Was springt bei diesem Paar besonders ins Auge? (Anzahl exakter Aspekte, Bandbreite)
3. Die 3 wichtigsten Aspekte kurz benennen.

**Reflexions-Box**: 1 offene Frage an das Paar.

**6 wichtigste Aspekte** (in eigener Sektion):

Aspekt-Auswahl-Regeln (für die LLM-Logik):
1. **Priorität 1**: Aspekte mit Orb < 1° (extrem exakt = sehr wirksam)
2. **Priorität 2**: Aspekte zwischen "wichtigen" Punkten:
   - Sonne, Mond, Aszendent, Venus, Mars
   - Chiron-Opposition zu Lichtern (= Heilungsthemen)
   - Pluto-Aspekte (= Transformation)
3. **Priorität 3**: Saturn-Aspekte (= Verbindlichkeit, Reife)
4. **Mischung erwünscht**: 4 harmonische (Trigon/Sextil/Konjunktion) + 2 spannungsreiche
   (Opposition/Quadrat), wenn vorhanden

**Pro Aspekt-Block** (~8-12 Zeilen Text):
- Title: "N. {Planet1} {Aspekt} {Planet2} (Orb X,X°)"
- Was bedeutet dieser Aspekt astrologisch? (2-3 Zeilen)
- Wie äussert sich das bei diesem konkreten Paar? (2-3 Zeilen)
- **Begegnungs-Tipp**: Konkrete Anregung wie das Paar damit umgehen kann (3-4 Zeilen)

## Dynamiken-Sektion

**Pro Box** (kompakt, max 3-4 Zeilen Text):
- Wert (Romantische Partnerschaft / Gleichberechtigt / Stark / Harmonisch)
- 2-3 Sätze Beschreibung
- 1 Satz mit konkretem Tipp bei Bedarf

**Langzeitpotenzial-Box** (etwas länger, 5-6 Zeilen):
- Aussagekräftiger Status (Hoch / Mittel / Erfordert Arbeit)
- Was die Voraussetzungen sind
- **Konkretes Ritual** (z.B. "Plant einmal pro Quartal einen Beziehungs-Abend...")

**Alltags-Tipp-Box** (separat):
- 2 konkrete Frage-Sätze: "{Name1} → {Name2}" und "{Name2} → {Name1}"
- Mit Beispielsätzen in Anführungszeichen
- Kein Familienstand-Annahmen!

## Composite-Sektion

**Intro**: 2 Absätze über das Composite-Konzept.

**4 Bullets**: Composite-Sonne, Composite-Venus-Mars, Composite-Saturn-Aspekt, Composite-Aszendent

**"So vertieft ihr eure Beziehung"-Tipp-Box** (deutlich länger als Standard-Tipp, 3 Absätze):
1. Vision / Wofür sind wir als Paar hier?
2. Konkretes Ritual (z.B. wöchentlicher Check-in)
3. Wie mit dem schwersten Composite-Aspekt umgehen (oft Saturn-Themen)

## Liebessprachen-Sektion

**Intro** (1-2 Absätze): Was die 5 Liebessprachen sind, warum sie wichtig sind.

**Pro Person**:
- "Zeigt Liebe durch: X" (primär)
- "Sekundär: Y"
- "Empfängt am tiefsten: Z"
- Beschreibungs-Text der astrologisch begründet, warum (Venus-Position, Mars)
- 3 Bullet-Punkte "Was diese Person braucht"

**WICHTIG bei Edge-Case sekundäre = empfangene Sprache**:
Erkläre explizit: "Die Tatsache, dass deine sekundäre und Empfangs-Sprache so dicht
zusammenliegen, ist kein Widerspruch: Du zeigst Liebe primär durch X, sekundär durch Y;
fühlst dich aber am tiefsten durch Y geliebt."

**Schnittmenge-Reflexion**: Welche Sprache haben beide gemeinsam? Das ist die Brücke.

**2 konkrete Beispiele**:
- "{Name1} → {Name2} (Aktion statt Worte):" mit banalem Alltagsbeispiel
- "{Name2} → {Name1} (Worte statt Aktion):" mit banalem Beispiel
- KEINE FAMILIEN-/WOHN-ANNAHMEN

## Numerologie-Sektion

**Intro** (1 Absatz): Was Numerologie ist und wie sie Astrologie ergänzt.

**Lebenspfade** (zwei grosse Badges nebeneinander):
- Badge mit Zahl
- Label: "{NAME}S LEBENSPFAD"
- Theme: "Der/Die {Archetyp}"
- Beschreibungstext (~5-7 Zeilen): Was diese Zahl bedeutet, was die Seele lernt

**Tipp-Box "Eure Kombination N + M"**: Wie diese zwei Lebenspfade zusammenwirken.

**Optional: weitere Zahlen** auf eigener Seite:
- Seelendrang (Soul Urge): Was das Herz wirklich will
- Schicksalszahl (Destiny/Expression): Wie die Person in der Welt wirkt

Wenn die zwei Seelendrang-Zahlen kontrastieren (z.B. 5 = Freiheit vs 6 = Familie): Tipp-Box
"Achtung: Mögliche Reibung" einfügen.

**Optional: gemeinsame Jahres-Resonanz** wenn beide im gleichen persönlichen Jahr.

## Stärken-Sektion (5 numerierte Blöcke)

**Pro Block** (~6-8 Zeilen):
- Title: Konkrete Stärke, astrologisch verankert
- Body: Erklärung + **"Was {Name2} {Name1} geben kann"** + **"Was {Name1} {Name2} geben kann"**

Beispiel-Struktur:
```
1. Tragende Sonne-Mond-Resonanz
Annas Sonne im Trigon zu Lenas Mond ist ein **Goldener Faden**. Anna fühlt sich von Lena
emotional gesehen. Lena fühlt sich von Annas Identität geborgen. Diese Achse trägt euch
durch schwierige Zeiten. **Was Lena Anna geben kann:** ungeteilte Aufmerksamkeit, wenn er
heimkommt – die ersten zehn Minuten ohne Handy, ohne Frage nach Aufgaben. **Was Anna Lena
geben kann:** Spiegelung: "Ich habe gespürt, dass du heute aufgewühlt warst – magst du
erzählen?"
```

## Trigger-Sektion (3 numerierte Blöcke)

**Pro Block**:
1. Numerierter Trigger mit astrologischem Aspekt im Titel
2. Body: Was der Trigger ist, warum er menschlich (nicht charakterlich) ist
3. **Tipp-Box** (goldfarben, mit "!"-Symbol):
   - Konkrete Aktionen für beide Personen
   - Beispielsätze in Anführungszeichen
   - Beide Richtungen ({Name1} → {Name2} UND {Name2} → {Name1})

## Profile-Sektion

**Zwei Karten linksbündig** (KEIN justify!):
- Bereitschaft X / 100
- Emotionale Reife X / 10
- Kommunikation: Charakterisierung
- Im Konflikt: Verhalten
- Stärke: konkret
- Wachstum: konkret

**Disclaimer-Absatz**: Bereitschafts-Zahl in Kontext setzen (nicht "Bindungsunfähigkeit").

**Flags**:
- Grün (3-4 Items): Was schon da ist
- Gelb (2-3 Items): Aufmerksam bleiben
- Rot (1 Item oder leer): Meist "Keine ernsthaften Warnsignale"

## Next-Steps-Sektion (5 numerierte Blöcke)

Jeder Schritt:
- Title: Klare Aktion
- Body: Was genau, wie oft, mit welchem Detail
- Konkret und alltagstauglich

Standard-Empfehlungen die fast immer passen:
1. Qualitätszeit ohne Funktion (1 Abend / Woche, definierte Zeit, kein Bildschirm)
2. Übersetzungs-Ritual (jede Liebessprache in die andere übersetzen)
3. Trigger-Pause-Vereinbarung (Signal-Wort, 20 Min Pause)
4. Gemeinsame Vision pflegen (quartalsweise auf Papier)
5. Körper als Anker nutzen (bei Konflikt-Verkanten)

## Closing-Quote

- Eigene letzte Seite (page-break davor)
- Closing-Bild (Unendlichkeit aus Assets)
- Goldene kursive Quote
- 1-2 Sätze Signoff mit beiden Namen
