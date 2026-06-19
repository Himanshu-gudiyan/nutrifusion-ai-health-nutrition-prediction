import joblib

health_model = joblib.load("models/health_model.pkl")
calorie_model = joblib.load("models/calorie_model.pkl")

import streamlit as st
import os
import google.generativeai as genai
import base64
from PIL import Image
# ui/ux designe 1 change 14
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()

# ui/ux designe 1 change 1
st.set_page_config(
    page_title="NutriFusion AI",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_dotenv()


st.markdown("""
<style>

/* ================= GLOBAL BACKGROUND ================= */
[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
    color: white;
}

/* ================= MAIN CONTENT AREA ================= */
.main {
    background-color: #0f172a;
    padding: 20px;
}

/* ================= SIDEBAR ================= */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

/* ================= TOP HEADER BAR ================= */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Hide Streamlit default top bar spacing */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display: none;}

/* ================= BUTTON STYLE ================= */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #06b6d4);
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

/* ================= TEXT ================= */
h1, h2, h3 {
    color: #f8fafc !important;
}

p {
    color: #cbd5e1;
}

/* ================= CARD STYLE ================= */
.card {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)


hide_streamlit_style = """
<style>

#/* Hide Deploy Button */
#.stDeployButton {
#   display: none;
#}
/* Hide Deploy Button */
.stDeployButton {
    display: none !important;
}

[data-testid="stDeployButton"] {
    display: none !important;
}

/* Hide Main Menu */
#MainMenu {
    visibility: hidden;
}

/* Hide Footer */
footer {
    visibility: hidden;
}

/* ⚠️ Header ko hide mat karo, warna sidebar arrow gayab ho jayega */

/*
header {
    visibility: hidden;
}
*/

/* Inhe bhi hide mat karo, ye sidebar toggle ko affect kar sakte hain */

/*
[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stStatusWidget"] {
    display: none;
}
*/

</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#0F172A,#1E293B);
}

/* Metric Cards */
[data-testid="metric-container"]{
    background-color: rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.2);
}

/* Buttons */
.stButton > button{
    width:100%;
    height:55px;
    border-radius:15px;
    background:linear-gradient(90deg,#00C9A7,#00B4D8);
    color:white;
    font-size:18px;
    font-weight:bold;
}

/* Text Area */
textarea{
    border-radius:12px !important;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)



# ui/ux designe 1 change 2
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

textarea {
    border-radius: 10px;
}

[data-testid="stSidebar"] {
    background-color: #1E1E2F;
}

</style>
""", unsafe_allow_html=True)


API_KEY = os.getenv("GEMINI_API_KEY")




import os
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)




health_model = joblib.load("models/health_model.pkl")
calorie_model = joblib.load("models/calorie_model.pkl")


def hero_banner():
    st.markdown("""
    <style>
    .hero-container {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        border-radius: 15px;
        color: white;
        margin-bottom: 20px;
    }

    .hero-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 20px;
    }

    .hero-badge {
        font-size: 14px;
        color: #94a3b8;
    }
    </style>

    <div class="hero-container">
        <div class="hero-title">🧠 NutriFusion AI v2.0</div>
        <div class="hero-subtitle">
            AI-Powered Nutrition Analysis • Food Intelligence • Health Scoring
        </div>
        <div class="hero-badge">
            Built with Python • Streamlit • Gemini AI • Plotly • Scikit-learn
        </div>
    </div>
    """, unsafe_allow_html=True)
    hero_banner()

#calori
def predict_calories(age, gender, height, weight, activity):
    prediction = calorie_model.predict([[age, gender, height, weight, activity]])
    return round(prediction[0], 2)


if 'health_profile' not in st.session_state:
   st.session_state.health_profile = {
    'goals': 'loss 10 pounds in 3 months\nimprove cardiovascular health',
    'conditions': 'None',   # FIXED
    'routines': '30-minutes walk 3x/week',
    'preferences': 'Vegetarian\nLow carb',
    'restrictions': 'No dairy\nNo nuts'
}
 # Function to get Gemini response


def get_gemini_response(prompt, image_data=None):
    model = genai.GenerativeModel("gemini-2.5-flash")

    if image_data is not None:
        response = model.generate_content([prompt, image_data])
    else:
        response = model.generate_content(prompt)

    return response.text


# ✅ Function to prepare image data

from PIL import Image

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        return Image.open(uploaded_file)
    return None


#Siderbar sor health profile
# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    # ui/ux design change 5
    st.image(
        "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Robot/3D/robot_3d.png",
        width=80
    )

    st.markdown("""
