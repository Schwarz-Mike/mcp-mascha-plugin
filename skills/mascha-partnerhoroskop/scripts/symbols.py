"""
Mascha Cosmos SVG Symbol Library
3D-Gold-Styled Tierkreiszeichen, Planeten, Icons und Numerologie-Badges.

Alle Symbole nutzen die 3-Layer-Stacking-Technik (dunkler Schatten + Gold + Highlight)
für einen 3D-Effekt ohne CSS-Filter (WeasyPrint-kompatibel).

Brand-Farben:
  Dark Shadow: #7A4F0F
  Gold Main:   #EAC973
  Highlight:   #FFE9A8
  Navy:        #0B1629
  Cream:       #EBE7DC
"""


def make_svg(content, size=120, viewbox="0 0 100 100"):
    """Wrapper: erzeugt vollständiges SVG-Element mit content darin."""
    return (
        f'<svg class="sym" width="{size}" height="{size}" '
        f'viewBox="{viewbox}" xmlns="http://www.w3.org/2000/svg">'
        f'{content}</svg>'
    )


# ============================================================
# TIERKREISZEICHEN (alle 12, gross mit Medaillon-Ring)
# ============================================================

ZODIAC_PATHS = {
    # Each path defined for 100x100 viewBox, centered around (50, 50)
    "Aries": [
        "M 32 38 Q 32 22 42 22 Q 50 22 50 38 Q 50 50 50 80",
        "M 68 38 Q 68 22 58 22 Q 50 22 50 38",
    ],
    "Taurus": [
        "M 30 38 Q 50 22 70 38",
        "M 32 60 A 18 18 0 1 0 68 60 A 18 18 0 1 0 32 60",
    ],
    "Gemini": [
        "M 30 22 L 30 78",
        "M 70 22 L 70 78",
        "M 30 22 L 70 22",
        "M 30 78 L 70 78",
    ],
    "Cancer": [
        "M 22 38 A 12 12 0 1 0 46 38 A 12 12 0 1 0 22 38",
        "M 54 62 A 12 12 0 1 0 78 62 A 12 12 0 1 0 54 62",
        "M 22 38 L 78 62",
    ],
    "Leo": [
        "M 30 70 A 14 14 0 1 1 58 70 A 14 14 0 1 1 30 70",
        "M 58 70 Q 58 30 40 30 Q 28 30 28 42",
    ],
    "Virgo": [
        "M 22 30 L 22 78",
        "M 22 30 Q 22 22 30 22 Q 38 22 38 30 L 38 78",
        "M 38 30 Q 38 22 46 22 Q 54 22 54 30 L 54 70 Q 54 78 62 78 Q 70 78 70 70 Q 70 62 62 62",
    ],
    "Libra": [
        "M 22 70 L 78 70",
        "M 28 60 L 72 60",
        "M 28 60 Q 50 25 72 60",
    ],
    "Scorpio": [
        "M 22 30 L 22 78",
        "M 22 30 Q 22 22 30 22 Q 38 22 38 30 L 38 78",
        "M 38 30 Q 38 22 46 22 Q 54 22 54 30 L 54 70 L 70 70",
        "M 62 60 L 78 70 L 62 80",
    ],
    "Sagittarius": [
        "M 25 75 L 70 30",
        "M 55 25 L 75 25 L 75 45",
        "M 38 50 L 58 50",
    ],
    "Capricorn": [
        "M 25 30 L 32 78",
        "M 32 78 L 50 30 L 60 78",
        "M 60 78 Q 78 78 78 62 Q 78 50 65 50 Q 55 50 55 60",
    ],
    "Aquarius": [
        "M 22 42 L 32 52 L 42 42 L 52 52 L 62 42 L 72 52 L 78 47",
        "M 22 58 L 32 68 L 42 58 L 52 68 L 62 58 L 72 68 L 78 63",
    ],
    "Pisces": [
        "M 22 30 Q 35 50 22 70",
        "M 78 30 Q 65 50 78 70",
        "M 28 50 L 72 50",
    ],
}


