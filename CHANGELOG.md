# Changelog

## 1.2.0 — 2026-11-05

- **Einheitliche Skill-Namen** `mascha-…`: `mascha-main` (vorher `astrology-mascha`),
  `mascha-partnerhoroskop` (vorher `partnerhoroscope`), `mascha-mutter-kind` (vorher
  `mutter-kind-horoskop`), `mascha-rectification` (vorher `rectification`). `mascha-setup` bleibt.
  Wer die alten Skills einzeln installiert hatte, entfernt sie (siehe README), sonst sind sie doppelt.
- **Klare Beschreibungen**: Jede Skill-Beschreibung sagt, was der Skill tut und wann Claude ihn laden soll.
- **Sterne und Preise im Hauptskill**: Preisliste unter https://mcp.mascha-cosmos.com/mascha-mcp-preise,
  Hinweis einmal je Gespräch, Kosten in jeder Antwort (`sterne_kosten`), ab 30 Sternen je Aufruf
  nur mit ausdrücklichem OK (`bestaetigt: true`).
- Hauptskill: 152 statt 130 Werkzeuge, neuer Abschnitt Audios (`get_audios`, `get_audio`,
  `create_audios`, `audio_status`).
- `mascha-rectification`: Preis (meist 75 Sterne) und OK-Schritt vor dem Suchlauf.
- README: Beispiel mit erfundenen Geburtsdaten.

## 1.1.0

- Sprachausgabe in der Mascha-Stimme.
