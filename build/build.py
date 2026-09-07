#!/usr/bin/env python3
"""Seitenbau fuer die Berichtsmappe "Artefakt".

Liest alle Ausgaben aus ``ausgaben/<ressort>/*.json`` und schreibt die
komplette statische Seite nach ``site/``. Nur Standardbibliothek.

- ``site/index.html``          -- Startseite, rechts die juengste Live-Ausgabe.
- ``site/berichte/<id>.html``  -- je Ausgabe eine Seite mit derselben
                                  linken Spalte und dem jeweiligen Bericht rechts.

Jede erzeugte Seite traegt ``<meta name="robots" content="noindex, nofollow">``
im ``<head>`` (siehe :func:`page`). Dazu gehoert ``site/robots.txt``: die Datei
liegt statisch im Repo und wird hier bewusst nicht erzeugt -- der Bau schreibt
nur die HTML-Dateien und loescht nichts, ``site/robots.txt`` bleibt also
unangetastet. Wer den Bau spaeter um ein Aufraeumen von ``site/`` erweitert,
muss ``robots.txt`` davon ausnehmen.

Farben, Schriften, Raster und Aufbau folgen
``docs/vorhaben/2026-09-06-flo-hub/design-artefakt-2026-09-06.md``.
Die Schriften Cormorant Garamond und Lora liegen lokal unter ``site/fonts/``
und werden per ``@font-face`` eingebunden -- keine externe Ressource.
"""

from __future__ import annotations

import glob
import html
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUSGABEN = os.path.join(ROOT, "ausgaben")
SITE = os.path.join(ROOT, "site")

# Reihenfolge der Ressorts in "Aktuell" und in den Filter-Chips.
RESSORTS = [
    ("medien", "Medien"),
    ("welt", "Welt"),
    ("krypto", "Krypto"),
    ("finanzen", "Finanzen"),
    ("reisen", "Reisen"),
]
RESSORT_LABEL = dict(RESSORTS)

BUILD_DATUM = "2026-09-06"


def e(value) -> str:
    """HTML-escape fuer Textinhalte."""
    return html.escape("" if value is None else str(value), quote=True)


# --------------------------------------------------------------------------- #
# Daten laden
# --------------------------------------------------------------------------- #
def load_reports():
    reports = []
    for path in sorted(glob.glob(os.path.join(AUSGABEN, "**", "*.json"), recursive=True)):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        data.setdefault("_path", path)
        reports.append(data)
    return reports


def latest_per_ressort(reports):
    latest = {}
    for r in reports:
        key = r.get("ressort")
        if key not in latest or str(r.get("stand", "")) > str(latest[key].get("stand", "")):
            latest[key] = r
    return latest


def archive_entries(reports):
    out = []
    for r in reports:
        out.append(
            {
                "datum": r.get("stand", ""),
                "ressort": r.get("ressort", ""),
                "ausgabe": r.get("ausgabe", ""),
                "titel": r.get("schlagzeile", ""),
                "ref": r.get("id", ""),
            }
        )
    out.sort(key=lambda x: (x["datum"], x["ressort"]), reverse=True)
    return out


