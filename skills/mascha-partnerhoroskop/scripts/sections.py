"""
Mascha Cosmos - Section Renderers für das Partnerhoroskop-PDF

Eine Render-Funktion pro Sektion. Jede nimmt das `data`-Dict (siehe data_schema.md) und
optional einen assets_dir/logo_path und gibt HTML-Fragment zurück.

Reihenfolge der 30 Sektionen entspricht Lisas Update:
 1. Cover
 2. Intro / Portraits
 3. Score
 4. Lebens-Prioritäten (NEU)
 5. Elemente-Mischung (NEU)
 6. Bedürfnisse (NEU)
 7. Gefühlsebene (NEU)
 8. Wie ihr miteinander sprecht (NEU)
 9. Liebessprachen vertieft (ERWEITERT)
10. Wertesystem und Lebensmission (NEU)
11. Leidenschaftsbereiche (NEU)
12. Materielles / Stabilität (NEU)
13. Welcher Typ ist sie / er (NEU)
14. Synastrie
15. Wichtigste Aspekte
16. Dynamiken
17. Composite
18. Numerologische Resonanz (ERWEITERT)
19. Stärken + Verantwortungs-Verteilung (ERWEITERT)
20. Schwächen + Schatten (NEU)
21. Konfliktlandkarte (ERWEITERT)
22. Authentizität + Masken (NEU)
23. Karmische Wunden + Heilung (NEU)
24. Krisenfähigkeit (NEU)
25. Sexueller Match (NEU)
26. Energetische Besonderheiten (NEU)
27. Spirituelle Aufgabe als Paar (NEU)
28. Beziehungs-Profile
29. Nächste Schritte
30. Closing
"""

from symbols import (
    zodiac_for_sign,
    PLANET_SYMBOLS,
    num_badge,
    icon_heart, icon_scale, icon_wave, icon_speech, icon_infinity,
)


# ============================================================
# HELPER
# ============================================================

def planet_symbol(name_de, size=22):
    fn = PLANET_SYMBOLS.get(name_de)
    if fn:
        return fn(size)
    return ""


def aspect_class(aspect_type):
    a = aspect_type.lower()
    if a in ("trigon", "trine", "sextil", "sextile"):
        return f"aspect-{a}"
    if a in ("konjunktion", "conjunction"):
        return "aspect-conjunction"
    if a in ("opposition",):
        return "aspect-opposition"
    if a in ("quadrat", "square"):
        return "aspect-square"
    return ""


def aspect_row(a):
    s1 = planet_symbol(a["planet1"])
    s2 = planet_symbol(a["planet2"])
    cls = aspect_class(a["aspect"])
    return f'''<tr>
        <td><div class="planet-cell">{s1}<span>{a["planet1"]}</span></div></td>
        <td class="aspect-type {cls}">{a["aspect"]}</td>
        <td><div class="planet-cell">{s2}<span>{a["planet2"]}</span></div></td>
        <td>{a["orb"]}</td>
    </tr>'''


def golden_quote(text):
    """Renders ein zentrales 'Goldener Satz'-Element."""
    return f'<div class="golden-quote">{text}</div>'


def reflection(text):
    """Renders eine Selbstreflexions-Frage-Box."""
    return f'<div class="reflection">{text}</div>'


def sacred_box(title, body):
    """Renders eine 'heilige' Box für Karma/Sex/Spiritualität (sanft gold)."""
    return f'''
<div class="sacred-box">
    <h4>{title}</h4>
    <div class="body">{body}</div>
</div>'''


# ============================================================
# 1. COVER
# ============================================================

def render_cover(d, cover_image_path, logo_path):
    p1, p2 = d["person1"], d["person2"]
    z1 = zodiac_for_sign(p1["sun_sign_code"], 45)
    z2 = zodiac_for_sign(p2["sun_sign_code"], 45)
    return f'''
<div class="cover">
    <img src="{logo_path}" class="logo" alt="Mascha Cosmos">
    <img src="{cover_image_path}" class="hero-img" alt="Cover">
    <div class="cover-block">
        <div class="eyebrow">PARTNERHOROSKOP</div>
        <h1>{p1["name"]} &amp; {p2["name"]}</h1>
        <div class="subtitle">
            Eine Landkarte eurer Verbindung<br>
            Synastrie · Composite · Liebessprachen · Numerologie
        </div>
    </div>
    <div class="persons-data">
        <div class="person-data">
            <div class="zodiac-symbol">{z1}</div>
            <div class="name">{p1["name"]}</div>
            <div class="data">
                {p1["sun_sign_de"]} · {p1["birth_date_de"]}<br>
                {p1["birth_time"]} · {p1["birth_place"]}
            </div>
        </div>
        <div class="person-data">
            <div class="zodiac-symbol">{z2}</div>
            <div class="name">{p2["name"]}</div>
            <div class="data">
                {p2["sun_sign_de"]} · {p2["birth_date_de"]}<br>
                {p2["birth_time"]} · {p2["birth_place"]}
            </div>
        </div>
    </div>
</div>
'''


# ============================================================
# 2. PORTRAITS
# ============================================================

