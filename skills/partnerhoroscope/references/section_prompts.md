# Section Prompts – Lisas KI-Anweisungen pro Sektion

Diese Datei enthält die **konkreten KI-Prompts pro Sektion**, wie Lisa sie für die
Text-Generierung definiert hat. Sie ergänzt `text_generation.md` (Stilrichtlinien) mit
sektions-spezifischen Anweisungen.

**Wichtig:** Alle astrologischen Fakten kommen IMMER aus den MCP-Calls (siehe
`data_collection.md`). Diese Prompts beschreiben die **Text-Erzeugung** auf Basis dieser
Fakten – nicht die Fakten selbst.

---

## Universelle Stil-Regeln (für jede Sektion)

- **Mascha Cosmos Persona:** warm, direkt, modern, psychologisch fundiert. Kein
  esoterisches Geschwätz.
- **Du/Ihr-Form:** beide Personen direkt ansprechen.
- **Anti-Determinismus:** keine "ihr werdet immer", "ihr müsst". Stattdessen "ihr neigt
  dazu", "viele Paare mit dieser Konstellation".
- **Astrologische Fachbegriffe immer fett:** `**Sonne im Skorpion**`,
  `**Mars Konjunktion Pluto**`.
- **Goldener Satz pro Sektion:** ein verdichteter Satz, fett markiert in eigener
  Quote-Box (`golden_quote` CSS).
- **Inklusivität:** keine Hetero-Norm voraussetzen, "eure Kinder oder eure kreativen
  Projekte" etc.
- **Konkrete Alltagsbeispiele** statt abstrakter Astro-Sprache.
- **Beide Personen gleichmäßig behandeln** (niemals Partei nehmen).
- **Selbstreflexionsfragen** verteilt einbauen.

---

## SEKTION 4 · Eure Lebens-Prioritäten im Vergleich (NEU)

**Was es ist:** Visualisierung was jedem im Leben wichtig ist.

**Layout:** Zwei nebeneinanderliegende Balken-Diagramme mit je 8 Lebensbereichen in
Prozent. Darunter Fließtext.

**KI-Prompt:**

```
Analysiere für beide Personen ihre Lebens-Prioritäten basierend auf Haus-Betonungen und
Planeten-Verteilung. Die Prozent-Werte kommen aus calc_helpers.py::calc_life_priorities().

8 Bereiche:
- Ich, Selbstentfaltung (1. Haus, Sonne, Aszendent)
- Partnerschaft (7. Haus, Venus)
- Beruf, Berufung (10. Haus, MC, Saturn)
- Familie, Wurzeln, Zuhause (4. Haus, Mond, IC)
- Kinder, Kreativität, Schöpfen (5. Haus)
- Finanzen, Sicherheit (2. und 8. Haus)
- Freundschaft, Gemeinschaft (11. Haus)
- Spiritualität, Rückzug (12. Haus, Neptun)

Schreibe danach 3 bis 4 Absätze:
- Wo seid ihr euch einig in den Prioritäten?
- Wo liegen eure größten Unterschiede?
- Welche Lebensbereiche sind bei einem stark, beim anderen kaum?
- Wer von euch ist mehr nach innen orientiert, wer nach außen?

Konkrete Beispielsätze nutzen:
"Wenn [Name 1] Karriere als oberste Priorität trägt und [Name 2] Familie, dann passiert
im Alltag dass..."

Schließe mit einem goldenen Satz.
```

**Länge:** 250-400 Wörter plus Visualisierung.

---

## SEKTION 5 · Eure Elemente-Mischung (NEU)

**Layout:** 4 horizontale Balken pro Person (Feuer/Erde/Luft/Wasser in Prozent),
darunter 5 Unter-Abschnitte.

**KI-Prompt:**

```
Berechne für beide Personen die prozentuale Element-Verteilung (Feuer, Erde, Luft,
Wasser) im Chart über calc_helpers.py::calc_element_distribution().

Schreibe dann 5 Unter-Abschnitte:

1. Element-Mix des Paares: was dominant, was fehlt
2. Wo eure Elemente sich verbinden (gleich starke Elemente)
3. Wo eure Elemente reiben (z.B. Feuer trifft Erde = Visionär trifft Pragmatikerin)
4. Was fehlt im Paar-System (wenn ein Element bei beiden unter 15%):
   - Wenig Feuer: gemeinsame Begeisterung muss bewusst gesucht werden
   - Wenig Erde: schnell aneinander vorbei, braucht Erdung
   - Wenig Luft: zu wenig Reden
   - Wenig Wasser: Gefühle bekommen wenig Raum
5. Praktische Übersetzung: 3 Alltagssituationen durch Element-Verständnis erklärt

Goldener Satz am Ende.
```

