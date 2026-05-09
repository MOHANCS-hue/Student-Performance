# ==========================================
# STUDENT GRADE PREDICTION SYSTEM
# STREAMLIT APP
# ==========================================

import streamlit as st
import pandas as pd
import joblib


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load("XGBoost.pkl")


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Student Grade Predictor",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("🎓 Student Grade Prediction System")

st.write(
    "Enter student details to predict the Grade Class"
)


# ==========================================
# USER INPUTS
# ==========================================

Age = st.slider(
    "Age",
    15,
    18,
    16
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Ethnicity = st.selectbox(
    "Ethnicity",
    ["Group 0", "Group 1", "Group 2", "Group 3"]
)

ParentalEducation = st.selectbox(
    "Parental Education",
    [
        "None",
        "High School",
        "College",
        "Bachelor",
        "Higher"
    ]
)

StudyTimeWeekly = st.slider(
    "Study Time Weekly (Hours)",
    0.0,
    25.0,
    10.0
)

Absences = st.slider(
    "Number of Absences",
    0,
    30,
    5
)

Tutoring = st.selectbox(
    "Tutoring",
    ["No", "Yes"]
)

ParentalSupport = st.selectbox(
    "Parental Support",
    [
        "Very Low",
        "Low",
        "Moderate",
        "High",
        "Very High"
    ]
)

Extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

Sports = st.selectbox(
    "Sports Participation",
    ["No", "Yes"]
)

Music = st.selectbox(
    "Music Participation",
    ["No", "Yes"]
)

Volunteering = st.selectbox(
    "Community Volunteering",
    ["No", "Yes"]
)


# ==========================================
# ENCODING INPUTS
# ==========================================

# Gender Encoding
Gender = 1 if Gender == "Male" else 0

# Ethnicity Encoding
ethnicity_map = {
    "Group 0": 0,
    "Group 1": 1,
    "Group 2": 2,
    "Group 3": 3
}

Ethnicity = ethnicity_map[Ethnicity]

# Parent Education Encoding
education_map = {
    "None": 0,
    "High School": 1,
    "College": 2,
    "Bachelor": 3,
    "Higher": 4
}

ParentalEducation = education_map[
    ParentalEducation
]

# Tutoring Encoding
Tutoring = 1 if Tutoring == "Yes" else 0

# Parent Support Encoding
support_map = {
    "Very Low": 0,
    "Low": 1,
    "Moderate": 2,
    "High": 3,
    "Very High": 4
}

ParentalSupport = support_map[
    ParentalSupport
]

# Binary Feature Encoding
Extracurricular = (
    1 if Extracurricular == "Yes"
    else 0
)

Sports = 1 if Sports == "Yes" else 0

Music = 1 if Music == "Yes" else 0

Volunteering = (
    1 if Volunteering == "Yes"
    else 0
)


# ==========================================
# PREDICTION
# ==========================================

if st.button("Predict Grade"):

    # Create dataframe
    input_data = pd.DataFrame([[
        Age,
        Gender,
        Ethnicity,
        ParentalEducation,
        StudyTimeWeekly,
        Absences,
        Tutoring,
        ParentalSupport,
        Extracurricular,
        Sports,
        Music,
        Volunteering
    ]], columns=[
        'Age',
        'Gender',
        'Ethnicity',
        'ParentalEducation',
        'StudyTimeWeekly',
        'Absences',
        'Tutoring',
        'ParentalSupport',
        'Extracurricular',
        'Sports',
        'Music',
        'Volunteering'
    ])

    # Prediction
    prediction = model.predict(input_data)[0]

    # ======================================
    # DISPLAY RESULT
    # ======================================

    st.subheader("Prediction Result")

    if prediction == 0:
        st.success(
            "Grade Class: A (Excellent)"
        )

    elif prediction == 1:
        st.success(
            "Grade Class: B (Very Good)"
        )

    elif prediction == 2:
        st.success(
            "Grade Class: C (Good)"
        )

    elif prediction == 3:
        st.warning(
            "Grade Class: D (Average)"
        )

    else:
        st.error(
            "Grade Class: F (Poor)"
        )


# ==========================================
# FOOTER
# ==========================================

st.write("---")

st.caption(
    "AI-Based Student Grade Prediction System using XGBoost"
)