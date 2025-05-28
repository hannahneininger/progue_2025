import streamlit as st
from PIL import Image

from src.read_data import get_person_names, get_person_data, get_person_data_by_name, get_person_image_by_name
from src.analyze_activity_data import dataplot, dataframe

if 'select_person' not in st.session_state:
    st.session_state.select_person = None


st.write("# Hello, Streamlit!")
st.write("## Zweite Ueberschrift")
    
st.write("This is a simple Streamlit app to demonstrate the setup.")


st.session_state.select_person = st.selectbox("Wähle eine Person", options=get_person_names())

st.write(st.session_state.select_person)
image = Image.open(get_person_image_by_name(st.session_state.select_person))

# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.select_person)
   

#Anzeigen analysed data
st.plotly_chart(dataplot()) 

# Anzeigen wie lang in einzelen Zonen
   
zone_minutes = (dataframe["Zone"].value_counts() / 60)
zone_minutes.index.name = "Zone"
zone_minutes.name = "Dauer (Minuten)"

# Durchschnittliche Power pro Zone berechnen
zone_power = dataframe.groupby("Zone")["PowerOriginal"].mean()

# Zusammenführen in ein DataFrame
zone_stats = zone_minutes.to_frame().join(zone_power.rename("Ø Power (W)"))

st.dataframe(zone_stats)

   