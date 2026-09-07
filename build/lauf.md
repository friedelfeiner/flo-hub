# Lauf eines Ressorts

Führe genau einen vollständigen FLO-Hub-Lauf für das Ressort
`<ressort>` aus. `<ressort>` ist der einzige Parameter und muss genau einer
dieser Ordnernamen sein: `medien`, `welt`, `krypto`, `finanzen`, `reisen`.

Arbeite in einer isolierten Branch oder einem isolierten Worktree. Die
öffentlich ausgelieferte Branch darf während Recherche, Entwurf und Prüfung
nicht verändert werden. Ein fehlgeschlagener oder abgebrochener Lauf endet
ohne Commit und ohne Veröffentlichung.

## Verbindliche Grenzen

- Lies `briefings/<ressort>.md` vollständig und befolge es als
  Ressort-Arbeitsanweisung.
- Lies `build/schema.md`. Das Ergebnis muss diesem Format entsprechen.
- Fasse das bestehende `generative-media-weekly`-Artefakt in der Claude-App
  nicht an und übernimm daraus keine Historie. `medien` startet allein mit den
  Ausgaben in diesem Repository als frische Baseline.
- Veröffentliche keine Depotwerte, Stückzahlen, Einstandskurse oder
  Euro-Gewinne. Gib keine Anlageempfehlungen, Kursziele oder Prognosen aus.
- Eine Meldung ohne erkennbares Veröffentlichungsdatum der belastbaren Quelle
  wird weggelassen. Das Datum eines Abrufs ersetzt kein Veröffentlichungsdatum.
- Erfinde keine Meldung, Quelle, Zahl, Verfügbarkeit oder Einordnung.
- Verwende keine kostenpflichtigen Modelle oder Dienste.

## Ablauf

1. **Briefing und Historie laden.** Lies das Briefing des Ressorts. Lade alle
   JSON-Dateien aus `ausgaben/<ressort>/`, sortiere sie absteigend nach `stand`
   und lies die jüngste Ausgabe sowie insgesamt höchstens die letzten acht.
   Andere Ressorts und externe Verlaufsspeicher sind keine Historie für diesen
   Lauf.

2. **Ausschlussliste bilden.** Erfasse für jede Meldung der acht Ausgaben den
   berichteten Vorgang, seine Quelle beziehungsweise URL und den damaligen
   Stand. Eine bloß umformulierte, neu betitelte oder von einer zweiten Quelle
   bestätigte Meldung bleibt derselbe Vorgang. Sie darf nur erneut erscheinen,
   wenn seitdem eine konkrete, datierte Veränderung eingetreten ist; dann
   berichtet die neue Zeile ausschließlich diese Veränderung und benennt den
   neuen Stand.

3. **Recherchieren.** Recherchiere nach den Quellen, Relevanzkriterien,
   Gewichtungen und Rubriken des Briefings. Öffne die Primärquelle jeder
   erwogenen Meldung und prüfe dort Veröffentlichungsdatum und Aussage. Ein
   Katalog, eine Suche oder eine Übersichtsseite darf einen Fund liefern, ist
   aber ohne datierte Primärquelle kein Nachweis. Halte die belastbaren Funde
   zunächst nur im isolierten Arbeitsbereich fest.

4. **Nur Veränderungen auswählen.** Vergleiche jeden Fund semantisch mit der
   Ausschlussliste. Entferne alles bereits Berichtete ohne neuen Stand. Prüfe
   unmittelbar vor dem Schreiben nochmals alle ausgewählten Quellen-URLs,
   Daten und Zahlen.

5. **Ausgabe im temporären Bereich entwerfen.** Erzeuge genau eine vollständige
   JSON-Datei nach `build/schema.md`; schreibe noch nicht nach
   `ausgaben/<ressort>/`. Dateiname ohne `.json` und `id` müssen identisch sein,
   `ressort` muss `<ressort>` entsprechen. Verwende eine neue, kollisionsfreie
   ID und setze `stand` auf das Datum des Laufs.

6. **Leerer Fund ist ein gültiges Ergebnis.** Bleibt nach Quellenprüfung und
   Ausschlussliste keine belastbare Veränderung übrig, erzeuge trotzdem eine
   kurze gültige Ausgabe. Sie sagt in `zeile`, `schlagzeile` und `lede`
   ausdrücklich, dass seit der letzten Ausgabe keine neue belastbare
   Veränderung gefunden wurde. Setze `zeilen` auf `[]`, `imBlick` auf `[]`,
   `quellen` nur auf tatsächlich geprüfte Quellen und erfinde keinen Füllpunkt.

7. **Vorab prüfen.** Parse die temporäre Datei mit der Python-Standardbibliothek
   als JSON und prüfe sämtliche Pflichtfelder aus `build/schema.md`, alle
   Ressortwerte, die Übereinstimmung von ID und Dateiname sowie jedes
   Meldungsdatum. Prüfe außerdem erneut, dass keine Meldung aus den letzten acht
   Ausgaben ohne datierte neue Entwicklung wiederholt wird und keine der
   verbindlichen Grenzen verletzt ist.

8. **Seite isoliert bauen.** Kopiere die geprüfte Kandidatendatei erst jetzt in
   `ausgaben/<ressort>/` des isolierten Arbeitsstands. Führe dort
   `python3 build/build.py` aus. Prüfe, dass `site/index.html`, die neue Seite
   `site/berichte/<id>.html`, alle Links auf lokale Berichtsseiten und das
   `noindex, nofollow`-Meta-Tag vorhanden sind. Prüfe außerdem, dass
   `site/CNAME`, `site/robots.txt` und `site/fonts/` unverändert geblieben sind.

9. **Fehlerfall.** Schlägt Recherche, JSON-Prüfung, Seitenbau oder eine
   Abschlussprüfung fehl, brich ab. Erstelle keinen Commit, übertrage keine
   Teildatei auf die Auslieferungs-Branch und veröffentliche nichts. Korrigiere
   nur innerhalb des isolierten Arbeitsstands und beginne die Prüfungen erneut.

10. **Abschluss und Commit.** Kontrolliere den Diff. Er darf nur das Briefing
    lesen, nicht verändern, und muss genau die neue JSON-Ausgabe sowie die vom
    Seitenbau erzeugten HTML-Dateien enthalten. Committe diese Dateien gezielt
    ohne `git add .` oder `git add -A`. Erst der vollständig geprüfte Commit ist
    das Ergebnis des Laufs; Veröffentlichung und Push erfolgen nur, wenn sie
    außerhalb dieses Prompts ausdrücklich beauftragt sind.

Berichte abschließend Ressort, neue ID, Zahl der neuen Meldungen, verwendete
Quellen, Ergebnis der Wiederholungsprüfung, Ergebnis des Seitenbaus und den
Commit-Hash. Bei einem Abbruch berichte stattdessen die Fehlerstelle und
bestätige, dass kein Commit und keine Veröffentlichung entstanden sind.
