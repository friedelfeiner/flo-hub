# flo-hub

Die Berichtsmappe „Artefakt" unter `hub.floachleitner.com`. Regelmäßig erzeugte
Berichte zu fünf Themen sammeln sich auf einer statisch gebauten Leseseite.

## Sprachregelung

- **Ressort** — ein laufendes Thema. Fünf: Medien, Welt, Krypto, Finanzen, Reisen.
- **Ausgabe** — eine einzelne Lieferung eines Ressorts (z. B. „KW 36").
- **Briefing** — die Markdown-Datei, die ein Ressort definiert. Genau eine je
  Ressort, unter `briefings/`.

## Ablauf

1. Flo pflegt je Ressort ein Briefing in `briefings/<ressort>.md`.
2. Ein zeitgesteuerter Lauf liest das Briefing des Ressorts.
3. Der Lauf lädt die letzte Ausgabe desselben Ressorts aus `ausgaben/<ressort>/`.
4. Er recherchiert entlang der im Briefing genannten Quellen.
5. Bereits berichtete Meldungen werden nicht wiederholt.
6. Das Ergebnis wird als JSON nach `build/schema.md` in `ausgaben/<ressort>/` abgelegt.
7. Findet ein Lauf nichts Belastbares, entsteht trotzdem eine kurze, gültige Ausgabe.
8. `python3 build/build.py` erzeugt aus allen Ausgaben die Seite nach `site/`.
9. Der Stand wird committet; `site/` ist das, was öffentlich ausgeliefert wird.
10. Ressorts ohne Briefing-Daten bleiben auf `status: "entwurf"` und zeigen ihren Bauplan.

## Ordner

- `briefings/` — je Ressort eine Markdown-Arbeitsanweisung.
- `ausgaben/<ressort>/` — die erzeugten Ausgaben als JSON.
- `build/` — `build.py` (Seitenbau, nur Standardbibliothek) und `schema.md`.
- `site/` — die gebaute, statische Seite. Kein Framework, keine Laufzeitabhängigkeit.
