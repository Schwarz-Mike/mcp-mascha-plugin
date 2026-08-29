"""
Mascha Cosmos - Berechnungs-Hilfsfunktionen

Diese Datei enthält:
- Element- und Modalitäten-Berechnung aus natal_chart-Daten
- Haus-Betonungs-Analyse
- Klienten-Briefing-Schreiber (klienten_briefing.md)

Diese Funktionen werden nach den API-Calls aufgerufen, BEVOR die data.json gebaut wird.
"""

from datetime import datetime
import os


# ============================================================
# ELEMENT / MODALITÄTS-BERECHNUNG
# ============================================================

# Sternzeichen-Mapping: Element + Modalität
SIGN_PROPERTIES = {
    "Ari": {"element": "Feuer", "modality": "Kardinal", "ruler": "Mars"},
    "Tau": {"element": "Erde", "modality": "Fix", "ruler": "Venus"},
    "Gem": {"element": "Luft", "modality": "Veränderlich", "ruler": "Merkur"},
    "Can": {"element": "Wasser", "modality": "Kardinal", "ruler": "Mond"},
    "Leo": {"element": "Feuer", "modality": "Fix", "ruler": "Sonne"},
    "Vir": {"element": "Erde", "modality": "Veränderlich", "ruler": "Merkur"},
    "Lib": {"element": "Luft", "modality": "Kardinal", "ruler": "Venus"},
    "Sco": {"element": "Wasser", "modality": "Fix", "ruler": "Pluto"},
    "Sag": {"element": "Feuer", "modality": "Veränderlich", "ruler": "Jupiter"},
    "Cap": {"element": "Erde", "modality": "Kardinal", "ruler": "Saturn"},
    "Aqu": {"element": "Luft", "modality": "Fix", "ruler": "Uranus"},
    "Pis": {"element": "Wasser", "modality": "Veränderlich", "ruler": "Neptun"},
}

# Planeten-Gewichtung für Element- und Modalitäts-Berechnung
# (Persönliche Planeten zählen mehr als äussere)
PLANET_WEIGHTS = {
    "sun": 4,
    "moon": 4,
    "ascendant": 3,
    "mercury": 2,
    "venus": 2,
    "mars": 2,
    "jupiter": 1.5,
    "saturn": 1.5,
    "uranus": 1,
    "neptune": 1,
    "pluto": 1,
    "medium_coeli": 2,  # MC ist wichtig
}


def calc_element_distribution(natal_chart_data):
    """
    Berechnet die Element-Verteilung (Feuer/Erde/Luft/Wasser) eines Charts in Prozent.

    Args:
        natal_chart_data: Das subject_data Dict aus MASCHA-MCP:natal_chart Response

    Returns:
        Dict mit "Feuer", "Erde", "Luft", "Wasser" -> Prozentwerten (gerundet)
    """
    counts = {"Feuer": 0.0, "Erde": 0.0, "Luft": 0.0, "Wasser": 0.0}

    for planet_key, weight in PLANET_WEIGHTS.items():
        planet = natal_chart_data.get(planet_key)
        if not planet:
            continue
        sign = planet.get("sign")
        if not sign or sign not in SIGN_PROPERTIES:
            continue
        element = SIGN_PROPERTIES[sign]["element"]
        counts[element] += weight

    total = sum(counts.values())
    if total == 0:
        return {k: 0 for k in counts}

    return {k: round(v / total * 100) for k, v in counts.items()}


def calc_modality_distribution(natal_chart_data):
    """Berechnet die Modalitäten-Verteilung (Kardinal/Fix/Veränderlich) in Prozent."""
    counts = {"Kardinal": 0.0, "Fix": 0.0, "Veränderlich": 0.0}

    for planet_key, weight in PLANET_WEIGHTS.items():
        planet = natal_chart_data.get(planet_key)
        if not planet:
            continue
        sign = planet.get("sign")
        if not sign or sign not in SIGN_PROPERTIES:
            continue
        modality = SIGN_PROPERTIES[sign]["modality"]
        counts[modality] += weight

    total = sum(counts.values())
    if total == 0:
        return {k: 0 for k in counts}

    return {k: round(v / total * 100) for k, v in counts.items()}


