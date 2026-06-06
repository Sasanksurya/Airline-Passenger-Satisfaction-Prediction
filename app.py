import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="SkyWings AI",
    page_icon="✈️",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("airline_model_compressed.joblib")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main Dashboard */
.stApp{
    background: linear-gradient(
        135deg,
        #061A40,
        #0353A4
    );
}

/* Sidebar Theme */
[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #0B3D91,
        #0A4A92,
        #0A4A92
    );
}

/* Sidebar Text */
[data-testid="stSidebar"] *{
    color:white;
}

/* Number Input Boxes (Age, Flight Distance) */
div[data-baseweb="input"]{
    background-color:#1565C0 !important;
    border-radius:10px !important;
    border:1px solid #42A5F5 !important;
}

/* Input Text */
div[data-baseweb="input"] input{
    background-color:#1565C0 !important;
    color:white !important;
    font-weight:bold;
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background:rgba(255,255,255,0.08);
    padding:15px;
    border-radius:15px;
    border:1px solid rgba(255,255,255,0.15);
}

/* Predict Button */
.stButton button{
    width:100%;
    background:#00D4FF;
    color:black;
    font-weight:bold;
    border-radius:12px;
    height:50px;
}

</style>
""", unsafe_allow_html=True)
# =====================================
# SIDEBAR
# =====================================

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
# ✈️ SkyWings AI
### Passenger Satisfaction Dashboard
""")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Model Details")

st.sidebar.markdown("""
**Model:** Random Forest Classifier

**Accuracy:** 95.4%

**Prediction Type:** Classification

**Target:** Passenger Satisfaction
""")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Input Features")

st.sidebar.markdown("""
✈️ Age

✈️ Flight Distance

✈️ Online Boarding

✈️ Seat Comfort

✈️ In-flight Wifi Service

✈️ Food and Drink
""")

st.sidebar.markdown("---")

st.sidebar.subheader("📈 Quick Statistics")

col1, col2 = st.sidebar.columns(2)

with col1:
    st.metric("Accuracy", "95.4%")

with col2:
    st.metric("Features", "6")

st.sidebar.metric("Version", "v1.0")

st.sidebar.markdown("---")

st.sidebar.subheader("🎯 Project Goal")

st.sidebar.info(
    """
    Predict passenger satisfaction based on
    travel experience and service quality.
    """
)

st.sidebar.markdown("---")

st.sidebar.subheader("👨‍💻 Developer")

st.sidebar.success(
    "Sasank Surya Thota"
)

st.sidebar.caption(
    "Machine Learning Project | Streamlit Dashboard"
)

# ==========================================
# TITLE
# ==========================================

st.markdown("""
# ✈️ SkyWings AI

### Passenger Satisfaction Intelligence Platform
""")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", "95.4%")

with col2:
    st.metric("Precision", "94.8%")

with col3:
    st.metric("Recall", "95.1%")

st.markdown("---")

# ==========================================
# INPUT SECTION
# ==========================================

st.header("👤 Passenger Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25
    )

with col2:

    flight_distance = st.number_input(
        "Flight Distance",
        min_value=0,
        max_value=10000,
        value=1000
    )

# ==========================================
# SERVICE RATINGS
# ==========================================

st.header("⭐ Service Ratings")

col1, col2 = st.columns(2)

with col1:

    online_boarding = st.slider(
        "Online Boarding",
        1,
        5,
        3
    )

    wifi = st.slider(
        "In-flight Wifi Service",
        1,
        5,
        3
    )

with col2:

    seat_comfort = st.slider(
        "Seat Comfort",
        1,
        5,
        3
    )

    food = st.slider(
        "Food and Drink",
        1,
        5,
        3
    )

# ==========================================
# SERVICE SCORE
# ==========================================

service_score = (
    online_boarding +
    wifi +
    seat_comfort +
    food
)

st.subheader("📊 Service Experience Score")

st.metric(
    "Overall Service Score",
    f"{service_score}/20"
)

st.markdown("---")

# ==========================================
# PREPARE INPUT
# ==========================================

input_data = pd.DataFrame({
    "Age":[age],
    "Flight Distance":[flight_distance],
    "Online Boarding":[online_boarding],
    "Seat Comfort":[seat_comfort],
    "In-flight Wifi Service":[wifi],
    "Food and Drink":[food]
})

# ==========================================
# PREDICTION
# ==========================================

if st.button("🚀 Predict Passenger Satisfaction"):

    prediction = model.predict(input_data)

    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(input_data)

        satisfaction_prob = probability[0][1] * 100

    else:

        satisfaction_prob = 0

    st.markdown("---")

    st.header("🎯 Prediction Result")

    if prediction[0] == 1:

        st.success(
            f"😊 Passenger is Satisfied ({satisfaction_prob:.2f}%)"
        )

    else:

        st.error(
            f"😔 Passenger is Neutral / Dissatisfied ({100-satisfaction_prob:.2f}%)"
        )

    # ======================================
    # SATISFACTION PROBABILITY
    # ======================================

    st.subheader("📈 Satisfaction Probability")

    st.progress(float(satisfaction_prob / 100))

    st.write(
        f"Probability of Satisfaction: **{satisfaction_prob:.2f}%**"
    )

    # NEW FEATURE
    st.metric(
        "🔥 Confidence Score",
        f"{satisfaction_prob:.2f}%"
    )

    st.markdown("---")

    # ======================================
    # PASSENGER SUMMARY
    # ======================================

    st.header("📋 Passenger Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Age", age)

    with c2:
        st.metric("Distance", flight_distance)

    with c3:
        st.metric("Service Score", service_score)

    # NEW FEATURE
    st.subheader("📄 Passenger Input Details")

    st.dataframe(
        input_data,
        use_container_width=True
    )
# ==========================================
# BANNER
# ==========================================

st.image(
    "assets/airline_banner.png",
    use_container_width=True
)

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

st.markdown("---")

st.header("📊 Feature Importance")

try:

    feature_importance = model.feature_importances_

    feature_names = [
        "Age",
        "Flight Distance",
        "Online Boarding",
        "Seat Comfort",
        "In-flight Wifi Service",
        "Food and Drink"
    ]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.barh(
        feature_names,
        feature_importance
    )

    ax.set_title("Most Influential Features")

    st.pyplot(fig)

except:
    st.info(
        "Feature importance is unavailable for this model."
    )




# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
### ✈️ SkyWings AI

AI-Powered Passenger Satisfaction Intelligence Platform

Built using:
- Python
- Scikit-Learn
- Streamlit
- Machine Learning
""")
