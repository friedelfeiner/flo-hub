# Logbuch: FLO Hub

## Block A — Seite und Gerüst · 2026-09-07

A1  Gebaut — Bruno (Sonnet): Git-Repo (`git init`, Branch main), Ordner `briefings/ ausgaben/ build/ site/`, `README.md` mit Sprachregelung und Ablauf in zehn Zeilen  ·  Geprüft — Mira (Sonnet): passt
A2  Gebaut — Bruno (Sonnet): `build/schema.md` (alle Felder inkl. `zeile`, beide Statuswerte, Archiv-Objekt) + fünf `ausgaben/<ressort>/beispiel.json` (Medien live mit echtem Inhalt, vier Entwürfe mit `plan`)  ·  Geprüft — Mira (Sonnet): passt
A3  Gebaut — Bruno (Sonnet): `build/build.py` (nur Stdlib) baut `site/index.html` + `site/berichte/<id>.html`, Design-Tokens/Raster nach Entwurf, lokale Fonts per `@font-face`, Archiv-Filter rein per CSS  ·  Geprüft — Mira (Sonnet): passt
A4  Gebaut — Bruno (Sonnet): responsives Layout, ab 900px eine Spalte, Ledger-Zeilen stapeln, Seitenspalte nach oben  ·  Geprüft — Mira (Sonnet): passt (375px per Geräte-Emulation nachgeprüft — kein Querüberlauf; Brunos Mobil-Screenshot ist ein `--window-size`-Artefakt und als Nachweis untauglich, die Sache selbst stimmt)
A5  Gebaut — Bruno (Sonnet): bei `status:"entwurf"` Bauplan (Geplante Quellen / Aufbau der Ausgabe) + Hinweissatz statt echter Zeilen, für alle vier Entwurfs-Ressorts  ·  Geprüft — Mira (Sonnet): passt

Nebenbefunde: Fonts nur als variable `.ttf` verfügbar (keine `.woff2`); `build.py` schreibt je Bericht eine eigene Seite statt einer Single-Page mit Umschaltung (vom Task gedeckt); Inhalts-`<a href>` im Medien-Beispiel sind `example.com`-Platzhalter.

| Wer | Rolle | Tasks | Tokens | Aufrufe | Ø/Aufruf |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Bruno (Sonnet) | Handwerk | A1–A5 | 89.808 | 33 | 2.722 |
| Mira (Sonnet) | Prüfung | A1–A5 | 72.611 | 25 | 2.904 |

## Block B — Hosting (Risiko: hoch) · 2026-09-07 — nur B3/B4, Block nicht abgeschlossen

B3  Gebaut — Berta (Opus): `site/robots.txt` (`Disallow: /`) + `<meta name="robots" content="noindex, nofollow">` zentral in `page()`, jede der sechs HTML-Seiten trägt den Tag  ·  Geprüft — Klara (Opus): passt (kein zweiter HTML-Pfad, neues Ressort verliert den Tag nicht, `robots.txt` überlebt den Bau)
B4  Gebaut — Berta (Opus): `build/pruef-historie.sh` — `git log -p --all` + Arbeitsstand gegen vier Muster (Zahl↔Währung, Zahl↔Stück-Einheit, Schlüsselwörter); Lauf: `exit=1`, 9 Fundstellen, alle Regeltext/Projektnotiz  ·  Geprüft — Klara (Opus): passt (Fundstellen von Hand geprüft, fünf `beispiel.json` von Hand durchgesehen, Wirksamkeits-Gegentest mit gelöschtem Stand bestätigt)

Nicht gebaut (blockiert): B1 `[FLO]` (CNAME bei All-Inkl → GitHub Pages), B2 (Seite über die Domain mit HTTPS erreichbar — braucht GitHub-Repo + ersten Push).

Offen für Flo:
- Prüfumfang-Politik für `pruef-historie.sh`: Gesamtlauf steht dauerhaft auf `exit=1`, weil Konzept/Plan/`schema.md` das Verbot im Klartext formulieren (+ „4 $/Monat", „etwa 20 Aktien"). Standard auf `ausgaben briefings site` beschränken, Ausnahmeliste, oder roten Lauf bewusst jedes Mal lesen?
- B4-Nachweis „vor dem ersten Push" verlangt Flos Blick auf die 9 Fundstellen, bevor gepusht wird.
- B2 braucht die Entscheidung, in welches GitHub-Repo/Konto gepusht wird, plus Freigabe des ersten Push (öffentlich, unwiderruflich).

Nebenbefunde: `build/build.py` hat `BUILD_DATUM = "2026-09-06"` fest verdrahtet — jede Seite zeigt dieses Datum unabhängig vom Baudatum (vor D4 beheben). `pruef-historie.sh`: Tippfehler im Pfadargument liefert still `exit=0` (nur relevant, falls das Skript später automatisch läuft).

| Wer | Rolle | Tasks | Tokens | Aufrufe | Ø/Aufruf |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Berta (Opus) | Handwerk | B3, B4 | 56.363 | 19 | 2.966 |
| Klara (Opus) | Prüfung | B3, B4 | 53.271 | 17 | 3.134 |
