import streamlit as st

from config.constants import COMMON_SYMPTOMS
from config.constants import EMERGENCY_MESSAGE

from modules.symptom_checker.symptom_engine import (
    generate_analysis,
    check_emergency
)


def show_symptom_checker_page():
    """
    Symptom Checker Main UI
    """

    st.title("🩺 Symptom Checker")

    st.markdown(
        """
        Select your symptoms below and click
        **Analyze Symptoms** to get possible
        health conditions.

        ⚠ This tool is for educational purposes only.
        """
    )

    st.divider()

    # =====================================
    # Symptom Selection
    # =====================================

    selected_symptoms = st.multiselect(
        "Select Symptoms",
        options=COMMON_SYMPTOMS,
        placeholder="Choose one or more symptoms..."
    )

    col1, col2 = st.columns([1, 4])

    with col1:
        analyze_btn = st.button(
            "🔍 Analyze Symptoms",
            use_container_width=True
        )

    # =====================================
    # Validation
    # =====================================

    if analyze_btn:

        if not selected_symptoms:
            st.warning(
                "Please select at least one symptom."
            )
            return

        # =====================================
        # Emergency Detection
        # =====================================

        if check_emergency(selected_symptoms):
            st.error(EMERGENCY_MESSAGE)

        st.divider()

        st.subheader("📋 Selected Symptoms")

        for symptom in selected_symptoms:
            st.write(f"✅ {symptom}")

        st.divider()

        # =====================================
        # Analysis
        # =====================================

        results = generate_analysis(selected_symptoms)

        if not results:
            st.warning(
                "No matching conditions found."
            )
            return

        st.subheader(
            "🩺 Possible Health Conditions"
        )

        # =====================================
        # Disease Cards
        # =====================================

        for index, item in enumerate(results, start=1):

            with st.expander(
                f"{index}. {item['disease']} "
                f"(Match Score: {item['match_score']})",
                expanded=(index == 1)
            ):

                st.markdown(
                    f"""
                    **Condition:** {item['disease']}
                    """
                )

                st.markdown(
                    f"""
                    **Match Score:** {item['match_score']}
                    """
                )

                st.markdown(
                    f"""
                    **Description**
                    
                    {item['description']}
                    """
                )

                st.markdown(
                    f"""
                    **Health Advice**
                    
                    {item['advice']}
                    """
                )

        st.divider()

        # =====================================
        # General Disclaimer
        # =====================================

        st.info(
            """
            ⚠ Disclaimer

            This symptom checker provides
            educational information only.

            It cannot diagnose diseases.

            Always consult a qualified
            healthcare professional for
            proper diagnosis and treatment.
            """
        )