# --------------------------------------------------------------------------- #
# CSS -- Tokens, Schrift, Raster, Aufbau, Mobil
# --------------------------------------------------------------------------- #
def css(fp: str) -> str:
    """fp -- relativer Pfad-Praefix zum Ordner ``site`` (``""`` oder ``"../"``)."""
    return f"""
/* Schriften lokal, OFL -- siehe site/fonts/OFL-*.txt */
@font-face {{
  font-family: 'Cormorant Garamond';
  src: url('{fp}fonts/CormorantGaramond-var.ttf') format('truetype');
  font-weight: 300 700; font-style: normal; font-display: swap;
}}
@font-face {{
  font-family: 'Lora';
  src: url('{fp}fonts/Lora-var.ttf') format('truetype');
  font-weight: 400 700; font-style: normal; font-display: swap;
}}
@font-face {{
  font-family: 'Lora';
  src: url('{fp}fonts/Lora-Italic-var.ttf') format('truetype');
  font-weight: 400 700; font-style: italic; font-display: swap;
}}

:root {{
  --color-bg: #f4f0e7;
  --color-surface: #eae9e9;
  --color-text: #201f1d;
  --color-accent: #b68235;
  --color-divider: rgba(32, 31, 29, 0.16);
  --color-accent-bg: rgba(182, 130, 53, 0.10);

  --space-1: 4.6px;
  --space-2: 9.2px;
  --space-3: 13.8px;
  --space-4: 18.4px;
  --space-5: 23px;
  --space-6: 27.6px;
  --space-7: 32.2px;
  --space-8: 36.8px;
}}

*, *::before, *::after {{ box-sizing: border-box; }}

html, body {{
  margin: 0; padding: 0;
  max-width: 100%;
  overflow-x: hidden;
  background: var(--color-bg);
  color: var(--color-text);
}}

body {{
  font-family: 'Lora', Georgia, serif;
  font-size: 15px;
  line-height: 1.55;
  font-feature-settings: 'tnum';
  -webkit-font-smoothing: antialiased;
}}

h1, h2, h3, .label, .schlagzeile, .marke {{
  font-family: 'Cormorant Garamond', 'Cormorant', Georgia, serif;
  letter-spacing: -0.015em;
  line-height: 1.12;
}}

a {{ color: var(--color-text); text-decoration-color: var(--color-divider); overflow-wrap: anywhere; }}
a:hover {{ text-decoration-color: var(--color-accent); }}

.label {{
  font-size: 10.5px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #6a655c;
  font-weight: 600;
}}

.rule3 {{ border-top: 3px solid var(--color-text); }}
.hair {{ border-top: 1px solid var(--color-divider); }}

/* ---- Grundraster ------------------------------------------------------- */
.wrap {{
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 320px) minmax(0, 1fr);
  gap: var(--space-8);
  padding: var(--space-6) var(--space-6) var(--space-8);
  align-items: start;
}}

/* ---- Linke Spalte ---------------------------------------------------- */
.seite {{
  position: sticky;
  top: var(--space-4);
  align-self: start;
  max-height: calc(100vh - var(--space-6));
  overflow: auto;
  min-width: 0;
}}

.seite .marke {{ font-size: 30px; font-weight: 400; margin: var(--space-2) 0 0; }}
.seite .kopfzeile {{ margin-bottom: var(--space-5); }}

.block-titel {{ margin: var(--space-5) 0 var(--space-2); }}

.aktuell-eintrag {{
  display: block;
  padding: var(--space-2) var(--space-3);
  border-left: 2px solid transparent;
  text-decoration: none;
  margin-bottom: var(--space-1);
}}
.aktuell-eintrag:hover {{ background: var(--color-surface); }}
.aktuell-eintrag.aktiv {{
  border-left-color: var(--color-accent);
  background: var(--color-accent-bg);
}}
.aktuell-eintrag .zeile-titel {{
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 17px;
  display: block;
  margin: 2px 0;
}}
.aktuell-eintrag .aufmacher {{ font-size: 13px; color: #4b473f; display: block; }}
.aktuell-eintrag .meta {{ font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase; color: #6a655c; }}
.tag {{ font-style: italic; letter-spacing: 0; text-transform: none; }}

/* Archiv: Filter per reinem CSS (Radio + Geschwister-Selektor) */
.archiv .filter {{ position: absolute; opacity: 0; pointer-events: none; }}
.chips {{ display: flex; flex-wrap: wrap; gap: var(--space-1); margin-bottom: var(--space-3); }}
.chips label {{
  font-size: 10.5px; letter-spacing: 0.14em; text-transform: uppercase;
  padding: 3px var(--space-2); border: 1px solid var(--color-divider);
  cursor: pointer; color: #6a655c; user-select: none;
}}
.archiv-liste .eintrag {{ display: none; }}
.archiv-liste .eintrag {{
  padding: var(--space-2) 0;
  border-top: 1px solid var(--color-divider);
  font-size: 13px;
}}
.archiv-liste .eintrag .a-datum {{ color: #6a655c; font-feature-settings: 'tnum'; }}
.archiv-liste .eintrag .a-meta {{ font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase; color: #6a655c; }}

{"".join(_archiv_css_rules())}

.seite .fuss {{ margin-top: var(--space-5); font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; display: flex; gap: var(--space-4); }}

/* ---- Rechte Spalte -- der Bericht ---------------------------------- */
.bericht {{ min-width: 0; max-width: 820px; }}

.bericht .kopf {{
  display: flex; justify-content: space-between; gap: var(--space-4);
  padding-top: var(--space-2); flex-wrap: wrap;
}}

.schlagzeile {{
  font-size: 46px; font-weight: 400; margin: var(--space-4) 0 var(--space-4);
  max-width: 20ch;
}}

.lede {{
  font-size: 16.5px; line-height: 1.72; text-align: justify;
  hyphens: auto; text-wrap: pretty; overflow-wrap: break-word; max-width: 64ch;
  margin: 0 0 var(--space-5);
}}

.bilanz {{
  display: flex; justify-content: space-between; gap: var(--space-4);
  padding: var(--space-3) 0; margin: var(--space-4) 0;
  border-top: 1px solid var(--color-divider);
  border-bottom: 1px solid var(--color-divider);
  font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase;
  flex-wrap: wrap;
}}
.bilanz .rechts {{ color: var(--color-accent); }}

.hinweis-beispiel {{
  font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--color-accent); margin: var(--space-4) 0 var(--space-2);
}}

.zeile {{
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: var(--space-4);
  padding: var(--space-5) 0;
  border-top: 1px solid var(--color-divider);
}}
.zeile .meta {{
  font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase;
  color: #6a655c;
}}
.zeile .meta span {{ display: block; margin-bottom: 2px; }}
.zeile .inhalt {{
  border-left: 1px solid var(--color-divider);
  padding-left: var(--space-4);
  min-width: 0;
}}
.zeile .inhalt h3 {{ font-size: 23px; font-weight: 400; margin: 0 0 var(--space-2); }}
.zeile .inhalt p {{ margin: 0; text-align: justify; hyphens: auto; text-wrap: pretty; overflow-wrap: break-word; font-size: 15.5px; }}
.zeile .quelle {{ display: inline-block; margin-top: var(--space-2); font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; }}
.zeile .quelle::after {{ content: ' \\2192'; }}

.bauplan {{
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-6); margin: var(--space-6) 0 var(--space-4);
  padding-top: var(--space-5); border-top: 3px solid var(--color-text);
}}
.bauplan ul {{ margin: var(--space-2) 0 0; padding-left: var(--space-4); }}
.bauplan li {{ margin-bottom: var(--space-1); font-size: 14px; }}
.bauplan .paar {{ margin-top: var(--space-2); }}
.bauplan .paar .p-label {{ font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase; color: #6a655c; }}
.bauplan .paar .p-text {{ font-size: 14px; }}
.bauplan-satz {{ font-style: italic; margin: var(--space-3) 0 var(--space-5); color: #4b473f; }}

.imblick .row {{
  display: flex; justify-content: space-between; gap: var(--space-4);
  padding: var(--space-2) 0; border-top: 1px solid var(--color-divider);
  font-size: 14px; flex-wrap: wrap;
}}
.imblick .row .stand {{ color: #6a655c; }}

.quellen-liste {{ margin-top: var(--space-2); font-size: 13px; }}
.quellen-liste a {{ margin-right: var(--space-3); white-space: nowrap; }}

.bericht .fuss {{
  margin-top: var(--space-7); padding-top: var(--space-4);
  border-top: 3px solid var(--color-text);
  display: flex; justify-content: space-between; gap: var(--space-4);
  font-size: 12px; flex-wrap: wrap;
}}
.bericht .fuss .regeltext {{ max-width: 52ch; color: #4b473f; }}
.bericht .fuss .aktionen {{ letter-spacing: 0.12em; text-transform: uppercase; }}
.bericht .fuss .inaktiv {{ color: #9a948a; }}

/* ---- Mobil: eine Spalte ab 900px --------------------------------- */
@media (max-width: 900px) {{
  .wrap {{
    grid-template-columns: minmax(0, 1fr);
    gap: var(--space-6);
    padding: var(--space-4);
  }}
  .seite {{
    position: static;
    max-height: none;
    overflow: visible;
    order: -1;
    border-bottom: 1px solid var(--color-divider);
    padding-bottom: var(--space-4);
  }}
  .schlagzeile {{ font-size: 34px; }}
  .zeile {{
    grid-template-columns: minmax(0, 1fr);
    gap: var(--space-2);
  }}
  .zeile .meta {{ display: flex; flex-wrap: wrap; gap: var(--space-3); }}
  .zeile .meta span {{ margin-bottom: 0; }}
  .zeile .inhalt {{
    border-left: 0;
    padding-left: 0;
  }}
  .bauplan {{ grid-template-columns: minmax(0, 1fr); gap: var(--space-4); }}
}}
"""