def zodiac_symbol(name, size=70, with_ring=True):
    """
    Erzeugt 3D-Gold-SVG für ein Tierkreiszeichen.

    Args:
        name: Englischer Name ("Aries", "Taurus", ...)
        size: Pixel-Grösse (default 70)
        with_ring: Mit Medaillon-Ring drumherum (default True)
    """
    paths = ZODIAC_PATHS.get(name)
    if not paths:
        return ""

    path_str = "".join(f'<path d="{p}"/>' for p in paths)

    ring = ""
    if with_ring:
        ring = (
            '<circle cx="50" cy="50" r="46" fill="#0B1629" '
            'stroke="#7A4F0F" stroke-width="3"/>'
            '<circle cx="50" cy="50" r="46" fill="none" '
            'stroke="#EAC973" stroke-width="1.5"/>'
        )

    # 3 Layer: Schatten unten, Gold mitte, Highlight oben
    layers = f"""
    {ring}
    <g stroke="#7A4F0F" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity="0.7" transform="translate(2,2)">{path_str}</g>
    <g stroke="#EAC973" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none">{path_str}</g>
    <g stroke="#FFE9A8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(-0.5,-1)">{path_str}</g>
    """
    return make_svg(layers, size)


# ============================================================
# PLANETEN (klein, für Aspekt-Tabellen)
# ============================================================

def sym_sun(size=22):
    content = """
    <circle cx="52" cy="52" r="32" fill="none" stroke="#7A4F0F" stroke-width="7" opacity="0.7"/>
    <circle cx="50" cy="50" r="32" fill="none" stroke="#EAC973" stroke-width="5"/>
    <circle cx="49" cy="49" r="32" fill="none" stroke="#FFE9A8" stroke-width="1.5"/>
    <circle cx="52" cy="52" r="7" fill="#7A4F0F"/>
    <circle cx="50" cy="50" r="7" fill="#EAC973"/>
    <circle cx="48" cy="48" r="3" fill="#FFE9A8"/>
    """
    return make_svg(content, size)


def sym_moon(size=22):
    # Mondsichel via fill-rule=evenodd: aussen Kreis + innen Kreis = transparenter Biss
    # 3D-Effekt: Schatten unten (dark gold), Mitte (gold), Highlight (light gold)
    moon_path = ('M 50 18 A 32 32 0 1 1 50 82 A 32 32 0 1 1 50 18 Z '
                 'M 62 22 A 26 26 0 1 1 62 74 A 26 26 0 1 1 62 22 Z')
    moon_path_shadow = ('M 52 20 A 32 32 0 1 1 52 84 A 32 32 0 1 1 52 20 Z '
                        'M 64 24 A 26 26 0 1 1 64 76 A 26 26 0 1 1 64 24 Z')
    content = f'''
    <path fill-rule="evenodd" fill="#7A4F0F" opacity="0.7" d="{moon_path_shadow}"/>
    <path fill-rule="evenodd" fill="#EAC973" d="{moon_path}"/>
    '''
    return make_svg(content, size)


def _three_layer(paths, size=22):
    """Helper für Planeten: 3 Layer-Pfade."""
    p = "".join(paths)
    content = f"""
    <g stroke="#7A4F0F" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity="0.7" transform="translate(2,2)">{p}</g>
    <g stroke="#EAC973" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none">{p}</g>
    <g stroke="#FFE9A8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(-0.5,-1)">{p}</g>
    """
    return make_svg(content, size)


def sym_mercury(size=22):
    return _three_layer([
        '<path d="M 38 22 Q 50 12 62 22"/>',
        '<circle cx="50" cy="42" r="13"/>',
        '<line x1="50" y1="58" x2="50" y2="82"/>',
        '<line x1="38" y1="72" x2="62" y2="72"/>',
    ], size)


