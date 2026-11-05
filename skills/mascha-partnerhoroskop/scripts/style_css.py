"""
Mascha Cosmos PDF Stylesheet (CSS).

Wird von build_report.py importiert. Enthält alle Style-Regeln für die 30 Sektionen.
"""

CSS = """
@page {
    size: A4;
    margin: 28mm 18mm 22mm 22mm;
    background: #EBE7DC;

    @top-center {
        content: "PARTNERHOROSKOP  ·  GENERIERT VON MASCHA";
        color: #EAC973;
        font-family: Arial, sans-serif;
        font-size: 9pt;
        font-weight: 700;
        letter-spacing: 1.5pt;
    }
    @top-right {
        content: "Seite " counter(page);
        color: #888780;
        font-family: Arial, sans-serif;
        font-size: 8.5pt;
        letter-spacing: 1pt;
    }
    @bottom-center {
        content: "MASCHA COSMOS  ·  FIND YOUR DESTINY";
        color: #BA7517;
        font-family: Arial, sans-serif;
        font-size: 8.5pt;
        font-weight: 700;
        letter-spacing: 2pt;
    }
    @bottom-right {
        content: counter(page);
        color: #888780;
        font-family: Arial, sans-serif;
        font-size: 8.5pt;
    }
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { background: #EBE7DC; }

body {
    font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    background: #EBE7DC;
    color: #0B1629;
    font-size: 10.5pt;
    line-height: 1.6;
}

body::before {
    content: "";
    position: fixed;
    top: -28mm;
    left: -22mm;
    right: -18mm;
    height: 20mm;
    background: #0B1629;
    z-index: -1;
}

body::after {
    content: "";
    position: fixed;
    top: -28mm;
    left: -22mm;
    bottom: -22mm;
    width: 5mm;
    background: #EAC973;
    z-index: -1;
}

h1, h2, h3, h4 { font-weight: 700; color: #0B1629; page-break-after: avoid; }
p { margin-bottom: 3mm; text-align: justify; }
strong { font-weight: 700; }

/* ===== COVER ===== */
.cover { text-align: center; page-break-after: always; }
.cover .logo { width: 30mm; margin: 0 auto 4mm auto; display: block; }
.hero-img { width: 100%; display: block; margin: 0 auto; }
.cover-block {
    background: #0B1629;
    color: #FFFFFF;
    padding: 11mm 10mm;
    margin: 2mm 0 5mm 0;
    border-bottom: 2.5pt solid #EAC973;
    box-shadow: 0 4mm 10mm rgba(11, 22, 41, 0.25);
}
.cover-block .eyebrow { color: #EAC973; font-size: 10pt; letter-spacing: 4pt; margin-bottom: 5mm; font-weight: 400; }
.cover-block h1 { font-size: 30pt; font-weight: 700; line-height: 1.1; margin-bottom: 5mm; color: #FFFFFF; }
.cover-block .subtitle { color: #EAC973; font-size: 10.5pt; line-height: 1.7; }

.persons-data { display: table; width: 100%; margin: 0 0 5mm 0; border-spacing: 4mm 0; border-collapse: separate; }
.persons-data .person-data {
    display: table-cell; width: 50%; text-align: center;
    background: #0B1629; color: #FFFFFF;
    padding: 5mm 4mm;
    border-bottom: 2pt solid #EAC973;
    vertical-align: middle;
    box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.25);
}
.persons-data .person-data .zodiac-symbol { margin-bottom: 2mm; }
.persons-data .person-data .name { font-size: 17pt; font-weight: 700; color: #FFFFFF; margin-bottom: 2mm; }
.persons-data .person-data .data { color: #EAC973; font-size: 9.5pt; line-height: 1.6; }

.intro-text { font-style: italic; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; font-size: 12pt; line-height: 1.65; color: #0B1629; text-align: justify; margin: 3mm 0; }

/* ===== SECTION HEADER ===== */
.section-header {
    background: #F3EEDB;
    border-left: 4pt solid #EAC973;
    padding: 3.5mm 5mm;
    margin: 9mm 0 4mm 0;
    font-weight: 700;
    font-size: 13pt;
    color: #0B1629;
    page-break-after: avoid;
    page-break-inside: avoid;
    box-shadow: 0 2mm 4mm rgba(11, 22, 41, 0.1);
}

/* ===== GOLDENER SATZ (Quote-Box) ===== */
.golden-quote {
    background: #F3EEDB;
    border-left: 4pt solid #EAC973;
    padding: 4mm 5mm;
    margin: 5mm 0;
    font-style: italic;
    font-weight: 700;
    color: #BA7517;
    font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif;
    font-size: 12pt;
    line-height: 1.55;
    box-shadow: 0 2mm 4mm rgba(11, 22, 41, 0.08);
    page-break-inside: avoid;
}

/* ===== SELF-REFLEXIONS-FRAGE ===== */
.reflection {
    background: #F3EEDB;
    border-left: 4pt solid #EAC973;
    padding: 4mm 5mm;
    margin: 5mm 0;
    font-style: italic;
    color: #BA7517;
    font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif;
    font-size: 11.5pt;
    line-height: 1.55;
    box-shadow: 0 2mm 4mm rgba(11, 22, 41, 0.08);
}
.reflection strong { color: #BA7517; }

/* ===== TIP BOX ===== */
.tip-box {
    background: linear-gradient(135deg, #FBF3D9 0%, #F3E4B0 100%);
    border-left: 4pt solid #EAC973;
    padding: 3mm 4mm 3mm 12mm;
    margin: 3mm 0;
    page-break-inside: avoid;
    position: relative;
    border-radius: 0 2mm 2mm 0;
    box-shadow: 0 2mm 4mm rgba(186, 117, 23, 0.15);
}
.tip-box::before {
    content: "";
    position: absolute;
    left: 3mm;
    top: 3mm;
    width: 6mm;
    height: 6mm;
    background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='46' fill='%23EAC973'/><text x='50' y='66' text-anchor='middle' font-family='Times' font-size='52' font-weight='bold' fill='%230B1629'>!</text></svg>") no-repeat center;
    background-size: contain;
}
.tip-box .tip-label { color: #BA7517; font-weight: 700; font-size: 8.5pt; letter-spacing: 1.5pt; text-transform: uppercase; margin-bottom: 1mm; }
.tip-box .tip-body { color: #0B1629; font-size: 10pt; line-height: 1.55; }
.tip-box .tip-body strong { color: #BA7517; }

/* ===== SCORE CARD ===== */
.score-card {
    background: #FFFFFF;
    border: 1pt solid #EAC973;
    border-radius: 2mm;
    padding: 5mm;
    margin: 4mm 0;
    text-align: center;
    page-break-inside: avoid;
    box-shadow: 0 4mm 8mm rgba(11, 22, 41, 0.12);
}
.score-card .big { font-size: 36pt; font-weight: 700; color: #EAC973; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; line-height: 1; }
.score-card .big .of { font-size: 16pt; color: #888780; font-weight: 400; }
.score-card .label { color: #0B1629; font-size: 9pt; letter-spacing: 2pt; text-transform: uppercase; margin-top: 2mm; }
.score-card .rating { font-weight: 700; margin-top: 2mm; color: #1D9E75; font-size: 11pt; }

.score-item { margin-bottom: 5mm; page-break-inside: avoid; }
.score-item-header { display: table; width: 100%; margin-bottom: 1.5mm; }
.score-item-name { display: table-cell; font-weight: 700; font-size: 10.5pt; width: 35%; vertical-align: middle; }
.score-item-bar { display: table-cell; width: 50%; vertical-align: middle; padding: 0 3mm; }
.score-item-value { display: table-cell; width: 15%; text-align: right; font-weight: 700; color: #BA7517; font-size: 11pt; vertical-align: middle; }
.bar-track { width: 100%; height: 3.5mm; background: #F3EEDB; border-radius: 1mm; overflow: hidden; box-shadow: inset 0 1pt 2pt rgba(0,0,0,0.1); }
.bar-fill { height: 100%; background: linear-gradient(90deg, #EAC973 0%, #BA7517 100%); border-radius: 1mm; }
.score-item-explanation { font-size: 9.5pt; color: #555; line-height: 1.55; padding-left: 0; font-style: italic; margin-top: 1mm; }

/* ===== BALKEN-DIAGRAMME (Lebens-Prioritäten, Elemente, etc.) ===== */
.bar-chart-grid {
    display: table;
    width: 100%;
    margin: 4mm 0;
    border-spacing: 4mm 0;
    border-collapse: separate;
}
.bar-chart-col {
    display: table-cell;
    background: #FFFFFF;
    border-top: 3pt solid #EAC973;
    padding: 5mm;
    width: 50%;
    vertical-align: top;
    box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.1);
    border-radius: 0 0 2mm 2mm;
}
.bar-chart-col .chart-title {
    font-weight: 700;
    font-size: 11.5pt;
    margin-bottom: 3mm;
    color: #0B1629;
    text-align: center;
    border-bottom: 0.5pt solid #D8D4C8;
    padding-bottom: 2mm;
}
.bar-chart-col .bar-row {
    display: table;
    width: 100%;
    margin-bottom: 1.8mm;
}
.bar-chart-col .bar-label {
    display: table-cell;
    font-size: 8.5pt;
    width: 38%;
    vertical-align: middle;
    color: #0B1629;
}
.bar-chart-col .bar-area {
    display: table-cell;
    width: 50%;
    vertical-align: middle;
    padding: 0 2mm;
}
.bar-chart-col .bar-val {
    display: table-cell;
    width: 12%;
    text-align: right;
    font-size: 8.5pt;
    font-weight: 700;
    color: #BA7517;
}
.bar-chart-col .bar-fill-small {
    height: 2.5mm;
    background: linear-gradient(90deg, #EAC973 0%, #BA7517 100%);
    border-radius: 0.5mm;
}
.bar-chart-col .bar-track-small {
    width: 100%;
    height: 2.5mm;
    background: #F3EEDB;
    border-radius: 0.5mm;
    overflow: hidden;
}

/* ===== ELEMENTE-VERTEILUNG (mit Farben pro Element) ===== */
.element-fire .bar-fill-small { background: linear-gradient(90deg, #FFA94D 0%, #C0392B 100%); }
.element-earth .bar-fill-small { background: linear-gradient(90deg, #A0826D 0%, #5C4033 100%); }
.element-air .bar-fill-small { background: linear-gradient(90deg, #B8D4E3 0%, #4A90A4 100%); }
.element-water .bar-fill-small { background: linear-gradient(90deg, #6B9EE0 0%, #2E5C8A 100%); }

/* ===== HORIZONTALE SKALA mit Markierungen (für Materielles) ===== */
.scale-row {
    background: #FFFFFF;
    border-left: 3pt solid #EAC973;
    padding: 4mm 5mm;
    margin: 4mm 0;
    box-shadow: 0 2mm 5mm rgba(11, 22, 41, 0.1);
    border-radius: 0 2mm 2mm 0;
    page-break-inside: avoid;
}
.scale-row .scale-title { font-weight: 700; font-size: 10pt; margin-bottom: 7mm; color: #0B1629; }
.scale-row .scale-track {
    position: relative;
    width: 100%;
    height: 6mm;
    background: linear-gradient(90deg, #FBF3D9 0%, #EAC973 50%, #BA7517 100%);
    border-radius: 3mm;
    margin: 3mm 0;
}
.scale-row .scale-marker {
    position: absolute;
    top: -3mm;
    width: 5mm;
    height: 12mm;
    background: #0B1629;
    border: 2pt solid #EAC973;
    border-radius: 1mm;
    transform: translateX(-2.5mm);
}
.scale-row .scale-marker .scale-marker-label {
    position: absolute;
    top: -5mm;
    left: 50%;
    transform: translateX(-50%);
    font-size: 8pt;
    font-weight: 700;
    color: #0B1629;
    white-space: nowrap;
}
.scale-row .scale-labels {
    display: table;
    width: 100%;
    font-size: 8pt;
    color: #888780;
    text-transform: uppercase;
    letter-spacing: 1pt;
}
.scale-row .scale-labels span { display: table-cell; }
.scale-row .scale-labels span:last-child { text-align: right; }

/* ===== NUMBERED BLOCK ===== */
.numbered-block { margin: 4mm 0; padding-left: 14mm; position: relative; padding-top: 1mm; padding-bottom: 2mm; page-break-inside: avoid; }
.numbered-block::before { content: ""; position: absolute; left: 12mm; top: 2mm; bottom: 2mm; width: 0.5pt; background: #D8D4C8; }
.numbered-block .num { position: absolute; left: 0; top: 1mm; width: 10mm; text-align: center; color: #EAC973; font-weight: 700; font-size: 22pt; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; line-height: 1; text-shadow: 1pt 1pt 0 #7A4F0F; }
.numbered-block .title { font-weight: 700; font-size: 11.5pt; color: #0B1629; margin-bottom: 1.5mm; }
.numbered-block .body { font-size: 10.2pt; line-height: 1.6; color: #0B1629; text-align: justify; }

/* ===== BULLETS ===== */
ul.bullets { list-style: none; margin: 3mm 0 4mm 4mm; }
ul.bullets li { position: relative; padding-left: 6mm; margin-bottom: 2.5mm; text-align: justify; line-height: 1.6; }
ul.bullets li::before { content: "•"; color: #EAC973; font-weight: 700; position: absolute; left: 0; font-size: 14pt; top: -3pt; }

/* ===== DYNAMICS GRID ===== */
.dynamics-grid { display: table; width: 100%; margin: 4mm 0; border-collapse: separate; border-spacing: 2mm 2mm; table-layout: fixed; }
.dyn-row { display: table-row; }
.dyn-cell { display: table-cell; background: #FFFFFF; border-left: 3pt solid #EAC973; padding: 2.5mm 3.5mm; width: 50%; vertical-align: top; box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.12); border-radius: 0 2mm 2mm 0; }
.dyn-cell-wide { background: #FFFFFF; border-left: 3pt solid #EAC973; padding: 3mm 4mm; margin: 2mm 0 3mm 0; page-break-inside: avoid; box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.12); border-radius: 0 2mm 2mm 0; }
.dyn-cell .dyn-header, .dyn-cell-wide .dyn-header { display: flex; align-items: center; gap: 2mm; margin-bottom: 1.5mm; }
.dyn-cell .dyn-label, .dyn-cell-wide .dyn-label { color: #888780; font-size: 8.5pt; text-transform: uppercase; letter-spacing: 1pt; }
.dyn-cell .dyn-value, .dyn-cell-wide .dyn-value { font-weight: 700; color: #0B1629; font-size: 10.5pt; margin-bottom: 1.5mm; }
.dyn-cell .dyn-desc, .dyn-cell-wide .dyn-desc { font-size: 9pt; line-height: 1.5; color: #0B1629; text-align: justify; }
.dyn-cell .dyn-desc strong, .dyn-cell-wide .dyn-desc strong { color: #BA7517; }

/* ===== PERSONS (zwei Karten nebeneinander) ===== */
.persons { display: table; width: 100%; margin: 4mm 0; border-spacing: 3mm 0; border-collapse: separate; }
.persons .person { display: table-cell; background: #FFFFFF; border-top: 3pt solid #EAC973; padding: 5mm; width: 50%; vertical-align: top; box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.12); border-radius: 0 0 2mm 2mm; }
.persons .person h3 { color: #0B1629; font-size: 14pt; margin-bottom: 2mm; font-weight: 700; display: flex; align-items: center; gap: 2mm; }
.persons .person .lang-primary { color: #BA7517; font-weight: 700; font-size: 12pt; margin-bottom: 2mm; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; font-style: italic; }
.persons .person p { font-size: 9.5pt; line-height: 1.55; margin-bottom: 2mm; text-align: left; }
.persons .person .meta-row { font-size: 9pt; color: #888780; margin-bottom: 1mm; }
.persons .person .meta-row strong { color: #0B1629; }
.persons .person ul { list-style: none; padding: 0; margin: 2mm 0 0 0; }
.persons .person ul li { font-size: 9.5pt; line-height: 1.5; padding: 1mm 0 1mm 5mm; position: relative; text-align: left; }
.persons .person ul li::before { content: "→"; color: #EAC973; position: absolute; left: 0; font-weight: 700; }

.profile-box { text-align: left; }
.profile-line { margin-bottom: 1.5mm; font-size: 9.5pt; line-height: 1.45; text-align: left; }
.profile-line strong { color: #BA7517; display: inline-block; min-width: 32mm; }

/* ===== FLAGS ===== */
.flag-box { background: #FFFFFF; padding: 4mm 5mm; margin: 3mm 0; border-left: 3pt solid; page-break-inside: avoid; box-shadow: 0 2mm 5mm rgba(11, 22, 41, 0.1); border-radius: 0 2mm 2mm 0; }
.flag-box.green { border-color: #1D9E75; }
.flag-box.yellow { border-color: #D4A824; }
.flag-box.red { border-color: #C0392B; }
.flag-box .flag-title { font-weight: 700; margin-bottom: 2mm; text-transform: uppercase; font-size: 9pt; letter-spacing: 1pt; }
.flag-box.green .flag-title { color: #1D9E75; }
.flag-box.yellow .flag-title { color: #BA7517; }
.flag-box.red .flag-title { color: #C0392B; }
.flag-box ul { list-style: none; }
.flag-box li { padding: 0.8mm 0; font-size: 10pt; line-height: 1.5; padding-left: 4mm; position: relative; }
.flag-box li::before { content: "•"; position: absolute; left: 0; color: #888780; }

/* ===== CLOSING ===== */
.closing-quote { background: #0B1629; border: 1pt solid #EAC973; padding: 10mm 12mm; margin: 6mm 0 0 0; text-align: center; color: #FFFFFF; page-break-inside: avoid; box-shadow: 0 5mm 10mm rgba(11, 22, 41, 0.3); }
.closing-quote .stars { color: #EAC973; font-size: 14pt; letter-spacing: 8pt; margin-bottom: 5mm; }
.closing-quote .quote { color: #EAC973; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; font-style: italic; font-weight: 700; font-size: 15pt; line-height: 1.5; margin-bottom: 5mm; }
.closing-quote .signoff { font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; font-style: italic; font-size: 11pt; color: #FFFFFF; line-height: 1.5; }

/* ===== ASPECT TABLE ===== */
.aspect-table { width: 100%; border-collapse: collapse; margin: 3mm 0; font-size: 9.5pt; background: #FFFFFF; page-break-inside: avoid; box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.12); }
.aspect-table th { background: #0B1629; color: #EAC973; text-align: left; padding: 2mm 3mm; font-weight: 400; font-size: 8.5pt; text-transform: uppercase; letter-spacing: 1pt; }
.aspect-table td { padding: 2mm 3mm; border-bottom: 0.5pt solid #EEE9D6; vertical-align: middle; }
.planet-cell { display: flex; align-items: center; gap: 2mm; }
.planet-cell svg { flex-shrink: 0; }
.planet-cell span { font-size: 9.5pt; }
.aspect-table td.aspect-type { font-weight: 700; font-size: 10pt; }
.aspect-trigon, .aspect-trine, .aspect-sextil, .aspect-sextile { color: #1D9E75; }
.aspect-conjunction { color: #2E75B6; }
.aspect-opposition, .aspect-quadrat, .aspect-square { color: #C0392B; }
.aspect-table tr:nth-child(even) { background: #FBF8EE; }

.page-break { page-break-before: always; }

.hero-mini { width: 100%; display: block; margin: 4mm 0; }
.hero-mini.narrow { width: 80%; margin-left: auto; margin-right: auto; }
.img-caption { text-align: center; font-style: italic; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; color: #888780; font-size: 10pt; margin: -2mm 0 5mm 0; }

/* ===== PORTRAIT ===== */
.portrait { background: #FFFFFF; padding: 6mm; margin: 4mm 0; border-left: 4pt solid #EAC973; box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.1); border-radius: 0 2mm 2mm 0; page-break-inside: avoid; }
.portrait-header { display: flex; align-items: center; gap: 4mm; margin-bottom: 4mm; padding-bottom: 3mm; border-bottom: 0.5pt solid #D8D4C8; }
.portrait-header .zodiac-mini { flex-shrink: 0; }
.portrait-header h2 { color: #0B1629; font-size: 17pt; margin: 0; line-height: 1.1; }
.portrait-header .subtitle { color: #BA7517; font-size: 10pt; font-style: italic; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; margin-top: 1mm; }
.portrait p { font-size: 10pt; line-height: 1.6; margin-bottom: 2.5mm; }
.portrait .strengths { background: #F3EEDB; padding: 3mm 4mm; margin-top: 3mm; border-radius: 1mm; }
.portrait .strengths .strength-title { font-weight: 700; color: #BA7517; font-size: 9pt; letter-spacing: 1pt; text-transform: uppercase; margin-bottom: 2mm; }
.portrait .strengths ul { list-style: none; margin: 0; }
.portrait .strengths li { font-size: 9.5pt; line-height: 1.5; padding: 0.5mm 0 0.5mm 5mm; position: relative; }
.portrait .strengths li::before { content: "✦"; color: #EAC973; position: absolute; left: 0; }
.portrait .means-for-partner { margin-top: 3mm; padding: 3mm 4mm; background: #FBF3D9; border-left: 3pt solid #EAC973; font-size: 9.5pt; line-height: 1.55; border-radius: 0 1mm 1mm 0; }
.portrait .means-for-partner strong { color: #BA7517; }

/* ===== NUMEROLOGY GRID ===== */
.num-grid { display: table; width: 100%; margin: 4mm 0; border-spacing: 3mm 3mm; border-collapse: separate; table-layout: fixed; }
.num-grid-row { display: table-row; }
.num-cell { display: table-cell; background: #FFFFFF; padding: 4mm; text-align: center; vertical-align: top; border-top: 3pt solid #EAC973; width: 50%; box-shadow: 0 3mm 6mm rgba(11, 22, 41, 0.1); border-radius: 0 0 2mm 2mm; }
.num-cell .num-badge-wrap { margin: 0 auto 3mm auto; width: 18mm; }
.num-cell .num-label { color: #888780; font-size: 8.5pt; text-transform: uppercase; letter-spacing: 1.5pt; margin-bottom: 1mm; }
.num-cell .num-theme { font-weight: 700; color: #BA7517; font-size: 11pt; margin-bottom: 2mm; font-family: "Cormorant Garamond", "Times New Roman", Georgia, serif; font-style: italic; }
.num-cell .num-desc { font-size: 9.5pt; line-height: 1.5; color: #0B1629; text-align: left; }

/* ===== TRANSLATION TABLE (für Sektion 9) ===== */
.translation-table {
    width: 100%;
    border-collapse: collapse;
    margin: 3mm 0;
    background: #FFFFFF;
    font-size: 9.5pt;
    page-break-inside: avoid;
    box-shadow: 0 2mm 5mm rgba(11, 22, 41, 0.08);
}
.translation-table th {
    background: #F3EEDB;
    color: #BA7517;
    padding: 2mm 3mm;
    text-align: left;
    font-weight: 700;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 1pt;
}
.translation-table td {
    padding: 2mm 3mm;
    border-bottom: 0.5pt solid #EEE9D6;
    vertical-align: top;
    line-height: 1.45;
}

/* ===== CONFLICT MAP (für Sektion 21) ===== */
.conflict-field {
    background: #FFFFFF;
    border-left: 3pt solid #C0392B;
    padding: 4mm 5mm;
    margin: 3mm 0;
    page-break-inside: avoid;
    box-shadow: 0 2mm 5mm rgba(11, 22, 41, 0.1);
    border-radius: 0 2mm 2mm 0;
}
.conflict-field h4 {
    color: #C0392B;
    font-size: 11pt;
    margin-bottom: 2mm;
    text-transform: none;
}
.conflict-field .anchor {
    font-style: italic;
    color: #888780;
    font-size: 9pt;
    margin-bottom: 2mm;
}
.conflict-field .body { font-size: 9.5pt; line-height: 1.55; }
.conflict-field .body strong { color: #BA7517; }

/* ===== SACRED BOX (für Karma, Sexualität, Spiritualität – heller Goldton, sanft) ===== */
.sacred-box {
    background: linear-gradient(135deg, #FBF3D9 0%, #F3EEDB 100%);
    border-left: 4pt solid #BA7517;
    padding: 4mm 5mm;
    margin: 4mm 0;
    page-break-inside: avoid;
    box-shadow: 0 2mm 5mm rgba(186, 117, 23, 0.15);
    border-radius: 0 2mm 2mm 0;
}
.sacred-box h4 {
    color: #BA7517;
    font-size: 11pt;
    margin-bottom: 2mm;
}
.sacred-box .body { font-size: 9.5pt; line-height: 1.6; }
.sacred-box .body strong { color: #BA7517; }
"""
