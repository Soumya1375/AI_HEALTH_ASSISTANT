import streamlit as st
from modules.auth.auth_service import register_user, login_user


# ==========================================
# LOGIN PAGE UI
# ==========================================
def show_login_page():

    st.title("🔐 AI Health Assistant Login")

    st.markdown("Login to access your health dashboard 🚀")

    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Register"])


    # ======================================
    # LOGIN TAB
    # ======================================
    with tab1:

        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login 🚀"):

            if username == "" or password == "":
                st.warning("Please fill all fields")
                return

            user = login_user(username, password)

            if user:
                st.session_state["user"] = username

                st.success("Login successful 🚀 Welcome!")

                st.rerun()   # 🔥 IMPORTANT FIX

            else:
                st.error("Invalid username or password ❌")


    # ======================================
    # REGISTER TAB
    # ======================================
    with tab2:

        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register 🆕"):

            if new_user == "" or new_pass == "":
                st.warning("Please fill all fields")
                return

            success = register_user(new_user, new_pass)

            if success:
                st.success("Account created successfully ✔ You can login now")
            else:
                st.error("Username already exists ❌ Try another one")