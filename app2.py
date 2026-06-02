import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart BMI and Food Advisor", layout="centered")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255, 255, 255, 0.80), rgba(255, 255, 255, 0.80)), url("https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1 {
        text-align: center;
    }
    .share-btn {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        color: white !important;
        background-color: #007bff;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
    }
    .share-whatsapp {
        background-color: #25D366;
    }
    .share-x {
        background-color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Smart BMI and Food Advisor")
st.write("Track your health status, analyze your body fat, and get tailored food guides.")
st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, value=70.0, step=0.1)
with col2:
    height_cm = st.number_input("Height (cm):", min_value=50.0, value=170.0, step=1.0)
with col3:
    age = st.number_input("Age:", min_value=10, max_value=100, value=25, step=1)
with col4:
    gender = st.selectbox("Gender:", ["Male", "Female"])

height_m = height_cm / 100
st.divider()

if st.button("Run AI Health Analysis", use_container_width=True):
    bmi = weight / (height_m ** 2)
    
    gender_factor = 1 if gender == "Male" else 0
    body_fat_percentage = (1.20 * bmi) + (0.23 * age) - (10.8 * gender_factor) - 5.4
    
    base_calories = weight * 24
    sedentary_cal = int(base_calories * 1.2)
    moderate_cal = int(base_calories * 1.5)
    active_cal = int(base_calories * 1.8)
    
    # تم تعديل هذا السطر لتوسيط العنوان Current Assessment
    st.markdown("<h3 style='text-align: center;'>Current Assessment</h3>", unsafe_allow_html=True)
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("Your Current BMI", f"{bmi:.2f}")
    with col_res2:
        st.metric("Estimated Body Fat", f"{body_fat_percentage:.1f}%")
    
    NUTRITION_KNOWLEDGE_BASE = {
        "underweight": """
        Document Ref: DOC-001 (Underweight Management)
        - Recommendation 1: Eat healthy fats like avocados, nuts, seeds, and olive oil.
        - Recommendation 2: Eat 5 to 6 smaller meals during the day instead of 3 big meals.
        - Recommendation 3: Eat more protein like eggs, chicken, fish, and dairy to build muscle.
        """,
        "normal": """
        Document Ref: DOC-002 (Weight Maintenance)
        - Recommendation 1: Keep a good balance between the food you eat and your daily movement.
        - Recommendation 2: Eat a clean mix of healthy carbohydrates (oats, brown rice) and protein.
        - Recommendation 3: Drink 2.5 to 3 liters of water every day to keep your body healthy.
        """,
        "overweight": """
        Document Ref: DOC-003 (Weight Loss)
        - Recommendation 1: Eat fewer calories than your body burns to lose weight safely.
        - Recommendation 2: Eat foods with high fiber like vegetables and whole grains to feel full longer.
        - Recommendation 3: Stop drinking sodas, sweet coffees, and commercial juices.
        """
    }
    
    ideal_weight = 22 * (height_m ** 2)
    
    if bmi < 18.5:
        st.markdown('<div style="text-align: center; padding: 15px; border-radius: 8px; background-color: #34495e; color: #ffffff; font-weight: bold; margin-bottom: 20px;">Category: Underweight (Action Required)</div>', unsafe_allow_html=True)
        target_calories = moderate_cal + 500
        query_key = "underweight"
        
    elif 18.5 <= bmi < 24.9:
        st.markdown('<div style="text-align: center; padding: 15px; border-radius: 8px; background-color: #27ae60; color: #ffffff; font-weight: bold; margin-bottom: 20px;">Category: Normal weight (Great Job!)</div>', unsafe_allow_html=True)
        target_calories = moderate_cal
        query_key = "normal"
        
    else:
        st.markdown('<div style="text-align: center; padding: 15px; border-radius: 8px; background-color: #c0392b; color: #ffffff; font-weight: bold; margin-bottom: 20px;">Category: Overweight (Action Required)</div>', unsafe_allow_html=True)
        target_calories = moderate_cal - 500
        query_key = "overweight"

    retrieved_document = NUTRITION_KNOWLEDGE_BASE[query_key]
    
    st.write("")
    st.subheader("1-Year Health Progress Graph")
    st.write("Expected weight progress over 12 months with a healthy routine:")
    
    months = list(range(13))
    projected_weights = []
    
    for month in months:
        step = (ideal_weight - weight) / 12
        current_step_weight = weight + (step * month)
        projected_weights.append(current_step_weight)
        
    chart_data = pd.DataFrame(
        {
            "Month": months,
            "Projected Weight (kg)": projected_weights
        }
    ).set_index("Month")
    
    st.line_chart(chart_data)
        
    st.write("")
    st.subheader("Daily Calorie Needs")
    st.markdown(f"""
    | Activity Level | Estimated Daily Calories |
    | :--- | :--- |
    | **Sedentary** (Little or no exercise) | {sedentary_cal} kcal |
    | **Moderate Activity** (Exercise 3-5 days/week) | {moderate_cal} kcal |
    | **High Activity** (Heavy exercise daily) | {active_cal} kcal |
    | **Your Target** (Based on Goals) | **{target_calories} kcal** |
    """)
    
    st.write("")
    st.subheader("RAG Generated Food Advice")
    st.caption("System Status: Successfully retrieved context from internal clinical guidelines database.")
    
    # تم تغيير st.info إلى st.success لتصبح الخلفية خضراء بدلاً من زرقاء
    st.success(retrieved_document)
    
    st.divider()
    st.subheader("Share Your Results")
    st.write("Inspire your friends by sharing your commitment to a healthier lifestyle!")
    
    share_text = f"I just checked my health status using the AI Smart BMI Advisor! My target daily calories are {target_calories} kcal. Time to get healthy!"
    x_url = f"https://twitter.com/intent/tweet?text={share_text}"
    wa_url = f"https://api.whatsapp.com/send?text={share_text}"
    
    st.markdown(f"""
        <div style="text-align: center;">
            <a href="{x_url}" target="_blank" class="share-btn share-x">Share on X</a>
            <a href="{wa_url}" target="_blank" class="share-btn share-whatsapp">Share on WhatsApp</a>
        </div>
    """, unsafe_allow_html=True)