# 🤖 NutriFusion AI
### AI Health Assistant
---
""")
    
    # ==========================
    # NAVIGATION BAR
    # ==========================

    navigation = st.radio(
    "🧭 Navigation",
    [
        "🏠 Dashboard",
        "🤖 AI Features",
        "📊 Analytics",
        "📈 ML Predictions",
        "📄 Reports"
    ]
) 
    

    st.markdown("---")

    # ==========================
    
    # ==========================
    # HEALTH PROFILE
    # ==========================

    st.subheader("Your Health Profile")

    health_goals = st.text_area(
        "Health Goals",
        value=st.session_state.health_profile['goals']
    )

    medical_conditions = st.text_area(
        "Medical Conditions",
        value=st.session_state.health_profile['conditions']
    )

    fitness_routines = st.text_area(
        "Fitness Routines",
        value=st.session_state.health_profile['routines']
    )

    food_preferences = st.text_area(
        "Food Preferences",
        value=st.session_state.health_profile['preferences']
    )

    restrictions = st.text_area(
        "Dietary Restrictions",
        value=st.session_state.health_profile['restrictions']
    )

    if st.button(
        "UPDATE PROFILE",
        key="update_profile_button"
    ):

        st.session_state.health_profile['goals'] = health_goals
        st.session_state.health_profile['conditions'] = medical_conditions
        st.session_state.health_profile['routines'] = fitness_routines
        st.session_state.health_profile['preferences'] = food_preferences
        st.session_state.health_profile['restrictions'] = restrictions

        st.success(
            "✅ Profile updated successfully!"
        )
# ==========================
# DASHBOARD
# ==========================

if navigation == "🏠 Dashboard":

    st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
🥗 NutriFusion AI
</h1>

<h4 style='text-align: center; color: gray;'>
AI Powered Nutrition & Health Assistant
</h4>

<hr>
""", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🍎 Meal Plans", "7 Days")
    col2.metric("🔥 Calories", "1800")
    col3.metric("💪 Protein", "120g")
    col4.metric("❤️ Health Score", "92%")

    # YAHAN PASTE KARO 👇

    st.markdown("### 🤖 AI Insights")

    st.info("""
    ✅ Personalized Nutrition Recommendations

    ✅ AI Meal Planning using Gemini

    ✅ Food Image Analysis

    ✅ Health Risk Assessment

    ✅ BMI & Health Score Tracking

    ✅ Data Analytics Dashboard

    ✅ Machine Learning Predictions
    """)

