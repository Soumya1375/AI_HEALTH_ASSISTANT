"""
=========================================
AI Diet Planner UI
=========================================

Author: Soumyadip
Project: AI Health Assistant

Features:
- User Details Form
- Goal Selection
- AI Diet Plan Generator
- Professional UI
- Download Option

=========================================
"""

import streamlit as st

from modules.ai_diet.diet_service import (
    generate_diet_plan
)


def show_diet_planner_page():

    # =====================================
    # CUSTOM CSS
    # =====================================

    st.markdown(
        """
        <style>

        .diet-header{
            background:linear-gradient(
                135deg,
                #16a34a,
                #22c55e
            );

            padding:25px;
            border-radius:20px;
            color:white;
            text-align:center;
            margin-bottom:20px;
        }

        .diet-card{
            background:#f8fafc;
            padding:20px;
            border-radius:15px;
            box-shadow:0px 4px 12px rgba(0,0,0,0.08);
            margin-bottom:15px;
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
        <div class="diet-header">

        <h1>🥗 AI Diet Planner</h1>

        <p>
        Get a personalized diet plan powered by AI
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # USER FORM
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

    with col2:

        weight = st.number_input(
            "Weight (kg)",
            min_value=20,
            max_value=250,
            value=70
        )

        height = st.number_input(
            "Height (cm)",
            min_value=100,
            max_value=250,
            value=170
        )

    goal = st.selectbox(
        "🎯 Select Goal",
        [
            "Weight Loss",
            "Weight Gain",
            "Maintain Weight"
        ]
    )

    st.markdown("---")

    # =====================================
    # GENERATE BUTTON
    # =====================================

    if st.button(
        "🤖 Generate AI Diet Plan",
        use_container_width=True
    ):

        with st.spinner(
            "Creating your personalized diet plan..."
        ):

            diet_plan = generate_diet_plan(
                age=age,
                gender=gender,
                weight=weight,
                height=height,
                goal=goal
            )

        st.success(
            "Diet Plan Generated Successfully!"
        )

        st.markdown("## 📋 Your Diet Plan")

        st.markdown(
            f"""
            <div class="diet-card">
            {diet_plan}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ================================
        # DOWNLOAD BUTTON
        # ================================

        st.download_button(
            label="📥 Download Diet Plan",
            data=diet_plan,
            file_name="diet_plan.txt",
            mime="text/plain"
        )

    # =====================================
    # HEALTHY TIPS
    # =====================================

    st.markdown("---")

    st.subheader("💡 Healthy Eating Tips")

    st.info(
        """
        ✅ Drink 2-3 liters of water daily

        ✅ Eat more fruits and vegetables

        ✅ Avoid excessive sugar

        ✅ Include protein in every meal

        ✅ Maintain regular meal timings
        """
    )