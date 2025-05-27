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


# 2. Aufgabenstellungen zur Programmierübung 2
## Funktionsumfang(Lastenheft)
-Die App ermöglicht die Analyse von EKG-Daten
-Datei werden folgende Use Case unterstützt:

![alt text](../../docs/uml_usecase.svg)

## Funktionale Anforderungen
Als Nutzer:in möchte ich eine Versuchsperson auswählen und die relevanten Daten angezeigt bekommen
Als Nutzer:in möchte ich mir das Bild einer Versuchsperson anzeigen lassen, um mich zu vergewissern, dass ich die richtige Person anzeige (Termin 2)
Als Nutzer:in möchte ich die zu einer Versuchsperson gehörenden EKG Datensätze auswählen können (sofern es mehrere gibt)
Als Nutzer:in möchte ich die EKG-Daten einer Versuchsperson als Grafik anzeigen lassen (Termin 3)
Als Nutzer:in möchte ich mir den Durchschnittspuls einer Versuchsperson als Zahl anzeigen lassen (Termin 4)

## Ablaufdiagramm
Zeigt den Ablauf
[![](https://mermaid.ink/img/pako:eNp9ks9y0zAQxl9FsyeYiTNJQ_GfAww0pQcuHHoi7mSEvbFMZcmzkghtJm_Dm_BirJ3GNi2DTl7t99vv044PUNgSIYMoinLja68xEx-M1A8OxfXnm9z0jZ22-0JJ8uL2Y24EH-e5eiVeTyoRRe8caiz8NjikzRey36QpayNkcPvfv5RGc_ekH2UdJbSV5QvIPGJdDcgg6QEl3daj8wfOGK2lRyN-WFJMonl_PBFnTRSJ75KpIR3eV5tbbrzMNUEMcoYOMrYHPiHr6HmqcWIXqyDkKNuKZLu5Ibmr7wWS86hHh9O0_g2TJZx6E7zfpbL7v2b939s2bWBa0WYdqFCuUKb23rVBu-6hhHwxsKN6cPo3-MzyJOzjI-96_AHOWactmEFFdQmZp4AzaJAa2ZVw6KAcvMIGc8j4s8SdDNrnkJsjY600X61tziTZUCnIdlI7rkJb8prWtWS_ZrilzpSubDAestWby34IZAf4CdnFMp5fLFereJmkb5PlgpsPLErmKZ84TRdJGsfx5XEGj73rYp5w9Qdcsgzd?type=png)](https://mermaid.live/edit#pako:eNp9ks9y0zAQxl9FsyeYiTNJQ_GfAww0pQcuHHoi7mSEvbFMZcmzkghtJm_Dm_BirJ3GNi2DTl7t99vv044PUNgSIYMoinLja68xEx-M1A8OxfXnm9z0jZ22-0JJ8uL2Y24EH-e5eiVeTyoRRe8caiz8NjikzRey36QpayNkcPvfv5RGc_ekH2UdJbSV5QvIPGJdDcgg6QEl3daj8wfOGK2lRyN-WFJMonl_PBFnTRSJ75KpIR3eV5tbbrzMNUEMcoYOMrYHPiHr6HmqcWIXqyDkKNuKZLu5Ibmr7wWS86hHh9O0_g2TJZx6E7zfpbL7v2b939s2bWBa0WYdqFCuUKb23rVBu-6hhHwxsKN6cPo3-MzyJOzjI-96_AHOWactmEFFdQmZp4AzaJAa2ZVw6KAcvMIGc8j4s8SdDNrnkJsjY600X61tziTZUCnIdlI7rkJb8prWtWS_ZrilzpSubDAestWby34IZAf4CdnFMp5fLFereJmkb5PlgpsPLErmKZ84TRdJGsfx5XEGj73rYp5w9Qdcsgzd)

## Anwendung der App

1. Sicherstellen dass virtuelle Umgebung aktiviert ist ".venv/Scripts/active"
2. Abhängigkeitvinstallieren "streamlit run main.py"
