#!/usr/bin/env bash
#
# pruef-historie.sh -- sucht in der gesamten Git-Historie und im Arbeitsstand
# nach Depotdaten, die in ein oeffentliches Repo nicht hineingehoeren.
#
# WARUM
#   Das Repo ist oeffentlich, und Git-Historie laesst sich nicht sauber
#   zuruecknehmen: was einmal committet war, bleibt in geloeschten Staenden
#   lesbar. Deshalb wird vor dem ersten Push geprueft -- danach ist es zu spaet.
#
# WAS DAS SKRIPT PRUEFT
#   1. Historie: "git log -p --all" ueber alle Commits aller Branches,
#      inklusive geloeschter Zeilen und geloeschter Dateien. Ausgegeben wird
#      jede Treffer-Zeile mit Commit, Datum, Autor, Betreff und Datei.
#   2. Arbeitsstand: alle nicht ignorierten Dateien im Arbeitsverzeichnis,
#      auch die noch nicht committeten -- die kaemen beim naechsten Commit dazu.
#   Gesucht wird nach vier Mustern (Gross-/Kleinschreibung egal):
#     M1  Zahl vor einer Waehrung          -- Waehrungszeichen, EUR, USD, CHF, GBP
#     M2  Waehrung vor einer Zahl
#     M3  Zahl vor einer Stueck-Einheit    -- Stueck, Stk, Anteile, Aktien, Coins,
#                                             BTC, ETH, Sats
#     M4  Begriffe fuer Bestand und Einstand -- siehe Variable BEGRIFFE unten
#
# WAS DAS SKRIPT NICHT PRUEFT -- es ersetzt kein Nachdenken
#   - Ein Treffer ist noch kein Verstoss. Ein Preis in einer Nachricht, eine
#     Monatsgebuehr in einer Notiz oder ein Text, der die Regel selbst
#     beschreibt, sind Treffer und trotzdem harmlos. Was ein Treffer bedeutet,
#     entscheidet ein Mensch.
#   - Umgekehrt findet es Depotdaten nicht, die ohne Waehrung, ohne Einheit und
#     ohne Schluesselwort dastehen -- eine nackte Zahlenspalte in einer JSON,
#     ein Feldwert ohne Einheit, ein Screenshot, eine PDF, ein Binaerformat.
#     Binaerdateien werden im Arbeitsstand uebersprungen (grep -I).
#   - Es liest keine Bilder, keine Anhaenge, keine externen Dienste.
#   - Es prueft nichts, was nie im Repo war (GitHub-Secrets, Issues, Kommentare).
#   - Es prueft nur dieses Repo, nicht Forks oder schon gepushte Kopien.
#   - Es prueft sich selbst nicht: diese Datei muss die gesuchten Woerter im
#     Klartext enthalten und wuerde sonst dauerhaft auf sich selbst anschlagen.
#     Wer diese Datei aendert, sieht sie von Hand durch.
#   - Es aendert nichts: nur lesende Git-Kommandos, kein commit, kein push.
#
# AUFRUF
#   bash build/pruef-historie.sh                 # ganzes Repo
#   bash build/pruef-historie.sh ausgaben site   # nur diese Pfade
#
# EXIT-CODES
#   0  kein Treffer
#   1  mindestens ein Treffer -- Ausgabe von Hand durchsehen
#   2  Aufruffehler (kein Git-Repo o. ae.)

set -u

cd "$(dirname "$0")/.." || exit 2

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "FEHLER: kein Git-Repo unter $(pwd)" >&2
  exit 2
fi

SELBST='build/pruef-historie.sh'

# Muster, kleingeschrieben; geprueft wird gegen eine kleingeschriebene Kopie
# der Zeile. Auf ein Waehrungskuerzel darf kein Buchstabe folgen, sonst wuerde
# "Europa" als "eur" durchgehen.
WAEHRUNG='(€|eur|euro|usd|chf|gbp|\$)'
EINHEIT='(stück|stueck|stk|anteile|anteilen|aktien|coins|coin|btc|eth|sats)'
BEGRIFFE='(einstand|einstandskurs|einstandspreis|kaufkurs|durchschnittskurs|depotwert|depotstand|depotbestand|portfoliowert|buchwert|positionsgröße|positionsgroesse|stückzahl|stueckzahl|kontostand|gewinn/verlust in euro)'

