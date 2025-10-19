import numpy as np
import pickle 
import streamlit as st

import os
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
loaded_model = pickle.load(open(model_path, "rb"))

def heart_disease_pred(input_data):
    input_data_as_numpy = np.asarray(input_data, dtype=np.float64)
    input_data_reshaped = input_data_as_numpy.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 1:
        return "The patient is likely to have heart disease."
    else:
        return "The patient is unlikely to have heart disease."
    

def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)

    Age = st.text_input("Enter your Age", key="age") 
    Gender = st.text_input("Enter your Gender (1 = Male, 0 = Female)", key="gender") 
    Chest_pain_type = st.text_input("Chest Pain Type", key="chest_pain") 
    Bp = st.text_input("Enter your Blood Pressure", key="bp")
    Cholesterol = st.text_input("Enter your Cholesterol Level", key="cholesterol")
    FBS_over_120 = st.text_input("Fasting Blood Sugar > 120 (1 = Yes, 0 = No)", key="fbs")
    EKG_results = st.text_input("EKG Results", key="ekg")
    Max_HR = st.text_input("Enter your Maximum Heart Rate", key="max_hr") 
    Exercise_angina = st.text_input("Exercise-Induced Angina (1 = Yes, 0 = No)", key="angina") 
    ST_depression = st.text_input("ST Depression", key="st_depression")
    Slope_of_ST = st.text_input("Slope of the ST Segment", key="st_slope")
    Number_of_vessels_fluro = st.text_input("Number of Major Vessels", key="vessels") 
    Thallium = st.text_input("Thallium Stress Test Result", key="thallium")

    diagnosis = ''
    
    if st.button("Get Heart Disease Prediction"):
        try:
            input_data = [float(Age), float(Gender), float(Chest_pain_type), float(Bp), float(Cholesterol),
                          float(FBS_over_120), float(EKG_results), float(Max_HR), float(Exercise_angina),
                          float(ST_depression), float(Slope_of_ST), float(Number_of_vessels_fluro), float(Thallium)]

            diagnosis = heart_disease_pred(input_data)
        except ValueError:
            diagnosis = "Please enter valid numerical inputs."

    st.success(diagnosis)

if __name__ == "__main__":
    main()
