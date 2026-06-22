import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("XGB.pkl")
columns = joblib.load("columns.pkl")

# Page Config
st.set_page_config(
    page_title="HeartAI",
    page_icon="❤️",
    layout="centered"
)

# Title
st.title("❤️ Heart Stock Risk Predictor")
st.markdown("Provide the following details to predict the risk.")

# User Inputs
age = st.slider("Age", 18, 100, 40)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=250,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dL)",
    min_value=0,
    max_value=700,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Max Heart Rate",
    60,
    220,
    150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    0.0,
    6.0,
    1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

# Prediction Button
if st.button("Predict"):

    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "RestingECG_" + resting_ecg: 1,
        "ExerciseAngina_" + exercise_angina: 1,
        "ST_Slope_" + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Add missing columns
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Arrange columns in training order
    input_df = input_df[columns]

    try:
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.error("⚠️ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")

    except Exception as e:
        st.error(f"Error: {e}")