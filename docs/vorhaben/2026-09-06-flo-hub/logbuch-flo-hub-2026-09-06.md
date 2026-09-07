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
