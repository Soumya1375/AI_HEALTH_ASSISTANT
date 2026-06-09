import streamlit as st

from modules.bmi.bmi_calculator import analyze_bmi


def show_bmi_page():

    st.title("⚖️ BMI Calculator")

    st.markdown(
        """
        Calculate your Body Mass Index (BMI) and get personalized health insights.
        """
    )

    st.markdown("---")

    # =====================================
    # CUSTOM CSS
    # =====================================

    st.markdown(
        """
        <style>
        .bmi-card {
            padding:20px;
            border-radius:15px;
            background-color:#f8f9fa;
            box-shadow:0px 4px 12px rgba(0,0,0,0.1);
            margin-top:15px;
        }

        .bmi-title {
            font-size:22px;
            font-weight:bold;
        }

        .bmi-score {
            font-size:40px;
            font-weight:bold;
            color:#1f77b4;
        }

        .health-tip {
            padding:15px;
            border-left:6px solid #1f77b4;
            background:#eef7ff;
            border-radius:10px;
            margin-top:10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # INPUT SECTION
    # =====================================

    col1, col2 = st.columns(2)

    with col1:
        height = st.number_input(
            "📏 Height (meters)",
            min_value=0.50,
            max_value=2.50,
            value=1.70,
            step=0.01
        )

    with col2:
        weight = st.number_input(
            "⚖️ Weight (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1
        )

    calculate_btn = st.button(
        "🚀 Calculate BMI",
        use_container_width=True
    )

    # =====================================
    # CALCULATE BMI
    # =====================================

    if calculate_btn:

        result = analyze_bmi(
            height=height,
            weight=weight
        )

        bmi = result["bmi"]

        # SAVE FOR OTHER MODULES
        st.session_state["bmi"] = bmi
        st.session_state["height"] = height
        st.session_state["weight"] = weight
        st.session_state["bmi_category"] = result["category"]

        category = result["category"]
        status = result["status"]
        message = result["message"]

        st.write("DEBUG RESULT:", result)
        st.write("DEBUG CATEGORY:", category)

        # =====================================
        # CATEGORY COLOR
        # =====================================

        if category == "Underweight":
            color = "blue"

        elif category == "Normal":
            color = "green"

        elif category == "Overweight":
            color = "orange"

        else:
            color = "red"

        # =====================================
        # RESULT CARD
        # =====================================

        st.markdown(
            f"""
            <div class="bmi-card">
                <div class="bmi-title">
                    Your BMI Result
                </div>

                <div class="bmi-score">
                    {bmi}
                </div>

                <h4 style="color:{color};">
                    {status}
                </h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        bmi_progress = min(bmi / 40, 1.0)
        st.progress(bmi_progress)

        # =====================================
        # RECOMMENDATION
        # =====================================

        st.markdown(
            f"""
            <div class="health-tip">
                💡 <b>Health Recommendation</b><br><br>
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # =====================================
        # BMI CATEGORIES
        # =====================================

        st.subheader("📊 BMI Categories")

        st.info(
            """
            Underweight : Below 18.5

            Normal Weight : 18.5 - 24.9

            Overweight : 25 - 29.9

            Obese : 30+
            """
        )

        # =====================================
        # HEALTH STATUS
        # =====================================

        st.subheader("❤️ Health Status")

        if category == "Normal":

            st.success(
                "Excellent! Your BMI is within the healthy range."
            )

            st.balloons()

        elif category == "Underweight":

            st.warning(
                "You may need nutritional improvements and weight gain strategies."
            )

        elif category == "Overweight":

            st.warning(
                "Consider increasing physical activity and monitoring calorie intake."
            )

        else:

            st.error(
                "Your BMI is in the obesity range. Professional medical guidance is recommended."
            )

        st.markdown("---")

        st.caption(
            "⚠ BMI is a screening tool and not a medical diagnosis."
        )