M1="[0-9][0-9.,]*[ ]?${WAEHRUNG}([^a-zäöüß]|\$)"
M2="${WAEHRUNG}[ ]?[0-9]"
M3="[0-9][0-9.,]*[ ]?${EINHEIT}([^a-zäöüß]|\$)"
M4="${BEGRIFFE}"

# Wird per Umgebungsvariable an awk gereicht -- "awk -v" wuerde die
# Backslash-Escapes im Muster noch einmal aufloesen und es kaputtmachen.
export MUSTER="${M1}|${M2}|${M3}|${M4}"

# Pfade: ohne Argument das ganze Repo, das Pruefskript selbst ausgenommen.
if [ "$#" -eq 0 ]; then
  set -- '.'
fi
PFADE=("$@" ":(exclude)${SELBST}")

trefferzahl=0

# --------------------------------------------------------------------------- #
echo "== 1. Git-Historie (git log -p --all, alle Commits, alle Branches) =="
echo

historie=$(
  git log --all --no-color --date=short -p \
      --format='%x01%h%x01%ad%x01%an%x01%s' -- "${PFADE[@]}" 2>/dev/null |
  awk '
    BEGIN { muster = ENVIRON["MUSTER"] }
    /^\001/ {
      n = split($0, f, "\001")
      commit = f[2]; datum = f[3]; autor = f[4]; betreff = f[5]
      for (i = 6; i <= n; i++) betreff = betreff "\001" f[i]
      datei = "?"
      next
    }
    /^diff --git / {
      datei = $0
      sub(/^diff --git a\/.* b\//, "", datei)
      next
    }
    /^(\+\+\+|---)/ { next }
    /^[+-]/ {
      zeile = $0
      if (tolower(zeile) ~ muster) {
        printf "Commit %s  %s  %s  %s\n", commit, datum, autor, betreff
        printf "  Datei: %s\n", datei
        printf "  %s\n\n", zeile
      }
    }
  '
)

if [ -n "$historie" ]; then
  printf '%s\n' "$historie"
  h=$(printf '%s\n' "$historie" | grep -c '^Commit ')
  trefferzahl=$((trefferzahl + h))
  echo "-> $h Trefferzeile(n) in der Historie."
else
  echo "Keine Treffer in der Historie."
fi

echo
# --------------------------------------------------------------------------- #
echo "== 2. Arbeitsstand (verfolgte + noch nicht committete Dateien) =="
echo

arbeit=$(
  git ls-files --cached --others --exclude-standard -z -- "${PFADE[@]}" 2>/dev/null |
  xargs -0 grep -I -n -i -E -e "$MUSTER" -- 2>/dev/null
)

if [ -n "$arbeit" ]; then
  printf '%s\n' "$arbeit"
  a=$(printf '%s\n' "$arbeit" | grep -c '')
  trefferzahl=$((trefferzahl + a))
  echo
  echo "-> $a Trefferzeile(n) im Arbeitsstand."
else
  echo "Keine Treffer im Arbeitsstand."
fi

echo
echo "Ausgenommen von beiden Durchlaeufen: ${SELBST} (siehe Skriptkopf)."
echo "======================================================================"
if [ "$trefferzahl" -eq 0 ]; then
  echo "ERGEBNIS: kein Treffer. (Heisst nicht automatisch sauber -- siehe"
  echo "          Abschnitt 'WAS DAS SKRIPT NICHT PRUEFT' im Skriptkopf.)"
  exit 0
fi

echo "ERGEBNIS: $trefferzahl Trefferzeile(n). Jede Zeile von Hand beurteilen:"
echo "          echte Depotdaten -- oder harmlos?"
exit 1
