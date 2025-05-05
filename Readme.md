# Programmierübung 2

## Ziel des Projektes

Hier werden erste Schritte mit PDM und git unternommen.

Außerdem wird eine Leistungskurve aus einer `csv`-Datei erstellt und geplottet.

## Umgang mit PDM

- Zum Ausetzen eines Projektes einmalig `pdm init`
- zum installieren eines Projektes nach dem clonen `pdm install`
- zum Hinzufügen eines Paketes 'pdm add `<packetname>`

- '.gitignore' legt fest, was von git ignoriert wird. Hier muss __immer vor__ dem ersten commit der Ordner `.venv/` drin stehen

## Nutzung des Projektes

Die Datei [`activity.csv`](activity.csv) enthält Leistungsdaten (z. B. Watt über Zeit).

Diese werden durch das Skript `power_curve.py` eingelesen, verarbeitet und als Power-Curve geplottet.


1. Repository klonen:
   ```bash
   git clone <REPO-URL>
   cd <Projektordner>

2. PDM-Projekt initialisieren (falls nicht vorhanden):

    pdm init

3. Abhängigkeiten installieren:

    pdm install

## Power-Curve Grafik:

![](https://raw.githubusercontent.com/hannahneininger/progue_2025/refs/heads/master/figures/power_curve.png)