def render_portraits(d):
    p1, p2 = d["person1"], d["person2"]
    pr1 = d["portraits"]["person1"]
    pr2 = d["portraits"]["person2"]
    z1 = zodiac_for_sign(p1["sun_sign_code"], 35)
    z2 = zodiac_for_sign(p2["sun_sign_code"], 35)

    def strengths_ul(items):
        return "".join(f"<li>{x}</li>" for x in items)

    return f'''
<p class="intro-text" style="text-align:center; font-size:13pt;">{d["intro_text"]}</p>

<div class="portrait">
    <div class="portrait-header">
        <div class="zodiac-mini">{z1}</div>
        <div>
            <h2>Wer ist {p1["name"]}?</h2>
            <div class="subtitle">{pr1["subtitle"]}</div>
        </div>
    </div>
    {"".join(f"<p>{para}</p>" for para in pr1["paragraphs"])}
    <div class="strengths">
        <div class="strength-title">Deine Stärken in Beziehung</div>
        <ul>{strengths_ul(pr1["strengths"])}</ul>
    </div>
    <div class="means-for-partner">
        <strong>Was das für {p2["name"]} bedeutet:</strong> {pr1["means_for_partner"]}
    </div>
</div>

<div class="portrait">
    <div class="portrait-header">
        <div class="zodiac-mini">{z2}</div>
        <div>
            <h2>Wer ist {p2["name"]}?</h2>
            <div class="subtitle">{pr2["subtitle"]}</div>
        </div>
    </div>
    {"".join(f"<p>{para}</p>" for para in pr2["paragraphs"])}
    <div class="strengths">
        <div class="strength-title">Deine Stärken in Beziehung</div>
        <ul>{strengths_ul(pr2["strengths"])}</ul>
    </div>
    <div class="means-for-partner">
        <strong>Was das für {p1["name"]} bedeutet:</strong> {pr2["means_for_partner"]}
    </div>
</div>
'''


# ============================================================
# 3. SCORE
# ============================================================

def render_score(d):
    s = d["score"]
    items_html = ""
    for item in s["dimensions"]:
        items_html += f'''
<div class="score-item">
    <div class="score-item-header">
        <div class="score-item-name">{item["name"]}</div>
        <div class="score-item-bar"><div class="bar-track"><div class="bar-fill" style="width: {item["bar_percent"]}%;"></div></div></div>
        <div class="score-item-value">{item["value"]}</div>
    </div>
    <div class="score-item-explanation">{item["explanation"]}</div>
</div>'''
    return f'''
<div class="section-header">Eure Kompatibilität auf einen Blick</div>
<p style="margin-bottom: 4mm;">{s["intro"]}</p>
<div class="score-card">
    <div class="big">{s["total"]}<span class="of">/100</span></div>
    <div class="label">ASTROLOGISCHER GESAMTWERT</div>
    <div class="rating">{s["rating"]}</div>
</div>
{items_html}
'''


# ============================================================
# 4. LEBENS-PRIORITÄTEN (NEU)
# ============================================================

