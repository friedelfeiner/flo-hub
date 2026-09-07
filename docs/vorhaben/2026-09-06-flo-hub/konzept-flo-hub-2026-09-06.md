# Konzept: FLO Hub

**Datum:** 2026-09-06
**Status:** ✅ freigegeben 2026-09-06

## Sprachregelung

- **Ressort** — ein laufendes Thema. Fünf: Medien, Welt, Krypto, Finanzen, Reisen.
- **Ausgabe** — eine einzelne Lieferung eines Ressorts („KW 36").
- **Briefing** — die Markdown-Datei, die ein Ressort definiert. Genau eine je
  Ressort, unter `briefings/`.

## Ziel

Flo hat unter `hub.floachleitner.com` eine eigene Leseseite, auf der sich
regelmäßig erzeugte Berichte zu seinen Themen sammeln — Generative Media,
Weltlage, Bitcoin, Finanzen, Reisen. Die Berichte entstehen ohne sein Zutun und
stehen morgens einfach da. Was ein Bericht enthält, welchen Rhythmus er hat und
wo recherchiert wird, steht pro Thema in **einer** Markdown-Datei, die Flo
selbst bearbeiten kann, ohne Code anzufassen.

Heute existiert nur ein einzelner Prompt für Generative Media, der von Hand in
der Claude-App läuft und dessen Ergebnis als loses HTML herumliegt.

## Erfolgskriterien

- Auf `hub.floachleitner.com` liegt eine Seite mit zwei Bereichen: links eine
  schmale Auswahl (oben die aktuellen Ausgaben je Thema, darunter das Archiv
  nach Thema und Datum), in der Mitte der gelesene Bericht.
- Vier Themen liefern automatisch: **Generative Media** (wöchentlich montags),
  **Weltlage** (werktäglich, fertig um 7:00), **Bitcoin & Krypto**
  (werktäglich, fertig um 7:00), **Finanzen & Märkte** (wöchentlich).
  **Reisen** ist als fünfter Bereich angelegt, kommt inhaltlich in Stufe 2.
- Für jedes Thema existiert genau eine Briefing-Datei in Markdown. Darin stehen
  weit oben und ohne Suchen die Quellen, auf denen recherchiert werden soll.
  Ändert Flo dort eine Zeile, wirkt das beim nächsten Lauf — ohne Codeänderung.
- Ein neuer Bericht entsteht, wird veröffentlicht und ist auf der Seite
  sichtbar, ohne dass Flo etwas anklickt. Ein ausgefallener Lauf wird beim
  nächsten Mal nachgeholt statt stillschweigend übersprungen.
- Bitcoin- und Finanzbericht enthalten harte Zahlen zu Flos eigenen Positionen:
  aktueller Kurs, Veränderung seit dem letzten Bericht, dazu die Nachrichtenlage
  zu genau diesen Werten und ihren Branchen.
- Jeder Bericht kennt seine Vorgänger: er meldet, was sich seit der letzten
  Ausgabe geändert hat, und wiederholt keine Meldung, die schon berichtet wurde.
- Ein Lauf, der nichts Belastbares findet, erzeugt einen kurzen Bericht, der das
  sagt — keinen erfundenen und keinen ausgefallenen.
- Am Desktop ist die Seite die primäre Leseumgebung; am Handy ist jeder Bericht
  vollständig lesbar (keine abgeschnittenen Tabellen, kein Seitenscrollen quer).
- Ein neues Thema hinzuzufügen heißt: eine Briefing-Datei schreiben. Nicht: das
  System erweitern.

## Nicht enthalten

- **Redaktion vor Veröffentlichung** — Berichte gehen direkt live. Korrektur
  passiert im Nachhinein, indem Flo eine Ausgabe löscht oder neu erzeugt.
- **Depotwerte, Stückzahlen, Einstandskurse, Gewinn/Verlust in Euro** —
  berichtet werden Kurse und prozentuale Veränderungen einer Watchlist, nicht
  Flos Vermögensstand. Das ist die eine Grenze, die auch bei einer öffentlichen
  Seite hält.
- **Anlageempfehlungen** — die Berichte sagen, was passiert ist, nicht was zu
  tun ist.
- **Kommentare, Nutzerkonten, Suche über alle Ausgaben** — Leser ist eine
  Person. Kommt, wenn Blättern im Archiv nervt.
- **Newsletter-Versand per Mail** — die Seite ist der Kanal.
- **Reise-Inhalte in Stufe 1** — vier zu verschiedene Wünsche (siehe unten),
  eigene Runde, sobald die vier News-Berichte laufen.
- **Zugangsschutz jeder Art** — die Seite ist öffentlich, nur unverlinkt und
  für Suchmaschinen gesperrt.

## Wie ich mir das Ergebnis vorstelle

**Die Seite.** Links eine ruhige Spalte, oben „Aktuell" mit einer Zeile je
Thema (Thema, Datum der jüngsten Ausgabe, Aufmacher in einem Halbsatz),
darunter „Archiv", nach Thema gruppiert und aufklappbar. Mitte: der Bericht,
Lesebreite um 760px, hell, keine Dark-Mode-Umschaltung. Am Handy klappt die
linke Spalte zu einem Menü zusammen.

**Der Look.** Steht: Flos Claude-Design-Entwurf `Artefakt Dashboard` liegt vor
und ist ausgewertet — Details in
[design-artefakt-2026-09-06.md](design-artefakt-2026-09-06.md). Kurz: eine
klassisch gesetzte Berichtsmappe auf warmem Papier (#f4f0e7), Cormorant
Garamond und Lora, ein einziger goldener Akzent, Haarlinien statt Kacheln,
Tabellenziffern, Blocksatz mit Silbentrennung. Kein Dark Mode. Die Ressorts
unterscheiden sich über gesperrte Textlabels, **nicht** über Farbe.

**Die Briefing-Datei.** Pro Thema eine Markdown-Datei, die Flo liest wie eine
Arbeitsanweisung an einen Mitarbeiter: was der Bericht leisten soll, welcher
Rhythmus, **welche Quellen** (namentlich, als erste inhaltliche Sektion), was
relevant ist und was nicht, wie gewichtet wird, welche Rubriken es gibt. Der
bestehende Generative-Media-Prompt wird die erste dieser Dateien.

**Die Themen im Einzelnen.**

- *Weltlage* — ein Bericht mit vier Rubriken: Deutschland, Ukraine, USA/Trump,
  International.
- *Bitcoin & Krypto* — Kursstand und Tagesveränderung für Flos Krypto-Watchlist,
  dazu die Nachrichtenlage dazu.
- *Finanzen & Märkte* — Wochenrückblick über Flos Aktien-Watchlist (etwa 20
  Werte) mit Wochenveränderung, ein paar Leitindizes, und was bei diesen Werten
  konkret passiert ist. Schwerpunkt der Branchenbeobachtung: **Windenergie,
  Solar/Erneuerbare, Big Tech**.
- *Generative Media* — wie bisher, Rubriken Bild, Video, Musik/Audio.

**Reisen.** Flo will dort vier Dinge, die sich nicht in einen Bericht pressen
lassen: Recherche zu konkreten Zielen, laufende Inspiration, aktive Planung
laufender Trips und eine Ablage eigener Reisen. Der Design-Entwurf löst das
elegant: Reisen ist von Anfang an als Bereich sichtbar, steht aber auf
„Entwurf" und zeigt statt Inhalten seinen Bauplan — geplante Quellen und
geplanter Aufbau. Inhaltlich beschränkt sich Stufe 1 auf den engsten Teil:
Preise, Fristen und Störungen für **konkret geplante Reisen**. Das setzt eine
gepflegte Liste aus Ziel und Zeitraum voraus. Inspiration und die Ablage
eigener Reisen bleiben Stufe 2.

## Entscheidungen und offene Fragen

- **Entschieden: öffentlich, ohne Zugangsschutz.** Öffentliches Repo,
  öffentliche Seite, nur `robots.txt` und `noindex` gegen Suchmaschinen. Flo
  hat abgewogen: die Inhalte sind Nachrichten, die Watchlist ist klein und
  uninteressant, der Link wird nicht weitergegeben. Ein zufälliger Fund wäre
  ihm egal.
- **Verworfen: Cloudflare Access.** `floachleitner.com` liegt bei All-Inkl,
  nicht bei Cloudflare — der Weg hieße Nameserver umstellen.
- **Verworfen: privates Repo mit GitHub Pro.** Kostet 4 $/Monat für einen
  Schutz, den Flo nicht braucht.
- **Verworfen: nur lokal.** Nimmt die Handy-Lesbarkeit.
- **Daraus folgt eine Regel, nicht aus Scham, sondern aus Mechanik:** In einem
  öffentlichen Repo ist auch die Git-Historie öffentlich, und Gelöschtes bleibt
  dort lesbar. Was einmal drin war, ist drin. Deshalb kommen Stückzahlen,
  Beträge und Einstandskurse gar nicht erst hinein.
- **Entschieden: Ein Hub-Design für alle, Ausreißer im Einzelfall erlaubt.**
- **Verworfen: Pro Bericht ein eigenes komplettes HTML.** Fünf Designs, die
  auseinanderlaufen und einzeln mobil repariert werden müssten.
- **Entschieden: Berichte gehen direkt live**, ohne Freigabeschritt.
- **Entschieden: Bitcoin und Finanzen sind zwei getrennte Berichte** — sie
  ticken unterschiedlich schnell.
- **Entschieden: Weltlage ist ein Bericht mit vier Rubriken**, Ukraine bekommt
  keinen eigenen täglichen Bericht.
- **Entschieden: Tägliche Berichte sind um 7:00 fertig.**
- **Entschieden: Das Design ist der `Artefakt`-Entwurf**, ausgewertet und
  festgehalten. Damit ist auch das Datenmodell vorgegeben, das ein
  Recherche-Lauf liefern muss.
- **Verworfen: eine Akzentfarbe je Thema.** Der Entwurf trennt Ressorts über
  Textlabels; eine zweite Farbdimension würde die Ruhe zerstören, die der
  ganze Look ausmacht.
- **Entschieden: alle fünf Themen sind ab Tag eins sichtbar**, vier davon
  zunächst als „Entwurf" mit Bauplan statt Inhalt. Der Bereich existiert, bevor
  er liefert.
- **Entschieden: die Läufe versuchen wir in der Cloud.** Geplante Cloud-Agenten
  von Claude Code, am GitHub-Repo hängend. Wird beim Aufsetzen praktisch
  geprüft; sagt es nein, ist ein lokaler Timer auf dem Mac der Rückfallweg.
- **Entschieden: ein Briefing je Ressort**, als Markdown, mit den Quellen als
  erster inhaltlicher Sektion.
- [ ] **Offen, blockiert aber nichts:** Die zwei Listen — etwa 20 Aktien (Name
  reicht, Ticker hilft) und die Coins. Ohne sie bleiben Krypto und Finanzen im
  Status „Entwurf" und zeigen ihren Bauplan; alles andere läuft.
- [ ] **Offen, blockiert aber nichts:** Die Reiseliste (Ziel + Zeitraum je
  geplanter Reise). Gleiche Regel: ohne sie bleibt Reisen ein Entwurf.

## Annahmen

- ⚠️ Alle Berichte sind auf Deutsch, im Ton des bestehenden
  Generative-Media-Berichts: knapp, keine Floskeln, nichts Erfundenes,
  Unsicheres wird als unsicher markiert oder weggelassen.
- ⚠️ Ausgaben bleiben dauerhaft im Archiv; nichts wird automatisch gelöscht.
- ⚠️ Die Domain `floachleitner.com` gehört Flo, DNS-Zugang vorhanden.
- ⚠️ Das bestehende `generative-media-weekly`-Artefakt wird nicht migriert — der
  erste Lauf startet als frische Baseline.
- ⚠️ Die Aktien-Watchlist wird wöchentlich berichtet, nicht täglich; täglich
  läuft nur Bitcoin/Krypto.
- ⚠️ Stufe 1 ist fertig, wenn die Seite steht und die vier Berichte automatisch
  liefern — am Desktop und am Handy gut lesbar.
