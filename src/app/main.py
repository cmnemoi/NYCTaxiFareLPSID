from os import getenv

import streamlit as st
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key=getenv("GOOGLE_MAPS_KEY"))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

st.write("Hello, World!")
st.write(directions_result)