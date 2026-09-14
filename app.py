import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .result-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 700;
    }

    .result-text {
        font-size: 18px;
        margin-top: 10px;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model = joblib.load("random_forest_model.pkl")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">❤️ Heart Disease Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Heart Disease Prediction'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# PATIENT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">👤 Patient Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMN 1
# ============================================================

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina",
            "Atypical Angina",
            "Non-anginal Pain",
            "Asymptomatic"
        ]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure (mmHg)",
        min_value=50,
        max_value=250,
        value=120,
        step=1
    )


# ============================================================
# COLUMN 2
# ============================================================

with col2:

    cholesterol = st.number_input(
        "Cholesterol (mg/dl)",
        min_value=0,
        max_value=700,
        value=200,
        step=1
    )

    fasting_blood_sugar = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        [
            "Normal",
            "ST-T Wave Abnormality",
            "Left Ventricular Hypertrophy"
        ]
    )

    max_heart_rate = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150,
        step=1
    )


# ============================================================
# COLUMN 3
# ============================================================

with col3:

    exercise_angina = st.selectbox(
        "Exercise-Induced Angina",
        ["No", "Yes"]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=-5.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    st_slope = st.selectbox(
        "ST Slope",
        [
            "Up",
            "Flat",
            "Down"
        ]
    )


# ============================================================
# CONVERT USER INPUT TO DATASET VALUES
# ============================================================

sex_value = 1 if sex == "Male" else 0


chest_pain_mapping = {
    "Typical Angina": 1,
    "Atypical Angina": 2,
    "Non-anginal Pain": 3,
    "Asymptomatic": 4
}

chest_pain_value = chest_pain_mapping[chest_pain]


fasting_value = 1 if fasting_blood_sugar == "Yes" else 0


resting_ecg_mapping = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}

resting_ecg_value = resting_ecg_mapping[resting_ecg]


exercise_value = 1 if exercise_angina == "Yes" else 0


st_slope_mapping = {
    "Up": 1,
    "Flat": 2,
    "Down": 3
}

st_slope_value = st_slope_mapping[st_slope]


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({

    "age": [age],

    "sex": [sex_value],

    "chest pain type": [chest_pain_value],

    "resting bp s": [resting_bp],

    "cholesterol": [cholesterol],

    "fasting blood sugar": [fasting_value],

    "resting ecg": [resting_ecg_value],

    "max heart rate": [max_heart_rate],

    "exercise angina": [exercise_value],

    "oldpeak": [oldpeak],

    "ST slope": [st_slope_value]

})


# ============================================================
# PREDICTION
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">🔍 Prediction</div>',
    unsafe_allow_html=True
)

predict_button = st.button(
    "Predict Heart Disease",
    use_container_width=True,
    type="primary"
)


if predict_button:

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    # Probability of heart disease
    disease_probability = probability[1] * 100


    st.divider()

    st.subheader("Prediction Result")


    # ========================================================
    # POSITIVE PREDICTION
    # ========================================================

    if prediction == 1:

        st.error(
            "⚠️ Higher likelihood of heart disease"
        )

        st.metric(
            "Heart Disease Probability",
            f"{disease_probability:.2f}%"
        )


    # ========================================================
    # NEGATIVE PREDICTION
    # ========================================================

    else:

        st.success(
            "✅ Lower likelihood of heart disease"
        )

        st.metric(
            "Heart Disease Probability",
            f"{disease_probability:.2f}%"
        )


    # ========================================================
    # INPUT SUMMARY
    # ========================================================

    with st.expander("View Entered Patient Information"):

        display_data = pd.DataFrame({
            "Parameter": [
                "Age",
                "Sex",
                "Chest Pain Type",
                "Resting Blood Pressure",
                "Cholesterol",
                "Fasting Blood Sugar",
                "Resting ECG",
                "Maximum Heart Rate",
                "Exercise Angina",
                "Oldpeak",
                "ST Slope"
            ],

            "Value": [
                age,
                sex,
                chest_pain,
                f"{resting_bp} mmHg",
                f"{cholesterol} mg/dl",
                fasting_blood_sugar,
                resting_ecg,
                max_heart_rate,
                exercise_angina,
                oldpeak,
                st_slope
            ]
        })

        st.table(display_data)


# ============================================================
# DISCLAIMER
# ============================================================

st.divider()

st.caption(
    "Disclaimer: This application is an educational machine-learning "
    "project and is not intended to provide medical diagnosis or treatment."
)