def calc_house_emphasis(natal_chart_data):
    """
    Zählt Planeten pro Haus. Returns Liste sortiert nach Anzahl, dann Haus-Nummer.

    Returns:
        Liste von Tupeln [(house_num, count, planet_names), ...]
    """
    house_map = {n: [] for n in range(1, 13)}

    house_name_to_num = {
        "First_House": 1, "Second_House": 2, "Third_House": 3, "Fourth_House": 4,
        "Fifth_House": 5, "Sixth_House": 6, "Seventh_House": 7, "Eighth_House": 8,
        "Ninth_House": 9, "Tenth_House": 10, "Eleventh_House": 11, "Twelfth_House": 12,
    }

    planet_names_de = {
        "sun": "Sonne", "moon": "Mond", "mercury": "Merkur", "venus": "Venus",
        "mars": "Mars", "jupiter": "Jupiter", "saturn": "Saturn",
        "uranus": "Uranus", "neptune": "Neptun", "pluto": "Pluto",
        "chiron": "Chiron",
    }

    for planet_key, name_de in planet_names_de.items():
        planet = natal_chart_data.get(planet_key)
        if not planet:
            continue
        house = planet.get("house")
        if house and house in house_name_to_num:
            house_num = house_name_to_num[house]
            house_map[house_num].append(name_de)

    # Sortiert nach Anzahl absteigend, dann Haus-Nummer aufsteigend
    result = sorted(
        [(n, len(planets), planets) for n, planets in house_map.items() if planets],
        key=lambda x: (-x[1], x[0])
    )
    return result


# ============================================================
# LEBENS-PRIORITÄTEN (für Sektion 4)
# ============================================================

LIFE_PRIORITY_HOUSES = {
    "Ich, Selbstentfaltung": [1],
    "Partnerschaft": [7],
    "Beruf, Berufung": [10],
    "Familie, Wurzeln, Zuhause": [4],
    "Kinder, Kreativität, Schöpfen": [5],
    "Finanzen, Sicherheit": [2, 8],
    "Freundschaft, Gemeinschaft": [11],
    "Spiritualität, Rückzug": [12],
}


def calc_life_priorities(natal_chart_data):
    """
    Berechnet Lebens-Prioritäten basierend auf Haus-Betonungen + relevante Planeten.

    Returns:
        Dict {"Bereich": prozent (gerundet)} – Summe ist normalisiert.
    """
    counts = {area: 0.0 for area in LIFE_PRIORITY_HOUSES}

    house_name_to_num = {
        "First_House": 1, "Second_House": 2, "Third_House": 3, "Fourth_House": 4,
        "Fifth_House": 5, "Sixth_House": 6, "Seventh_House": 7, "Eighth_House": 8,
        "Ninth_House": 9, "Tenth_House": 10, "Eleventh_House": 11, "Twelfth_House": 12,
    }

    for planet_key, weight in PLANET_WEIGHTS.items():
        planet = natal_chart_data.get(planet_key)
        if not planet:
            continue
        house = planet.get("house")
        if not house or house not in house_name_to_num:
            continue
        house_num = house_name_to_num[house]
        for area, houses in LIFE_PRIORITY_HOUSES.items():
            if house_num in houses:
                counts[area] += weight

    total = sum(counts.values())
    if total == 0:
        return {k: 0 for k in counts}

    # Auf 100% normalisieren
    return {k: round(v / total * 100) for k, v in counts.items()}


# ============================================================
# KLIENTEN-BRIEFING SCHREIBER
# ============================================================

# Mapping englische Sign-Codes -> Deutsch
SIGN_EN_TO_DE = {
    "Ari": "Widder", "Tau": "Stier", "Gem": "Zwilling", "Can": "Krebs",
    "Leo": "Löwe", "Vir": "Jungfrau", "Lib": "Waage", "Sco": "Skorpion",
    "Sag": "Schütze", "Cap": "Steinbock", "Aqu": "Wassermann", "Pis": "Fische",
}

PLANET_DE = {
    "sun": "Sonne", "moon": "Mond", "ascendant": "Aszendent",
    "mercury": "Merkur", "venus": "Venus", "mars": "Mars",
    "jupiter": "Jupiter", "saturn": "Saturn", "uranus": "Uranus",
    "neptune": "Neptun", "pluto": "Pluto", "chiron": "Chiron",
    "medium_coeli": "MC", "mean_lilith": "Lilith (Mean)",
    "mean_node": "Nordknoten",
}