def sym_venus(size=22):
    return _three_layer([
        '<circle cx="50" cy="38" r="18"/>',
        '<line x1="50" y1="56" x2="50" y2="84"/>',
        '<line x1="38" y1="72" x2="62" y2="72"/>',
    ], size)


def sym_mars(size=22):
    return _three_layer([
        '<circle cx="42" cy="60" r="18"/>',
        '<line x1="55" y1="47" x2="78" y2="24"/>',
        '<polyline points="62,22 78,22 78,38"/>',
    ], size)


def sym_jupiter(size=22):
    return _three_layer([
        '<path d="M 26 28 Q 26 18 38 18 Q 52 18 52 36 L 52 78"/>',
        '<line x1="42" y1="55" x2="78" y2="55"/>',
    ], size)


def sym_saturn(size=22):
    return _three_layer([
        '<line x1="42" y1="22" x2="42" y2="76"/>',
        '<line x1="28" y1="34" x2="58" y2="34"/>',
        '<path d="M 42 58 Q 42 80 60 80 Q 78 80 78 64"/>',
    ], size)


def sym_uranus(size=22):
    return _three_layer([
        '<line x1="50" y1="20" x2="50" y2="60"/>',
        '<line x1="30" y1="40" x2="70" y2="40"/>',
        '<circle cx="50" cy="72" r="10"/>',
    ], size)


def sym_neptune(size=22):
    return _three_layer([
        '<path d="M 22 28 L 22 50 Q 22 70 50 70 Q 78 70 78 50 L 78 28"/>',
        '<line x1="50" y1="28" x2="50" y2="80"/>',
        '<line x1="36" y1="72" x2="64" y2="72"/>',
    ], size)


def sym_pluto(size=22):
    return _three_layer([
        '<line x1="50" y1="44" x2="50" y2="84"/>',
        '<line x1="38" y1="64" x2="62" y2="64"/>',
        '<path d="M 30 38 Q 30 18 50 18 Q 70 18 70 38 Q 70 50 50 50 Q 30 50 30 38"/>',
    ], size)


def sym_chiron(size=22):
    return _three_layer([
        '<path d="M 35 22 L 62 32 L 35 42"/>',
        '<line x1="52" y1="32" x2="52" y2="62"/>',
        '<circle cx="52" cy="74" r="10"/>',
    ], size)


def sym_asc(size=22):
    """Aszendent - Text 'AC' im 3D-Gold-Stil."""
    content = """
    <text x="52" y="68" text-anchor="middle" font-family="Times, serif" font-size="42" font-weight="bold" fill="#7A4F0F" transform="translate(2,2)" opacity="0.7">AC</text>
    <text x="50" y="66" text-anchor="middle" font-family="Times, serif" font-size="42" font-weight="bold" fill="#EAC973">AC</text>
    """
    return make_svg(content, size)


def sym_mc(size=22):
    """MC - Medium Coeli."""
    content = """
    <text x="52" y="68" text-anchor="middle" font-family="Times, serif" font-size="42" font-weight="bold" fill="#7A4F0F" transform="translate(2,2)" opacity="0.7">MC</text>
    <text x="50" y="66" text-anchor="middle" font-family="Times, serif" font-size="42" font-weight="bold" fill="#EAC973">MC</text>
    """
    return make_svg(content, size)


# Mapping deutsch → SVG-Funktion (für Aspekt-Tabelle)
PLANET_SYMBOLS = {
    "Sonne": sym_sun,
    "Mond": sym_moon,
    "Merkur": sym_mercury,
    "Venus": sym_venus,
    "Mars": sym_mars,
    "Jupiter": sym_jupiter,
    "Saturn": sym_saturn,
    "Uranus": sym_uranus,
    "Neptun": sym_neptune,
    "Pluto": sym_pluto,
    "Chiron": sym_chiron,
    "Aszendent": sym_asc,
    "MC": sym_mc,
}


# ============================================================
# DYNAMICS ICONS (Box-Symbole)
# ============================================================