**Länge:** 350-500 Wörter.

---

## SEKTION 6 · Eure Bedürfnisse im Vergleich (NEU)

**Was es ist:** Die intimste Sektion. Welches Nervensystem braucht was?

**KI-Prompt:**

```
Analysiere für beide Personen die emotionalen Grundbedürfnisse:
- Mond-Position (Zeichen, Haus, Element)
- Wichtigste Mond-Aspekte
- Nervensystem-Signatur (Was beruhigt, was überfordert)

Pro Person: 4-6 Sätze mit konkreten Aussagen wie:
"Dein Nervensystem reguliert sich nicht durch Worte allein, sondern durch [...]"
"Was deinem System Sicherheit gibt: [...]"

Dann 4 Vergleichs-Abschnitte:
1. Wo eure Bedürfnisse sich treffen (die gemeinsame Insel)
2. Wo eure Bedürfnisse kollidieren (mit konkretem Beispiel)
3. Bedürfnisse die ihr beim anderen schwer versteht (weil ihr sie selbst nicht habt)
4. Nervensystem-Sprache pro Person als praktischer Schlüssel

Eine Selbstreflexionsfrage am Ende. Goldener Satz.

WICHTIG: Niemals "du brauchst Liebe", sondern präzise: "Dein System beruhigt sich
durch X, nicht durch Y".
```

**Länge:** 500-700 Wörter.

---

## SEKTION 7 · Eure Gefühlsebene (NEU)

**KI-Prompt:**

```
Analysiere wie wichtig Gefühl für jede Person ist und wie es ausgedrückt wird:
- Mond-Element als Hauptindikator:
  * Wassermond: tief, intuitiv, oft versteckt
  * Feuermond: impulsiv, sichtbar, lebendig
  * Erdmond: kontrolliert, körperlich ausgedrückt
  * Luftmond: rationalisiert, verbal
- Mond-Haus: wo werden Gefühle erlebt
- Mond-Aspekte: was hemmt oder verstärkt den Ausdruck
- Venus-Position: wie wichtig sind weiche Gefühle
- 12. Haus: unbewusste Gefühlsschichten

Pro Person konkrete Aussagen:
"[Name] zeigt Gefühle am liebsten durch [...] und friert ein wenn [...]"
"Wenn [Name] traurig ist, erkennt man das daran dass [...]"
"Was sie/er braucht um sich gefühlsmäßig sicher zu fühlen: [...]"

Dann 4 Vergleichs-Abschnitte:
1. Wo ihr im Gefühl synchron schwingt
2. Wo ihr aneinander vorbei fühlt
3. Wer trägt mehr emotionale Last
4. Wer geht zuerst auf den anderen zu nach einem Streit

Selbstreflexionsfrage. Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 8 · Wie ihr miteinander sprecht (NEU)

**KI-Prompt:**

```
Analysiere die Kommunikationsstile beider Personen:
- Merkur-Position, Zeichen, Haus, Aspekte
- Konzeptuell, bildhaft, direkt, diplomatisch?
- Wann schweigt diese Person, wann wird sie laut?

Dann die Vergleichs-Sektionen:
1. Merkur-Aspekte zwischen euch (passen die Sprach-Frequenzen?)
2. Im Alltag heißt das: 3-4 konkrete Beispielsätze
   - "Wenn [Name 1] sagt 'wir müssen reden', meint sie..."
   - "Wenn [Name 2] sagt 'wir müssen reden', meint er..."
3. Wie ihr im Streit redet (Mars und Saturn-Konstellationen)
   - Wer wird laut, wer wird leise, wer geht weg