def format_person_briefing(name, person_data, natal_chart_data, numerology_data):
    """
    Erstellt den Markdown-Block für eine Person im klienten_briefing.md.

    Args:
        name: Vorname
        person_data: Dict mit birth_date, birth_time, birth_place
        natal_chart_data: subject_data aus natal_chart API
        numerology_data: Numerology core numbers response
    """
    elements = calc_element_distribution(natal_chart_data)
    modalities = calc_modality_distribution(natal_chart_data)
    houses = calc_house_emphasis(natal_chart_data)
    priorities = calc_life_priorities(natal_chart_data)

    out = []
    out.append(f"## 👤 Person: {name}\n")
    out.append("### Stammdaten\n")
    out.append(f"- **Vorname:** {name}")
    out.append(f"- **Geburtsdatum:** {person_data.get('birth_date', 'n/a')}")
    out.append(f"- **Geburtszeit:** {person_data.get('birth_time', 'n/a')}")
    out.append(f"- **Geburtsort:** {person_data.get('birth_place', 'n/a')}")
    if "lat" in person_data:
        out.append(f"- **Koordinaten:** Lat {person_data['lat']}, Lng {person_data['lng']}")
    out.append("")

    out.append("### Astrologische Kernfakten (aus natal_chart API)\n")
    out.append("| Position | Sign (de) | Grad | Haus | Element | Modalität |")
    out.append("|----------|-----------|------|------|---------|-----------|")

    house_name_short = {
        "First_House": "1", "Second_House": "2", "Third_House": "3",
        "Fourth_House": "4", "Fifth_House": "5", "Sixth_House": "6",
        "Seventh_House": "7", "Eighth_House": "8", "Ninth_House": "9",
        "Tenth_House": "10", "Eleventh_House": "11", "Twelfth_House": "12",
    }

    for planet_key in ["sun", "moon", "ascendant", "mercury", "venus", "mars",
                       "jupiter", "saturn", "uranus", "neptune", "pluto",
                       "chiron", "medium_coeli", "mean_lilith", "mean_node"]:
        planet = natal_chart_data.get(planet_key)
        if not planet:
            continue
        sign_en = planet.get("sign", "")
        sign_de = SIGN_EN_TO_DE.get(sign_en, sign_en)
        pos = planet.get("position", 0)
        house_full = planet.get("house", "")
        house_short = house_name_short.get(house_full, "—") if house_full else "—"
        props = SIGN_PROPERTIES.get(sign_en, {})
        element = props.get("element", "—")
        modality = props.get("modality", "—")
        name_de = PLANET_DE.get(planet_key, planet_key)
        out.append(f"| {name_de} | {sign_de} | {pos:.1f}° | {house_short} | {element} | {modality} |")

    out.append("")

    out.append("### Element-Verteilung (berechnet)\n")
    out.append(f"- 🔥 Feuer: {elements['Feuer']}%")
    out.append(f"- 🌍 Erde: {elements['Erde']}%")
    out.append(f"- 💨 Luft: {elements['Luft']}%")
    out.append(f"- 💧 Wasser: {elements['Wasser']}%\n")

    out.append("### Modalitäten-Verteilung (berechnet)\n")
    out.append(f"- ⚡ Kardinal: {modalities['Kardinal']}%")
    out.append(f"- 🔒 Fix: {modalities['Fix']}%")
    out.append(f"- 🌀 Veränderlich: {modalities['Veränderlich']}%\n")

    out.append("### Haus-Betonungen (Top 5)\n")
    for house_num, count, planets in houses[:5]:
        planet_list = ", ".join(planets)
        out.append(f"- Haus {house_num}: {count} Planeten ({planet_list})")
    out.append("")

    out.append("### Lebens-Prioritäten (berechnet aus Haus-Betonung)\n")
    sorted_priorities = sorted(priorities.items(), key=lambda x: -x[1])
    for area, pct in sorted_priorities:
        if pct > 0:
            out.append(f"- {area}: {pct}%")
    out.append("")

    out.append("### Numerologie\n")
    if numerology_data:
        out.append(f"- **Lebenspfad:** {numerology_data.get('life_path', 'n/a')}")
        out.append(f"- **Schicksalszahl:** {numerology_data.get('destiny', 'n/a')}")
        out.append(f"- **Seelendrang:** {numerology_data.get('soul_urge', 'n/a')}")
        out.append(f"- **Persönlichkeit:** {numerology_data.get('personality', 'n/a')}")
        out.append(f"- **Persönliches Jahr:** {numerology_data.get('personal_year', 'n/a')}")
    out.append("\n---\n")

    return "\n".join(out)