def icon_heart(size=20):
    content = """
    <path d="M 50 82 Q 18 60 18 38 Q 18 22 34 22 Q 44 22 50 34 Q 56 22 66 22 Q 82 22 82 38 Q 82 60 50 82 Z" fill="#7A4F0F" opacity="0.7" transform="translate(2,2)"/>
    <path d="M 50 80 Q 16 58 16 36 Q 16 20 32 20 Q 42 20 50 32 Q 58 20 68 20 Q 84 20 84 36 Q 84 58 50 80 Z" fill="#EAC973"/>
    <path d="M 50 70 Q 25 52 25 36 Q 25 26 35 26 Q 42 26 48 34 L 50 36 L 50 70 Z" fill="#FFE9A8" opacity="0.5"/>
    """
    return make_svg(content, size)


def icon_scale(size=20):
    content = """
    <g stroke="#7A4F0F" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.7" transform="translate(2,2)">
        <line x1="50" y1="20" x2="50" y2="80"/>
        <line x1="20" y1="80" x2="80" y2="80"/>
        <line x1="20" y1="38" x2="80" y2="38"/>
        <path d="M 10 50 L 30 50 L 25 60 Z"/>
        <path d="M 70 50 L 90 50 L 85 60 Z"/>
    </g>
    <g stroke="#EAC973" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <line x1="50" y1="20" x2="50" y2="80"/>
        <line x1="20" y1="80" x2="80" y2="80"/>
        <line x1="20" y1="38" x2="80" y2="38"/>
        <path d="M 10 50 L 30 50 L 25 60 Z"/>
        <path d="M 70 50 L 90 50 L 85 60 Z"/>
    </g>
    """
    return make_svg(content, size)


def icon_wave(size=20):
    content = """
    <g stroke="#7A4F0F" stroke-width="8" fill="none" stroke-linecap="round" opacity="0.7" transform="translate(2,2)">
        <path d="M 14 50 Q 26 30 38 50 T 62 50 T 86 50"/>
        <path d="M 14 70 Q 26 50 38 70 T 62 70 T 86 70"/>
    </g>
    <g stroke="#EAC973" stroke-width="6" fill="none" stroke-linecap="round">
        <path d="M 14 50 Q 26 30 38 50 T 62 50 T 86 50"/>
        <path d="M 14 70 Q 26 50 38 70 T 62 70 T 86 70"/>
    </g>
    """
    return make_svg(content, size)


def icon_speech(size=20):
    content = """
    <path d="M 18 22 L 82 22 Q 88 22 88 28 L 88 60 Q 88 66 82 66 L 56 66 L 42 80 L 42 66 L 18 66 Q 12 66 12 60 L 12 28 Q 12 22 18 22 Z" fill="#7A4F0F" opacity="0.7" transform="translate(2,2)"/>
    <path d="M 16 20 L 80 20 Q 86 20 86 26 L 86 58 Q 86 64 80 64 L 54 64 L 40 78 L 40 64 L 16 64 Q 10 64 10 58 L 10 26 Q 10 20 16 20 Z" fill="#EAC973"/>
    <circle cx="32" cy="42" r="3" fill="#0B1629"/>
    <circle cx="48" cy="42" r="3" fill="#0B1629"/>
    <circle cx="64" cy="42" r="3" fill="#0B1629"/>
    """
    return make_svg(content, size)


def icon_infinity(size=22):
    content = """
    <g stroke="#7A4F0F" stroke-width="9" fill="none" stroke-linecap="round" opacity="0.7" transform="translate(2,2)">
        <path d="M 30 50 Q 18 32 30 32 Q 42 32 50 50 Q 58 68 70 68 Q 82 68 70 50 Q 58 32 50 50 Q 42 68 30 68 Q 18 68 30 50"/>
    </g>
    <g stroke="#EAC973" stroke-width="7" fill="none" stroke-linecap="round">
        <path d="M 30 50 Q 18 32 30 32 Q 42 32 50 50 Q 58 68 70 68 Q 82 68 70 50 Q 58 32 50 50 Q 42 68 30 68 Q 18 68 30 50"/>
    </g>
    """
    return make_svg(content, size)