def _archiv_css_rules():
    """Erzeugt die CSS-Regeln fuer den reinen CSS-Filter im Archiv."""
    rules = [
        "#rf-all:checked ~ .archiv-liste .eintrag { display: block; }",
        "#rf-all:checked ~ .chips label[for='rf-all'] { color: var(--color-text); "
        "border-color: var(--color-accent); background: var(--color-accent-bg); }",
    ]
    for key, _label in RESSORTS:
        rules.append(
            f"#rf-{key}:checked ~ .archiv-liste .eintrag[data-ressort='{key}'] "
            f"{{ display: block; }}"
        )
        rules.append(
            f"#rf-{key}:checked ~ .chips label[for='rf-{key}'] "
            f"{{ color: var(--color-text); border-color: var(--color-accent); "
            f"background: var(--color-accent-bg); }}"
        )
    return "\n".join(rules) + "\n"


# --------------------------------------------------------------------------- #
# Bausteine -- linke Spalte
# --------------------------------------------------------------------------- #
def render_aktuell(latest, active_id, fp):
    rows = []
    for key, label in RESSORTS:
        r = latest.get(key)
        if not r:
            continue
        aktiv = " aktiv" if r.get("id") == active_id else ""
        status = r.get("status")
        tag = "Aktiv" if status == "live" else "Entwurf"
        href = f"{fp}berichte/{e(r.get('id'))}.html"
        rows.append(
            f"""      <a class="aktuell-eintrag{aktiv}" href="{href}">
        <span class="meta">{e(label)} &middot; {e(r.get('stand'))}</span>
        <span class="zeile-titel">{e(r.get('titel'))}</span>
        <span class="aufmacher">{e(r.get('zeile'))}</span>
        <span class="meta"><span class="tag">{e(tag)}</span> &middot; {e(r.get('rhythmus'))}</span>
      </a>"""
        )
    return "\n".join(rows)


