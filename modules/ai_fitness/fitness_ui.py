"""
=========================================
AI Fitness Planner UI
=========================================

Author: Soumyadip
Project: AI Health Assistant

Features:
- AI Fitness Plan Generator
- Fitness Score
- Goal Selection
- Download Plan
- Modern UI

=========================================
"""

import streamlit as st

from modules.ai_fitness.fitness_service import (
    generate_fitness_plan,
    calculate_fitness_score
)


def show_fitness_planner_page():

    # =====================================
    # PAGE TITLE
    # =====================================

    st.title("🏋️ AI Fitness Planner")

    st.caption(
        "Get a personalized AI-powered fitness plan."
    )

    # =====================================
    # CUSTOM CSS
    # =====================================

    st.markdown(
        """
        <style>

        .fitness-header{
            background: linear-gradient(
                135deg,
                #2563eb,
                #7c3aed
            );

            padding:25px;
            border-radius:20px;
            color:white;
            text-align:center;
            margin-bottom:20px;
        }

        .result-card{
            background:#f8fafc;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #2563eb;
            box-shadow:0px 4px 10px rgba(0,0,0,0.08);
        }

        .metric-card{
            background:white;
            padding:15px;
            border-radius:15px;
            text-align:center;
            box-shadow:0px 4px 10px rgba(0,0,0,0.08);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # HEADER
    # =====================================

    st.markdown(
        """
        <div class="fitness-header">

        <h1>🏋️ AI Fitness Planner</h1>

        <p>
        Create your personalized workout routine
        using Artificial Intelligence.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # USER INPUT
    # =====================================

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=22
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=20,
            max_value=250,
            value=70
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=100,
            max_value=250,
            value=170
        )

        goal = st.selectbox(
            "🎯 Fitness Goal",
            [
                "Weight Loss",
                "Muscle Gain",
                "Stay Fit"
            ]
        )

        fitness_level = st.selectbox(
            "💪 Fitness Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    st.divider()

    # =====================================
    # BMI + FITNESS SCORE
    # =====================================

    bmi = weight / ((height / 100) ** 2)

    fitness_score = calculate_fitness_score(
        bmi
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "⚖️ BMI",
            round(bmi, 2)
        )

    with col2:

        st.metric(
            "🏆 Fitness Score",
            f"{fitness_score}/100"
        )

    st.progress(
        fitness_score / 100
    )

    st.divider()

    # =====================================
    # GENERATE PLAN
    # =====================================

    if st.button(
        "🚀 Generate AI Fitness Plan",
        use_container_width=True
    ):

        with st.spinner(
            "Creating personalized fitness plan..."
        ):

            plan = generate_fitness_plan(
                age=age,
                gender=gender,
                weight=weight,
                height=height,
                goal=goal,
                fitness_level=fitness_level
            )

        st.success(
            "Fitness Plan Generated Successfully!"
        )

        st.subheader(
            "📋 Your AI Fitness Plan"
        )

        st.markdown(
            f"""
            <div class="result-card">
            {plan}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.download_button(
            label="📥 Download Fitness Plan",
            data=plan,
            file_name="fitness_plan.txt",
            mime="text/plain"
        )

    st.divider()

    # =====================================
    # HEALTH TIPS
    # =====================================

    st.subheader("💡 Fitness Tips")

    st.info(
        """
        ✅ Warm up before exercise

        ✅ Stay hydrated

        ✅ Maintain proper form

        ✅ Get 7-9 hours sleep

        ✅ Take recovery days

        ✅ Consistency beats intensity
        """
    )

    # =====================================
    # MOTIVATION CARD
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

        <h3>🔥 Stay Consistent</h3>

        Small daily efforts create
        massive long-term results.

        </div>
        """,
        unsafe_allow_html=True
    )