# ============================================================
# NUMEROLOGIE BADGE (grosse Zahl im Medaillon)
# ============================================================

def num_badge(number, size=80):
    """Goldene Zahl im 3D-Medaillon (für Numerologie)."""
    return (
        f'<svg class="num-badge" width="{size}" height="{size}" '
        'viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="52" cy="52" r="46" fill="#7A4F0F" opacity="0.8"/>'
        '<circle cx="50" cy="50" r="46" fill="#0B1629"/>'
        '<circle cx="50" cy="50" r="46" fill="none" stroke="#EAC973" stroke-width="2.5"/>'
        '<circle cx="50" cy="50" r="42" fill="none" stroke="#FFE9A8" stroke-width="0.8"/>'
        f'<text x="52" y="71" text-anchor="middle" font-family="Cormorant Garamond, Times, serif" font-size="56" font-weight="bold" fill="#7A4F0F" opacity="0.6">{number}</text>'
        f'<text x="50" y="69" text-anchor="middle" font-family="Cormorant Garamond, Times, serif" font-size="56" font-weight="bold" fill="#EAC973">{number}</text>'
        f'<text x="49" y="68" text-anchor="middle" font-family="Cormorant Garamond, Times, serif" font-size="56" font-weight="bold" fill="#FFE9A8" opacity="0.5">{number}</text>'
        '</svg>'
    )


# ============================================================
# Hilfsfunktionen
# ============================================================

# Mapping englisch → deutsch (für Tierkreiszeichen)
SIGN_EN_TO_DE = {
    "Aries": "Widder", "Ari": "Widder",
    "Taurus": "Stier", "Tau": "Stier",
    "Gemini": "Zwilling", "Gem": "Zwilling",
    "Cancer": "Krebs", "Can": "Krebs",
    "Leo": "Löwe",
    "Virgo": "Jungfrau", "Vir": "Jungfrau",
    "Libra": "Waage", "Lib": "Waage",
    "Scorpio": "Skorpion", "Sco": "Skorpion",
    "Sagittarius": "Schütze", "Sag": "Schütze",
    "Capricorn": "Steinbock", "Cap": "Steinbock",
    "Aquarius": "Wassermann", "Aqu": "Wassermann",
    "Pisces": "Fische", "Pis": "Fische",
}

# Mapping englisch → vollname EN (für ZODIAC_PATHS)
SIGN_TO_FULL_EN = {
    "Ari": "Aries", "Aries": "Aries",
    "Tau": "Taurus", "Taurus": "Taurus",
    "Gem": "Gemini", "Gemini": "Gemini",
    "Can": "Cancer", "Cancer": "Cancer",
    "Leo": "Leo",
    "Vir": "Virgo", "Virgo": "Virgo",
    "Lib": "Libra", "Libra": "Libra",
    "Sco": "Scorpio", "Scorpio": "Scorpio",
    "Sag": "Sagittarius", "Sagittarius": "Sagittarius",
    "Cap": "Capricorn", "Capricorn": "Capricorn",
    "Aqu": "Aquarius", "Aquarius": "Aquarius",
    "Pis": "Pisces", "Pisces": "Pisces",
}


def sign_de(sign_en):
    """Wandelt englischen Sternzeichen-Code in deutsche Bezeichnung."""
    return SIGN_EN_TO_DE.get(sign_en, sign_en)


def zodiac_for_sign(sign_code, size=70, with_ring=True):
    """
    Erzeugt Tierkreiszeichen-SVG für einen API-Sign-Code (z.B. 'Aqu', 'Aquarius').
    """
    full = SIGN_TO_FULL_EN.get(sign_code)
    if not full:
        return ""
    return zodiac_symbol(full, size, with_ring)
