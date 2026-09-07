---
ressort: finanzen
rhythmus: wöchentlich
status: entwurf
---

## Quellen

- Gepflegte Aktien-Watchlist (Name, optional Ticker)
- [Deutsche Börse Newsroom](https://www.deutsche-boerse.com/dbg-de/media/newsroom)
- [SEC Press Releases](https://www.sec.gov/newsroom/press-releases)
- Unternehmensmitteilungen der Werte auf der Watchlist

## Auftrag

Erstelle einen wöchentlichen deutschen Finanz- und Märktebericht als JSON nach
`build/schema.md`, sobald eine Aktien-Watchlist gepflegt ist. Berichte die
Wochenveränderung der beobachteten Werte, Leitindizes und eine Terminvorschau.
Zahlen stehen immer mit Vergleichswert daneben. Ohne gepflegte Watchlist bleibt
das Ressort ein Entwurf und liefert keinen inhaltlichen Bericht.

## Relevanzkriterien

Nimm datierte, belastbare Entwicklungen zu den beobachteten Unternehmen und
ihren Branchen auf: Ergebnisse, bestätigte Unternehmensmeldungen, regulatorische
Entscheidungen und relevante Markttermine. Jede Meldung braucht ein erkennbares
Veröffentlichungsdatum; ohne Datum wird sie weggelassen.

## Gewichtung

Gewichte zuerst Ereignisse mit direktem Bezug zur Watchlist und danach die
Branchen Windenergie, Solar/Erneuerbare und Big Tech. Lege die
Terminvorschau hinter die Wochenbilanz. Keine Wiederholung ohne neue Entwicklung.

## Rubriken

- Wochenbilanz der Watchlist
- Leitindizes
- Windenergie
- Solar/Erneuerbare
- Big Tech
- Terminvorschau

## Tonregeln

Sachlich, knapp und ohne Handlungshinweise. Keine Anlageempfehlungen, Kursziele
oder Prognosen. Keine Depotwerte, Stückzahlen, Einstandskurse oder Euro-Gewinne.

