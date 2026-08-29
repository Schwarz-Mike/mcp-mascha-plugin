---
name: mascha-setup
description: Prüft die Verbindung zu Mascha Cosmos und führt durch die Einrichtung. Verwende diesen Skill, wenn jemand die Einrichtung prüfen will, fragt ob die Verbindung steht, nach dem Sterne-Guthaben fragt, wissen will welche Skills verfügbar sind, oder wenn ein Aufruf an Mascha Cosmos scheitert — Trigger: "mascha setup", "einrichtung prüfen", "funktioniert mascha", "bin ich verbunden", "wie viele sterne habe ich", "mascha geht nicht", "verbindung testen".
version: 1.0.0
---

Prüfe die Einrichtung von Mascha Cosmos und führe die Person durch, was noch fehlt.

## Vorgehen

**1. Verbindung prüfen**

Rufe `my_account` auf. Das Ergebnis sagt dir alles Weitere:

- **Antwort mit Namen und Guthaben** → Die Verbindung steht. Nenne Vornamen, Sterne-Guthaben
  und ob Geburtsdaten hinterlegt sind. Erwähne, dass die Geburtsdaten dadurch nicht jedes
  Mal genannt werden müssen.

- **Aufforderung zur Anmeldung** → Sag der Person, dass sich gleich ein Browserfenster
  öffnet, in dem sie sich mit ihrem Mascha-Konto anmelden soll. Das ist einmalig.

- **Hinweis auf fehlende Freischaltung oder kein Guthaben** → Erkläre, dass ein Konto auf
  https://app.mascha-cosmos.com/register nötig ist und Sterne aufgeladen sein müssen.
  Ohne Guthaben lehnt der Server jede Anfrage ab, auch bei bestehender Verbindung.

- **Werkzeug nicht gefunden** → Das Plugin ist installiert, aber Claude wurde seither nicht
  neu gestartet. Bitte um einen Neustart.

**2. Skills prüfen**

Rufe `list_skills` auf und nenne die verfügbaren Skills mit einem Satz, was sie tun.
Erwähne, dass sie automatisch greifen, wenn sie zur Frage passen — man muss sie nicht
aufrufen.

**3. Loslegen**

Schlage zwei, drei konkrete erste Schritte vor, passend zum Kontostand:

- Sind Geburtsdaten hinterlegt: „Erzähl mir über mein Geburtshoroskop" oder
  „Wie sind meine Transite heute?"
- Sind keine hinterlegt: frage nach Geburtsdatum, -zeit und -ort und biete an, damit
  das Radix zu erstellen.
- Ist kein Guthaben da: verweise auf https://app.mascha-cosmos.com zum Aufladen.

## Ton

Kurz und freundlich. Keine technischen Details über MCP, Tokens oder Endpunkte — die
Person will Astrologie nutzen, nicht Software verstehen. Bei Problemen nenne
support@mascha-cosmos.com.