4. Die roten Sätze: 2-3 typische Sätze die euer Gegenüber besonders triggern
5. Die grünen Sätze: 2-3 typische Sätze die zuverlässig andocken
6. Konkrete Gespräche-Rituale passend zur Konstellation
   - Morgen-Check-in? Wochen-Reflektion? Streit-Pause-Regel?

Goldener Satz.
```

**Länge:** 450-650 Wörter.

---

## SEKTIONEN 9-10 · Eure Liebessprachen vertieft (ERWEITERT)

**KI-Prompt:**

```
Behalte das bestehende 2-Spalten-Profil (Hauptliebessprache, sekundär, empfängt) pro
Person.

Ergänze danach 5 neue Unter-Sektionen:

1. Übersetzungs-Tabelle (kleine Tabelle):
   - "Wenn [Name 1] sagt X, meint sie Y"
   - "Wenn [Name 2] sagt X, meint er Y"
   - "Wenn [Name 1] schweigt, bedeutet das..."
   - "Wenn [Name 2] schweigt, bedeutet das..."

2. Was lädt den Liebes-Akku auf (3 konkrete Beispiele pro Person):
   Sehr präzise, nicht "Aufmerksamkeit" sondern "wenn er ihr morgens ohne Aufforderung
   den Kaffee bringt".

3. Was leert den Akku (3 konkrete Beispiele pro Person)

4. Tägliche Mini-Gesten: was würde Person A heute in 2 Minuten zeigen können und umgekehrt

5. Eure Schnittmenge: was ihr BEIDE als Liebe versteht. Konkrete Aktivitäten benennen.

Goldener Satz.
```

**Länge:** 500-700 Wörter.

---

## SEKTION 11 · Wertesystem und Lebensmission (NEU)

**KI-Prompt:**

```
Analysiere Wertesystem und Lebensmission beider Personen:
- Sonne-Zeichen und Haus (Kern-Identität)
- 2. Haus und Venus-Zeichen (was hat Wert)
- 9. Haus, Jupiter (Überzeugungen, Glaubenssätze)
- Saturn (was ernst genommen wird)
- Nördlicher Mondknoten (Lebensmission)
- MC (berufliche Mission)
- Selena (spirituelle Mission, falls relevant)

Pro Person:
- "Für [Name] ist das wichtigste im Leben [...]"
- "Sie/er kann schwer leben mit [...]"
- "[Name] ist hier um [...]"

Dann 3 Vergleichs-Sektionen:
1. Wo eure Missionen sich treffen
2. Wo eure Missionen sich reiben (klassisch: einer will Familie, der andere die Welt
   verändern)
3. Gemeinsame Mission als Paar (Composite-Sonne als Wegweiser)

Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 12 · Eure Leidenschaftsbereiche (NEU)

**KI-Prompt:**

```
Analysiere wo jede Person besonders elektrisiert ist:
- Mars-Position (wo wird Energie investiert)
- 5. Haus (Lebensfreude, kreativer Ausdruck)
- Dominante Planeten und Häuser
- Pluto-Position (obsessive Tiefe)
- Jupiter (wo öffnet sich Begeisterung)

Pro Person 3-5 konkrete Leidenschaftsthemen mit Beispielsätzen:
- "Was [Name] richtig in Brand setzt: [...]"
- "Wenn sie/er über [...] redet, leuchtet etwas auf"
- "Themen die sie/ihn nicht loslassen: [...]"

Dann 3 Vergleichs-Sektionen:
1. Eure gemeinsame Leidenschaft (Schnittmenge)
2. Wo eure Leidenschaften auseinandergehen (Raum für Eigenständigkeit)
3. Wie ihr eure Leidenschaften gegenseitig nähren könnt

Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 13 · Materielles, Stabilität, Erdung (NEU)

**Layout:** Horizontale Skala 0-100 mit zwei Markierungen pro Person. Darunter Fließtext.

**KI-Prompt:**

```
Analysiere jede Person auf der Materiell-Stabil-Skala:
- 2. Haus (Verhältnis zu Geld und Besitz)
- Erde-Anteil im Chart (Bodenhaftung)
- Saturn-Position (Verantwortungs- und Strukturbereitschaft)
- Stier/Steinbock/Jungfrau-Energie (Realitätssinn)

Pro Person:
- "[Name] ist [stark materiell verankert / mittel / eher unmateriell]"
- "Stabilität entsteht für sie/ihn durch [...]"
- "In Krisen verhält sie/er sich [stabil / wechselhaft / zusammenfallend]"

