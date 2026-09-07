# Plan: FLO Hub

## Ziel

Unter `hub.floachleitner.com` steht die Berichtsmappe „Artefakt". Fünf
Ressorts sind sichtbar, vier davon erzeugen ihre Ausgaben zeitgesteuert von
selbst — jedes aus genau einem Briefing, das Flo bearbeiten kann, ohne Code
anzufassen.

## Überblick

- **A** ✅ — Die Seite entsteht: aus abgelegten Daten wird die Berichtsmappe, so
  wie der Artefakt-Entwurf sie zeigt, am Rechner wie am Handy.
- **B** `Risiko: hoch` — Die Seite geht unter Flos Adresse online, unverlinkt
  und für Suchmaschinen gesperrt.
- **C** — Für jedes der fünf Ressorts entsteht die Arbeitsanweisung, nach der
  recherchiert wird.
- **D** `[Kern]` `Risiko: hoch` — Ein Lauf macht aus einer Anweisung eine
  fertige Ausgabe und stellt sie auf die Seite.
- **E** `Risiko: hoch` — Die Läufe starten von allein, zur richtigen Zeit, ohne
  dass Flo etwas anklickt.

## Projekt-Kontext

**Projekt:** Neues Vorhaben, leeres Verzeichnis. Es entsteht ein Git-Repo mit
den Briefings, den erzeugten Ausgaben, dem Seitenbau und dem Lauf-Prompt.

**Relevante Dateien:**
- `docs/vorhaben/2026-09-06-flo-hub/konzept-flo-hub-2026-09-06.md` — das
  freigegebene Konzept, verbindlich für Umfang und Ton.
- `docs/vorhaben/2026-09-06-flo-hub/design-artefakt-2026-09-06.md` — Farben,
  Schrift, Aufbau, Datenmodell. Verbindlich für alles Sichtbare.

**Produktive Ordner:** Ab Block B ist der Inhalt von `site/` das, was
öffentlich ausgeliefert wird. Ab Block E laufen Agenten unbeaufsichtigt gegen
das Repo.

**Harte Verbote:**
- Keine Depotwerte, Stückzahlen, Einstandskurse oder Euro-Gewinne — weder in
  Briefings noch in Ausgaben. Das Repo ist öffentlich und seine Historie
  unwiderruflich: Gelöschtes bleibt lesbar.
- Keine Meldung ohne erkennbares Veröffentlichungsdatum. Lieber weglassen.
- Keine Anlageempfehlungen, keine Kursziele, keine Prognosen.
- Das bestehende `generative-media-weekly`-Artefakt in der Claude-App wird
  nicht angefasst und nicht migriert.

## Block A — Seite und Gerüst ✅

**Abhängigkeit:** —
**Kontext:** `design-artefakt-2026-09-06.md` (Farben, Schrift, Aufbau,
Datenmodell), `konzept-flo-hub-2026-09-06.md`
**Offene Entscheidungen:** —

Vorgabe für den ganzen Block: Die ausgelieferte Seite ist **statisches HTML,
zur Bauzeit erzeugt**. Kein Framework im Browser, keine Laufzeitabhängigkeit.
Der Design-Entwurf ist eine React-Komponente — er dient als Vorlage, wird aber
nicht als solche ausgeliefert. Das Build-Skript ist Python ohne Fremdpakete.

- [x] **A1** [mechanisch] Git-Repo `flo-hub` ist angelegt, mit `briefings/`,
      `ausgaben/`, `build/`, `site/` und einem `README.md`, das die
      Sprachregelung (Ressort / Ausgabe / Briefing) und den Ablauf in zehn
      Zeilen erklärt.
- [x] **A2** Das Ausgabeformat liegt als dokumentiertes JSON-Schema in
      `build/schema.md` fest, exakt nach dem Datenmodell im Design-Dokument
      (`id, ressort, titel, stand, status, rhythmus, ausgabe, naechste,
      schlagzeile, lede, bilanz, bilanzRechts, zeilen[], plan?, imBlick[],
      quellen[]`). Dazu je eine Beispieldatei unter
      `ausgaben/<ressort>/beispiel.json` für alle fünf Ressorts — Medien mit
      echtem Inhalt aus dem Entwurf, die vier anderen mit `status: "entwurf"`
      und gefülltem `plan`.
