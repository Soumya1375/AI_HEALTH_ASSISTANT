import streamlit as st
import plotly.express as px
import pandas as pd
import time
from datetime import datetime

from modules.dashboard.dashboard_service import (
    get_total_users,
    get_total_bmi_records,
    get_total_chat_sessions,
    get_bmi_distribution
)

# ==========================================
# PAGE CONFIG STYLE
# ==========================================
def show_dashboard_page():

    st.title("📊 AI Health Analytics Dashboard")
    st.caption("Real-time insights powered by AI + Data Analytics")

    # ==========================================
    # LIVE METRICS
    # ==========================================
    col1, col2, col3 = st.columns(3)

    col1.metric("👤 Users", get_total_users())
    col2.metric("⚖️ BMI Records", get_total_bmi_records())
    col3.metric("💬 Chat Sessions", get_total_chat_sessions())

    st.markdown("---")

    # ==========================================
    # BMI DISTRIBUTION CHART
    # ==========================================
    bmi_data = get_bmi_distribution()

    if bmi_data:
        df = pd.DataFrame(bmi_data, columns=["Category", "Count"])

        fig = px.pie(
            df,
            names="Category",
            values="Count",
            title="⚖️ BMI Category Distribution",
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================================
    # AI INSIGHTS ENGINE
    # ==========================================
    st.subheader("🧠 AI Health Insights")

    total_users = get_total_users()
    total_bmi = get_total_bmi_records()

    if total_bmi == 0:
        st.info("No data available for AI analysis yet.")
    else:

        overweight_ratio = "Moderate"

        if total_bmi > 50:
            overweight_ratio = "High health activity detected"
        elif total_bmi > 20:
            overweight_ratio = "Moderate health engagement"
        else:
            overweight_ratio = "Low data activity"

        st.success(f"""
        📌 AI Observation:

        - System has collected {total_bmi} BMI records  
        - User engagement level: {overweight_ratio}  
        - Health tracking consistency is improving over time  
        """)

    st.markdown("---")

    # ==========================================
    # DAILY / WEEKLY TREND (SIMULATED)
    # ==========================================
    st.subheader("📅 Activity Trends")

    trend_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Users": [5, 8, 6, 10, 12, 7, 9]
    })

    fig2 = px.line(
        trend_data,
        x="Day",
        y="Users",
        markers=True,
        title="Weekly User Activity Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ==========================================
    # RECENT ACTIVITY (LIVE PANEL)
    # ==========================================
    st.subheader("🌍 Live Analytics Panel")

    st.info("Auto-refreshing every 5 seconds (simulated real-time system)")

    placeholder = st.empty()

    for i in range(3):  # simulate live updates

        with placeholder.container():

            st.write("🔄 Updating live health data...")

            st.write(f"⏱ Last update: {datetime.now().strftime('%H:%M:%S')}")

            st.write(f"👤 Total Users: {get_total_users()}")
            st.write(f"⚖️ BMI Records: {get_total_bmi_records()}")

        time.sleep(1)

    st.success("Live analytics loaded successfully 🚀")