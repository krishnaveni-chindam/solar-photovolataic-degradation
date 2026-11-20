# Solar Photovoltaic Degradation Prediction

Predict solar panel power degradation over time using weather and panel data with Machine Learning.

## Features
- Predict power output degradation based on temperature, sunlight, and age
- Trained ML model using SolarTechLab Dataset
- Interactive prediction using Streamlit app
- Data analysis with Pandas

## Dataset
Dataset-SolarTechLab.csv contains temperature, irradiance, voltage, current, and power output data.

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Tech Used
Python, Pandas, Scikit-learn, Streamlit, Machine Learning

## Files
- app.py - Streamlit web app
- main.py - Model training code
- model.pkl - Trained ML model
- Dataset-SolarTechLab.csv - Dataset
