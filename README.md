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
rm -rf ~/.claude/skills/{astrology-mascha,partnerhoroscope,mutter-kind-horoskop,rectification}
```

Unter Windows in der PowerShell:

```powershell
"astrology-mascha","partnerhoroscope","mutter-kind-horoskop","rectification" | ForEach-Object {
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

Ein Remote-MCP-Server mit **134 Werkzeugen** rund um Astrologie:

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

Die Kontowerkzeuge greifen auf deine bereits in Mascha gespeicherten Daten zu: `my_account`
zeigt Guthaben und hinterlegte Geburtsdaten, `my_radix` das gespeicherte Geburtshoroskop
ohne Neuberechnung, `list_sub_users` und `sub_user_radix` die Personen, die du in Mascha
angelegt hast.

### Die Skills

Fünf Arbeitsanleitungen, die Claude automatisch heranzieht, wenn sie passen:

**`astrology-mascha`** — die Grundlage. Erklärt Claude alle Werkzeuge, ihre Parameter,
typische Abläufe und die Besonderheiten der Deutung (Huber-Methode, Koch-Häuser,
nicht-ptolemäische Aspekte). Wird bei fast jeder astrologischen Frage aktiv.

**`partnerhoroscope`** — erstellt ein rund 50-seitiges Premium-PDF-Beziehungshoroskop im
Mascha-Cosmos-Stil: 30 Abschnitte von Synastrie über Kommunikation und Konfliktlandkarte
bis zur spirituellen Aufgabe. Bringt Layout-Skripte, Symbolbibliothek und Bildmaterial mit.

**`mutter-kind-horoskop`** — ein rund 35-seitiges PDF, mit dem ein Elternteil sein Kind in
der Tiefe versteht: Wesen, Gefühlswelt, Lernen, sensible Stellen und wie es liebevoll
begleitet wird. Funktioniert für Mutter oder Vater, Sohn oder Tochter.

**`rectification`** — Geburtszeit-Rektifikation: rechnet aus bekannten Lebensereignissen
zurück, wann jemand wahrscheinlich geboren wurde. Für alle, die ihre Geburtszeit nicht
kennen.

**`mascha-setup`** — prüft die Einrichtung: Verbindung, Sterne-Guthaben, hinterlegte
Geburtsdaten. Greift automatisch bei Fragen wie „funktioniert Mascha?" oder wenn ein
Aufruf scheitert.

---

## Beispiele

> „Erstelle mir mein Geburtshoroskop"

> „Wie sind meine Transite heute?"

> „Wie passen wir zusammen? Ich bin am 6.2.1973 um 9:05 in Zürich geboren, sie am
> 7.10.1972 um 12:57 in Bern"

> „Zeig mir mein Human Design"

> „Wie viele Sterne habe ich noch?"

> „Erstelle ein Partnerhoroskop als PDF für uns beide"

Sind deine Geburtsdaten in Mascha hinterlegt, musst du sie nicht jedes Mal nennen — Claude
liest sie über `my_account` aus deinem Konto.

---

## Sterne und Kosten

Jeder Aufruf kostet Sterne, je nach Aufwand ein bis fünf. Werkzeuge, die nur deine
gespeicherten Daten lesen, kosten einen Stern. Berechnungen mit Grafiken oder ausführlichen
Deutungstexten kosten mehr.

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

Kommen weitere Skills dazu, erscheinen sie nach einem Update des Plugins automatisch:

```bash
claude plugin marketplace update mascha-cosmos
```

---

## Hilfe

**support@mascha-cosmos.com**

Bei Verbindungsproblemen hilft meist:

1. Prüfen, ob das Konto auf [app.mascha-cosmos.com](https://app.mascha-cosmos.com)
   freigeschaltet ist und Sterne vorhanden sind
2. Claude neu starten
3. „Prüf mal meine Mascha-Einrichtung" sagen — Claude prüft die Verbindung und sagt,
   woran es hakt
