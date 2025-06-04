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

## EKG - Analyse App
- Die App ermöglicht die Analyse von EKG-Daten
- Dabei können folgende Use Cases unterstützt werden
![](docs/uml_usecase2.svg)

### Funktionale Anforderungen
- Als Nutzer:in möchte ich eine Versuchsperson auswählen und die relevanten Daten angezeigt bekommen
- Als Nutzer:in möchte ich mir das Bild einer Versuchsperson anzeigen lassen, um mich zu vergewissern, dass ich die richtige Person anzeige (Termin 2)
- Als Nutzer:in möchte ich die zu einer Versuchsperson gehörenden EKG Datensätze auswählen können (sofern es mehrere gibt)
- Als Nutzer:in möchte ich die EKG-Daten einer Versuchsperson als Grafik anzeigen lassen (Termin 3)
- Als Nutzer:in möchte ich mir den Durchschnittspuls einer Versuchsperson als Zahl anzeigen lassen (Termin 4)

## Flowchart

![](https://mermaid.ink/img/pako:eNp9kk1u2zAQha9CcJUCliHLMi1p0aKt2yy6ySKrWIXBSGNRDUUK_KmbGL5NbtKLdSTXkuME4Uqjed-8xwH3tNAl0IwGQZArVzsJGfmsuHy0QL79uM5V39hKvSsEN47cfskVwWMdVlfkw1lFguCjBQmF23gLZn1j9D1XZa0I93b391lIUD__60dZRxGpefkKUk9QVwMySHpAcLtxYN0eMwYr7kCR39oIJEF9OhyJkyYIyC-O1JAOHqr1LTZe5zpDFGCGDlK6B74D6sxlqnFiF6swgFE2leHt-trwbf1AwFgHcnQ4TuvvcLaEY-8M73cp9O7FrPe9ddN6pIVZr7wphC2Eqp2zrZe2u6gB_DGwo3pwehu8sDwK-_iAux4fwCnrZYtOaGXqkmbOeJjQBkzDu5Luu25OnYAGcprhZwlb7qXLaa4OiLVc3WndnEijfSVotuXSYuXbEle1qjl6jpLO13zVXjmaRawfQbM9_YNVGE_jRZpG4SJJwnkaT-gjzWYRmyYJY4vlMp2xaJbMDxP61JuGU8bmIZsnMYsSFkfL9PAPH28QLw?type=png)

## Anwendung der App
1. Sicherstellen dass virtuelle Umgebung aktiviert ist `.venv/Scripts/activate´
2. Abhängigikeiten installieren `streamlit run main.py´


## Beispielbilder der App

![](figures\Screenshot_2025-06-04_55027.png)
![](figures\Screenshot_2025-06-04_155103.png)
![](figures\Screenshot_2025-06-04_155126.png)