def render_archiv(entries, fp):
    radios = ['      <input class="filter" type="radio" name="rf" id="rf-all" checked>']
    chips = ['        <label for="rf-all">Alle</label>']
    for key, label in RESSORTS:
        radios.append(f'      <input class="filter" type="radio" name="rf" id="rf-{key}">')
        chips.append(f'        <label for="rf-{key}">{e(label)}</label>')

    items = []
    for a in entries:
        href = f"{fp}berichte/{e(a['ref'])}.html"
        items.append(
            f"""        <a class="eintrag" data-ressort="{e(a['ressort'])}" href="{href}">
          <span class="a-datum">{e(a['datum'])}</span> &mdash; {e(a['titel'])}<br>
          <span class="a-meta">{e(RESSORT_LABEL.get(a['ressort'], a['ressort']))} &middot; {e(a['ausgabe'])}</span>
        </a>"""
        )

    return f"""    <div class="archiv">
      <h2 class="label block-titel">Archiv</h2>
{chr(10).join(radios)}
      <div class="chips">
{chr(10).join(chips)}
      </div>
      <div class="archiv-liste">
{chr(10).join(items)}
      </div>
    </div>"""


def render_left(latest, entries, active_id, fp):
    return f"""  <aside class="seite">
    <div class="kopfzeile rule3">
      <div class="marke">Artefakt</div>
      <div class="label" style="margin-top: var(--space-1);">Berichtsmappe &middot; {e(BUILD_DATUM)}</div>
    </div>

    <h2 class="label block-titel">Aktuell</h2>
{render_aktuell(latest, active_id, fp)}

{render_archiv(entries, fp)}

    <div class="fuss">
      <span>Gesamtarchiv</span>
      <span>Neuer Bericht</span>
    </div>
  </aside>"""


# --------------------------------------------------------------------------- #
# Bausteine -- rechte Spalte
# --------------------------------------------------------------------------- #
def render_zeile(z):
    quelle = ""
    if z.get("linkLabel") and z.get("href"):
        quelle = f'\n        <a class="quelle" href="{e(z["href"])}">{e(z["linkLabel"])}</a>'
    return f"""      <article class="zeile">
        <div class="meta">
          <span>{e(z.get('kategorie'))}</span>
          <span>{e(z.get('art'))}</span>
          <span>{e(z.get('datum'))}</span>
        </div>
        <div class="inhalt">
          <h3>{e(z.get('titel'))}</h3>
          <p>{e(z.get('text'))}</p>{quelle}
        </div>
      </article>"""


