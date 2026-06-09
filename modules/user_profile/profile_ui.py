"""
=========================================
User Profile UI
=========================================

Author: Soumyadip
Project: AI Health Assistant

=========================================
"""

import streamlit as st

from config.constants import (
    GENDER_OPTIONS,
    BLOOD_GROUPS,
    PROFILE_SAVED,
    ERROR_EMPTY_NAME,
    ERROR_INVALID_AGE,
    ERROR_INVALID_HEIGHT,
    ERROR_INVALID_WEIGHT
)

from modules.user_profile.profile_service import (
    create_user,
    get_latest_user
)


def show_profile_page():

    st.title("👤 User Profile")

    st.markdown(
        """
        Create and manage your health profile.

        This information will be used for:
        - BMI Calculation
        - Health Dashboard
        - Personalized Recommendations
        """
    )

    st.divider()

    # =====================================
    # Existing User Preview
    # =====================================

    latest_user = get_latest_user()

    if latest_user:

        st.subheader("📋 Latest Profile")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Name:** {latest_user['name']}")
            st.write(f"**Age:** {latest_user['age']}")
            st.write(f"**Gender:** {latest_user['gender']}")

        with col2:
            st.write(f"**Height:** {latest_user['height']} m")
            st.write(f"**Weight:** {latest_user['weight']} kg")
            st.write(
                f"**Blood Group:** {latest_user['blood_group']}"
            )

        st.divider()

    # =====================================
    # User Form
    # =====================================

    st.subheader("➕ Create New Profile")

    with st.form("profile_form"):

        name = st.text_input(
            "Full Name"
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=18
        )

        gender = st.selectbox(
            "Gender",
            GENDER_OPTIONS
        )

        height = st.number_input(
            "Height (meters)",
            min_value=0.50,
            max_value=2.50,
            value=1.70,
            step=0.01
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1
        )

        blood_group = st.selectbox(
            "Blood Group",
            BLOOD_GROUPS
        )

        submit_btn = st.form_submit_button(
            "💾 Save Profile"
        )

    # =====================================
    # Save User
    # =====================================

    if submit_btn:

        if not name.strip():

            st.error(ERROR_EMPTY_NAME)
            return

        if age <= 0:

            st.error(ERROR_INVALID_AGE)
            return

        if height <= 0:

            st.error(ERROR_INVALID_HEIGHT)
            return

        if weight <= 0:

            st.error(ERROR_INVALID_WEIGHT)
            return

        user_id = create_user(
            name=name.strip(),
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            blood_group=blood_group
        )

        if user_id:

            st.success(PROFILE_SAVED)

            st.info(
                f"User ID: {user_id}"
            )

            st.balloons()

        else:

            st.error(
                "Failed to save profile."
            )