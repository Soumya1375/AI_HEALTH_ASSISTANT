# app.py

import streamlit as st
import sys
import os

# ==========================================
# ROOT FIX
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# ==========================================
# IMPORT CONFIG + AUTH
# ==========================================
from config.settings import APP_CONFIG
from config.constants import APP_NAME
from modules.auth.login_ui import show_login_page

# ==========================================
# STREAMLIT CONFIG
# ==========================================
st.set_page_config(
    page_title=APP_CONFIG["page_title"],
    page_icon=APP_CONFIG["page_icon"],
    layout=APP_CONFIG["layout"],
    initial_sidebar_state=APP_CONFIG["initial_sidebar_state"]
)

# ==========================================
# LOAD CSS
# ==========================================

def load_css():

    css_path = os.path.join(
        BASE_DIR,
        "assets",
        "style.css"
    )

    if os.path.exists(css_path):

        with open(
            css_path,
            encoding="utf-8"
        ) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
# ==========================================
# LOGIN GATE
# ==========================================
if "user" not in st.session_state:
    show_login_page()
    st.stop()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🏥 AI Health Assistant")

st.sidebar.success(
    f"👤 {st.session_state['user']}"
)

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()

# ==========================================
# NAVIGATION
# ==========================================
PAGES = {
    "🏠 Home": "home",
    "👤 User Profile": "profile",
    "⚖️ BMI Calculator": "bmi",
    "🩺 Symptom Checker": "symptom",
    "🤖 AI Chatbot": "chatbot",
    "💊 Medicine Reminder": "reminder",
    "🥗 Lifestyle Recommendation": "lifestyle",
    "🥙 AI Diet Planner": "diet",
    "🏋️ AI Fitness Planner": "fitness",
    "📊 Health Dashboard": "dashboard",
    "📄 Report Analyzer": "report"
}

choice = st.sidebar.radio(
    "Navigation",
    list(PAGES.keys())
)

page = PAGES[choice]

st.sidebar.markdown("---")

st.sidebar.info(
    f"{APP_NAME} v1.0 | Gemini AI Powered"
)

# ==========================================
# PAGE LOADER
# ==========================================
def load_page(page):

    try:

        # ==================================
        # HOME PAGE
        # ==================================
        if page == "home":

            st.title("🏥 AI Health Assistant")

            st.success(
                f"Welcome {st.session_state['user']} 🚀"
            )

            st.markdown("---")

            st.subheader(
                "📊 Project Overview"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Modules",
                    "11"
                )

            with col2:
                st.metric(
                    "AI Features",
                    "4+"
                )

            with col3:
                st.metric(
                    "Database",
                    "SQLite"
                )

            with col4:
                st.metric(
                    "Framework",
                    "Streamlit"
                )

            st.markdown("---")

            st.subheader(
                "🚀 Available Features"
            )

            st.write("👤 User Profile Management")
            st.write("⚖️ BMI Calculator")
            st.write("🩺 Symptom Checker")
            st.write("🤖 AI Health Chatbot")
            st.write("💊 Medicine Reminder")
            st.write("🥗 Lifestyle Recommendation")
            st.write("🥙 AI Diet Planner")
            st.write("🏋️ AI Fitness Planner")
            st.write("📊 Health Dashboard")
            st.write("📄 Report Analyzer")

            st.markdown("---")

            st.subheader(
                "🤖 AI Health Summary"
            )

            st.info(
                """
                This application combines
                Artificial Intelligence and
                Healthcare tools to provide:

                • Health Monitoring

                • AI Chat Assistance

                • Diet Planning

                • Fitness Planning

                • Report Analysis

                • Lifestyle Recommendations
                """
            )

            st.markdown("---")

            st.subheader(
                "💡 Daily Health Tip"
            )

            st.warning(
                "Drink 2-3 liters of water and walk at least 30 minutes today."
            )

        # ==================================
        # PROFILE
        # ==================================
        elif page == "profile":

            from modules.user_profile.profile_ui import (
                show_profile_page
            )

            show_profile_page()

        # ==================================
        # BMI
        # ==================================
        elif page == "bmi":

            from modules.bmi.bmi_ui import (
                show_bmi_page
            )

            show_bmi_page()

        # ==================================
        # SYMPTOM CHECKER
        # ==================================
        elif page == "symptom":

            from modules.symptom_checker.symptom_ui import (
                show_symptom_checker_page
            )

            show_symptom_checker_page()

        # ==================================
        # CHATBOT
        # ==================================
        elif page == "chatbot":

            from modules.chatbot.chatbot_ui import (
                show_chatbot_page
            )

            show_chatbot_page()

        # ==================================
        # MEDICINE REMINDER
        # ==================================
        elif page == "reminder":

            from modules.medicine_reminder.reminder_ui import (
                show_reminder_page
            )

            show_reminder_page()

        # ==================================
        # LIFESTYLE
        # ==================================
        elif page == "lifestyle":

            from modules.lifestyle.recommendation_ui import (
                show_recommendation_page
            )

            show_recommendation_page()

        # ==================================
        # DIET PLANNER
        # ==================================
        elif page == "diet":

            from modules.ai_diet.diet_ui import (
                show_diet_planner_page
            )

            show_diet_planner_page()

        # ==================================
        # FITNESS PLANNER
        # ==================================
        elif page == "fitness":

            from modules.ai_fitness.fitness_ui import (
                show_fitness_planner_page
            )

            show_fitness_planner_page()

        # ==================================
        # DASHBOARD
        # ==================================
        elif page == "dashboard":

            from modules.dashboard.dashboard_ui import (
                show_dashboard_page
            )

            show_dashboard_page()

        # ==================================
        # REPORT ANALYZER
        # ==================================
        elif page == "report":

            from modules.report_analyzer.report_ui import (
                show_report_analyzer_page
            )

            show_report_analyzer_page()

    except Exception as e:

        st.error(
            f"❌ Page Error: {e}"
        )

        import traceback

        st.code(
            traceback.format_exc()
        )

# ==========================================
# RUN APP
# ==========================================
load_page(page)

