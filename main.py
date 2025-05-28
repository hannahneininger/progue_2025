import streamlit as st

from src.read_data import get_person_data, get_image_by_name, get_person_names

# wir schreiben die userinterface mit python, aber eigentlich ist das peinlich


st.write('# Hello MTV')
st.write('## Welcome to my Crib!')
# Eine Überschrift der ersten Ebene
st.write("# EKG APP")
# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in selected_person gespeichert
st.session_state.selected_person = st.selectbox(
    'Versuchsperson',
    options = get_person_names(), key="sbVersuchsperson")


st.image(get_image_by_name(st.session_state.selected_person), caption= st.session_state.selected_person)


if __name__ == "__main__":
    person_data= get_person_data()
    #print(person_data)

