"""
Mascha Cosmos Partnerhoroskop PDF Generator (Orchestrator)

Verwendung:
    python3 build_report.py <data.json> <cover_image_path> <output.pdf>

Das Skript lädt:
- style_css.py → CSS-String
- sections.py → 30 Render-Funktionen
- symbols.py → SVG-Symbole
- calc_helpers.py → Berechnungen (wenn von Sektionen gebraucht)
"""

import json
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from style_css import CSS
import sections as sec
from weasyprint import HTML


def build_html(data, cover_image_path, assets_dir, logo_path):
    """Baut komplettes HTML aus data-Dict für alle 30 Sektionen."""

    blocks = [
        # 1+2 Cover und Portraits
        sec.render_cover(data, cover_image_path, logo_path),
        sec.render_portraits(data),

        # 3 Score
        sec.render_score(data),

        # 4 Lebens-Prioritäten (NEU)
        sec.render_life_priorities(data),

        # 5 Elemente-Mischung (NEU)
        sec.render_elements(data, assets_dir),

        # 6 Bedürfnisse (NEU)
        sec.render_needs(data),

        # 7 Gefühlsebene (NEU)
        sec.render_feelings(data),

        # 8 Kommunikation (NEU)
        sec.render_communication(data),

        # 9 Liebessprachen vertieft (ERWEITERT)
        sec.render_love_languages(data, assets_dir),

        # 10 Wertesystem (NEU)
        sec.render_values(data),

        # 11 Leidenschaft (NEU)
        sec.render_passion(data, assets_dir),

        # 12 Materielles (NEU)
        sec.render_materiality(data),

        # 13 Typ-Profile (NEU)
        sec.render_type_profiles(data),

        # 14+15 Synastrie + Aspekte
        sec.render_synastry(data, assets_dir),

        # 16 Dynamiken
        sec.render_dynamics(data),

        # 17 Composite
        sec.render_composite(data, assets_dir),

        # 18 Numerologie (ERWEITERT)
        sec.render_numerology(data),

        # 19 Stärken + Verantwortung (ERWEITERT)
        sec.render_strengths(data, assets_dir),

        # 20 Schwächen + Schatten (NEU)
        sec.render_shadows(data),

        # 21 Konfliktlandkarte (ERWEITERT)
        sec.render_conflict_map(data, assets_dir),

        # 22 Authentizität + Masken (NEU)
        sec.render_masks(data),

        # 23 Karmische Wunden (NEU)
        sec.render_karma(data, assets_dir),

        # 24 Krisenfähigkeit (NEU)
        sec.render_crisis(data),

        # 25 Sexueller Match (NEU)
        sec.render_sexual_match(data, assets_dir),

        # 26 Energetische Besonderheiten (NEU)
        sec.render_energetic(data),

        # 27 Spirituelle Aufgabe (NEU)
        sec.render_spiritual_mission(data, assets_dir),

        # 28 Profile
        sec.render_profiles(data),

        # 29 Next Steps
        sec.render_next_steps(data, assets_dir),

        # 30 Closing
        sec.render_closing(data, assets_dir),
    ]

    body = "\n".join(blocks)

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Partnerhoroskop &middot; {data["person1"]["name"]} &amp; {data["person2"]["name"]}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>'''


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 build_report.py <data.json> <cover_image_path> <output.pdf>")
        sys.exit(1)

    data_path = sys.argv[1]
    cover_path = sys.argv[2]
    output_pdf = sys.argv[3]

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    skill_root = SCRIPT_DIR.parent
    assets_dir = str(skill_root / "assets")
    logo_path = str(skill_root / "assets" / "logo.png")

    print(f"Building HTML for {data['person1']['name']} & {data['person2']['name']}...")
    html_str = build_html(data, cover_path, assets_dir, logo_path)

    html_path = output_pdf.replace(".pdf", ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_str)
    print(f"HTML: {len(html_str)/1024:.1f} KB written to {html_path}")

    print(f"Generating PDF: {output_pdf}")
    HTML(string=html_str, base_url=str(skill_root)).write_pdf(output_pdf)

    size_mb = os.path.getsize(output_pdf) / 1024 / 1024
    print(f"Done: {output_pdf} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
