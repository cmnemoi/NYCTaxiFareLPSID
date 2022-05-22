import streamlit as st
from back import *


st.title("Estimation du prix d'une course de taxis à New York")
st.subheader("Par Enzo Risbetz et Charles-Meldhine Madi Mnemoi")

with st.form("Submit Form"):
    fields = {}
    form_fields = load_form_fields()

    columns = st.columns(2)
    with columns[0]:
        fields["PULocationLabel"] = st.selectbox(label="Lieu de départ", options=form_fields["Lieu de départ"])
        fields["DOLocationLabel"] = st.selectbox(label="Lieu d'arrivée", options=form_fields["Lieu d'arrivée"])
        fields["date"] = [st.date_input(label="Date prévue de la course")]
    with columns[1]:
        fields["passenger_count"] = [st.number_input("Nombre de passagers", min_value=1, max_value=6)]
        fields["payment_type"] = st.selectbox(label="Type de paiement", options=form_fields["Type de paiement"])
        fields["VendorID"] = st.selectbox(label="Société de taxis", options=form_fields["Société de taxis"])

    
    fields["time"] = [st.time_input("Heure prévue de la course")]
        
    submitted = st.form_submit_button("Calculer le prix de la course")
    if submitted:
        trip_distance = get_trip_distance(fields["PULocationLabel"], 
                fields["DOLocationLabel"])
        
        fields["trip_distance"] = 0.1 if trip_distance < 0.1 else trip_distance
        
        st.write("Votre trajet de {:.2f}km coûtera environ {:.2f} $."
                .format(fields["trip_distance"], get_trip_fare(fields)))