import streamlit as st

st.image("assets/hospital.png", use_container_width=True)

st.title("🔐 Doctor Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "doctor" and password == "admin":

        st.session_state["login"] = True
        st.success("Login Successful ✔")

        # ❌ REMOVE switch_page (CAUSES ERROR)
        st.info("Now go to Dashboard from sidebar or app")

    else:
        st.error("Invalid Credentials")