---
name: mutter-kind-horoskop
description: >
  Erstellt ein hochwertiges Premium-PDF "Mutter-Kind-Horoskop" bzw. Eltern-Kind-Horoskop
  im Mascha Cosmos Brand-Stil (warmes Cover, Gold/Navy/Cream, 3D-Boxen, Index, Bild pro
  Kapitel, CTA) für ein Elternteil und sein Kind. Der Elternteil liest den Report, um sein
  Kind in der Tiefe zu verstehen: Wesen, Gefühle, Kommunikation, Herausforderungen und wie
  es liebevoll begleitet wird. Nutze diesen Skill bei Trigger-Phrasen wie
  "Mutter-Kind-Horoskop", "Mutter Kind Horoskop erstellen", "Eltern-Kind-Horoskop",
  "Kind-Horoskop für die Mama/den Papa", "erstelle ein Horoskop für Mutter und Kind",
  "Vater-Kind-Horoskop", "wie begleite ich mein Kind astrologisch". Holt Daten via
  MASCHA-MCP (Natal beider, Synastrie, Numerologie, psychologische Analyse), generiert
  personenspezifische Bilder, schreibt herzliche Du-Form-Texte aus den echten Daten, baut
  ein ~35-seitiges A4-PDF und prüft die Umbrüche.
version: 1.0.0
---

# Mutter-Kind-Horoskop (Mascha Cosmos)

Erstellt ein ~35-seitiges Premium-PDF, mit dem ein **Elternteil sein Kind in der Tiefe
versteht**: Wesenskern, Gefühlswelt, wie es lernt und kommuniziert, sensible Stellen, die
Eltern-Kind-Verbindung (Synastrie), Herausforderungen und wie sie liebevoll begleitet werden,
plus Selbstfürsorge für den Elternteil. Ton: warm, berührend, Du-Form an den Elternteil.

## Wann verwenden
Trigger: "Mutter-Kind-Horoskop", "Eltern-Kind-Horoskop", "Vater-Kind-Horoskop", "Kind-Horoskop
für die Mama/den Papa", "erstelle ein Horoskop für Mutter und Kind", "wie begleite ich mein Kind
astrologisch", "Report über mein Kind für mich als Mutter/Vater".

## Konstellation (namensneutral)
Der Skill funktioniert für **Mutter–Sohn, Mutter–Tochter, Vater–Sohn, Vater–Tochter**. Passe
automatisch an:
- Anrede des Elternteils: **Mama / Papa** (bzw. "liebe [Name]" / "lieber [Name]").
- Kind: **Sohn / Tochter**, Pronomen er/sie.
- Titel/Fusszeile: "Mutter-Kind-Horoskop" bzw. "Vater-Kind-Horoskop".
Frage bei Unklarheit einmal kurz nach Rollen/Geschlecht, sonst leite es aus den Namen/Angaben ab.

## ⚠️ Zentrale Regel: keine Halluzinationen
Alle astrologischen Fakten (Sonne/Mond/Aszendent, Häuser, Aspekte, Orbs) und numerologischen
Zahlen MÜSSEN aus den MCP-Calls stammen. Niemals aus dem Sonnenzeichen ableiten oder erfinden.
Direkt nach den Calls alles in `klienten_briefing.md` sichern und beim Texten nur daraus zitieren.

## ⚠️ Zentrale Regel: dunkle Boxen sind einfarbig

Die navyfarbenen Boxen (`.goldbox`, `.cta`) dürfen **niemals einen `linear-gradient` und niemals
einen `inset`-Boxshadow** bekommen. Auf breiten, flachen Boxen legt ein Diagonalverlauf einen
sichtbaren hellen Schleier über die obere Hälfte – im PDF wirkt das wie ein verrutschter Layer.
Der frühere Wert `linear-gradient(158deg,#16233b,#0B1629 70%)` war genau dieser Fehler.

Gilt für jede dunkle Fläche in diesem Report:
- **Hintergrund:** immer `background: #0B1629;` (Volltonfarbe, kein Verlauf).
- **Kein `inset 0 1px 0 rgba(255,255,255,…)`** – WeasyPrint zieht das als hellen Film über die Fläche.
- **Erlaubt** bleibt der äussere Schlagschatten (`box-shadow: 0 10px 26px rgba(11,22,41,.28)`),
  weil er ausserhalb der Box liegt, sowie der goldene Rahmen.
- Helle Boxen (`.pcard`, `.tip`, `.ex`, `.check`, Cover-Box) dürfen ihre sanften Hell-auf-Hell-
  Verläufe behalten – dort entsteht kein sichtbarer Schleier.

Ausserdem funktionieren in WeasyPrint **keine** Text-Gradienten (`background-clip:text` /
`-webkit-text-fill-color:transparent`) – solche Stellen (`.sec-num`, `.cover-glyph`) immer mit
einer Volltonfarbe setzen, sonst wird der Text unsichtbar oder grau.

**Pflicht-Check nach jedem Build** (siehe Schritt 7): dunkle Boxen pixelweise auf Einfarbigkeit prüfen.

