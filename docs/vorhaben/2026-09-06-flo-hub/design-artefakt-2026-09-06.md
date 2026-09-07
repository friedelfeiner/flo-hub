# Design: Artefakt (aus Claude-Design-Entwurf)

**Quelle:** `Artefakt Dashboard.dc.html`, Claude Design, Projekt
`9ea0213e-98f2-44a8-8d7b-aad60f76e5dc`
**Stand:** 2026-09-06

Destillat des Entwurfs — genug, um die Seite ohne die Original-Datei zu bauen.
Die Original-`.dc.html` (rund 500 KB, Fonts eingebettet) sollte zusätzlich unter
`design/` im Projekt liegen.

## Der Grundgedanke

Kein Dashboard, sondern eine **Berichtsmappe**: klassisch gesetzte Zeitung,
Haarlinien statt Kacheln, Tabellenziffern, gesperrte Versal-Labels,
Blocksatz mit Silbentrennung. Nichts blinkt, nichts ist bunt. Der Name der
Seite im Entwurf ist **Artefakt**.

## Farben

```
--color-bg          #f4f0e7   warmes Papier (überschreibt das hellere #f3f2f2)
--color-surface     #eae9e9
--color-text        #201f1d   fast schwarz, leicht warm
--color-accent      #b68235   Ocker/Gold — der einzige Akzent
--color-divider     16 % Text auf transparent
```

Dazu neutrale und Akzent-Rampen in je neun Stufen (`--color-neutral-100…900`,
`--color-accent-100…900`), in OKLCH auf einer gemeinsamen Helligkeitsskala
erzeugt. Kein Dark Mode.

**Wichtig:** Es gibt **keine Farbe je Thema.** Alle Ressorts nutzen denselben
goldenen Akzent; unterschieden wird über gesperrte Textlabels
(`MEDIEN`, `WELT`, `KRYPTO`, `FINANZEN`, `REISEN`). Das korrigiert die
Annahme im Konzept, jedes Thema bekomme eine eigene Akzentfarbe.

## Schrift

- Überschriften: **Cormorant Garamond**, 400 für die große Schlagzeile,
  600 für Interface-Labels. Zeilenhöhe 1.12, Laufweite −0.015em.
- Fließtext: **Lora**, 15px/1.55, Blocksatz mit `hyphens: auto`,
  `text-wrap: pretty`, Textbreite auf 64–68 Zeichen begrenzt.
- Labels: 10–11px, `letter-spacing: 0.18–0.24em`, Versalien, Grau.
- Zahlen überall `font-feature-settings: 'tnum'`.

Abstände laufen auf einem 4.6px-Raster (`--space-1` … `--space-8`).

## Aufbau der Seite

Zweispaltig, `max-width: 1440px`, `grid-template-columns: minmax(0,320px)
minmax(0,1fr)`.

**Links (klebt, eigener Scroll):**
1. Kopf: „Artefakt" + `BERICHTSMAPPE · <Datum>`, darüber eine 3px-Linie.
2. **Aktuell** — ein Eintrag je Thema: Ressort-Label, Datum, Titel, eine Zeile
   Aufmacher, Status-Tag (`Aktiv` / `Entwurf`) und Rhythmus. Der aktive Eintrag
   bekommt einen 2px-Balken links und einen hellen Goldton als Hintergrund.
3. **Archiv** — Filter-Chips nach Ressort, darunter eine Liste
   `Datum | Titel + Ressort · Ausgabe`.
4. Fußzeile: „Gesamtarchiv" und „Neuer Bericht".

**Rechts (der Bericht):**
1. Kopfzeile über 3px-Linie: Titel links, Ausgabe rechts, beide als Versal-Label.
2. **Schlagzeile** — 46px, Cormorant 400, `max-width: 20ch`.
3. **Lede** — 16.5px/1.72, Blocksatz, max. 68 Zeichen.
4. **Bilanzzeile** zwischen zwei Haarlinien: Zählung links
   („Video 3 · Bild 2 · Musik 1"), offene Punkte rechts in Gold.
5. **Ledger-Zeilen** — das Herzstück. Zwei Spalten, 150px links:
   `Kategorie / Art / Datum`, rechts durch eine senkrechte Haarlinie getrennt:
   Titel (23px), Text (15.5px, Blocksatz), optional ein Quellenlink mit Pfeil.
6. **Bauplan** (nur bei Status `Entwurf`) — zwei Spalten: „Geplante Quellen"
   als Liste, „Aufbau der Ausgabe" als Label/Text-Paare. Darunter ein Satz:
   „Die Zeilen oben sind Beispielinhalte zur Ansicht — <Thema> läuft noch nicht
   automatisch."
7. **Im Blick** — Was-links / Stand-rechts.
8. **Quellen** — Label plus Links in einer Zeile umbrechend.
9. Fußzeile über 3px-Linie: „Automatisch erstellt für Flo · nächste Ausgabe
   <Datum>. Meldungen ohne erkennbares Veröffentlichungsdatum werden nicht
   aufgenommen." Rechts „Als E-Mail", „Quellen bearbeiten".

## Mobil

Ab 900px Breite: eine Spalte. Die linke Spalte klebt nicht mehr und wandert
nach oben. Die Ledger-Zeilen verlieren ihre Trennlinie und stapeln sich, wobei
Kategorie/Art/Datum in eine umbrechende Zeile rutschen. Schlagzeile auf 34px.

## Datenmodell, das der Entwurf voraussetzt

Pro Bericht:

```
id, ressort, titel, stand, zeile (Aufmacher),
status: "live" | "entwurf", rhythmus,
ausgabe, naechste, schlagzeile, lede,
bilanz, bilanzRechts,
zeilen[]:  { kategorie, art, datum, titel, text, linkLabel?, href? }
plan?:     { quellen[], aufbau[]: { label, text } }
imBlick[]: { was, stand }
quellen[]: { label, href }
```

Archiv: `{ datum, ressort, ausgabe, titel, ref }` — `ref` zeigt auf die
Bericht-`id`.

Das ist zugleich die Vorgabe, was ein Recherche-Lauf produzieren muss.

## Was der Entwurf mitentscheidet

- **Alle fünf Themen sind von Anfang an sichtbar.** Vier davon stehen im
  Entwurf auf `entwurf` und zeigen statt Inhalten ihren Bauplan. Reisen muss
  also nicht auf Stufe 2 warten, um zu existieren — nur um zu liefern.
- **Der Ton steht.** „Sechs Änderungen, drei mit Auswirkung." Zahlen mit
  Vergleichswert daneben. Preise alt → neu in Euro, nicht in Prozent.
  Ausdrücklicher Hinweis, wenn es keinen Anlass gab.
- **Eine Regel steht in der Fußzeile**, nicht im Kleingedruckten: keine
  Meldung ohne erkennbares Datum.
- **„Als E-Mail" ist im Entwurf vorgesehen.** Im Konzept steht Newsletter-
  Versand unter „Nicht enthalten" — der Link kann vorerst inaktiv bleiben.