def render_life_priorities(d):
    lp = d["life_priorities"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    def bars_for_person(items):
        rows = ""
        for area, pct in items:
            rows += f'''
<div class="bar-row">
    <div class="bar-label">{area}</div>
    <div class="bar-area"><div class="bar-track-small"><div class="bar-fill-small" style="width:{pct}%;"></div></div></div>
    <div class="bar-val">{pct}%</div>
</div>'''
        return rows

    return f'''
<div class="section-header">Eure Lebens-Prioritäten im Vergleich</div>
<p>{lp["intro"]}</p>

<div class="bar-chart-grid">
    <div class="bar-chart-col">
        <div class="chart-title">{p1}</div>
        {bars_for_person(lp["person1"])}
    </div>
    <div class="bar-chart-col">
        <div class="chart-title">{p2}</div>
        {bars_for_person(lp["person2"])}
    </div>
</div>

{"".join(f"<p>{para}</p>" for para in lp["analysis_paragraphs"])}

{golden_quote(lp["golden_sentence"])}
'''


# ============================================================
# 5. ELEMENTE-MISCHUNG (NEU)
# ============================================================

def render_elements(d, assets_dir):
    el = d["elements"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    def element_bars(percents):
        order = [("Feuer", "fire"), ("Erde", "earth"), ("Luft", "air"), ("Wasser", "water")]
        rows = ""
        for de_name, css_cls in order:
            pct = percents.get(de_name, 0)
            rows += f'''
<div class="bar-row element-{css_cls}">
    <div class="bar-label">{de_name}</div>
    <div class="bar-area"><div class="bar-track-small"><div class="bar-fill-small" style="width:{pct}%;"></div></div></div>
    <div class="bar-val">{pct}%</div>
</div>'''
        return rows

    return f'''
<div class="section-header">Eure Elemente-Mischung</div>

<img src="{assets_dir}/hero_elements.webp" class="hero-mini narrow" alt="Elemente">
<div class="img-caption">{el["image_caption"]}</div>

<div class="bar-chart-grid">
    <div class="bar-chart-col">
        <div class="chart-title">{p1}</div>
        {element_bars(el["person1"])}
    </div>
    <div class="bar-chart-col">
        <div class="chart-title">{p2}</div>
        {element_bars(el["person2"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:3mm;">Element-Mix als Paar</h3>
<p>{el["mix"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure Elemente sich verbinden</h3>
<p>{el["connection"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure Elemente reiben</h3>
<p>{el["friction"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Was im Paar-System fehlt</h3>
<p>{el["missing"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Praktische Übersetzung im Alltag</h3>
<p>{el["everyday"]}</p>

{golden_quote(el["golden_sentence"])}
'''


# ============================================================
# 6. BEDÜRFNISSE (NEU)
# ============================================================

def render_needs(d):
    n = d["needs"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    return f'''
<div class="section-header">Eure Bedürfnisse im Vergleich</div>
<p>{n["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        {"".join(f"<p>{para}</p>" for para in n["person1"]["paragraphs"])}
    </div>
    <div class="person">
        <h3>{p2}</h3>
        {"".join(f"<p>{para}</p>" for para in n["person2"]["paragraphs"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Wo eure Bedürfnisse sich treffen</h3>
<p>{n["meeting"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure Bedürfnisse kollidieren</h3>
<p>{n["colliding"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Bedürfnisse, die ihr schwer versteht beim anderen</h3>
<p>{n["hard_to_understand"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Nervensystem-Sprache als Schlüssel</h3>
<p>{n["nervous_system"]}</p>

{reflection(n["reflection"])}

{golden_quote(n["golden_sentence"])}
'''


# ============================================================
# 7. GEFÜHLSEBENE (NEU)
# ============================================================

def render_feelings(d):
    f = d["feelings"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]
    return f'''
<div class="section-header">Eure Gefühlsebene · Wie ihr fühlt und zeigt</div>
<p>{f["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        {"".join(f"<p>{para}</p>" for para in f["person1"])}
    </div>
    <div class="person">
        <h3>{p2}</h3>
        {"".join(f"<p>{para}</p>" for para in f["person2"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Wo ihr im Gefühl synchron schwingt</h3>
<p>{f["synchron"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo ihr aneinander vorbei fühlt</h3>
<p>{f["pass_by"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wer trägt mehr emotionale Last</h3>
<p>{f["emotional_load"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wer geht nach Streit zuerst aufeinander zu</h3>
<p>{f["who_approaches"]}</p>

{reflection(f["reflection"])}

{golden_quote(f["golden_sentence"])}
'''


# ============================================================
# 8. KOMMUNIKATION (NEU als eigene Sektion)
# ============================================================

def render_communication(d):
    c = d["communication"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    examples_html = "".join(f"<li>{ex}</li>" for ex in c["examples"])
    red_html = "".join(f"<li>{x}</li>" for x in c["red_sentences"])
    green_html = "".join(f"<li>{x}</li>" for x in c["green_sentences"])

    return f'''
<div class="section-header">Wie ihr miteinander sprecht</div>
<p>{c["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        {"".join(f"<p>{para}</p>" for para in c["person1"])}
    </div>
    <div class="person">
        <h3>{p2}</h3>
        {"".join(f"<p>{para}</p>" for para in c["person2"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Im Alltag heisst das</h3>
<ul class="bullets">{examples_html}</ul>

<h3 style="font-size:11pt; margin-top:3mm;">Wie ihr im Streit redet</h3>
<p>{c["in_fight"]}</p>

<div class="dynamics-grid">
    <div class="dyn-row">
        <div class="dyn-cell">
            <div class="dyn-header"><div class="dyn-label">🔴 Rote Sätze</div></div>
            <div class="dyn-value">Diese triggern</div>
            <ul class="bullets" style="font-size:9pt; margin:1mm 0;">{red_html}</ul>
        </div>
        <div class="dyn-cell">
            <div class="dyn-header"><div class="dyn-label">🟢 Grüne Sätze</div></div>
            <div class="dyn-value">Diese docken an</div>
            <ul class="bullets" style="font-size:9pt; margin:1mm 0;">{green_html}</ul>
        </div>
    </div>
</div>

<div class="tip-box">
    <div class="tip-label">Empfohlene Gesprächs-Rituale</div>
    <div class="tip-body">{c["rituals"]}</div>
</div>

{golden_quote(c["golden_sentence"])}
'''


# ============================================================
# 9. LIEBESSPRACHEN VERTIEFT (ERWEITERT)
# ============================================================

def render_love_languages(d, assets_dir):
    ll = d["love_languages"]
    p1 = d["person1"]
    p2 = d["person2"]
    z1 = zodiac_for_sign(p1["sun_sign_code"], 28)
    z2 = zodiac_for_sign(p2["sun_sign_code"], 28)

    # Übersetzungs-Tabelle
    trans = ll["translation_table"]
    trans_rows = "".join(
        f'<tr><td>{row["situation"]}</td><td>{row["meaning_p1"]}</td><td>{row["meaning_p2"]}</td></tr>'
        for row in trans
    )

    def list_html(items):
        return "".join(f"<li>{x}</li>" for x in items)

    return f'''
<div class="section-header">Eure Liebessprachen vertieft</div>

<img src="{assets_dir}/hero_love.webp" class="hero-mini narrow" alt="Liebessprachen">
<div class="img-caption">{ll["image_caption"]}</div>

<p>{ll["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{z1} {p1["name"]}</h3>
        <div class="lang-primary">Primär: {ll["person1"]["primary"]}</div>
        <div class="meta-row"><strong>Sekundär</strong> &middot; {ll["person1"]["secondary"]}</div>
        <div class="meta-row"><strong>Empfängt am tiefsten</strong> &middot; {ll["person1"]["receives"]}</div>
        {"".join(f"<p>{para}</p>" for para in ll["person1"]["paragraphs"])}
    </div>
    <div class="person">
        <h3>{z2} {p2["name"]}</h3>
        <div class="lang-primary">Primär: {ll["person2"]["primary"]}</div>
        <div class="meta-row"><strong>Sekundär</strong> &middot; {ll["person2"]["secondary"]}</div>
        <div class="meta-row"><strong>Empfängt am tiefsten</strong> &middot; {ll["person2"]["receives"]}</div>
        {"".join(f"<p>{para}</p>" for para in ll["person2"]["paragraphs"])}
    </div>
</div>

<h3 style="font-size:11pt;">Übersetzungs-Tabelle</h3>
<table class="translation-table">
    <tr><th>Situation</th><th>Bei {p1["name"]} heisst das</th><th>Bei {p2["name"]} heisst das</th></tr>
    {trans_rows}
</table>

<div class="dynamics-grid">
    <div class="dyn-row">
        <div class="dyn-cell">
            <div class="dyn-header"><div class="dyn-label">⚡ Was lädt {p1["name"]}s Akku</div></div>
            <ul class="bullets" style="font-size:9pt; margin:1mm 0;">{list_html(ll["person1"]["charges"])}</ul>
        </div>
        <div class="dyn-cell">
            <div class="dyn-header"><div class="dyn-label">⚡ Was lädt {p2["name"]}s Akku</div></div>
            <ul class="bullets" style="font-size:9pt; margin:1mm 0;">{list_html(ll["person2"]["charges"])}</ul>
        </div>
    </div>
    <div class="dyn-row">
        <div class="dyn-cell">
            <div class="dyn-header"><div class="dyn-label">🔻 Was leert {p1["name"]}s Akku</div></div>
            <ul class="bullets" style="font-size:9pt; margin:1mm 0;">{list_html(ll["person1"]["drains"])}</ul>
        </div>
        <div class="dyn-cell">
            <div class="dyn-header"><div class="dyn-label">🔻 Was leert {p2["name"]}s Akku</div></div>
            <ul class="bullets" style="font-size:9pt; margin:1mm 0;">{list_html(ll["person2"]["drains"])}</ul>
        </div>
    </div>
</div>

<div class="tip-box">
    <div class="tip-label">Tägliche Mini-Gesten (2 Minuten)</div>
    <div class="tip-body">{ll["mini_gestures"]}</div>
</div>

<h3 style="font-size:11pt; margin-top:3mm;">Eure Schnittmenge</h3>
<p>{ll["overlap"]}</p>

{golden_quote(ll["golden_sentence"])}
'''


# ============================================================
# 10. WERTESYSTEM (NEU)
# ============================================================

def render_values(d):
    v = d["values"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]
    return f'''
<div class="section-header">Wertesystem und Lebensmission</div>
<p>{v["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        {"".join(f"<p>{para}</p>" for para in v["person1"])}
    </div>
    <div class="person">
        <h3>{p2}</h3>
        {"".join(f"<p>{para}</p>" for para in v["person2"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Wo eure Missionen sich treffen</h3>
<p>{v["meeting"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure Missionen sich reiben</h3>
<p>{v["friction"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Eure gemeinsame Mission als Paar</h3>
<p>{v["common_mission"]}</p>

{golden_quote(v["golden_sentence"])}
'''


# ============================================================
# 11. LEIDENSCHAFT (NEU)
# ============================================================

def render_passion(d, assets_dir):
    p = d["passion"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]
    return f'''
<div class="section-header">Eure Leidenschaftsbereiche · Was euch antreibt</div>

<img src="{assets_dir}/hero_passion.webp" class="hero-mini narrow" alt="Leidenschaft">
<div class="img-caption">{p["image_caption"]}</div>

<p>{p["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        {"".join(f"<p>{para}</p>" for para in p["person1"])}
    </div>
    <div class="person">
        <h3>{p2}</h3>
        {"".join(f"<p>{para}</p>" for para in p["person2"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Eure gemeinsame Leidenschaft</h3>
<p>{p["common"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure Leidenschaften auseinandergehen</h3>
<p>{p["different"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wie ihr eure Leidenschaften gegenseitig nähren könnt</h3>
<p>{p["nourish"]}</p>

{golden_quote(p["golden_sentence"])}
'''


# ============================================================
# 12. MATERIELLES / STABILITÄT (NEU)
# ============================================================

def render_materiality(d):
    m = d["materiality"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    return f'''
<div class="section-header">Materielles · Stabilität · Erdung</div>
<p>{m["intro"]}</p>

<div class="scale-row">
    <div class="scale-title">{p1}: {m["person1"]["label"]}</div>
    <div class="scale-track">
        <div class="scale-marker" style="left:{m["person1"]["position"]}%;">
            <div class="scale-marker-label">{m["person1"]["position"]}%</div>
        </div>
    </div>
    <div class="scale-labels">
        <span>Unmateriell</span><span>Stark verankert</span>
    </div>
</div>
{"".join(f"<p>{para}</p>" for para in m["person1"]["paragraphs"])}

<div class="scale-row" style="margin-top:5mm;">
    <div class="scale-title">{p2}: {m["person2"]["label"]}</div>
    <div class="scale-track">
        <div class="scale-marker" style="left:{m["person2"]["position"]}%;">
            <div class="scale-marker-label">{m["person2"]["position"]}%</div>
        </div>
    </div>
    <div class="scale-labels">
        <span>Unmateriell</span><span>Stark verankert</span>
    </div>
</div>
{"".join(f"<p>{para}</p>" for para in m["person2"]["paragraphs"])}

<h3 style="font-size:11pt; margin-top:4mm;">Wer trägt was im Paar</h3>
<p>{m["who_carries"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Risiken</h3>
<p>{m["risks"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Optimale Verteilung</h3>
<p>{m["optimal_split"]}</p>

{golden_quote(m["golden_sentence"])}
'''


# ============================================================
# 13. TYP-PROFILE (NEU)
# ============================================================

def render_type_profiles(d):
    t = d["type_profiles"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]
    return f'''
<div class="section-header">Welcher Typ ist sie · Welcher Typ ist er</div>
<p>{t["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        <div class="lang-primary">{t["person1"]["archetype"]}</div>
        {"".join(f"<p>{para}</p>" for para in t["person1"]["description"])}
        <h4 style="font-size:9.5pt; margin-top:3mm; color:#BA7517;">Worauf {p1} anspringt</h4>
        <p style="font-size:9pt;">{t["person1"]["attracts"]}</p>
    </div>
    <div class="person">
        <h3>{p2}</h3>
        <div class="lang-primary">{t["person2"]["archetype"]}</div>
        {"".join(f"<p>{para}</p>" for para in t["person2"]["description"])}
        <h4 style="font-size:9.5pt; margin-top:3mm; color:#BA7517;">Worauf {p2} anspringt</h4>
        <p style="font-size:9pt;">{t["person2"]["attracts"]}</p>
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Resonanz-Analyse</h3>
<p>{t["resonance"]}</p>

{golden_quote(t["golden_sentence"])}
'''


# ============================================================
# 14-15. SYNASTRIE (unverändert)
# ============================================================

def render_synastry(d, assets_dir):
    s = d["synastry"]
    aspect_rows = "".join(aspect_row(a) for a in s["aspect_table"])
    explanations = "".join(f'<p>{e}</p>' for e in s["aspect_explanations"])

    return f'''
<div class="section-header">Eure Synastrie &ndash; Was zwischen euch wirklich passiert</div>

<img src="{assets_dir}/hero_synastry.webp" class="hero-mini narrow" alt="Synastrie">
<div class="img-caption">{s["image_caption"]}</div>

{"".join(f"<p>{p}</p>" for p in s["intro_paragraphs"])}

{reflection(s["reflection"])}

<div class="section-header">Die wichtigsten Aspekte zwischen euch</div>

<table class="aspect-table">
    <tr><th>{d["person1"]["name"]}</th><th>Aspekt</th><th>{d["person2"]["name"]}</th><th>Orb</th></tr>
    {aspect_rows}
</table>

<p style="margin-top: 4mm;">
    Die astrologisch <strong>sechs wesentlichsten Aspekte</strong> bei euch tragen oder fordern
    die Beziehung am stärksten. Hier sind sie ausführlich erklärt &ndash; mit dem, was sie für
    euer Miteinander bedeuten und wie ihr ihnen am besten begegnet.
</p>
{explanations}
'''


# ============================================================
# 16. DYNAMIKEN
# ============================================================

def render_dynamics(d):
    dyn = d["dynamics"]
    icons = {
        "heart": icon_heart(20),
        "scale": icon_scale(20),
        "wave": icon_wave(20),
        "speech": icon_speech(20),
        "infinity": icon_infinity(22),
    }
    return f'''
<div class="section-header">Eure Dynamiken &ndash; Wie eure Beziehung tickt</div>

<p>{dyn["intro"]}</p>

<div class="dynamics-grid">
    <div class="dyn-row">
        <div class="dyn-cell">
            <div class="dyn-header">{icons["heart"]}<div class="dyn-label">Beziehungstyp</div></div>
            <div class="dyn-value">{dyn["relationship_type"]["value"]}</div>
            <div class="dyn-desc">{dyn["relationship_type"]["desc"]}</div>
        </div>
        <div class="dyn-cell">
            <div class="dyn-header">{icons["scale"]}<div class="dyn-label">Machtbalance</div></div>
            <div class="dyn-value">{dyn["power_balance"]["value"]}</div>
            <div class="dyn-desc">{dyn["power_balance"]["desc"]}</div>
        </div>
    </div>
    <div class="dyn-row">
        <div class="dyn-cell">
            <div class="dyn-header">{icons["wave"]}<div class="dyn-label">Emotionale Verbindung</div></div>
            <div class="dyn-value">{dyn["emotional"]["value"]}</div>
            <div class="dyn-desc">{dyn["emotional"]["desc"]}</div>
        </div>
        <div class="dyn-cell">
            <div class="dyn-header">{icons["speech"]}<div class="dyn-label">Kommunikation</div></div>
            <div class="dyn-value">{dyn["communication"]["value"]}</div>
            <div class="dyn-desc">{dyn["communication"]["desc"]}</div>
        </div>
    </div>
</div>

<div class="dyn-cell-wide">
    <div class="dyn-header">{icons["infinity"]}<div class="dyn-label">Langzeitpotenzial</div></div>
    <div class="dyn-value">{dyn["long_term"]["value"]}</div>
    <div class="dyn-desc">{dyn["long_term"]["desc"]}</div>
</div>

<div class="tip-box">
    <div class="tip-label">Tipp für euren Alltag</div>
    <div class="tip-body">{dyn["daily_tip"]}</div>
</div>
'''


# ============================================================
# 17. COMPOSITE
# ============================================================

def render_composite(d, assets_dir):
    c = d["composite"]
    bullets = "".join(f"<li>{b}</li>" for b in c["bullets"])
    return f'''
<div class="section-header">Composite &ndash; Eure Beziehung als drittes Wesen</div>

<img src="{assets_dir}/hero_composite.webp" class="hero-mini narrow" alt="Composite">
<div class="img-caption">{c["image_caption"]}</div>

<p>{c["intro"]}</p>

<ul class="bullets">{bullets}</ul>

<div class="tip-box">
    <div class="tip-label">So vertieft ihr eure Beziehung</div>
    <div class="tip-body">{c["deepening_tip"]}</div>
</div>
'''


# ============================================================
# 18. NUMEROLOGIE ERWEITERT
# ============================================================

def render_numerology(d):
    n = d["numerology"]
    p1 = d["person1"]["name"]
    p2 = d["person2"]["name"]

    badge_p1_lp = num_badge(n["person1"]["lifepath"], 70)
    badge_p2_lp = num_badge(n["person2"]["lifepath"], 70)
    badge_p1_soul = num_badge(n["person1"]["soul"], 40)
    badge_p2_soul = num_badge(n["person2"]["soul"], 40)
    badge_p1_dest = num_badge(n["person1"]["destiny"], 40)
    badge_p2_dest = num_badge(n["person2"]["destiny"], 40)
    badge_year = num_badge(n["personal_year"]["number"], 50)
    badge_res = num_badge(n["resonance"]["number"], 50)

    return f'''
<div class="section-header">Numerologische Resonanz &ndash; Eure Zahlen-DNA</div>
<p>{n["intro"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Eure Lebenspfade</h3>

<div class="num-grid">
    <div class="num-grid-row">
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_p1_lp}</div>
            <div class="num-label">{p1.upper()}S LEBENSPFAD</div>
            <div class="num-theme">{n["person1"]["lifepath_theme"]}</div>
            <div class="num-desc">{n["person1"]["lifepath_desc"]}</div>
        </div>
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_p2_lp}</div>
            <div class="num-label">{p2.upper()}S LEBENSPFAD</div>
            <div class="num-theme">{n["person2"]["lifepath_theme"]}</div>
            <div class="num-desc">{n["person2"]["lifepath_desc"]}</div>
        </div>
    </div>
</div>

<div class="tip-box">
    <div class="tip-label">Eure Kombination {n["person1"]["lifepath"]} + {n["person2"]["lifepath"]}</div>
    <div class="tip-body">{n["combination"]}</div>
</div>

<div class="section-header">Eure weiteren Zahlen im Vergleich</div>
<p>{n["other_intro"]}</p>

<div class="num-grid">
    <div class="num-grid-row">
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_p1_soul}</div>
            <div class="num-label">{p1.upper()}S SEELENDRANG &middot; {n["person1"]["soul"]}</div>
            <div class="num-theme">{n["person1"]["soul_theme"]}</div>
            <div class="num-desc">{n["person1"]["soul_desc"]}</div>
        </div>
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_p2_soul}</div>
            <div class="num-label">{p2.upper()}S SEELENDRANG &middot; {n["person2"]["soul"]}</div>
            <div class="num-theme">{n["person2"]["soul_theme"]}</div>
            <div class="num-desc">{n["person2"]["soul_desc"]}</div>
        </div>
    </div>
</div>

<div class="num-grid">
    <div class="num-grid-row">
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_p1_dest}</div>
            <div class="num-label">{p1.upper()}S SCHICKSALSZAHL &middot; {n["person1"]["destiny"]}</div>
            <div class="num-theme">{n["person1"]["destiny_theme"]}</div>
            <div class="num-desc">{n["person1"]["destiny_desc"]}</div>
        </div>
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_p2_dest}</div>
            <div class="num-label">{p2.upper()}S SCHICKSALSZAHL &middot; {n["person2"]["destiny"]}</div>
            <div class="num-theme">{n["person2"]["destiny_theme"]}</div>
            <div class="num-desc">{n["person2"]["destiny_desc"]}</div>
        </div>
    </div>
</div>

<div class="num-grid">
    <div class="num-grid-row">
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_res}</div>
            <div class="num-label">BEZIEHUNGS-RESONANZ &middot; {n["resonance"]["number"]}</div>
            <div class="num-theme">{n["resonance"]["theme"]}</div>
            <div class="num-desc">{n["resonance"]["desc"]}</div>
        </div>
        <div class="num-cell">
            <div class="num-badge-wrap">{badge_year}</div>
            <div class="num-label">GEMEINSAMES JAHR {n["personal_year"]["year"]}</div>
            <div class="num-theme">{n["personal_year"]["theme"]}</div>
            <div class="num-desc">{n["personal_year"]["text"]}</div>
        </div>
    </div>
</div>

{golden_quote(n["golden_sentence"])}
'''


# ============================================================
# 19. STÄRKEN + VERANTWORTUNG (ERWEITERT)
# ============================================================

def render_strengths(d, assets_dir):
    s = d["strengths"]
    blocks = ""
    for i, item in enumerate(s["items"], 1):
        blocks += f'''
<div class="numbered-block">
    <div class="num">{i}</div>
    <div class="title">{item["title"]}</div>
    <div class="body">{item["body"]}</div>
</div>'''

    resp_blocks = "".join(f"<li>{x}</li>" for x in s["responsibility"])

    return f'''
<div class="section-header">Eure Stärken &ndash; Wo ihr leuchtet</div>
<p>{s["intro"]}</p>
{blocks}

<img src="{assets_dir}/hero_strengths.webp" class="hero-mini narrow" alt="Stärken">
<div class="img-caption">{s["image_caption"]}</div>

<div class="section-header">Wo ihr euch ergänzt</div>
<p>{s["complement"]}</p>

<div class="section-header">Verantwortungs-Verteilung &ndash; Wer trägt was</div>
<p>{s["responsibility_intro"]}</p>
<ul class="bullets">{resp_blocks}</ul>

<div class="tip-box">
    <div class="tip-label">Das Tandem-Prinzip</div>
    <div class="tip-body">{s["tandem"]}</div>
</div>

{golden_quote(s["golden_sentence"])}
'''


# ============================================================
# 20. SCHWÄCHEN + SCHATTEN (NEU)
# ============================================================

def render_shadows(d):
    sh = d["shadows"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]
    return f'''
<div class="section-header">Eure Schwächen und Schatten im Vergleich</div>
<p>{sh["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        <ul class="bullets" style="font-size:9pt;">
            {"".join(f"<li>{x}</li>" for x in sh["person1"])}
        </ul>
    </div>
    <div class="person">
        <h3>{p2}</h3>
        <ul class="bullets" style="font-size:9pt;">
            {"".join(f"<li>{x}</li>" for x in sh["person2"])}
        </ul>
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Wo eure Schwächen sich gegenseitig triggern</h3>
<p>{sh["trigger"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure Schwächen sich gegenseitig auffangen</h3>
<p>{sh["catch"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Warum Schatten-Bewusstsein die Beziehung erleichtert</h3>
<p>{sh["awareness"]}</p>

{golden_quote(sh["golden_sentence"])}
'''


# ============================================================
# 21. KONFLIKTLANDKARTE (ERWEITERT)
# ============================================================

def render_conflict_map(d, assets_dir):
    cm = d["conflict_map"]
    fields = ""
    for i, field in enumerate(cm["fields"], 1):
        fields += f'''
<div class="conflict-field">
    <h4>{i}. {field["title"]}</h4>
    <div class="anchor">Astrologischer Anker: {field["anchor"]}</div>
    <div class="body">{field["body"]}</div>
</div>'''

    return f'''
<div class="section-header">Eure Konfliktlandkarte</div>

<img src="{assets_dir}/hero_triggers.webp" class="hero-mini narrow" alt="Konflikte">
<div class="img-caption">{cm["image_caption"]}</div>

<p>{cm["intro"]}</p>

{fields}

{golden_quote(cm["golden_sentence"])}
'''


# ============================================================
# 22. AUTHENTIZITÄT + MASKEN (NEU)
# ============================================================

def render_masks(d):
    m = d["masks"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]
    return f'''
<div class="section-header">Authentizität und Masken</div>
<p>{m["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{p1}</h3>
        {"".join(f"<p>{para}</p>" for para in m["person1"])}
    </div>
    <div class="person">
        <h3>{p2}</h3>
        {"".join(f"<p>{para}</p>" for para in m["person2"])}
    </div>
</div>

<h3 style="font-size:11pt; margin-top:4mm;">Wo eure Masken aufeinandertreffen</h3>
<p>{m["meeting"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wann fällt die Maske</h3>
<p>{m["when_falls"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wie ihr euch zur Authentizität einladet</h3>
<p>{m["invitation"]}</p>

{reflection(m["reflection"])}

{golden_quote(m["golden_sentence"])}
'''


# ============================================================
# 23. KARMA + HEILUNG (NEU, behutsam)
# ============================================================

def render_karma(d, assets_dir):
    k = d["karma"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    rituals = "".join(f"<li>{x}</li>" for x in k["rituals"])

    return f'''
<div class="section-header">Karmische Wunden und gegenseitige Heilung</div>

<img src="{assets_dir}/hero_karma.webp" class="hero-mini narrow" alt="Karmische Heilung">
<div class="img-caption">{k["image_caption"]}</div>

<p>{k["intro"]}</p>

{sacred_box(f"{p1}s Wunde", "<br><br>".join(k["person1"]))}
{sacred_box(f"{p2}s Wunde", "<br><br>".join(k["person2"]))}

<h3 style="font-size:11pt; margin-top:4mm;">Wie ihr euch unbewusst triggert</h3>
<p>{k["trigger_loop"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Eure Heilungs-Achse</h3>
<p>{k["healing_axis"]}</p>

<div class="tip-box">
    <div class="tip-label">Heilungs-Rituale für euch</div>
    <div class="tip-body"><ul style="margin:0;padding-left:5mm;">{rituals}</ul></div>
</div>

{golden_quote(k["golden_sentence"])}
'''


# ============================================================
# 24. KRISENFÄHIGKEIT (NEU)
# ============================================================

def render_crisis(d):
    c = d["crisis"]
    hints = "".join(f"<li>{x}</li>" for x in c["hints"])
    return f'''
<div class="section-header">Krisenfähigkeit</div>
<p>{c["intro"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Ressourcen, die im Chart angelegt sind</h3>
<p>{c["resources"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wo eure grösste Verletzungs-Gefahr liegt</h3>
<p>{c["vulnerability"]}</p>

<div class="tip-box">
    <div class="tip-label">Wenn die Krise da ist – konkrete Hinweise</div>
    <div class="tip-body"><ul style="margin:0;padding-left:5mm;">{hints}</ul></div>
</div>

{golden_quote(c["golden_sentence"])}
'''


# ============================================================
# 25. SEXUELLER MATCH (NEU, behutsam)
# ============================================================

def render_sexual_match(d, assets_dir):
    s = d["sexual"]
    p1, p2 = d["person1"]["name"], d["person2"]["name"]

    return f'''
<div class="section-header">Sexueller Match · detaillierte Analyse</div>

<img src="{assets_dir}/hero_essence.webp" class="hero-mini narrow" alt="Sexueller Match">
<div class="img-caption">{s["image_caption"]}</div>

<p>{s["intro"]}</p>

{sacred_box(f"{p1}s sexueller Antrieb", "<br><br>".join(s["person1"]))}
{sacred_box(f"{p2}s sexueller Antrieb", "<br><br>".join(s["person2"]))}

<h3 style="font-size:11pt; margin-top:4mm;">Eure körperliche Resonanz</h3>
<p>{s["body_resonance"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Eure sexuellen Bedürfnisse im Vergleich</h3>
<p>{s["needs_compare"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Wenn die Lust einschläft</h3>
<p>{s["lust_sleeps"]}</p>

<div class="tip-box">
    <div class="tip-label">Körperkontakt als Ressource</div>
    <div class="tip-body">{s["body_resource"]}</div>
</div>

<h3 style="font-size:11pt; margin-top:3mm;">Sexuelle Tabus und Wachstumsräume</h3>
<p>{s["growth_spaces"]}</p>

{golden_quote(s["golden_sentence"])}
'''


# ============================================================
# 26. ENERGETISCHE BESONDERHEITEN (NEU)
# ============================================================

def render_energetic(d):
    e = d["energetic"]
    return f'''
<div class="section-header">Energetische Besonderheiten</div>
<p>{e["intro"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Eure Aura-Resonanz</h3>
<p>{e["aura"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Mediale Verbindung</h3>
<p>{e["medial"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Karmische Magnetik</h3>
<p>{e["magnetic"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Energetische Lecks</h3>
<p>{e["leaks"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Was lädt eure gemeinsame Energie auf</h3>
<p>{e["charging"]}</p>

{golden_quote(e["golden_sentence"])}
'''


# ============================================================
# 27. SPIRITUELLE AUFGABE (NEU)
# ============================================================

def render_spiritual_mission(d, assets_dir):
    sm = d["spiritual_mission"]
    return f'''
<div class="section-header">Eure spirituelle Aufgabe als Paar</div>

<img src="{assets_dir}/hero_spiritual.webp" class="hero-mini narrow" alt="Spirituelle Aufgabe">
<div class="img-caption">{sm["image_caption"]}</div>

<p>{sm["intro"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Composite-Sonne als Wegweiser</h3>
<p>{sm["composite_sun"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Composite-Mondknoten</h3>
<p>{sm["nodes"]}</p>

<h3 style="font-size:11pt; margin-top:3mm;">Was lernt ihr durcheinander</h3>
<p>{sm["learning"]}</p>

{sacred_box("Eure Verabredung", sm["agreement"])}

{golden_quote(sm["golden_sentence"])}
'''


# ============================================================
# 28. BEZIEHUNGS-PROFILE
# ============================================================

def render_profiles(d):
    pf = d["profiles"]
    p1, p2 = d["person1"], d["person2"]
    z1 = zodiac_for_sign(p1["sun_sign_code"], 28)
    z2 = zodiac_for_sign(p2["sun_sign_code"], 28)

    def profile_box(p_data):
        return "".join(
            f'<div class="profile-line"><strong>{k}</strong> {v}</div>'
            for k, v in p_data.items()
        )

    def flag_li(items):
        return "".join(f"<li>{x}</li>" for x in items)

    return f'''
<div class="section-header">Eure Beziehungs-Profile im Vergleich</div>
<p>{pf["intro"]}</p>

<div class="persons">
    <div class="person">
        <h3>{z1} {p1["name"]}</h3>
        <div class="profile-box">{profile_box(pf["person1"])}</div>
    </div>
    <div class="person">
        <h3>{z2} {p2["name"]}</h3>
        <div class="profile-box">{profile_box(pf["person2"])}</div>
    </div>
</div>

<p style="margin-top: 4mm; font-size: 9.5pt; color: #555; font-style: italic;">{pf["note"]}</p>

<div class="flag-box green">
    <div class="flag-title">Grüne Signale &middot; das ist da</div>
    <ul>{flag_li(pf["green"])}</ul>
</div>

<div class="flag-box yellow">
    <div class="flag-title">Gelbe Signale &middot; aufmerksam bleiben</div>
    <ul>{flag_li(pf["yellow"])}</ul>
</div>

<div class="flag-box red">
    <div class="flag-title">Rote Signale</div>
    <ul>{flag_li(pf["red"])}</ul>
</div>
'''


# ============================================================
# 29. NEXT STEPS
# ============================================================

def render_next_steps(d, assets_dir):
    ns = d["next_steps"]
    blocks = ""
    for i, item in enumerate(ns["items"], 1):
        blocks += f'''
<div class="numbered-block">
    <div class="num">{i}</div>
    <div class="title">{item["title"]}</div>
    <div class="body">{item["body"]}</div>
</div>'''
    return f'''
<div class="section-header">Eure nächsten Schritte &ndash; Konkret und alltagstauglich</div>

<img src="{assets_dir}/hero_steps.webp" class="hero-mini narrow" alt="Pfad">
<div class="img-caption">{ns["image_caption"]}</div>

<p>{ns["intro"]}</p>

{blocks}
'''


# ============================================================
# 30. CLOSING
# ============================================================

def render_closing(d, assets_dir):
    cl = d["closing"]
    return f'''
<div class="cover" style="page-break-before: always; page-break-after: avoid;">
    <img src="{assets_dir}/hero_closing.webp" class="hero-mini" alt="Closing" style="margin-top: 10mm;">

    <div class="closing-quote">
        <div class="stars">* * *</div>
        <div class="quote">«{cl["quote"]}»</div>
        <div class="signoff">{cl["signoff"]}</div>
    </div>
</div>
'''
