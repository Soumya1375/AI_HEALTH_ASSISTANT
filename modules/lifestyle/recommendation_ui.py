"""
=========================================
Lifestyle Recommendation UI
=========================================

Author: Soumyadip
Project: AI Health Assistant
=========================================
"""

import streamlit as st

from modules.lifestyle.recommendation_engine import (
    get_recommendation
)


def show_recommendation_page(bmi=None):

    # =====================================
    # BMI FETCH
    # =====================================

    if bmi is None:

        bmi = st.session_state.get("bmi")

        if bmi is None:
            st.warning("⚠ Please calculate your BMI first.")
            return

    recommendation = get_recommendation(bmi)

    # =====================================
    # CUSTOM CSS
    # =====================================

    st.markdown(
        """
        <style>

        .main-card{
            background: linear-gradient(
                135deg,
                #2563eb,
                #7c3aed
            );

            color:white;
            padding:25px;
            border-radius:20px;
            margin-bottom:20px;
        }

        .section-card{
            background:#f8fafc;
            padding:20px;
            border-radius:15px;
            margin-bottom:15px;
            border-left:6px solid #2563eb;
            box-shadow:0 4px 10px rgba(0,0,0,0.08);
        }

        .category-box{
            background:#ecfeff;
            padding:15px;
            border-radius:12px;
            text-align:center;
            font-size:24px;
            font-weight:bold;
            color:#0f766e;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # HEADER
    # =====================================

    st.markdown(
        f"""
        <div class="main-card">

        <h1>💡 Lifestyle Recommendation</h1>

        <h3>BMI Score: {round(bmi,2)}</h3>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # CATEGORY
    # =====================================

    st.markdown(
        f"""
        <div class="category-box">

        📊 {recommendation['category']}

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================
    # DIET + EXERCISE
    # =====================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="section-card">
            <h3>🍽 Diet Plan</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        for item in recommendation["diet"]:
            st.success(item)

    with col2:

        st.markdown(
            """
            <div class="section-card">
            <h3>🏃 Exercise Plan</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        for item in recommendation["exercise"]:
            st.info(item)

    # =====================================
    # HEALTH TIPS
    # =====================================

    st.markdown(
        """
        <div class="section-card">
        <h3>💡 Health Tips</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    for tip in recommendation["tips"]:
        st.warning(tip)

    # =====================================
    # HEALTH STATUS
    # =====================================

    st.subheader("📈 Health Status")

    if bmi < 18.5:

        st.progress(25)

        st.error(
            "Underweight: Focus on healthy weight gain."
        )

    elif bmi < 25:

        st.progress(100)

        st.success(
            "Excellent! Your BMI is in the healthy range."
        )

    elif bmi < 30:

        st.progress(65)

        st.warning(
            "Overweight: Consider gradual lifestyle changes."
        )

    else:

        st.progress(40)

        st.error(
            "Obese: Professional medical guidance is recommended."
        )

    # =====================================
    # DAILY HEALTH CHECKLIST
    # =====================================

    st.subheader("✅ Daily Health Checklist")

    st.checkbox("Drink 2-3 Liters Water")
    st.checkbox("30+ Minutes Physical Activity")
    st.checkbox("Eat Fruits & Vegetables")
    st.checkbox("Sleep 7-9 Hours")
    st.checkbox("Avoid Excess Junk Food")

    # =====================================
    # MOTIVATION
    # =====================================

    st.markdown(
        """
        <div style="
            background:#dcfce7;
            padding:20px;
            border-radius:15px;
            text-align:center;
            margin-top:20px;
        ">

        <h3>🌟 Healthy Lifestyle = Better Future</h3>

        Small daily improvements lead to
        long-term health benefits.

        </div>
        """,
        unsafe_allow_html=True
    )