# Ausgabeformat (JSON-Schema, dokumentiert)

Eine **Ausgabe** eines **Ressorts** ist genau eine JSON-Datei unter
`ausgaben/<ressort>/<id>.json`. Ressort-Ordnernamen: `medien`, `welt`,
`krypto`, `finanzen`, `reisen`.

Das Format folgt dem Datenmodell aus
`docs/vorhaben/2026-09-06-flo-hub/design-artefakt-2026-09-06.md`
(Abschnitt „Datenmodell, das der Entwurf voraussetzt"). Dieses Dokument ist
für alles Sichtbare verbindlich; hier steht nur, wie es als JSON abgelegt wird.

Kein Wert darf Depotwerte, Stückzahlen, Einstandskurse oder Euro-Gewinne
enthalten. Jede `zeile` braucht ein erkennbares `datum`; ohne Datum wird eine
Meldung weggelassen.

## Feldübersicht (Bericht)

| Feld          | Typ            | Pflicht | Bedeutung |
|---------------|----------------|---------|-----------|
| `id`          | string         | ja      | Eindeutige Kennung der Ausgabe, z. B. `medien-2026-kw36`. Dateiname ohne `.json` = `id`. |
| `ressort`     | string         | ja      | Eines von `medien`, `welt`, `krypto`, `finanzen`, `reisen`. |
| `titel`       | string         | ja      | Klartext-Name des Ressorts, z. B. „Generative Media". |
| `stand`       | string (Datum) | ja      | Veröffentlichungsdatum der Ausgabe, `YYYY-MM-DD`. |
| `zeile`       | string         | ja      | Aufmacher in einem Halbsatz. Erscheint links unter „Aktuell". |
| `status`      | string         | ja      | `"live"` oder `"entwurf"` (siehe unten). |
| `rhythmus`    | string         | ja      | Lieferrhythmus im Klartext, z. B. „wöchentlich, montags". |
| `ausgabe`     | string         | ja      | Bezeichnung dieser Lieferung, z. B. „KW 36". |
| `naechste`    | string (Datum) | ja      | Geplantes Datum der nächsten Ausgabe, `YYYY-MM-DD`. |
| `schlagzeile` | string         | ja      | Große Überschrift des Berichts. Richtwert bis ~20 Zeichen je Zeile. |
| `lede`        | string         | ja      | Anrisstext, ein Absatz, Blocksatz. Richtwert bis ~68 Zeichen je Zeile. |
| `bilanz`      | string         | ja      | Zählung links in der Bilanzzeile, z. B. „Video 3 · Bild 2 · Musik 1". |
| `bilanzRechts`| string         | ja      | Offene Punkte rechts in der Bilanzzeile, in Gold gesetzt. Leerstring erlaubt. |
| `zeilen`      | array          | ja      | Die Ledger-Zeilen (siehe unten). Bei `status: "entwurf"` Beispielinhalte. |
| `plan`        | object         | nur bei `status: "entwurf"` | Bauplan (siehe unten). Bei `"live"` weglassen. |
| `imBlick`     | array          | ja      | „Im Blick"-Punkte (siehe unten). Darf leer sein (`[]`). |
| `quellen`     | array          | ja      | Quellen-Links (siehe unten). Darf leer sein (`[]`). |

### `status`

- `"live"` — das Ressort läuft automatisch. Der Bericht zeigt seine
  Ledger-Zeilen. Links erscheint das Status-Tag „Aktiv".
- `"entwurf"` — das Ressort ist sichtbar, liefert aber noch nicht automatisch.
  Statt der Ledger-Zeilen wird der `plan` gezeigt, dazu der Satz:
  „Die Zeilen oben sind Beispielinhalte zur Ansicht — <Thema> läuft noch nicht
  automatisch." Links erscheint das Status-Tag „Entwurf".

## `zeilen[]` — eine Ledger-Zeile

| Feld        | Typ    | Pflicht | Bedeutung |
|-------------|--------|---------|-----------|
| `kategorie` | string | ja      | Rubrik, z. B. „Bild", „Video", „Deutschland". |
| `art`       | string | ja      | Kurzform der Meldungsart, z. B. „Release", „Update", „Einordnung". |
| `datum`     | string | ja      | Erkennbares Veröffentlichungsdatum der Meldung, `YYYY-MM-DD`. |
| `titel`     | string | ja      | Überschrift der Zeile. |
| `text`      | string | ja      | Fließtext, Blocksatz. Zahlen mit Vergleichswert daneben. |
| `linkLabel` | string | optional| Beschriftung des Quellenlinks. Nur zusammen mit `href`. |
| `href`      | string | optional| Ziel des Quellenlinks. Nur zusammen mit `linkLabel`. |

## `plan` — Bauplan (nur `status: "entwurf"`)

| Feld      | Typ    | Pflicht | Bedeutung |
|-----------|--------|---------|-----------|
| `quellen` | array von string | ja | „Geplante Quellen", je Eintrag eine Zeile. |
| `aufbau`  | array           | ja | „Aufbau der Ausgabe", Label/Text-Paare. |

`aufbau[]`: `{ "label": string, "text": string }`.

## `imBlick[]` — ein „Im Blick"-Punkt

| Feld    | Typ    | Pflicht | Bedeutung |
|---------|--------|---------|-----------|
| `was`   | string | ja      | Was beobachtet wird (links). |
| `stand` | string | ja      | Aktueller Stand dazu (rechts). |

## `quellen[]` — ein Quellen-Link

| Feld    | Typ    | Pflicht | Bedeutung |
|---------|--------|---------|-----------|
| `label` | string | ja      | Anzeigename der Quelle. |
| `href`  | string | ja      | URL der Quelle. |

## Archiv-Objekt

Das Archiv links wird vom Seitenbau aus allen vorhandenen Ausgaben erzeugt.
Ein Archiv-Eintrag hat die Form:

| Feld      | Typ            | Bedeutung |
|-----------|----------------|-----------|
| `datum`   | string (Datum) | `stand` der Ausgabe, `YYYY-MM-DD`. |
| `ressort` | string         | Ressort-Schlüssel der Ausgabe. |
| `ausgabe` | string         | `ausgabe` der Ausgabe, z. B. „KW 36". |
| `titel`   | string         | `schlagzeile` der Ausgabe. |
| `ref`     | string         | `id` der Ausgabe, auf die der Eintrag zeigt. |

## Vollständiges Beispiel

Siehe `ausgaben/medien/beispiel.json` (Status `live`, mit Inhalt) und
`ausgaben/welt/beispiel.json`, `ausgaben/krypto/beispiel.json`,
`ausgaben/finanzen/beispiel.json`, `ausgaben/reisen/beispiel.json`
(Status `entwurf`, mit gefülltem `plan`).
