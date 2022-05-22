import streamlit as st
from back import load_form_fields, get_trip_fare, trim

st.title("Prédiction du prix de la course de taxis à New York")
st.subheader("Par Enzo Risbetz et Charles-Meldhine Madi Mnemoi")

with st.form("Submit Form"):
    variables = {}
    form_fields = load_form_fields()

    columns = st.columns(2)
    with columns[0]:
        variables["PULocationLabel"] = st.selectbox(label="Lieu de départ", options=form_fields["Lieu de départ"])
        variables["DOLocationLabel"] = st.selectbox(label="Lieu d'arrivée", options=form_fields["Lieu d'arrivée"])
        variables["date"] = [st.date_input(label="Date prévue de la course")]
        variables["time"] = [st.time_input("Heure prévue de la course")]
    with columns[1]:
        variables["passenger_count"] = [st.number_input("Nombre de passagers", min_value=1, max_value=6)]
        variables["trip_distance"] = [st.number_input("Longueur du trajet (en km)", min_value=0.1, 
                                        max_value=100.0*1.609, step=0.5, value=1.0) / 1.609]
        variables["payment_type"] = st.selectbox(label="Type de paiement", options=form_fields["Type de paiement"])
        variables["VendorID"] = st.selectbox(label="Société de taxis", options=form_fields["Société de taxis"])
        
        
    submitted = st.form_submit_button("Prédire le prix de la course")
    if submitted:
        st.write(f"Votre trajet coûtera environ {get_trip_fare(variables):.2f} $.")