# main content area 
if navigation == "🤖 AI Features":

    tab1, tab2, tab3 = st.tabs(
        [
            "🍽 Meal Planning",
            "📸Food Analysis",
            "🩺Health Insights"
        ]
    )

    # ==========================
    # TAB 1
    # ==========================

    with tab1:

        st.subheader("Personalized Meal Planning")

        col1, col2 = st.columns(2)

        with col1:

            st.write("### Your Current Needs")

            user_input = st.text_area(
                "Describe any specific requirements for your meal plan:",
                placeholder="e.g., I need quick meals for work days"
            )

        with col2:

            st.write("### Your Health Profile")
            st.json(st.session_state.health_profile)

        if st.button(
            "Generate Personalized Meal Plan",
            key="generate_meal_plan_button"
        ):

            if not any(st.session_state.health_profile.values()):

                st.warning(
                    "Please complete your health profile in the sidebar first."
                )

            else:

                with st.spinner(
                    "Creating your personalized meal plan..."
                ):

                    prompt = f"""
Create a personalized meal plan based on the following health profile:

Health Goals:
{st.session_state.health_profile['goals']}

Medical Conditions:
{st.session_state.health_profile['conditions']}

Fitness Routines:
{st.session_state.health_profile['routines']}

Food Preferences:
{st.session_state.health_profile['preferences']}

Dietary Restrictions:
{st.session_state.health_profile['restrictions']}

Additional Requirements:
{user_input if user_input else "None provided"}

Provide:
1. A 7-day meal plan
2. Breakfast, Lunch, Dinner, and Snacks
3. Nutritional breakdown
4. Reasons for meal selection
5. Shopping list
6. Preparation tips
"""

                    response = get_gemini_response(prompt)

                    st.subheader(
                        "Your Personalized Meal Plan"
                    )

                    st.markdown(response)

                    st.download_button(
                        label="Download Meal Plan",
                        data=response,
                        file_name="personalized_meal_plan.txt",
                        mime="text/plain",
                        key="download_meal_plan"
                    )

        st.success(
            "🤖 Welcome to NutriFusion AI | Your Personal AI Health & Nutrition Coach"
        )

    # ==========================
    # TAB 2
    # ==========================

    with tab2:

        st.subheader("Food Analysis")

        uploaded_file = st.file_uploader(
            "Upload an image of your food",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:

            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Food Image."
            )

        if st.button(
            "Analyze Food",
            key="analyze_food_button"
        ):

            if uploaded_file is None:

                st.warning(
                    "Please upload an image first."
                )

            else:

                with st.spinner(
                    "Analyzing your food..."
                ):

                    image_data = input_image_setup(
                        uploaded_file
                    )

                    prompt = """
You are an expert nutritionist.

Analyze this food image.

Provide:

- Calories
- Protein
- Carbs
- Fat
- Health Benefits
- Portion Recommendation
"""

                    response = get_gemini_response(
                        prompt,
                        image_data
                    )

                    st.subheader(
                        "Food Analysis Results"
                    )

                    st.markdown(response)

    # ==========================
    # TAB 3
    # ==========================

    with tab3:

        st.subheader(
            "Health Insights"
        )

        health_query = st.text_input(
            "Ask any health/nutrition-related question",
            placeholder="e.g., How can I improve my gut health?"
        )

        if st.button(
            "Get Expert Insights",
            key="expert_insights_button"
        ):

            if not health_query:

                st.warning(
                    "Please enter a health question"
                )

            else:

                with st.spinner(
                    "Researching your question..."
                ):

                    prompt = f"""
You are a certified nutritionist and health expert.

Question:

{health_query}

Health Profile:

{st.session_state.health_profile}

Provide:

1. Science
2. Practical Advice
3. Precautions
4. References
5. Food Suggestions
"""

                    response = get_gemini_response(
                        prompt
                    )

                    st.subheader(
                        "Expert Health Insights"
                    )

                    st.markdown(response)

# ====================================
# ANALYTICS DASHBOARD (DATA ANALYST LAYER)
# ====================================
# ====================================
# ANALYTICS PAGE
# ====================================

if navigation == "📊 Analytics":
    st.subheader("📊 Nutrition Analytics")

    nutrition_data = pd.DataFrame({
    "Nutrient": ["Protein", "Carbs", "Fats"],
    "Value": [120, 200, 70]
    })

    col1, col2 = st.columns(2)

    with col1:
            fig1 = px.pie(
                nutrition_data,
                names="Nutrient",
                values="Value",
                title="Macronutrient Distribution"
    )
            st.plotly_chart(fig1, use_container_width=True)

    with col2:
            weekly_calories = pd.DataFrame({
            "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            "Calories": [1800, 2000, 1900, 2100, 1950, 2200, 2000]
        })

            fig2 = px.line(
                weekly_calories,
                x="Day",
                y="Calories",
                markers=True,
                title="Weekly Calorie Trend"
                )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

