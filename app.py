import streamlit as st
import pandas as pd
import pickle

# -----------------------------------
# Load Model
# -----------------------------------

with open('svc.pkl', 'rb') as file:
    model = pickle.load(file)

# -----------------------------------
# Load Scaler
# -----------------------------------

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# -----------------------------------
# Streamlit Title
# -----------------------------------

st.title("Student Grade Prediction System")

st.write("Enter student details to predict grade")

# -----------------------------------
# Input Fields
# -----------------------------------

# Sex
sex_option = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

sex = 1 if sex_option == "Male" else 0

# Scholarship
scholarship = st.number_input(
    "Scholarship",
    min_value=0.0,
    max_value=100.0,
    value=0.0
)

# Additional Work
additional_work_option = st.selectbox(
    "Additional Work",
    ["Yes", "No"]
)

additional_work = 1 if additional_work_option == "Yes" else 0

# Sports Activity
sports_option = st.selectbox(
    "Sports Activity",
    ["Yes", "No"]
)

sports_activity = 1 if sports_option == "Yes" else 0

# Transportation
transport_option = st.selectbox(
    "Transportation",
    [0, 1]
)

transportation = transport_option

# Weekly Study Hours
weekly_study_hours = st.number_input(
    "Weekly Study Hours",
    min_value=0.0,
    max_value=100.0,
    value=5.0
)

# Reading
reading_option = st.selectbox(
    "Reading",
    ["Yes", "No"]
)

reading = 1 if reading_option == "Yes" else 0

# Notes
notes_option = st.selectbox(
    "Taking Notes",
    ["Yes", "No"]
)

notes = 1 if notes_option == "Yes" else 0

# Listening in Class
listening_option = st.selectbox(
    "Listening in Class",
    ["Yes", "No"]
)

listening_in_class = 1 if listening_option == "Yes" else 0

# Project Work
project_option = st.selectbox(
    "Project Work",
    ["Yes", "No"]
)

project_work = 1 if project_option == "Yes" else 0

# -----------------------------------
# Age Group
# -----------------------------------

age = st.selectbox(
    "Student Age",
    ["18", "19-22", "23-27"]
)

student_age_18 = 1 if age == "18" else 0
student_age_19_22 = 1 if age == "19-22" else 0
student_age_23_27 = 1 if age == "23-27" else 0

# -----------------------------------
# High School Type
# -----------------------------------

high_school = st.selectbox(
    "High School Type",
    ["Other", "Private", "State"]
)

high_school_other = 1 if high_school == "Other" else 0
high_school_private = 1 if high_school == "Private" else 0
high_school_state = 1 if high_school == "State" else 0

# -----------------------------------
# Attendance
# -----------------------------------

attendance = st.selectbox(
    "Attendance",
    ["Always", "Never", "Sometimes"]
)

attendance_always = 1 if attendance == "Always" else 0
attendance_never = 1 if attendance == "Never" else 0
attendance_sometimes = 1 if attendance == "Sometimes" else 0

# -----------------------------------
# Prediction Button
# -----------------------------------

if st.button("Predict Grade"):

    # Create dataframe
    input_data = pd.DataFrame({

        'Sex': [sex],
        'Scholarship': [scholarship],
        'Additional_Work': [additional_work],
        'Sports_activity': [sports_activity],
        'Transportation': [transportation],
        'Weekly_Study_Hours': [weekly_study_hours],
        'Reading': [reading],
        'Notes': [notes],
        'Listening_in_Class': [listening_in_class],
        'Project_work': [project_work],

        'Student_Age_18': [student_age_18],
        'Student_Age_19-22': [student_age_19_22],
        'Student_Age_23-27': [student_age_23_27],

        'High_School_Type_Other': [high_school_other],
        'High_School_Type_Private': [high_school_private],
        'High_School_Type_State': [high_school_state],

        'Attendance_Always': [attendance_always],
        'Attendance_Never': [attendance_never],
        'Attendance_Sometimes': [attendance_sometimes]

    })

    # -----------------------------------
    # Scale Numerical Columns
    # -----------------------------------

    scale_cols = [
        'Scholarship',
        
    ]

    input_data[scale_cols] = scaler.transform(
        input_data[scale_cols]
    )

    # -----------------------------------
    # Prediction
    # -----------------------------------

    prediction = model.predict(input_data)[0]

    # -----------------------------------
    # Reverse Grade Mapping
    # -----------------------------------

    grade_mapping = {

        0: 'Fail',
        1: 'DD',
        2: 'DC',
        3: 'CC',
        4: 'CB',
        5: 'BB',
        6: 'BA',
        7: 'AA'

    }

    predicted_grade = grade_mapping[prediction]

    # -----------------------------------
    # Output
    # -----------------------------------

    st.success(f"Predicted Grade: {predicted_grade}")