## Voraussetzungen (MCP)
Tool-Namen sind stabil, der Server-Präfix variiert – bei Bedarf via Tool-Suche laden
(Keywords: "natal chart", "synastry", "numerology core numbers", "psychological analysis",
"generate image"). Genutzt werden:
- **MASCHA-MCP** (astrology-api): `natal_chart`, `synastry_chart`, `numerology_core_numbers`,
  `psychological_analysis` (optional, für Charakter/Schatten-Sektionen). Für Häuser/Aszendent
  immer exakte **Geburtszeit** verwenden; bei mehrdeutigen Orten `latitude`/`longitude`
  mitgeben (z. B. Halle (Westfalen) ≠ Halle/Saale). Parameter: `language="de"`,
  `house_system="P"`, `zodiac_type="Tropic"`, `detail_level="full"`, `timezone="Europe/Berlin"`.
- **Bildgenerierung** (KIMASTERMIND_IMAGES / image-generator): `generate_image`
  (`model="gpt-image-2"`, `quality="medium"`).

## Workflow

### 1. Speicherort & Rollen klären
Frage, wo der Output hin soll (Default: neuer Unterordner `mutter-kind-<nachname>` unter dem
Astrogutachten-Ordner) und lege darin `assets/` an. Kläre Rollen (Mama/Papa, Sohn/Tochter),
falls nicht klar. Erfrage Geburtsdaten beider (Datum, **exakte Zeit**, Ort/Land).

### 2. Daten holen (MASCHA-MCP)
1. `natal_chart` für **Kind** und **Elternteil** (zwingend).
2. `synastry_chart` (Elternteil = Person 1, Kind = Person 2) → Interaspekte mit Orbs.
3. `numerology_core_numbers` für beide (Name + Geburtsdatum).
4. (optional) `psychological_analysis` für das Kind (tiefe Charakter-/Schatten-Sektionen).
Wähle die **engsten** Synastrie-Aspekte (Orb < ~1,5°), v. a. Kontakte zu Sonne/Mond/Aszendent/
Chiron/Venus/Mars und den Achsen – das sind die tragenden Fäden der Beziehung.

### 3. `klienten_briefing.md` schreiben (sofort)
Rohdaten-Snapshot: beide Geburtsdaten, pro Person Sonne/Mond/Aszendent/MC + alle Planeten mit
Zeichen/Haus/Grad, Kern-Natal-Aspekte, Top-Synastrie-Aspekte mit Orbs, Numerologie-Kernzahlen,
persönliches Jahr des Elternteils. Diese Datei erlaubt spätere Re-Runs ohne neue API-Credits.