# ui/ux designe 1 change 12
# AI Health Score Dashboard
# ====================================
# ML PREDICTIONS
# ====================================
if navigation == "📈 ML Predictions":

    st.subheader("🤖 AI Health Score Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=200.0,
            value=70.0,
            key="ml_weight"
        )

    with col2:
        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            key="ml_height"
        )

    with col3:
        water = st.slider(
            "Water Intake (L)",
            0.0,
            5.0,
            2.5,
            key="ml_water"
        )

    # BMI Calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Health Score
    health_score = 100

    if bmi < 18.5:
        health_score -= 15
    elif bmi > 25:
        health_score -= 10

    if water < 2:
        health_score -= 10

    health_score = max(0, health_score)

    st.metric("🏆 Health Score", f"{health_score}/100")

    import plotly.graph_objects as go

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={"text": "Health Score"},
            gauge={"axis": {"range": [0, 100]}}
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(f"Current BMI: {bmi:.2f}")

    # ==========================
    # HEALTH RISK PREDICTION
    # ==========================

    prediction = health_model.predict([[weight, height, water, bmi]])
    risk = prediction[0]

    st.subheader("🚨 AI Health Risk Prediction")

    if risk == "Low":
        st.success(f"Risk Level: {risk}")

    elif risk == "Medium":
        st.warning(f"Risk Level: {risk}")

    else:
        st.error(f"Risk Level: {risk}")

    # ==========================
    # AI RECOMMENDATION
    # ==========================

    st.subheader("🤖 AI Recommendation Engine")

    if risk == "Low":
        st.success("""
Maintain your current lifestyle.
Continue hydration and balanced nutrition.
""")

    elif risk == "Medium":
        st.warning("""
Increase daily water intake.
Improve protein consumption.
Add regular exercise.
""")

    else:
        st.error("""
Health risk detected.
Consult a healthcare professional.
Improve diet and hydration immediately.
""")

    # ==========================
    # DAILY CALORIE PREDICTION
    # ==========================

    st.markdown("---")
    st.subheader("🔥 Daily Calorie Prediction")

    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=25,
        key="cal_age"
    )

    cal_height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=170.0,
        key="cal_height"
    )

    cal_weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=200.0,
        value=70.0,
        key="cal_weight"
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        key="cal_gender"
    )

    gender_value = 1 if gender == "Male" else 0

    activity = st.selectbox(
        "Activity Level",
        [
            "Sedentary",
            "Light",
            "Moderate",
            "Active",
            "Very Active"
        ],
        key="cal_activity"
    )

    activity_map = {
        "Sedentary": 1,
        "Light": 2,
        "Moderate": 3,
        "Active": 4,
        "Very Active": 5
    }

    activity_value = activity_map[activity]

    if st.button("🔥 Predict Daily Calories"):

        calories = predict_calories(
            age,
            gender_value,
            cal_height,
            cal_weight,
            activity_value
        )

        st.success(f"🔥 Recommended Daily Calories: {calories:.0f} kcal")

# ====================================
#💬 AI Doctor Chat   
if navigation == "💬 AI Doctor Chat":

    st.subheader("🧠 Gemini AI Health Assistant")

    user_query = st.text_input(
        "Ask your health question",
        placeholder="e.g. How can I reduce weight?"
    )

    if st.button("Get AI Advice"):

        if not user_query:
            st.warning("Please enter a question")
        else:

            prompt = f"""
            You are a professional health & nutrition AI assistant.
            Give short, practical, easy-to-understand advice.

            User question: {user_query}
            """

            response = genai.GenerativeModel("gemini-pro").generate_content(prompt)

            st.success(response.text)
#=================
# REPORTS
# ====================================

if navigation == "📄 Reports":


    st.subheader("📄 AI Health Report")

    st.markdown("""
### Report Summary

This report includes:

✅ User Health Profile  
✅ Nutrition Analytics  
✅ AI Health Score  
✅ BMI Analysis  
✅ Personalized AI Recommendations  
""")

    report_text = f"""
NUTRIFUSION AI HEALTH REPORT

Health Goals:
{st.session_state.health_profile['goals']}

Medical Conditions:
{st.session_state.health_profile['conditions']}

Fitness Routines:
{st.session_state.health_profile['routines']}

Food Preferences:
{st.session_state.health_profile['preferences']}

Dietary Restrictions:
{st.session_state.health_profile['restrictions']}
"""

    st.download_button(
        label="📥 Download Report",
        data=report_text,
        file_name="NutriFusion_Report.txt",
        mime="text/plain",
        key="download_report"
    )


# ------------------------------
# Footer
# ------------------------------

st.markdown("---")

st.markdown("""
<div style="text-align:center;padding:20px;">

<h4>🥗 NutriFusion AI v2.0</h4>

<p>
Built with ❤️ using
<b>Python</b> •
<b>Streamlit</b> •
<b>Gemini AI</b> •
<b>Plotly</b> •
<b>Scikit-learn</b>
</p>

<p style="color:gray;">
© 2026 Himanshu Gudiyan
</p>

</div>
""", unsafe_allow_html=True)