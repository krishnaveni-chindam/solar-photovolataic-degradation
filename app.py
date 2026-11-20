import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Solar PV Power Prediction App")

st.write("Enter the following feature values:")

# Input fields
time = st.number_input(" Time")
pv_power = st.number_input("PV Power")
t_air = st.number_input("Air Temperature (T_air)")
g_h = st.number_input("Global Horizontal Irradiance (G_h)")
g_tilt = st.number_input("Tilt Irradiance (G_tilt)")
w_s = st.number_input("Wind Speed (W_s)")
w_d = st.number_input("Wind Direction (W_d)")

if st.button("Predict"):
    
    input_data = np.array([[time, pv_power, t_air, g_h, g_tilt, w_s, w_d]])
    
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")