- [x] **A3** `build/build.py` erzeugt aus den Dateien in `ausgaben/` die
      komplette Seite nach `site/`: linke Spalte mit „Aktuell" und
      gefiltertem Archiv, rechte Spalte mit der gewählten Ausgabe. Farben,
      Schriften, Abstände und der Seitenaufbau entsprechen dem
      Design-Dokument; Cormorant Garamond und Lora liegen als lokale
      Schriftdateien im Repo, nicht als externe Einbindung.
- [x] **A4** Die gebaute Seite ist am Desktop und bei 375px Breite vollständig
      lesbar: keine waagerechte Scrollleiste, die Ledger-Zeilen stapeln sich,
      die Seitenspalte klappt nach oben. Nachweis: Screenshots beider Breiten
      im Task-Ergebnis.
- [x] **A5** Ein Ressort mit `status: "entwurf"` zeigt statt der Ledger-Zeilen
      seinen Bauplan („Geplante Quellen" und „Aufbau der Ausgabe") plus den
      Satz, dass es noch nicht automatisch läuft. Nachweis: sichtbar in der
      gebauten Seite für alle vier Entwurfs-Ressorts.

## Block B — Hosting

**Abhängigkeit:** Block A
**Risiko:** hoch
**Kontext:** `site/` (das, was ausgeliefert wird), Konzept-Abschnitt
„Entscheidungen"
**Offene Entscheidungen:** —

Die Seite ist bewusst öffentlich: öffentliches Repo, kein Zugangsschutz. Der
Schutz besteht darin, dass der Link nicht weitergegeben wird und die Seite
nicht indexiert ist. Der Block trägt trotzdem `Risiko: hoch`, weil hier zum
ersten Mal etwas nach außen geht und das im öffentlichen Repo unwiderruflich
ist.

- [ ] **B1** `[FLO]` Bei All-Inkl zeigt ein CNAME für `hub.floachleitner.com`
      auf GitHub Pages.
- [ ] **B2** Die gebaute Seite ist über `hub.floachleitner.com` mit gültigem
      HTTPS-Zertifikat erreichbar.
- [ ] **B3** `site/robots.txt` sperrt alle Bots, und jede erzeugte Seite trägt
      `<meta name="robots" content="noindex, nofollow">`. Nachweis: beides im
      ausgelieferten Stand abrufbar.
- [ ] **B4** Ein `git log -p`-Durchlauf über das gesamte Repo enthält keine
      Stückzahlen, Beträge oder Einstandskurse — auch nicht in gelöschten
      Ständen. Nachweis vor dem ersten Push, weil Git-Historie sich nicht
      sauber zurücknehmen lässt.

## Block C — Die fünf Briefings

**Abhängigkeit:** Block A
**Kontext:** `briefings/`, der bestehende Generative-Media-Prompt (im Konzept
zitiert), `build/schema.md`
**Offene Entscheidungen:** Die Aktien- und Krypto-Listen sowie die Reiseliste
liegen noch nicht vor. Fehlen sie, bleiben die betroffenen Ressorts auf
`status: "entwurf"` — der Block ist trotzdem abschließbar.

- [ ] **C1** `briefings/medien.md` existiert und ist die überführte Fassung des
      bestehenden Generative-Media-Prompts: Kopfdaten (Ressort, Rhythmus,
      Uhrzeit) als Frontmatter, **die Quellenliste als erste inhaltliche
      Sektion**, danach Auftrag, Relevanzkriterien, Gewichtung, Rubriken und
      Tonregeln. Der Abschnitt zur HTML-Erzeugung entfällt — der Lauf liefert
      JSON nach `build/schema.md`.
- [ ] **C2** `briefings/welt.md` existiert, mit den Rubriken Deutschland,
      Ukraine, USA/Trump, International, werktäglich 7:00, höchstens zwölf
      Zeilen, sortiert nach Bedeutung statt nach Uhrzeit.
- [ ] **C3** `briefings/krypto.md` und `briefings/finanzen.md` existieren.
      Krypto werktäglich 7:00 mit Kursstand, 24-Stunden- und
      7-Tage-Veränderung. Finanzen wöchentlich mit Wochenveränderung,
      Leitindizes und Terminvorschau, Branchenschwerpunkt Windenergie,
      Solar/Erneuerbare, Big Tech. Beide enthalten die Regel, dass Zahlen
      immer mit Vergleichswert daneben stehen und dass keine Empfehlungen
      ausgesprochen werden.
