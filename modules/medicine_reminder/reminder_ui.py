import streamlit as st

from modules.medicine_reminder.reminder_service import (
    add_reminder,
    get_all_reminders,
    delete_reminder
)


def show_reminder_page():

    st.title("💊 Medicine Reminder")

    st.caption(
        "Manage your daily medicine schedule."
    )

    # =====================================
    # CUSTOM CSS
    # =====================================

    st.markdown(
        """
        <style>

        .metric-card{
            background:linear-gradient(
                135deg,
                #4F46E5,
                #7C3AED
            );

            padding:20px;
            border-radius:15px;
            color:white;
            text-align:center;
            margin-bottom:20px;
        }

        .reminder-card{
            background:#f8fafc;
            padding:18px;
            border-radius:12px;
            border-left:6px solid #4F46E5;
            margin-bottom:10px;
            box-shadow:0 2px 8px rgba(0,0,0,0.08);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    reminders = get_all_reminders()

    # =====================================
    # DASHBOARD CARD
    # =====================================

    st.markdown(
        f"""
        <div class="metric-card">

        <h3>Total Reminders</h3>

        <h1>{len(reminders)}</h1>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # ADD REMINDER
    # =====================================

    st.subheader("➕ Add New Reminder")

    col1, col2 = st.columns(2)

    with col1:

        medicine_name = st.text_input(
            "Medicine Name",
            placeholder="Paracetamol"
        )

    with col2:

        reminder_time = st.time_input(
            "Reminder Time"
        )

    if st.button(
        "💾 Save Reminder",
        use_container_width=True
    ):

        if medicine_name.strip() == "":

            st.warning(
                "Please enter medicine name."
            )

        else:

            add_reminder(
                medicine_name,
                str(reminder_time)
            )

            st.success(
                "Reminder Added Successfully!"
            )

            st.rerun()

    st.divider()

    # =====================================
    # REMINDER LIST
    # =====================================

    st.subheader("📋 Active Reminders")

    reminders = get_all_reminders()

    if not reminders:

        st.info(
            "No reminders added yet."
        )

        return

    for reminder in reminders:

        reminder_id = reminder["id"]

        medicine = reminder["medicine_name"]

        time = reminder["reminder_time"]

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(
                f"""
                <div class="reminder-card">

                <h4>💊 {medicine}</h4>

                <p>
                🕒 {time}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            if st.button(
                "🗑",
                key=f"delete_{reminder_id}"
            ):

                delete_reminder(
                    reminder_id
                )

                st.success(
                    "Reminder Deleted"
                )

                st.rerun()

    st.divider()

    # =====================================
    # HEALTH TIPS
    # =====================================

    st.subheader("💡 Medication Tips")

    st.info(
        """
        • Take medicines exactly as prescribed.

        • Do not skip doses.

        • Keep medicines away from children.

        • Consult a doctor before changing dosage.

        • Maintain a healthy lifestyle.
        """
    )