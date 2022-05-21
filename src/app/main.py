import streamlit as st
from back import load_form_fields, get_trip_fare, trim

st.title("Prédiction du prix de la course de taxis à New York")
st.subheader("Par Enzo Risbetz et Charles-Meldhine Madi Mnemoi")

with st.form("Submit Form"):
    form_fields = load_form_fields()
    variables = {}

    for field, field_content in form_fields.items():
        variables[field] = [st.selectbox(label=field, options=field_content)]
    
    variables["passenger_count"] = [st.number_input("Nombre de passagers", min_value=1, max_value=6)]
    variables["date"] = [st.date_input(label="Date prévue de la course")]
    variables["time"] = [st.time_input("Heure prévue de la course")]
    variables["trip_distance"] = [st.number_input("Longueur du trajet (en km)", min_value=0.1, max_value=100.0*1.609, step=0.5, value=1.0) / 1.609]

    submitted = st.form_submit_button("Prédire le prix de la course")
    if submitted:
        st.write(f"Votre trajet coûtera environ {get_trip_fare(variables):.2f} $.")