- [ ] **C4** `briefings/reisen.md` existiert, beschränkt auf konkret geplante
      Reisen: Preisverlauf beobachteter Strecken, Fristen der nächsten neunzig
      Tage, Störungen auf betroffenen Strecken. Enthält den Hinweis, dass das
      Ressort ohne gepflegte Reiseliste keinen Inhalt hat.
- [ ] **C5** `[FLO]` Die drei Listen sind hinterlegt: Aktien (Name, gern
      Ticker), Coins, Reiseziele mit Zeitraum. Keine Stückzahlen, keine
      Beträge.

## Block D — Der Lauf [Kern]

**Abhängigkeit:** Block C
**Risiko:** hoch
**Kontext:** `briefings/`, `ausgaben/`, `build/schema.md`, `build/build.py`
**Offene Entscheidungen:** —

- [ ] **D1** Ein Lauf-Prompt in `build/lauf.md` beschreibt den vollständigen
      Ablauf für ein beliebiges Ressort: Briefing lesen, letzte Ausgabe des
      Ressorts aus `ausgaben/<ressort>/` laden, recherchieren, neue Ausgabe
      als JSON nach Schema schreiben, Seite bauen, committen. Das Ressort ist
      der einzige Parameter.
- [ ] **D2** Der Lauf meldet nur Veränderungen: Was in einer der letzten acht
      Ausgaben desselben Ressorts schon berichtet wurde, erscheint nicht
      erneut als Neuigkeit. Nachweis: zwei Läufe desselben Ressorts
      hintereinander; der zweite wiederholt keine Meldung des ersten.
- [ ] **D3** Ein Lauf ohne belastbare Funde erzeugt trotzdem eine gültige,
      kurze Ausgabe, die genau das sagt — statt keiner Ausgabe oder einer
      erfundenen. Nachweis: Lauf mit künstlich leerem Rechercheergebnis.
- [ ] **D4** Ein Lauf für `medien` läuft von Hand durch und erzeugt eine
      Ausgabe, die auf der gebauten Seite korrekt erscheint. Sie startet als
      frische Baseline, ohne Bezug auf die Claude-App-Historie.
- [ ] **D5** Ein fehlgeschlagener Lauf hinterlässt keine halbe Ausgabe und
      keinen kaputten Stand auf der Seite. Nachweis: Abbruch mitten im Lauf,
      danach ist die Seite unverändert und lauffähig.

## Block E — Zeitsteuerung

**Abhängigkeit:** Block D
**Risiko:** hoch
**Kontext:** `build/lauf.md`, das Repo als Ganzes
**Offene Entscheidungen:** Ob geplante Cloud-Agenten von Claude Code das
Nötige leisten (Web-Recherche, Schreibzugriff aufs Repo, verlässliche
Auslösung), ist praktisch zu prüfen. Ergibt die Prüfung Nein, gilt der
Rückfallweg aus dem Konzept: ein lokaler Timer auf dem Mac. Die Entscheidung
fällt in E1, bevor der Rest des Blocks gebaut wird.

- [ ] **E1** Ein einzelner geplanter Lauf ist in der Cloud eingerichtet und
      einmal ausgelöst worden. Das Ergebnis dokumentiert, ob Recherche und
      Commit funktionieren — und damit, ob Cloud oder lokaler Timer gilt.
- [ ] **E2** Alle vier liefernden Ressorts sind eingeplant: Medien montags,
      Welt und Krypto werktäglich, Finanzen wöchentlich. Die täglichen Läufe
      sind um 7:00 fertig, nicht erst gestartet.
- [ ] **E3** Ein ausgefallener Lauf wird beim nächsten Anlauf nachgeholt und
      nicht stillschweigend übersprungen. Nachweis: Lauf gezielt ausfallen
      lassen, danach den nächsten beobachten.
- [ ] **E4** Nach einer Woche Betrieb liegen die erwarteten Ausgaben vor, und
      die Seite zeigt sie in „Aktuell" und im Archiv an der richtigen Stelle.
