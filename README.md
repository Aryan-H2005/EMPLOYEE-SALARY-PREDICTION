# 💼 Employee Salary Prediction System
## 📌 Problem Statement

In large organizations operating across multiple departments, countries, and business centers, determining fair and competitive employee compensation is a complex challenge. Salary decisions depend on multiple factors such as experience, department, job performance, location, and workload.

Traditional compensation benchmarking is often manual and subjective, leading to:

Salary inconsistencies

Pay gaps across departments

Budget inefficiencies

Limited transparency in compensation decisions

This project aims to build a machine learning-based salary prediction system that estimates an employee’s annual salary based on professional and organizational attributes.

## 🏭 Industry Problem

Organizations face several real-world compensation challenges:

🔹 1. Salary Standardization

Ensuring employees with similar experience and roles are compensated fairly.

🔹 2. Budget Planning

HR teams must forecast salary budgets for upcoming hiring cycles.

🔹 3. Compensation Benchmarking

Companies need data-driven salary estimation to stay competitive in the market.

🔹 4. Detecting Salary Anomalies

Identifying overpaid or underpaid employees compared to similar profiles.

Manual methods are slow, inconsistent, and not scalable.
A predictive model enables automated and objective compensation analysis.

## 🎯 Project Objective

The objective of this project is to:

Perform exploratory data analysis on employee data

Engineer meaningful features such as tenure/experience

Build a regression model to predict annual salary

Evaluate model performance using R², MAE, and RMSE

Deploy the model using Streamlit for real-time predictions

## 📊 Dataset Description

The dataset contains employee-level information including:

Gender

Start Date

Years of Experience

Department

Country

Center

Job Performance Rate

Sick Leaves

Unpaid Leaves

Overtime Hours

Monthly Salary

Annual Salary (Target Variable)

## 🧠 Approach
1️⃣ Data Cleaning

Removed irrelevant columns (ID, Names)

Handled missing values

Converted Start Date to Experience feature

2️⃣ Feature Engineering

Created Experience from Start Date

Generated interaction features (Experience × Overtime)

Encoded categorical variables using One-Hot Encoding

3️⃣ Model Building

Used Random Forest Regressor

Split data into training and testing sets

Scaled numerical features

4️⃣ Model Evaluation

R² Score

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

5️⃣ Deployment

Saved model using joblib

Built interactive Streamlit web application

Enabled real-time salary prediction

## 📈 Results

Built an end-to-end regression model

Identified key salary drivers such as experience and department

Developed an interactive HR decision-support system

## 💻 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Matplotlib & Seaborn

Streamlit

Joblib

## 🚀 Deployment

The model is deployed using Streamlit, allowing HR teams to:

Enter employee details

Get predicted annual salary

Analyze influencing factors

## Run locally:

streamlit run app.py