Dann 4 Vergleichs-Sektionen:
1. Wer trägt was im Paar (wer ist Anker, wer ist Bewegung)
2. Risiken (wenn beide nicht verankert oder beide zu materiell)
3. Optimale Verteilung: Empfehlung wer welche Realitäts-Funktion übernehmen sollte
4. Wer ist materieller Realist, wer Visionär; wer plant, wer improvisiert

Goldener Satz.
```

**Länge:** 350-500 Wörter.

---

## SEKTION 14 · Welcher Typ ist sie · Welcher Typ ist er (NEU)

**KI-Prompt:**

```
Analysiere für beide Personen den "Beziehungs-Typ" den sie verkörpern UND den sie
unbewusst anziehen.

Pro Person als zusammenhängendes Bild beschreiben:
- Sonne + Aszendent + Mond als Drei-Achsen-Persönlichkeit
- Venus: welchen Liebes-Typ verkörpert sie/er nach außen
- Mars: welche Anziehungs-Energie strahlt sie/er aus
- Dominante Elemente und Modalitäten

Beschreibung:
- Wirkung auf andere
- Was Menschen an ihr/ihm zuerst bemerken
- Was unter der Oberfläche brodelt
- Archetyp-Bild (z.B. "die stille Beobachterin mit innerem Feuer" oder "der ruhige
  Stratege")

Worauf sie/er anspringt (Anziehungs-Profil):
- DC (Descendant) als Spiegel-Eigenschaft
- Venus-Zeichen (welcher Typ emotional anzieht)
- Mars-Zeichen (welcher Typ körperlich anzieht)
- 7. Haus (welche Partnerschaft sie/er unbewusst aufbaut)

Dann Resonanz-Analyse:
- Passt euer Typ-Profil zueinander?
- Spiegelt ihr euch?
- Ergänzt ihr euch?
- Triggert ihr euch?

Beispiel: "Sie sucht den ruhigen Stratege, er bietet das. Das ist Resonanz."
Oder: "Sie sucht den Abenteurer, er ist Bewahrer. Hier liegt eine Diskrepanz."

WICHTIG: Bei gleichgeschlechtlichen Paaren keine Mann/Frau-Klischees, stattdessen
energetische Polarität (nährend/treibend, yin/yang).

Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 18 · Numerologische Resonanz (ERWEITERT)

**KI-Prompt:**

```
Erstelle eine volle Seite Numerologie statt nur 3 Sätzen.

Inhalt:
1. [Name 1]s Lebenszahl: Berechnung transparent zeigen, Bedeutung in 3-4 Sätzen
2. [Name 2]s Lebenszahl: analog
3. Eure Lebenszahlen-Verbindung: wie ergänzen oder reiben sich diese beiden Zahlen?
4. Persönliche Jahreszahlen aktuelles Jahr für beide
5. Beziehungs-Resonanz-Zahl: Summe beider Lebenszahlen reduziert
6. Ausdruckszahlen (aus den Namen): was zeigen die für die Außenwirkung?

Häufige Lebenszahlen-Kombinationen erklären:
- 1 und 9: Pionier trifft Vollenderin
- 2 und 4: Harmonie trifft Struktur
- 3 und 7: Lebensfreude trifft Tiefsinn
- 5 und 6: Freiheit trifft Geborgenheit
- 8 und 2: Macht trifft Diplomatie

Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 19 · Eure Stärken und Verantwortungs-Verteilung (ERWEITERT)

**KI-Prompt:**

```
Behalte die bestehenden 5 Stärken-Punkte. Ergänze danach 3 neue Sektionen:

1. Wo ihr euch ergänzt
   Klassisches Beispiel: einer plant, einer setzt um. Einer fühlt, einer denkt.

2. Wer sollte für was verantwortlich sein (DAS HERZSTÜCK)
   Konkrete Empfehlungen für symbiotische Verteilung, basierend auf den Charts:
   - "[Name 1] mit Mond im Stier und Venus in Jungfrau hat den besseren Zugang zu Geld.
     Eure Finanz-Übersicht sollte bei ihr liegen."
   - "[Name 2] mit Mars im Schütze trägt die Vision. Die größeren Lebens-Pläne und
     Reisen darf er anführen."
   - "Bei Konflikten mit Außenstehenden ist [Name 1] mit Mars in Waage diplomatischer.
     Diese Rolle darf sie übernehmen."

   Als Vorschlag formulieren, niemals als Vorschrift.

3. Das Tandem-Prinzip
   Wo ihr GEMEINSAM stärker seid als alleine. 2-3 Bereiche wo eure Stärken sich
   potenzieren.

Goldener Satz.
```

**Länge:** 500-700 Wörter inklusive der bestehenden 5 Stärken.

---

## SEKTION 20 · Eure Schwächen und Schatten (NEU)

**KI-Prompt:**

```
Analysiere mögliche Schwächen beider Personen. Behutsam aber ehrlich.

Pro Person 3-4 Punkte aus:
- Saturn-Position (wo blockiert oder zu eng)
- Chiron (verletzlicher Punkt)
- Harte Aspekte (Quadrate, Oppositionen)
- 12. Haus-Themen (unbewusste Schatten)

Beispielsätze:
- "Tendenz zu [...]"
- "Schwierigkeit mit [...]"
- "Wiederkehrendes Muster: [...]"

WICHTIG: Schwächen niemals abwertend. Immer als:
- Wachstumsthema
- Schatten-Aspekt einer Stärke
- Anlage die bewusst werden darf

Dann 3 Vergleichs-Sektionen:
1. Wo eure Schwächen sich gegenseitig triggern
2. Wo eure Schwächen sich gegenseitig auffangen
3. Schatten-Bewusstsein: warum es leichter wird wenn beide ihre Schatten kennen

Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 21 · Eure Konfliktlandkarte (ERWEITERT)

**KI-Prompt:**

```
Statt nur 3 Trigger eine vollständige Konfliktlandkarte. 5-6 typische Reibungsfelder.

Pro Reibungsfeld:
- Astrologischer Anker
- Wie zeigt es sich im Alltag konkret
- Warum entsteht das (Mechanik nicht Schuld)
- Tipp für beide Seiten

Reale Konflikt-Felder die meist relevant sind (nur die nehmen, die wirklich aus den
Aspekten herauskommen):
1. Bedürftigkeit vs Unabhängigkeit (Mond-Aspekte)
2. Tempo (Mars-Aspekte, Element-Mix)
3. Geld und Werte (Venus, 2. und 8. Haus)
4. Nähe und Sexualität
5. Familie und Herkunft (Mond, 4. Haus, IC-Aspekte)
6. Karriere und Außenwelt (MC-Aspekte)
7. Kinder, Kreativität oder gemeinsame Schöpfung (5. Haus)
8. Alltag, Pflichten, Verteilung (6. Haus, Saturn)

Goldener Satz.
```

**Länge:** 450-650 Wörter.

---

## SEKTION 22 · Authentizität und Masken (NEU)

**KI-Prompt:**

```
Analysiere für beide Personen wie viel Maske sie tragen.

Pro Person:
- Aszendent vs Sonne: wie groß ist der Spalt zwischen Außen und Innen?
- 12. Haus: was wird unbewusst versteckt?
- Saturn: welche Maske der Erwachsenen-Rolle wird getragen?
- Mond vs Aszendent: Spalt zwischen Bedürfnis und Auftreten

Konkrete Aussagen:
- "[Name] zeigt sich nach außen als [...] obwohl sie/er innerlich [...] ist"
- "Ihre/seine Maske: [...]"
- "Man erkennt dass [Name] sich schützt wenn [...]"

Dann 4 Vergleichs-Sektionen:
1. Wo eure Masken aufeinander treffen
2. Wann fällt die Maske (welche Situationen lassen euch echt sein)
3. Sind eure Masken kompatibel
4. Wie ihr euch gegenseitig zur Authentizität einlädt

Selbstreflexionsfrage. Goldener Satz.
```

**Länge:** 400-550 Wörter.

---

## SEKTION 23 · Karmische Wunden und gegenseitige Heilung (NEU)

**KI-Prompt:**

```
Eine der tiefsten Sektionen. Sehr behutsam formulieren.

Pro Person:
- Chiron-Position (Haus, Zeichen, Aspekte)
- 12. Haus (kollektive und karmische Schicht)
- Südlicher Mondknoten (was wurde mitgebracht)
- Saturn-Aspekte zu Sonne und Mond
- Pluto-Aspekte (transformative Wunde)

Karmische Schicht behutsam formulieren:
"Deine Seele kennt dieses Thema schon länger, als wäre die Wunde älter als dieses Leben."

Konkret:
- Was die Wunde ist (3-4 Sätze)
- Wie sie sich heute zeigt (Alltagsbeispiele)
- Wie sie in Beziehung getriggert wird

Dann 3 wichtige Vergleichs-Sektionen:

1. Wie ihr euch unbewusst triggert
   Beispiel: "[Name 1]s Verlassenwerden-Wunde trifft [Name 2]s Rückzug-Tendenz. Wenn er
   sich zurückzieht, triggert das ihre Wunde, sie wird klammernd, das triggert seine
   Wunde tieferen Rückzugs. Ein Kreislauf."

2. Eure Heilungs-Achse
   Chiron-Aspekte zwischen euch. Konkret:
   - "Wenn [Name 2] [Name 1]s Wunde anschaut ohne wegzugehen, heilt sie schneller als
     jede Therapie."
   - "Wenn [Name 1] [Name 2]s Wunde nicht persönlich nimmt, kann er weich werden."

3. Heilungs-Rituale: 3-4 konkrete Praktiken passend zu der spezifischen Wunde

Goldener Satz.

WICHTIG: Niemals dramatisch werden. Niemals "in deinem vorigen Leben warst du eine Hexe
die verbrannt wurde". Weiches "deine Seele kennt das schon länger" reicht.
```

**Länge:** 500-700 Wörter.

---

## SEKTION 24 · Krisenfähigkeit (NEU)

**KI-Prompt:**

```
Wie kommt dieses Paar durch Krisen?

Inhalt:
1. Welche Ressourcen sind im Chart angelegt (welche Aspekte tragen)
2. Wo eure größte Verletzungs-Gefahr liegt (behutsam, ohne Drohung)
3. Wenn die Krise da ist: 3-4 konkrete Hinweise was zu tun ist

Goldener Satz.
```

**Länge:** 300-450 Wörter.

---

## SEKTION 25 · Sexueller Match · detaillierte Analyse (NEU)

**KI-Prompt:**

```
Detaillierte sexuelle Analyse. Respektvoll formuliert, keine Vulgarität, aber präzise.

Pro Person der sexuelle Antrieb:
- Mars-Position (wie wird Energie sexuell ausgedrückt)
- Mars-Zeichen (Stil der Lust: impulsiv, sinnlich, intensiv, sanft)
- Mars-Haus (wo wird sexuelle Energie investiert)
- Venus-Mars-Aspekte im eigenen Chart
- Pluto-Aspekte (Tiefe und Intensität)
- 8. Haus (Tabu-Energie, Verschmelzung)

Aussagen:
- "[Name]s sexueller Antrieb ist [hoch / mittel / eher gedämpft]"
- "Was sie/ihn anmacht: [...]"
- "Wann sie/er sexuell schließt: [...]"
- "Die erotische Sprache die sie/er spricht: [...]"

Dann Synastrie-Analyse:
1. Eure körperliche Resonanz
   - Mars zwischen euch (passen Tempi und Intensitäten?)
   - Venus-Mars zwischen euch
   - Pluto-Aspekte (magnetische Anziehung?)
   - Aszendent-Mars (Sofort-Resonanz?)

2. Eure sexuellen Bedürfnisse im Vergleich
   - Frequenz: passt eure Lust-Frequenz?
   - Stil: passt euer Lust-Stil?
   - Initiierung: wer geht zuerst auf den anderen zu?

3. Wenn die Lust einschläft
   - Bei Mond-Saturn: zu viel Verantwortung, zu wenig Spiel
   - Bei Venus-Neptun: Erwartungen statt Realität
   - Bei Mars-Saturn: Druck statt Lust
   Konkrete Hinweise was hilft.

4. Körperkontakt als Ressource
   Bei starken Mars-Pluto-Aspekten: Körper als Heilraum bei Konflikten.

5. Sexuelle Tabus und Wachstumsräume
   Wenn 8. Haus-Energie stark: dürft ihr euch tiefer hinein wagen?

Goldener Satz.

WICHTIG: Respektvoll, niemals reißerisch. Bei sehr klassischen oder älteren Paaren
etwas behutsamer.
```

**Länge:** 500-700 Wörter.

---

## SEKTION 26 · Energetische Besonderheiten (NEU)

**KI-Prompt:**

```
Subtile Schichten die in normalen Astrologie-Analysen oft übersehen werden.

Inhalt:
1. Eure Aura-Resonanz (was passiert energetisch wenn ihr im selben Raum seid)
   - Neptun-Aspekte: feinstoffliche Vermischung
   - Pluto-Aspekte: tiefe Magnetik
   - Uranus-Aspekte: elektrische Erregung
   - Saturn-Aspekte: bremsende oder stabilisierende Energie

2. Mediale Verbindung (12. Haus, Neptun, Fische): spürt ihr euch über Distanz?

3. Karmische Magnetik (Mondknoten und Chiron verbunden): warum wurdet ihr zueinander
   gezogen?

4. Energetische Lecks (wo verliert eure Beziehung Energie?)

5. Energetische Aufladung (was lädt eure gemeinsame Energie auf?)
   - Bestimmte Aktivitäten basierend auf den Charts
   - Bestimmte Orte (Natur, Wasser, Berge)
   - Bestimmte Praktiken (Meditation, Körperarbeit)

Goldener Satz.
```

**Länge:** 300-450 Wörter.

---

## SEKTION 27 · Eure spirituelle Aufgabe als Paar (NEU)

**KI-Prompt:**

```
Was ist die übergeordnete Aufgabe dieser Verbindung?

Inhalt:
1. Composite-Sonne als Wegweiser (welches Lebensthema trägt die Beziehung in die Welt)
2. Composite-Mondknoten (wohin führt euch die Verbindung)
3. Was lernt ihr durcheinander (jede Person ist Lehrer für die andere)
4. Eure Verabredung (bei starken Mondknoten- oder Chiron-Aspekten behutsam ansprechen)

Goldener Satz.
```

**Länge:** 250-400 Wörter.

---

## Goldenen Satz formulieren – Anleitung

Der goldene Satz ist die wichtigste Verdichtung jeder Sektion. Er soll:

- **Ein Satz, max. zwei** – kein Absatz
- **Verdichtet** – das Wesentliche der Sektion in einem Bild
- **Anti-deterministisch** – nicht "ihr werdet immer", sondern "ihr habt"
- **Konkret und bildhaft** – nicht abstrakt
- **Du/Ihr-Form** – direkt an das Paar gesprochen
- **Fett markiert** – im `golden_quote` CSS-Container

Beispiele aus dem Anna+Lena-Report:

> "Eure Lebenslandkarten überschneiden sich da, wo es zählt – und ergänzen sich da, wo
> sie verschieden sind."

> "Eure Sprache ist Luft, eure Polarität ist Wasser und Feuer – was ihr gemeinsam erden
> müsst, ist der Boden unter euren Füssen."

> "Eure Wunden haben euch zueinander geführt – nicht trotz ihrer, sondern wegen ihrer
> Verwandtschaft."

> "Ihr seid nicht hier, um es einfach zu haben – ihr seid hier, um etwas zu zeigen."

---

## Sicherheits-Checkliste vor Veröffentlichung

Bevor das PDF dem Klienten gegeben wird, prüfen:

- [ ] Astrologische Fakten kommen alle aus den MCP-API-Responses?
- [ ] Keine Familien-/Wohn-/Job-Annahmen in den Beispielen?
- [ ] Keine Hetero-Norm-Annahmen?
- [ ] Karma-Sektion behutsam, keine "vorigen Leben"-Dramatik?
- [ ] Sex-Sektion respektvoll, keine Vulgarität?
- [ ] Spirituelle Sektion fundiert, nicht esoterisch-floskelhaft?
- [ ] 30 Sektionen alle befüllt?
- [ ] Goldene Sätze pro Sektion vorhanden?
- [ ] Selbstreflexionsfragen verteilt?
- [ ] Klientenbriefing.md im richtigen Klienten-Ordner gespeichert (NICHT im Skill-Repo)?
