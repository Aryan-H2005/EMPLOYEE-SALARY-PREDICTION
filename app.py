import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Salary Prediction", layout="wide")

st.title("💼 Employee Salary Prediction System")

st.write("Predict employee annual salary based on experience, department, and work factors.")

# Sidebar inputs
st.header("Enter Employee Details")

gender = st.selectbox("Gender", ["Male", "Female"])
years = st.slider("Years of Experience", 0, 40, 5)
job_rate = st.slider("Job Performance Rate", 1, 5, 3)
sick = st.number_input("Sick Leaves", 0, 50, 2)
unpaid = st.number_input("Unpaid Leaves", 0, 50, 0)
overtime = st.slider("Overtime Hours", 0, 200, 20)

department = st.selectbox("Department", ["IT", "HR", "Finance", "Sales"])
country = st.selectbox("Country", ["India", "USA", "UK", "Germany"])
center = st.selectbox("Center", ["Pune", "Mumbai", "New York", "London"])

# Create input dataframe
input_data = pd.DataFrame({
    "Gender": [gender],
    "Years": [years],
    "Job Rate": [job_rate],
    "Sick Leaves": [sick],
    "Unpaid Leaves": [unpaid],
    "Overtime Hours": [overtime],
    "Department": [department],
    "Country": [country],
    "Center": [center]
})

# One-hot encoding
input_data = pd.get_dummies(input_data)

# Match training columns
for col in features:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[features]

# Scaling
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(input_scaled)[0]

    st.subheader(f"💰 Predicted Annual Salary: ₹ {round(prediction, 2)}")

    # Business insights
    st.write("### 📊 Insights")
    if overtime > 50:
        st.success("High overtime contribution increases salary.")
    if job_rate >= 4:
        st.success("Strong performance positively impacts salary.")
    if years > 10:
        st.success("Experience is a major salary driver.")