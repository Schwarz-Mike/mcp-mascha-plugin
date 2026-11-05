# Mascha Cosmos für Claude

Astrologie, Human Design und Numerologie direkt in Claude — über den Mascha-Cosmos-Server.
Das Plugin bringt die Serververbindung und fünf fertige Skills in einem Schritt mit.

---

## ⚠️ Voraussetzung: Konto und Sterne

Ohne Mascha-Konto funktioniert die Verbindung nicht.

1. **Konto anlegen:** [app.mascha-cosmos.com/register](https://app.mascha-cosmos.com/register)
2. **Sterne aufladen** — jede Berechnung kostet Sterne. Ohne Guthaben lehnt der Server
   jede Anfrage ab, auch wenn die Verbindung steht.
3. **Anmelden**, wenn Claude beim ersten Aufruf danach fragt (siehe unten).

Fragen oder Probleme: **support@mascha-cosmos.com**

---

## Installation

### Schon Mascha-Skills einzeln installiert?

Dann bitte vorher entfernen, sonst hast du sie doppelt — das Plugin bringt alle mit und
hält sie aktuell:

```bash
rm -rf ~/.claude/skills/{astrology-mascha,partnerhoroscope,mutter-kind-horoskop,rectification,mascha-main,mascha-partnerhoroskop,mascha-mutter-kind,mascha-rectification}
```

Unter Windows in der PowerShell:

```powershell
"astrology-mascha","partnerhoroscope","mutter-kind-horoskop","rectification","mascha-main","mascha-partnerhoroskop","mascha-mutter-kind","mascha-rectification" | ForEach-Object {
  Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\skills\$_" -ErrorAction SilentlyContinue }
```

### Variante A — Terminal (empfohlen)

Drei Befehle, danach nur noch anmelden:

```bash
claude plugin marketplace add Schwarz-Mike/mcp-mascha-plugin
claude plugin install mascha-cosmos@mascha-cosmos
claude mcp add --transport http --scope user mascha-cosmos https://mcp.mascha-cosmos.com/mcp
```

### Variante B — über die Oberfläche

Einstellungen → Plugins → Marketplace hinzufügen → `Schwarz-Mike/mcp-mascha-plugin`
eintragen → Plugin installieren. Anschliessend fragt Claude, ob der Mascha-Server
verbunden werden darf — das bestätigen.

> **Nur eine der beiden Varianten wählen.** Wer den dritten Befehl aus Variante A nutzt,
> soll den Server in Variante B **nicht** zusätzlich bestätigen — sonst ist er doppelt
> registriert und alle Werkzeuge erscheinen zweimal.

Danach Claude neu starten.

**Beim ersten Aufruf öffnet sich ein Anmeldefenster im Browser.** Dort meldest du dich mit
deinem Mascha-Konto an und bestätigst den Zugriff. Das passiert einmalig — danach bleibt
die Verbindung bestehen.

Zum Prüfen, ob alles läuft, sag einfach:

> „Prüf mal meine Mascha-Einrichtung"

Claude geht dann durch, ob die Verbindung steht, wie viele Sterne du hast und ob deine
Geburtsdaten hinterlegt sind.

---

## Was das Plugin mitbringt

### Die Serververbindung

Ein Remote-MCP-Server mit **137 Werkzeugen** rund um Astrologie:

| Bereich | Was möglich ist |
|---|---|
| **Geburtshoroskop** | Radix, Planetenpositionen, Häuser, Aspekte, Fixsterne |
| **Zeitqualität** | Transite, Progressionen, Solar- und Lunar-Return, Profektionen |
| **Beziehung** | Synastrie, Composite, Davison, Kompatibilität, Liebessprachen |
| **Horoskope** | Tag, Woche, Monat, Jahr — persönlich oder nach Sternzeichen |
| **Human Design** | Bodygraph, Typ, Kanäle, Tore, Kompatibilität, als Grafik |
| **Numerologie** | Kernzahlen, vollständiger Report, Kompatibilität, Glückszahlen |
| **Karten** | Astrokartographie, Relocation, Power-Zonen |
| **Traditionell** | Stundenastrologie, Wahl-Astrologie, Rektifikation, Arabische Punkte |
| **Konto** | eigenes Guthaben, gespeichertes Radix, angelegte Personen |
| **Sprachausgabe** | Texte in der Mascha-Stimme vorlesen lassen, als MP3 oder WAV |

Die Kontowerkzeuge greifen auf deine bereits in Mascha gespeicherten Daten zu: `my_account`
zeigt Guthaben und hinterlegte Geburtsdaten, `my_radix` das gespeicherte Geburtshoroskop
ohne Neuberechnung, `list_sub_users` und `sub_user_radix` die Personen, die du in Mascha
angelegt hast.

### Sprachausgabe — Texte in der Mascha-Stimme

Claude kann Texte vorlesen lassen — in derselben Stimme, die du aus den Audios in der
Mascha-App kennst. Gedacht für Erklärfilme, Sprechertexte, Meditationen oder einfach, um
sich das eigene Tageshoroskop anzuhören statt es zu lesen.

> „Lies mir mein Tageshoroskop vor“

> „Mach aus diesem Text ein MP3 für meinen Erklärfilm“

Bis 25 000 Zeichen pro Aufruf. Absatzgrenzen werden als hörbare Pausen umgesetzt, du
kannst zwischen 15 Stimmen wählen und eine Sprechanweisung mitgeben („ruhig und
feierlich“). Am Ende bekommst du einen Download-Link, der **24 Stunden** gilt — danach
wird die Datei gelöscht. Längere Texte laufen im Hintergrund, Claude meldet den
Fortschritt und sagt Bescheid, sobald die Aufnahme fertig ist.

> **Extra freizuschalten.** Die Sprachausgabe ist nicht im normalen Zugang enthalten und
> muss für dein Konto einzeln freigegeben werden. Schreib dazu an
> **support@mascha-cosmos.com**. Ohne Freigabe erscheinen die beiden Werkzeuge nicht —
> abgebucht wird in diesem Fall nichts.

### Die Skills

Fünf Arbeitsanleitungen, die Claude automatisch heranzieht, wenn sie passen. Alle heissen
einheitlich `mascha-…` und lassen sich auch von Hand mit `/` aufrufen. Im Plugin lautet der
Aufruf `/mascha-cosmos:mascha-main` usw.; Claude lädt sie aber von selbst, wenn du z. B. sagst
„mach mir mein Radix".

| Skill | Aufruf | Was er tut |
|---|---|---|
| `mascha-main` | `/mascha-main` | Hauptskill: alle Werkzeuge, Parameter, Abläufe, Preisregeln |
| `mascha-partnerhoroskop` | `/mascha-partnerhoroskop` | Premium-PDF Beziehungshoroskop |
| `mascha-mutter-kind` | `/mascha-mutter-kind` | Premium-PDF Mutter-/Eltern-Kind-Horoskop |
| `mascha-rectification` | `/mascha-rectification` | Geburtszeit-Rektifikation |
| `mascha-setup` | `/mascha-setup` | Einrichtung und Guthaben prüfen |

**`mascha-main`** — die Grundlage. Erklärt Claude alle Werkzeuge, ihre Parameter,
typische Abläufe und die Besonderheiten der Deutung (Huber-Methode, Koch-Häuser,
nicht-ptolemäische Aspekte), dazu die Preisregeln mit Sternen. Wird bei fast jeder
astrologischen Frage aktiv.

**`mascha-partnerhoroskop`** — erstellt ein rund 50-seitiges Premium-PDF-Beziehungshoroskop im
Mascha-Cosmos-Stil: 30 Abschnitte von Synastrie über Kommunikation und Konfliktlandkarte
bis zur spirituellen Aufgabe. Bringt Layout-Skripte, Symbolbibliothek und Bildmaterial mit.

**`mascha-mutter-kind`** — ein rund 35-seitiges PDF, mit dem ein Elternteil sein Kind in
der Tiefe versteht: Wesen, Gefühlswelt, Lernen, sensible Stellen und wie es liebevoll
begleitet wird. Funktioniert für Mutter oder Vater, Sohn oder Tochter.

**`mascha-rectification`** — Geburtszeit-Rektifikation: rechnet aus bekannten Lebensereignissen
zurück, wann jemand wahrscheinlich geboren wurde. Für alle, die ihre Geburtszeit nicht
kennen. Der Suchlauf ist teuer (meist 75 Sterne) und läuft erst nach deinem OK.

**`mascha-setup`** — prüft die Einrichtung: Verbindung, Sterne-Guthaben, hinterlegte
Geburtsdaten. Greift automatisch bei Fragen wie „funktioniert Mascha?" oder wenn ein
Aufruf scheitert.

---

## Beispiele

> „Erstelle mir mein Geburtshoroskop"

> „Wie sind meine Transite heute?"

> „Wie passen wir zusammen? Ich bin am 14.3.1985 um 8:30 in Zürich geboren, sie am
> 2.9.1987 um 17:10 in Bern"

> „Zeig mir mein Human Design"

> „Wie viele Sterne habe ich noch?"

> „Erstelle ein Partnerhoroskop als PDF für uns beide"

Sind deine Geburtsdaten in Mascha hinterlegt, musst du sie nicht jedes Mal nennen — Claude
liest sie über `my_account` aus deinem Konto.

---

## Sterne und Kosten

Jeder Aufruf kann Sterne kosten, je nach Aufwand und je nach deiner Mitgliedschaft.
Werkzeuge, die nur deine gespeicherten Daten lesen, sind günstig oder kostenlos; Grafiken und
ausführliche Berechnungen kosten mehr.

- **Preisliste:** [mcp.mascha-cosmos.com/mascha-mcp-preise](https://mcp.mascha-cosmos.com/mascha-mcp-preise)
  — öffentlich, immer aktuell, dieselben Zahlen wie bei der Abbuchung.
- Claude weist dich **einmal** zu Beginn darauf hin, nicht bei jedem Aufruf. Jede Antwort nennt,
  was der Aufruf gekostet hat (`sterne_kosten`).
- **Ab 30 Sternen je Aufruf** fragt Claude zuerst nach deinem ausdrücklichen OK und nennt den
  Preis. Ohne dein Ja wird nichts ausgeführt und nichts abgebucht.

Die Sprachausgabe rechnet nach Textlänge ab: **fünf Sterne je angefangene 5 000 Zeichen**.
Ein kurzer Absatz kostet also fünf Sterne, ein langer Sprechertext über 25 000 Zeichen
fünfundzwanzig. Den Fortschritt abzufragen kostet nichts.

Dein aktuelles Guthaben siehst du jederzeit mit „wie viele Sterne habe ich noch?" oder in
der App unter [app.mascha-cosmos.com](https://app.mascha-cosmos.com).

---

## Datenschutz

Das Plugin enthält **keine** Zugangsdaten. Die Anmeldung läuft über OAuth: Du meldest dich
direkt bei Mascha Cosmos an, Claude erhält nur ein zeitlich begrenztes Zugriffstoken.

Deine Geburtsdaten liegen in deinem Mascha-Konto, nicht im Plugin. Die mitgelieferten
Beispiele in den Skills verwenden ausschliesslich erfundene Personen.

---

## Neue Skills

Kommen weitere Skills dazu oder ändert sich einer, erscheint das nach einem Update des Plugins
(die Version steht in `.claude-plugin/plugin.json`):

```bash
claude plugin marketplace update mascha-cosmos
claude plugin update mascha-cosmos@mascha-cosmos
```

Danach Claude neu starten. Die Änderungen je Version stehen in [CHANGELOG.md](CHANGELOG.md).

---

## Hilfe

**support@mascha-cosmos.com**

Bei Verbindungsproblemen hilft meist:

1. Prüfen, ob das Konto auf [app.mascha-cosmos.com](https://app.mascha-cosmos.com)
   freigeschaltet ist und Sterne vorhanden sind
2. Claude neu starten
3. „Prüf mal meine Mascha-Einrichtung" sagen — Claude prüft die Verbindung und sagt,
   woran es hakt
