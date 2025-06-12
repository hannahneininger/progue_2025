# wenn man etwas verändert muss man in VSC nur STRG s drücken und dann wird es automatisch aktualisiert in Streamlitimport streamlit as st
import os
# füge den Pfad zum src-Ordner hinzu, damit die Module importiert werden können
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
import pandas as pd
from src.analyze_activity_data import create_table
from src.analyze_activity_data import power_stats_per_zone
from src.read_data import get_person_names, get_person_image_by_name




if  "selected_person" not in st.session_state:
    st.session_state.selected_person = "Name 1"

st.write("# EKG App")	

st.write("## Zweite Überschrift")
st.write("This is a Streamlit app to demonstrate the setup.")


st.session_state.selected_person = st.selectbox("Wähle eine Versuchsperson", options= get_person_names())

#st.write(st.session_state.selected_person)

#st.write(st.session_state)



# Anzeigen eines Bilds mit Caption
st.image(get_person_image_by_name(st.session_state.selected_person), caption=st.session_state.selected_person)

#print(create_table())

st.dataframe(create_table())


# heart_rate_power_curve
st.write("# Herzfrequenz-Leistungs-Kurve")
st.image("figures/heart_rate_power_curve.png", caption="Herzfrequenz-Leistungs-Kurve")
# Anzeigen der Tabelle mit Mittelwert und Maximalwert der Leistung pro Zone
st.write("# Leistung pro Zone")
st.dataframe(power_stats_per_zone())

st.write('# Leistungskurve II')
st.image('figures/Leistungskurve_II.png')