### 4. Bilder generieren (nach `assets/`)
**Cover** (`aspect_ratio="21:9"`), Vorlage – Tierkreis-Glyphen von Kind & Elternteil einsetzen:
> Mystical cosmic artwork on warm cream beige background (#EBE7DC). A tender scene of a larger
> glowing astral parent figure gently holding and leaning forehead to forehead with a small
> glowing astral child figure in the center, made of golden stardust and starlight, radiating
> warmth and protection. Between them a soft golden heart-star. {CHILD_GLYPH} zodiac symbol on
> the left, {PARENT_GLYPH} zodiac symbol on the right, glowing gold in circular medallions.
> Background fades from rich gold/amber center to soft cream beige edges, golden mist, soft
> vignette blending into cream. Premium painterly digital art, tender, no text, no hard edges.
> Cream beige (#EBE7DC) dominates the outer 30%.

**Hero-Bilder** (`aspect_ratio="16:9"`), gleicher Look, Suffix an jeden Prompt anhängen:
> Warm gold and amber glow at the center fading seamlessly to soft cream beige (#EBE7DC) at the
> edges, golden mist and starlight, soft vignette blending fully into cream, painterly digital
> art, tender, no text, no hard edges, vintage astrology poster style. Cream beige dominates the
> outer 35%.

Motive (Dateiname → Bildidee): `hero_brief` (glühender Federkiel + Herz aus Licht),
`hero_ueberblick` (zwei Sternbilder nebeneinander), `hero_wesenskern` (luftiges Sternenkind),
`hero_herz` (zarte Mondsichel + Herzflamme), `hero_aufnehmen` (Kind vor leuchtendem Buch,
Wassertropfen), `hero_antrieb` (ruhendes Kind an starkem Goldbaum), `hero_elemente` (vier
Elemente als Goldwirbel um ein Sternkind), `hero_sensibel` (zartes Herz in Lichtblüten),
`hero_seelenweg` (Sternenpfad zum Horizont), `hero_verbindung` (Eltern-Kind-Silhouette im
Sternenhimmel), `hero_verstehen` (zwei verschlungene Herzen aus Goldfäden), `hero_knistert`
(zwei sanfte Goldströmungen, die zusammenfinden), `hero_sprechen` (goldene Herz-Sprechblasen),
`hero_troesten` (Elternfigur umhüllt Kind in Lichtkokon), `hero_liebessprachen` (zwei
verschiedene Goldblüten zueinander), `hero_numerologie` (goldene Zahlen + heilige Geometrie),
`hero_begleiten` (schützende goldene Hände um ein Sternchen), `hero_herausforderung` (sanfter
Goldpfad einen Hügel hinauf), `hero_freiraum` (kleiner Vogel verlässt goldenes Nest, Faden zurück),
`hero_selbststaendig` (Kinderhände um goldenen Setzling), `hero_fuersorge` (Figur giesst Licht in
die eigene Tasse), `hero_rituale` (gemütliche goldene Kerze), `hero_closing` (aufgehender Stern),
`hero_steckbrief` (goldene Sternkarte), `hero_cta` (einladende Lichttür ins Sternenall).
Bilder von der zurückgegebenen URL nach `assets/<name>.jpg` herunterladen. Bei Re-Runs
vorhandene `assets/` wiederverwenden. Zum Sparen kann man Motive über ähnliche Kapitel
wiederverwenden.

### 5. Texte schreiben – Stil
- Deutsche **Du-Form an den Elternteil**, Swiss German (ss statt ß), warm, berührend, konkret.
- Astrologische Begriffe **fett** (`<b>Mond Widder</b>`). Pro Kapitel ein **Goldener Satz**.
- Anti-Determinismus ("er neigt dazu", nicht "er wird immer"). Behutsam bei sensiblen Themen.
- **Praxisbeispiele, situative Szenen und Metaphern** machen alles verständlich, grosszügig nutzen.
- Reihenfolge Trösten: 1. Nähe/Sicherheit → 2. Beruhigung → 3. Worte. Keine Familien-/Job-Annahmen.
- Verankere jede Aussage in den echten Positionen/Aspekten aus `klienten_briefing.md`.
- **Kein Gedankenstrich im Fliesstext** – siehe die Regel direkt darunter.

#### ⚠️ Regel: keine Gedankenstriche

Der lange Gedankenstrich (`&mdash;`, `—`) ist das auffälligste Stilmerkmal von KI-Text und stört
den Lesefluss. In diesem Report kommt er **gar nicht** vor. Setze stattdessen das Satzzeichen,
das die Beziehung der Satzteile tatsächlich abbildet:

| Funktion des Strichs | Ersatz | Beispiel |
|---|---|---|
| Aufzählung / Erläuterung folgt | **Doppelpunkt** | `Das 2. Haus steht für das Konkrete: Besitz, Materie, Körper` |
| Zweiter Hauptsatz mit *und / aber / denn / sondern* | **Komma** | `Das Feuer ist da, aber es sitzt an entscheidenden Stellen` |
| Eigenständiger neuer Gedanke | **Punkt** | `Ennie kann beides. Sie muss nicht wählen` |
| Beidseitiger Einschub (`— … —`) | **Klammern** oder **Kommapaar** | `wenn viel los ist (Umzug, Krankheit, Stress), ist …` |
| Begriff + Kurzdefinition in `<li>` | **Doppelpunkt** | `<li><b>Wasser</b>: Sonne, Venus, Saturn …</li>` |
| Nachgestellte Apposition | **Komma** | `in einem persönlichen Jahr 11, einem Meisterjahr der Sensibilität` |

**Erlaubt bleiben:** Bindestriche in zusammengesetzten Wörtern und Fachbegriffen
(`Mond-Saturn-Quadrat`, `Fische-Kind`, `Mutter-Kind-Horoskop`, `Zwillinge-Mond`) sowie der
Bis-Strich `&ndash;` in Zahlenbereichen (`0&ndash;27 Jahre`, `28&ndash;36 Jahre`).

**Pflicht-Check vor dem Ausliefern** (siehe Schritt 7): Der Zähler muss null ergeben.

### 6. `data.json` bauen und PDF erzeugen
Schreibe `data.json` (Schema unten) mit allen Kapiteltexten und rufe:
```
python3 build_report.py data.json
```
`build_report.py` (unten) mit **WeasyPrint** rendern (`pip install weasyprint --break-system-packages`).

**Seitenränder.** Zwei Stellschrauben in `data.json`:

- `page_margin` steuert `@page content` in der Reihenfolge *oben rechts unten links*
  (Default `"20mm 17mm 17mm 20mm"`). Der Wert gilt für **alles**: Text, Hero-Bilder,
  Kapitel-Trennlinie und Fusszeile.
- `text_padding_right` rückt **nur die Textspalte** zusätzlich von rechts ein (Default `"0mm"`).
  Bilder, Titellinien, Fusszeile und die ganzseitige Checkliste behalten die volle Breite.

Fragt der Nutzer nach mehr Rand zum **Laminieren, Lochen, Heften oder Binden**, ist das der
bewährte Satz – links über `page_margin`, rechts über die Textspalte, damit die Bilder gross bleiben:
```json
"page_margin": "20mm 17mm 17mm 25mm",
"text_padding_right": "8mm"
```
Ergebnis: Fliesstext links **und** rechts 25mm vom Blattrand, Bilder weiterhin bis 17mm.
Eine genannte Mindestangabe ist die Untergrenze, nicht das Ziel – lieber grosszügig.
**Nachmessen statt schätzen:** Seite rendern und die Textspalte vermessen (Code in Schritt 7).

**Achtung Rückwirkung:** Jede Randänderung verändert den Textumbruch. Danach zwingend Schritt 7
erneut durchlaufen und die `hero_w`-Werte nachjustieren – und `hero_w` nie grösser wählen als die
Inhaltsbreite (`210mm − links − rechts`), sonst wird das Bild stillschweigend herunterskaliert.

**Tierkreis-Glyphen:** `♈`–`♓` (U+2648–2653) rutschen in WeasyPrint sonst in den Emoji-Font und
erscheinen als bunter Kreis. Deshalb immer mit Text-Variantenselektor schreiben – `&#9811;&#65038;`
statt `♓` – und im Fliesstext in `<span class="gl">…</span>` setzen. Zeichen in Fusszeilen und
CSS-`content:` müssen **echte Zeichen** sein (`·`), keine HTML-Entities (`&middot;` erscheint
sonst wörtlich im PDF).

### 7. Umbrüche prüfen (Python) und feinjustieren
```python
import pypdf
r = pypdf.PdfReader("<pfad>.pdf")
print("Seiten:", len(r.pages))
for i,pg in enumerate(r.pages,1):
    n = len((pg.extract_text() or "").strip())
    if i>=3 and n<330: print("Fast leere Seite:", i, n)
```
Wenn eine Box fast allein auf einer Seite steht: das **Hero-Bild** des betroffenen Kapitels
**vergrössern** (`hero_w` grösser, z. B. 150–170mm) – das schiebt einen Absatz auf die zweite
Seite und füllt sie. Boxen brechen nie um (`break-inside:avoid` ist gesetzt). Ganzseitige
Checklisten (`[[CHECKPAGE]]`) sollen mit allen Punkten auf **eine** Seite passen; sonst Punkte
kürzen oder Zeilenabstand im CSS leicht reduzieren. Zum Prüfen einzelne Seiten mit
`pdftoppm -png -r 72 -f N -l N file.pdf out` rendern und ansehen.

**Gedankenstrich-Check (Pflicht).** Muss `0` ausgeben, sonst zurück in den Text:
```python
import json, pypdf
print("Quelle:", open("data.json", encoding="utf-8").read().count("&mdash;"))   # erwartet 0
txt = " ".join(p.extract_text() or "" for p in pypdf.PdfReader("<pfad>.pdf").pages)
print("PDF:", txt.count("\u2014"))                                             # erwartet 0
print("Bis-Striche (ok):", txt.count("\u2013"))                                # nur Zahlenbereiche
```
Findet der Zähler Treffer, jeden einzeln im Kontext anschauen und nach der Tabelle in Schritt 5
ersetzen – **nicht** pauschal per Suchen-und-Ersetzen, sonst entstehen falsche Satzzeichen.

**Randprüfung (Pflicht, wenn der Nutzer Ränder vorgegeben hat).** Eine reine Textseite rendern
und die Textspalte vermessen – nicht auf die CSS-Werte verlassen:
```python
from PIL import Image; import numpy as np
im = Image.open("out-09.png").convert("RGB"); w, h = im.size
a = np.array(im).astype(int)
d = np.abs(a - np.array([235,231,220])).sum(2) > 25      # alles, was nicht Cream ist
sub = d[int(h*0.55):int(h*0.85)]                          # Fliesstextzone, ohne Hero/Kopf
c = np.where(sub.any(0))[0]
print("links", round(c.min()/w*210,1), "mm | rechts", round((w-c.max())/w*210,1), "mm")
```

**Farbprüfung der dunklen Boxen (Pflicht).** Eine Seite mit `[[GOLD]]`-Box und die CTA-Seite
rendern und den Boxhintergrund messen. Liegen `min` und `mean` beide bei `[11 22 41]`, ist die
Fläche sauber einfarbig. Weicht der Mittelwert deutlich nach oben ab, ist wieder ein Verlauf
oder ein Inset-Shadow im CSS gelandet:
```python
from PIL import Image; import numpy as np
a = np.array(Image.open("out-20.png").convert("RGB")).astype(int)
m = (a.sum(2) < 260) & (a[:,:,2] > a[:,:,0])          # navyfarbene Pixel
ys, xs = np.where(m)
bg = a[ys.min()+4:ys.max()-3, xs.min()+4:xs.max()-3].reshape(-1,3)
bg = bg[bg.sum(1) < 200]                               # Goldtext ausblenden
print("min", bg.min(0), "mean", bg.mean(0).round(2))   # erwartet: [11 22 41] / [11.x 22.x 41.x]
```

### 8. Abschluss
Fertiges PDF, `klienten_briefing.md` und `data.json` im Zielordner ablegen und dem Nutzer zeigen.
Re-Runs (anderer Text/Layout) nur aus `klienten_briefing.md` + `data.json` – **ohne** neue API-Calls.

## Sektionsstruktur (Vorschlag, 25 Kapitel)
Teil I Ankommen: (Brief an den Elternteil), (Euer Himmel auf einen Blick).
Teil II Wer ist dein Kind?: 01 Wesenskern · 02 Herz & Gefühle · 03 Wie es die Welt aufnimmt ·
04 Was es antreibt & beruhigt · 05 Gaben & Temperament · 06 Sensible Stellen · 07 Seelenweg.
Teil III Ihr beide: 08 Eure Herzverbindung · 09 Wo ihr euch tief versteht · 10 Wo es knistern
kann (mit Harmonie-Tipps) · 11 Wie du mit ihm/ihr sprichst · 12 Wie du tröstest & Halt gibst ·
13 Eure Sprachen der Liebe · 14 Numerologische Resonanz.
Teil IV Begleiten & Wachsen: 15 Was es am meisten braucht · 16 Herausforderungen liebevoll
angehen · 17 Freiraum & Geborgenheit · 18 Selbstständigkeit stärken · 19 Deine eigene Fürsorge
(mit ganzseitiger 12-Punkte-Balance-Checkliste auf eigener Seite) · 20 Kleine Rituale.
Teil V Abschluss: 21 Ein Wunsch für euren Weg · 22 Steckbrief & Merkzettel · (CTA-Seite).
Die Kapitel 01, 02, 03, 04, 06, 10, 13 dürfen ausführlicher sein (mehrere Absätze + Beispiele).

## data.json – Schema
```json
{
  "assets_dir": "assets",
  "out": "Mutter-Kind-Horoskop_<Kind>.pdf",
  "page_margin": "20mm 17mm 17mm 20mm",
  "text_padding_right": "0mm",
  "footer_left": "Mutter-Kind-Horoskop · <Kind>",
  "child":  {"name":"<Kind>",  "glyph":"♊", "born_text":"geboren am 11. Juni 2026"},
  "parent": {"role":"Mama",     "name":"<Elternteil>", "glyph":"♍", "born_text":"geboren am 5. September 1986"},
  "cover": {
    "kicker":"MASCHA COSMOS · MUTTER-KIND-HOROSKOP",
    "image":"cover",
    "subtitle":"Ein kosmisches Portrait deines Sohnes,<br/>und ein Wegweiser für euren gemeinsamen Weg",
    "line":"Sonne Zwillinge · Mond Widder · Aszendent Jungfrau",
    "for_line":"für seine Mama <Elternteil> · geboren am 5. September 1986 · ♍ Jungfrau"
  },
  "sections": [
    {"id":"brief","num":null,"part":"Teil I · Ankommen","title":"Ein Brief an dich, liebe <Elternteil>","hero":"hero_brief","body":"<p class=\"lead\">…</p>[[GOLD]]…[[/GOLD]]"},
    {"id":"s1","num":1,"part":"Teil II · Wer ist dein Sohn?","title":"Wesenskern","hero":"hero_wesenskern","hero_w":128,"body":"…"}
  ],
  "cta": {
    "toc":"Dein nächster Schritt mit Mascha Cosmos","image":"hero_cta",
    "title":"Dein nächster Schritt mit Mascha Cosmos",
    "paragraphs":[
      "Diese Auswertung wurde erstellt von <b>Anna Muster</b> mit <b>Mascha Cosmos</b>. …",
      "Gehe auf <b>mascha-cosmos.com</b> und registriere dich. Erfasse dich als Hauptperson und <Kind> als zweite Person. …",
      "Bei Fragen erreichst du uns unter <b>info@mascha-cosmos.com</b>"
    ],
    "mail_last": true,
    "close":"Schön, dass es euch zwei gibt!"
  }
}
```
Feld `num`: Zahl = nummeriertes Kapitel, `null` = Sonderkapitel (Stern-Symbol). `hero_w`
(optional, mm) steuert die Bildbreite (Standard 128; grösser = mehr Text auf Folgeseite).

### Body-Makros (im Fliesstext)
- Absätze: `<p class="lead">…</p>` (Einleitung), sonst `<p>…</p>`; Betonung `<b>…</b>`, kursiv `<i>…</i>`.
- `[[GOLD]]…[[/GOLD]]` → goldene Zitat-Box (Stern links & rechts vom Text).
- `[[TIP:Für dich]]…[[/TIP]]` → heller Tipp-Kasten (Label frei wählbar).
- `[[EX]]…[[/EX]]` → "Aus dem Alltag"-Beispielkasten.
- `[[REFLECT]]…[[/REFLECT]]` → kursive Reflexionsfrage.
- `[[CHECKPAGE:Titel|Intro]]Punkt 1|Punkt 2|…[[/CHECKPAGE]]` → ganzseitige Checkliste auf
  **eigener** Seite (für Kap. 19; 10–12 Punkte, je eine Zeile).
- Zwei-Spalten-Karten (für Überblick/Steckbrief):
  `<div class="two-col"><div class="pcard"><div class="pcard-h">Titel</div><ul><li>…</li></ul></div>…</div>`
- Aufzählung mit Stern-Bullets: `<ul class="need"><li>…</li></ul>`.

## build_report.py (vollständig – so in den Zielordner schreiben)
```python
# -*- coding: utf-8 -*-
"""Mutter/Vater-Kind-Horoskop: generischer PDF-Builder (Mascha Cosmos).
Aufruf:  python3 build_report.py data.json"""
import os, sys, json, re
from string import Template
from weasyprint import HTML

data = json.load(open(sys.argv[1], encoding="utf-8"))
BASE = os.path.dirname(os.path.abspath(sys.argv[1]))
ASSETS = data.get("assets_dir") or os.path.join(BASE, "assets")
if not os.path.isabs(ASSETS): ASSETS = os.path.join(BASE, ASSETS)
OUT = data["out"] if os.path.isabs(data["out"]) else os.path.join(BASE, data["out"])

NAVY="#0B1629"; GOLD="#EAC973"; GOLD2="#f2dd9e"
CREAM="#EBE7DC"; CARD="#F4EFE1"; BURNT="#BA7517"; DARKGOLD="#7A4F0F"; HL="#FFE9A8"; INK="#2B2A26"

def expand(body):
    body = re.sub(r'\[\[GOLD\]\](.*?)\[\[/GOLD\]\]',
        lambda m: f'<div class="goldbox"><span class="gb-s">✦</span><span class="gb-t">{m.group(1).strip()}</span><span class="gb-s">✦</span></div>', body, flags=re.S)
    body = re.sub(r'\[\[TIP:(.*?)\]\](.*?)\[\[/TIP\]\]',
        lambda m: f'<div class="tip"><span class="tip-l">{m.group(1).strip()}</span>{m.group(2).strip()}</div>', body, flags=re.S)
    body = re.sub(r'\[\[EX\]\](.*?)\[\[/EX\]\]',
        lambda m: f'<div class="ex"><span class="ex-l">Aus dem Alltag</span>{m.group(1).strip()}</div>', body, flags=re.S)
    body = re.sub(r'\[\[REFLECT\]\](.*?)\[\[/REFLECT\]\]',
        lambda m: f'<div class="reflect"><span class="rf-q">?</span>{m.group(1).strip()}</div>', body, flags=re.S)
    def cp(m):
        title, _, intro = m.group(1).partition("|")
        lis = "".join(f"<li>{it.strip()}</li>" for it in m.group(2).split("|") if it.strip())
        return f'<div class="check-page"><div class="cp-h">{title.strip()}</div><div class="cp-intro">{intro.strip()}</div><ul>{lis}</ul></div>'
    body = re.sub(r'\[\[CHECKPAGE:(.*?)\]\](.*?)\[\[/CHECKPAGE\]\]', cp, body, flags=re.S)
    return body

def render_section(s):
    hw = s.get("hero_w", 128)
    hero = f'<div class="hero"><img style="width:{hw}mm" src="{s["hero"]}.jpg"/></div>' if s.get("hero") else ""
    numhtml = f'<div class="sec-num">{int(s["num"]):02d}</div>' if s.get("num") else '<div class="sec-num sec-num-star">✦</div>'
    return (f'<section class="page" id="{s["id"]}"><div class="sec-head">{numhtml}'
            f'<div class="sec-titles"><div class="part-label">{s["part"]}</div>'
            f'<h2>{s["title"]}</h2></div></div>{hero}<div class="sec-body">{expand(s["body"])}</div></section>')

c = data["cover"]; ch = data["child"]
cover = f"""<section class="cover"><div class="cover-img"><img src="{c.get('image','cover')}.jpg"/></div>
  <div class="cover-box">
    <div class="cover-kicker">{c['kicker']}</div>
    <div class="cover-glyph">{ch.get('glyph','')}</div>
    <h1>{ch['name']}</h1>
    <div class="cover-born">{ch.get('born_text','')}</div>
    <div class="cover-sub">{c['subtitle']}</div>
    <div class="cover-line">{c['line']}</div>
    <div class="cover-for">{c['for_line']}</div>
  </div></section>"""

toc_rows = ""
for s in data["sections"]:
    label = s["title"].replace("&amp;", "&")
    pre = f'<span class="toc-no">{int(s["num"]):02d}</span> ' if s.get("num") else '<span class="toc-no">✦</span> '
    toc_rows += f'<a class="toc-a" href="#{s["id"]}"><span class="toc-t">{pre}{label}</span><span class="toc-dots"></span></a>'
if data.get("cta"):
    toc_rows += f'<a class="toc-a" href="#cta"><span class="toc-t"><span class="toc-no">✦</span> {data["cta"]["toc"]}</span><span class="toc-dots"></span></a>'
toc = f"""<section class="page toc-page"><div class="sec-head"><div class="sec-num sec-num-star">✦</div><div class="sec-titles"><div class="part-label">Übersicht</div><h2>Inhalt</h2></div></div><div class="toc">{toc_rows}</div></section>"""

body_sections = "".join(render_section(s) for s in data["sections"])

cta_html = ""
if data.get("cta"):
    ct = data["cta"]
    paras = ""
    for i, p in enumerate(ct["paragraphs"]):
        cls = ' class="cta-mail"' if (ct.get("mail_last") and i == len(ct["paragraphs"]) - 1) else ""
        paras += f"<p{cls}>{p}</p>"
    cta_html = (f'<section class="page" id="cta"><div class="hero"><img style="width:128mm" src="{ct.get("image","hero_cta")}.jpg"/></div>'
                f'<div class="cta"><div class="cta-h">{ct["title"]}</div>{paras}</div>'
                f'<div class="cta-close">{ct["close"]}</div></section>')

FOOTER_L = data.get("footer_left", "Mutter-Kind-Horoskop")
MARGIN = data.get("page_margin", "20mm 17mm 17mm 20mm")  # oben rechts unten links
TEXTPAD = data.get("text_padding_right", "0mm")  # ruckt NUR die Textspalte weiter ein
CSS = Template(r"""
@page { size: A4; margin: 0; background: $CREAM; }
@page content { margin: $MARGIN;
  @bottom-left { content: "$FOOTER_L"; font-family: Georgia,'DejaVu Serif',serif; font-size: 8pt; color: $DARKGOLD; }
  @bottom-center { content: "erstellt mit mascha-cosmos.com"; font-family: Georgia,'DejaVu Serif',serif; font-size: 8pt; color: $BURNT; }
  @bottom-right { content: counter(page); font-family: Georgia,'DejaVu Serif',serif; font-size: 10pt; color: $DARKGOLD; } }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background:$CREAM; color:$INK; font-family: Helvetica, Arial, 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.6; }
h1,h2,h3 { font-family: Georgia, 'DejaVu Serif', serif; font-weight: normal; }
.cover { width:210mm; height:297mm; background:$CREAM; position:relative; page-break-after: always; }
.cover-img { width:100%; } .cover-img img { width:100%; height:auto; display:block; }
.cover-box { position:absolute; left:20mm; right:20mm; top:112mm; background: linear-gradient(160deg,#FBF3DA 0%,#ECD9A6 55%,#E4CB92 100%);
  color:$NAVY; padding:17mm 15mm 14mm 15mm; text-align:center; border-radius:5px; border:1px solid $BURNT;
  box-shadow: 0 14px 42px rgba(122,79,15,.30), inset 0 1px 0 rgba(255,255,255,.65); }
.cover-kicker { color:$BURNT; letter-spacing:3px; font-size:9pt; margin-bottom:5mm; }
.cover-glyph { font-family:'DejaVu Sans'; font-size:26pt; line-height:1; margin-bottom:2mm; color:$BURNT; }
.cover-box h1 { font-size:56pt; margin:0 0 2mm 0; color:$NAVY; letter-spacing:2px; }
.cover-born { font-family:Georgia,serif; font-style:italic; font-size:12pt; color:$DARKGOLD; margin-bottom:7mm; }
.cover-sub { font-family:Georgia,serif; font-style:italic; font-size:14pt; color:$DARKGOLD; line-height:1.5; margin-bottom:9mm; }
.cover-line { font-size:10pt; color:$NAVY; letter-spacing:1px; border-top:1px solid rgba(122,79,15,.35); border-bottom:1px solid rgba(122,79,15,.35); padding:4mm 0; margin:0 3mm; }
.cover-for { margin-top:7mm; font-size:10pt; color:$BURNT; font-style:italic; }
.cover-for .gl, .cover-line .gl { font-family:'DejaVu Sans'; font-style:normal; }
.page { page: content; page-break-before: always; }
.sec-head { display:flex; align-items:center; gap:6mm; margin-bottom:5mm; border-bottom:2.5px solid $GOLD; padding-bottom:4mm; box-shadow: 0 2px 0 rgba(122,79,15,.18); }
.sec-num { font-family:Georgia,serif; font-size:36pt; line-height:1; min-width:22mm; text-align:center; color:$BURNT; }
.sec-num-star { font-size:26pt; }
.part-label { color:$BURNT; font-size:9pt; letter-spacing:2.5px; text-transform:uppercase; margin-bottom:2mm; }
.sec-head h2 { font-size:23pt; color:$NAVY; margin:0; line-height:1.12; }
.hero { text-align:center; margin:0.5mm 0 4mm 0; } .hero img { max-width:100%; height:auto; display:block; margin:0 auto; }
.sec-body { padding-right:$TEXTPAD; }
.sec-body p { margin:0 0 3.4mm 0; text-align:justify; } .sec-body p.lead { font-size:12pt; color:$NAVY; }
.sec-body b { color:$DARKGOLD; } .lead b { color:$NAVY; } .sec-body i { color:$NAVY; }
ul.clean, ul.need { list-style:none; padding-left:0; margin:3mm 0; }
ul.clean li, ul.need li { position:relative; padding-left:8mm; margin-bottom:2.6mm; break-inside:avoid; }
ul.clean li:before, ul.need li:before { content:"\2726"; color:$BURNT; position:absolute; left:0; }
.goldbox { display:flex; align-items:center; gap:6mm; break-inside:avoid; page-break-inside:avoid; background: $NAVY; color:$GOLD2; padding:5.5mm 8mm; border-radius:5px; margin:5mm 0 2mm 0; border:1px solid rgba(234,201,115,.45); box-shadow: 0 10px 26px rgba(11,22,41,.28); }
.gb-s { flex:none; color:$GOLD; font-size:12pt; } .gb-t { flex:1; text-align:center; font-family:Georgia,serif; font-style:italic; font-size:12.5pt; line-height:1.42; }
.tip { break-inside:avoid; page-break-inside:avoid; background: linear-gradient(180deg,#F7F1E0,$CARD); border-left:4px solid $GOLD; padding:4mm 5.5mm; margin:4mm 0; border-radius:3px; font-size:10pt; line-height:1.55; box-shadow: 0 5px 14px rgba(122,79,15,.12), inset 0 1px 0 rgba(255,255,255,.6); }
.tip-l { display:block; color:$BURNT; font-weight:bold; letter-spacing:1.5px; font-size:8pt; text-transform:uppercase; margin-bottom:1.6mm; } .tip b { color:$DARKGOLD; }
.ex { break-inside:avoid; page-break-inside:avoid; background: linear-gradient(180deg,#fbf7ec,#F1ECDC); border:1px solid rgba(234,201,115,.7); border-radius:4px; padding:4mm 5.5mm; margin:4mm 0; font-size:10pt; line-height:1.55; box-shadow: 0 5px 14px rgba(122,79,15,.10), inset 0 1px 0 rgba(255,255,255,.6); }
.ex-l { display:block; color:$BURNT; font-weight:bold; letter-spacing:1.5px; font-size:8pt; text-transform:uppercase; margin-bottom:1.6mm; }
.reflect { break-inside:avoid; page-break-inside:avoid; position:relative; font-family:Georgia,serif; font-style:italic; color:$NAVY; border-left:3px solid $BURNT; padding:2.5mm 0 2.5mm 9mm; margin:4mm 0; font-size:11pt; }
.rf-q { position:absolute; left:2mm; top:1mm; font-size:15pt; color:$GOLD; font-style:normal; font-family:Georgia,serif; }
.two-col { display:flex; gap:6mm; margin:2.5mm 0 2mm 0; }
.pcard { flex:1; break-inside:avoid; page-break-inside:avoid; background: linear-gradient(180deg,#FBF6E9,$CARD); border-radius:5px; padding:5.5mm; border:1px solid rgba(234,201,115,.8); position:relative; box-shadow: 0 8px 20px rgba(122,79,15,.14), inset 0 1px 0 rgba(255,255,255,.7); }
.pcard:before { content:""; position:absolute; left:0; right:0; top:0; height:4px; background:linear-gradient(90deg,$BURNT,$GOLD,$HL); border-radius:5px 5px 0 0; }
.pcard-h { font-family:Georgia,serif; color:$NAVY; font-size:13pt; border-bottom:1px solid $GOLD; padding-bottom:2mm; margin:2mm 0 3mm 0; }
.pcard ul { margin:0; padding-left:5mm; } .pcard li { margin-bottom:1.4mm; font-size:10.5pt; }
.closing-note { font-size:9.5pt; color:$DARKGOLD; font-style:italic; margin-top:5mm !important; border-top:1px solid $GOLD; padding-top:3mm; }
.check { break-inside:avoid; page-break-inside:avoid; background: linear-gradient(180deg,#FBF6E9,$CARD); border:1px solid rgba(234,201,115,.8); border-radius:5px; padding:5mm 6mm; margin:4mm 0; box-shadow: 0 6px 16px rgba(122,79,15,.12), inset 0 1px 0 rgba(255,255,255,.7); }
.check-h { font-family:Georgia,serif; color:$NAVY; font-size:12pt; margin-bottom:3mm; border-bottom:1px solid $GOLD; padding-bottom:2mm; }
.check ul { column-count:2; column-gap:8mm; list-style:none; padding-left:0; margin:0; }
.check li { position:relative; padding-left:6mm; margin-bottom:2.2mm; font-size:9.5pt; line-height:1.4; break-inside:avoid; }
.check li:before { content:"\2713"; color:$BURNT; position:absolute; left:0; font-weight:bold; }
.check-page { page-break-before: always; margin-right:-$TEXTPAD; }
.cp-h { font-family:Georgia,serif; color:$NAVY; font-size:21pt; text-align:center; margin:4mm 0 2mm; }
.cp-intro { text-align:center; font-family:Georgia,serif; font-style:italic; color:$DARKGOLD; font-size:12pt; margin-bottom:6mm; }
.check-page ul { list-style:none; padding:0; margin:0; }
.check-page li { position:relative; font-size:13pt; line-height:1.3; padding:5.3mm 4mm 5.3mm 12mm; border-bottom:1px solid rgba(234,201,115,.55); break-inside:avoid; }
.check-page li:first-child { border-top:1px solid rgba(234,201,115,.55); }
.check-page li:before { content:"\2713"; position:absolute; left:3mm; top:5.3mm; color:$BURNT; font-size:14pt; font-weight:bold; }
.toc { column-count:2; column-gap:12mm; margin-top:4mm; }
.toc-a { display:flex; align-items:baseline; text-decoration:none; color:$INK; break-inside:avoid; margin-bottom:3.6mm; font-size:9.5pt; }
.toc-no { color:$BURNT; font-family:Georgia,serif; font-weight:bold; }
.toc-t { white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:68mm; color:$NAVY; }
.toc-dots { flex:1; border-bottom:1px dotted $BURNT; margin:0 1.5mm 1.2mm 1.5mm; height:0; min-width:5mm; }
.toc-a::after { content: target-counter(attr(href), page); color:$DARKGOLD; font-family:Georgia,serif; font-weight:bold; font-size:10pt; }
.cta { break-inside:avoid; page-break-inside:avoid; background: $NAVY; color:$CREAM; border-radius:6px; padding:9mm 11mm; margin:2mm 0 5mm 0; border:1.5px solid rgba(234,201,115,.5); box-shadow: 0 14px 34px rgba(11,22,41,.3); }
.cta-h { font-family:Georgia,serif; font-size:20pt; color:$GOLD; text-align:center; margin-bottom:5mm; }
.cta p { margin:0 0 3.6mm 0; text-align:center; font-size:11pt; line-height:1.6; } .cta b { color:$GOLD2; }
.cta-mail { margin-top:5mm !important; padding-top:4mm; border-top:1px solid rgba(234,201,115,.35); }
.cta-close { text-align:center; font-family:Georgia,serif; font-style:italic; font-size:16pt; color:$BURNT; margin-top:6mm; }
""").safe_substitute(NAVY=NAVY,GOLD=GOLD,GOLD2=GOLD2,CREAM=CREAM,CARD=CARD,BURNT=BURNT,DARKGOLD=DARKGOLD,HL=HL,INK=INK,FOOTER_L=FOOTER_L,MARGIN=MARGIN,TEXTPAD=TEXTPAD)

html_doc = f"""<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{cover}{toc}{body_sections}{cta_html}</body></html>"""
HTML(string=html_doc, base_url=ASSETS).write_pdf(OUT)
print("PDF erstellt:", OUT)
```

## Brand-Konstanten
Navy `#0B1629` · Gold `#EAC973` · Cream `#EBE7DC` · Burnt Gold `#BA7517` · Dark Gold `#7A4F0F`.
Schriften: Georgia (Serif, Titel/Zitate), Helvetica/Arial (Body). Cover-Box: warmes Champagner-
Gold mit Navy-Schrift (festlich, gut lesbar – nie dunkel/„Todesanzeige").
Dunkle Flächen immer **einfarbig** `#0B1629` – siehe die Regel oben.

## Erinnerung
Namensneutral: keine Klientendaten im Skill. Alles Personenbezogene lebt in `data.json` und
`klienten_briefing.md` im gewählten Zielordner. Jede astrologische Aussage muss aus den echten
MCP-Daten stammen.

