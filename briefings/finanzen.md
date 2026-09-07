---
ressort: finanzen
rhythmus: wöchentlich
status: entwurf
---

## Quellen

- Gepflegte Aktien-Watchlist (siehe Abschnitt „Aktien-Watchlist")
- [Deutsche Börse Newsroom](https://www.deutsche-boerse.com/dbg-de/media/newsroom)
- [SEC Press Releases](https://www.sec.gov/newsroom/press-releases)
- Unternehmensmitteilungen der Werte auf der Watchlist

## Aktien-Watchlist

| Name | ISIN | WKN |
| --- | --- | --- |
| AIS-A.MSCI ROB+AI UEA | LU1861132840 | A2JSC9 |
| ALPHABET INC.CL.A DL-,001 | US02079K3059 | A14Y6F |
| AMAZON.COM INC. DL-,01 | US0231351067 | 906866 |
| APPLE INC. | US0378331005 | 865985 |
| EDISUN POWER E.NAM. SF30 | CH0024736404 | A0KFH3 |
| ENI S.P.A. | IT0003132476 | 897791 |
| ENVITEC BIOGAS O.N. | DE000A0MVLS8 | A0MVLS |
| EQUINOR ASA NK 2,50 | NO0010096985 | 675213 |
| JINKOSOLAR ADR/4 DL-00002 | US47759T1007 | A0Q87R |
| MICROSOFT DL-,00000625 | US5949181045 | 870747 |
| NESTE OYJ | FI0009013296 | A0D9U6 |
| NVIDIA CORP. DL-,001 | US67066G1040 | 918422 |
| SCATEC ASA NK -,02 | NO0010715139 | A12C5D |
| SIEMENS ENERGY AG NA O.N. | DE000ENER6Y0 | ENER6Y |
| SONY FINANCIAL GROUP INC. | JP3435350008 | A0M06N |
| SONY GROUP CORP. | JP3435000009 | 853687 |
| TELEFONICA DTLD HLDG NA | DE000A1J5RX9 | A1J5RX |
| VESTAS WIND SYS. DK -,20 | DK0061539921 | A3CMNS |
| WAERTSILAE | FI0009003727 | 881050 |
| X(I)-AI+BIG DATA ETF 1CDL | IE00BGV5VN51 | A2N6LC |

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