def render_bauplan(plan, titel):
    quellen = "\n".join(f"        <li>{e(q)}</li>" for q in plan.get("quellen", []))
    paare = "\n".join(
        f"""        <div class="paar">
          <div class="p-label">{e(p.get('label'))}</div>
          <div class="p-text">{e(p.get('text'))}</div>
        </div>"""
        for p in plan.get("aufbau", [])
    )
    satz = (
        "Die Zeilen oben sind Beispielinhalte zur Ansicht &mdash; "
        f"{e(titel)} l&auml;uft noch nicht automatisch."
    )
    return f"""      <div class="bauplan">
        <div>
          <h3 class="label">Geplante Quellen</h3>
          <ul>
{quellen}
          </ul>
        </div>
        <div>
          <h3 class="label">Aufbau der Ausgabe</h3>
{paare}
        </div>
      </div>
      <p class="bauplan-satz">{satz}</p>"""


def render_report(r):
    is_entwurf = r.get("status") != "live"
    tag = "Entwurf" if is_entwurf else "Aktiv"

    zeilen_html = "\n".join(render_zeile(z) for z in r.get("zeilen", []))
    beispiel_hinweis = (
        '      <p class="hinweis-beispiel">Beispielinhalte zur Ansicht</p>\n'
        if is_entwurf
        else ""
    )

    bauplan_html = ""
    if is_entwurf and r.get("plan"):
        bauplan_html = "\n" + render_bauplan(r["plan"], r.get("titel"))

    imblick = r.get("imBlick", [])
    imblick_html = ""
    if imblick:
        rows = "\n".join(
            f"""        <div class="row"><span class="was">{e(i.get('was'))}</span>"""
            f"""<span class="stand">{e(i.get('stand'))}</span></div>"""
            for i in imblick
        )
        imblick_html = f"""
    <section class="imblick">
      <h2 class="label block-titel">Im Blick</h2>
{rows}
    </section>"""

    quellen = r.get("quellen", [])
    quellen_html = ""
    if quellen:
        links = "\n".join(
            f'        <a href="{e(q.get("href"))}">{e(q.get("label"))}</a>' for q in quellen
        )
        quellen_html = f"""
    <section class="quellen">
      <h2 class="label block-titel">Quellen</h2>
      <div class="quellen-liste">
{links}
      </div>
    </section>"""

    return f"""  <main class="bericht">
    <div class="kopf rule3">
      <span class="label">{e(r.get('titel'))}</span>
      <span class="label">Ausgabe {e(r.get('ausgabe'))}</span>
    </div>

    <h1 class="schlagzeile">{e(r.get('schlagzeile'))}</h1>

    <p class="lede">{e(r.get('lede'))}</p>

    <div class="bilanz">
      <span class="links">{e(r.get('bilanz'))}</span>
      <span class="rechts">{e(r.get('bilanzRechts'))}</span>
    </div>

    <section class="zeilen">
{beispiel_hinweis}{zeilen_html}
    </section>{bauplan_html}
{imblick_html}{quellen_html}

    <div class="fuss">
      <span class="regeltext">Automatisch erstellt f&uuml;r Flo &middot; n&auml;chste Ausgabe {e(r.get('naechste'))}.
      Meldungen ohne erkennbares Ver&ouml;ffentlichungsdatum werden nicht aufgenommen.</span>
      <span class="aktionen"><span class="inaktiv">Als E-Mail</span> &nbsp; Quellen bearbeiten</span>
    </div>
  </main>"""


# --------------------------------------------------------------------------- #
# Seiten zusammensetzen
# --------------------------------------------------------------------------- #
def page(title, fp, left, right):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)} &middot; Artefakt</title>
<style>{css(fp)}</style>
</head>
<body>
<div class="wrap">
{left}

{right}
</div>
</body>
</html>
"""


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def build():
    reports = load_reports()
    if not reports:
        print("Keine Ausgaben in ausgaben/ gefunden.", file=sys.stderr)
        return 1

    latest = latest_per_ressort(reports)
    entries = archive_entries(reports)

    # Einzelseiten je Bericht.
    for r in reports:
        left = render_left(latest, entries, r.get("id"), fp="../")
        right = render_report(r)
        write(
            os.path.join(SITE, "berichte", f"{r['id']}.html"),
            page(r.get("titel", "Bericht"), "../", left, right),
        )

    # Startseite: juengste Live-Ausgabe, sonst juengste ueberhaupt.
    live = [r for r in reports if r.get("status") == "live"]
    pool = live or reports
    start = max(pool, key=lambda r: str(r.get("stand", "")))
    left = render_left(latest, entries, start.get("id"), fp="")
    right = render_report(start)
    write(os.path.join(SITE, "index.html"), page(start.get("titel", "Artefakt"), "", left, right))

    print(f"{len(reports)} Ausgabe(n) verbaut -> site/index.html + site/berichte/")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
