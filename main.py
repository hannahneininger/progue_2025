
import streamlit as st
from PIL import Image
from src.ekgdata import EKGdata
from src.person import Person
from src.analyze_activity_data import dataplot, dataframe

st.write("# Hello, Streamlit!")
st.write("## Zweite Ueberschrift")
st.write("Dies ist eine einfache Streamlit App mit Klassen.")

# Personen laden und Auswahl anzeigen
persons = Person.get_person_data()
person_names = Person.get_person_list(persons)
selected_name = st.selectbox("Wähle eine Person", options=person_names)
selected_person = next(p for p in persons if p.get_full_name() == selected_name)

# Bild anzeigen
st.image(Image.open(selected_person.picture_path), caption=selected_name)

# Maximalpuls-Eingabe (aus Klasse vorbelegen)
hr_max = st.number_input("Maximale Herzfrequenz", min_value=100, max_value=250, value=int(selected_person.hr_max), step=1)

# Analyse-Plot anzeigen (öffnet kein extra Fenster!)
st.plotly_chart(dataplot(hr_max))

# Zonenstatistik berechnen und anzeigen
zone_minutes = (dataframe["Zone"].value_counts() / 60)
zone_minutes.index.name = "Zone"
zone_minutes.name = "Dauer (Minuten)"

zone_power = dataframe.groupby("Zone")["PowerOriginal"].mean()
zone_stats = zone_minutes.to_frame().join(zone_power.rename("Ø Power (W)"))

st.write("## Zonenstatistik")
st.dataframe(zone_stats)

# Beispiel: Erstes EKG der ausgewählten Person verwenden
if selected_person.ekg_tests:
    ekg_obj = EKGdata(selected_person.ekg_tests[0])
    ekg_obj.find_peaks()
    hr_est = ekg_obj.estimate_hr()
    st.write(f"Geschätzte Herzfrequenz aus EKG: {hr_est:.1f} bpm")
else:
    st.write("Keine EKG-Daten für diese Person vorhanden.")