def write_klienten_briefing(
    output_path,
    person1, person2,
    natal1, natal2,
    numerology1, numerology2,
    compatibility, synastry, composite, love_languages, red_flags,
    cover_image_url=None,
    skill_version="partnerhoroscope v1.0",
):
    """
    Schreibt die komplette klienten_briefing.md in den angegebenen Pfad.

    Args:
        output_path: Pfad zur zu erstellenden .md Datei
        person1, person2: Dicts mit name, birth_date, birth_time, birth_place
        natal1, natal2: subject_data aus natal_chart APIs
        numerology1, numerology2: numerology_core_numbers responses
        compatibility: relationship_compatibility / score Response
        synastry: synastry_chart Response
        composite: composite_chart / davison Response
        love_languages: relationship_love_languages Response
        red_flags: relationship_red_flags Response
        cover_image_url: optional, URL des generierten Cover-Bilds
        skill_version: Versions-String
    """
    out = []
    out.append(f"# Klienten-Briefing · {person1['name']} & {person2['name']}\n")
    out.append(f"**Erstellt am:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    out.append(f"**Skill-Version:** {skill_version}")
    out.append("**Datenquelle:** MASCHA-MCP (mcp.mascha-cosmos.com)")
    out.append("**Status:** ✅ Vollständiger Datenabruf\n")
    out.append("---\n")

    # Person 1
    out.append(format_person_briefing(person1["name"], person1, natal1, numerology1))

    # Person 2
    out.append(format_person_briefing(person2["name"], person2, natal2, numerology2))

    # Beziehungs-Daten
    out.append("## 💞 Beziehungs-Daten\n")

    if compatibility:
        out.append("### Kompatibilitäts-Score\n")
        total = compatibility.get("overall_score") or compatibility.get("total", "n/a")
        rating = compatibility.get("rating", "n/a")
        out.append(f"- **Gesamt:** {total} / 100")
        out.append(f"- **Rating:** {rating}\n")

        breakdown = compatibility.get("score_breakdown", {})
        if breakdown:
            out.append("### Score-Dimensionen\n")
            for key, val in breakdown.items():
                out.append(f"- {key}: {val}")
            out.append("")

    if synastry:
        aspects = synastry.get("aspects", [])[:12]
        if aspects:
            out.append("### Top 12 Synastrie-Aspekte\n")
            out.append("| Person1 | Aspekt | Person2 | Orb |")
            out.append("|---------|--------|---------|-----|")
            for asp in aspects:
                p1 = PLANET_DE.get(asp.get("point1", "").lower(), asp.get("point1", ""))
                p2 = PLANET_DE.get(asp.get("point2", "").lower(), asp.get("point2", ""))
                atype = asp.get("aspect_type", "")
                orb = asp.get("orb", "")
                if isinstance(orb, (int, float)):
                    orb = f"{abs(orb):.2f}°"
                out.append(f"| {p1} | {atype} | {p2} | {orb} |")
            out.append("")

    if composite:
        out.append("### Composite-Hauptpunkte\n")
        for key in ["sun", "moon", "venus", "mars", "ascendant", "medium_coeli"]:
            obj = composite.get(key)
            if obj and isinstance(obj, dict):
                sign = SIGN_EN_TO_DE.get(obj.get("sign", ""), obj.get("sign", ""))
                house = obj.get("house", "")
                out.append(f"- **Composite-{PLANET_DE.get(key, key)}:** {sign}, Haus {house}")
        out.append("")

    if love_languages:
        out.append("### Liebessprachen-Rohdaten\n")
        p1_ll = love_languages.get("person1", {})
        p2_ll = love_languages.get("person2", {})
        out.append(f"- **{person1['name']}:**")
        out.append(f"  - Primary shown: {p1_ll.get('primary_love_language_shown', 'n/a')}")
        out.append(f"  - Secondary shown: {p1_ll.get('secondary_love_language_shown', 'n/a')}")
        out.append(f"  - Primary received: {p1_ll.get('primary_love_language_received', 'n/a')}")
        out.append(f"- **{person2['name']}:**")
        out.append(f"  - Primary shown: {p2_ll.get('primary_love_language_shown', 'n/a')}")
        out.append(f"  - Secondary shown: {p2_ll.get('secondary_love_language_shown', 'n/a')}")
        out.append(f"  - Primary received: {p2_ll.get('primary_love_language_received', 'n/a')}")
        out.append("")

    if red_flags:
        out.append("### Red Flags\n")
        out.append(f"- **Grüne Signale:** {red_flags.get('green_flags', [])}")
        out.append(f"- **Gelbe Signale:** {red_flags.get('yellow_flags', [])}")
        out.append(f"- **Rote Signale:** {red_flags.get('red_flags', [])}\n")

    # Technische Infos
    out.append("---\n")
    out.append("## 🛠️ Technische Informationen\n")
    out.append("### Verwendete MCP-Endpunkte")
    out.append("- ✅ MASCHA-MCP:natal_chart (×2)")
    out.append("- ✅ MASCHA-MCP:relationship_compatibility / score")
    out.append("- ✅ MASCHA-MCP:synastry_chart")
    out.append("- ✅ MASCHA-MCP:relationship_love_languages")
    out.append("- ✅ MASCHA-MCP:composite_chart / relationship_davison")
    out.append("- ✅ MASCHA-MCP:relationship_red_flags")
    out.append("- ✅ MASCHA-MCP:numerology_core_numbers (×2)")
    out.append("")

    if cover_image_url:
        out.append("### Cover-Bild")
        out.append(f"- **Generiert mit:** KIMASTERMIND_IMAGES:generate_image")
        out.append(f"- **URL:** {cover_image_url}")
        out.append("")

    out.append("### Datenschutz-Hinweis")
    out.append("Diese Datei enthält personenbezogene Daten. Sie gehört NICHT in ein")
    out.append("öffentliches Repository.")

    # Schreiben
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    return output_path
