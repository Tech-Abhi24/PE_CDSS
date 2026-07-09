import streamlit as st

def login():

    st.title("🏥 Hospital CDSS Login")

    st.markdown("### Doctor Authentication System")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):

        if username == "doctor" and password == "1234":

            st.session_state["logged_in"] = True
            st.session_state["user"] = username

            st.success("Login Successful ✔")

            st.rerun()

        else:
            st.error("Invalid Credentials ❌")