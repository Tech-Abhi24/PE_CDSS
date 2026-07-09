import streamlit as st
from ui_style import apply_ui

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="CDSS System",
    page_icon="🏥",
    layout="wide"
)
apply_ui()

# =========================
# HOME UI
# =========================

st.title("🏥 Clinical Decision Support System (CDSS)")

st.caption(
    "AI-assisted hospital decision system for patient risk analysis"
)



# =========================
# SESSION INIT
# =========================

if "login" not in st.session_state:

    st.session_state["login"] = False



# =========================
# LOGIN CHECK
# =========================


if not st.session_state["login"]:



    st.info(
        "🔐 Please login to access clinical modules"
    )


    page = st.selectbox(
        "Choose Page",
        [
            "Login"
        ]
    )



    if page == "Login":

        st.switch_page(
            "pages/login.py"
        )



# =========================
# AFTER LOGIN
# =========================


else:


    st.success(
        "Logged in ✔"
    )


    st.markdown("---")


    st.subheader(
        "🏥 CDSS Modules"
    )



    col1,col2,col3,col4 = st.columns(4)



    with col1:

        st.info(
            """
            📊

            Dashboard

            Patient monitoring
            and risk overview
            """
        )


    with col2:

        st.info(
            """
            👤

            Patient Profile

            Individual clinical
            assessment
            """
        )


    with col3:

        st.info(
            """
            📈

            Analytics

            Clinical trends
            and statistics
            """
        )


    with col4:

        st.info(
            """
            📄

            Reports

            Risk reports
            and audit logs
            """
        )



    st.markdown("---")



    # =========================
    # NAVIGATION
    # =========================


    page = st.selectbox(

        "Navigate",

        [
            "Dashboard",
            "Patient Profile",
            "Analytics",
            "Reports",
            "Add Patient"
        ]

    )



    if page == "Dashboard":


        st.switch_page(
            "pages/Dashboard.py"
        )



    elif page == "Patient Profile":


        st.switch_page(
            "pages/Patient_Profile.py"
        )



    elif page == "Analytics":


        st.switch_page(
            "pages/Analytics.py"
        )



    elif page == "Reports":


        st.switch_page(
            "pages/Reports.py"
        )

    elif page == "Add Patient":
        
        st.switch_page(
            "pages/Add_Patient.py"
        )




    # =========================
    # SAFETY MESSAGE
    # =========================


    st.markdown("---")


    st.warning(
        """
        ⚠ Clinical Safety Notice

        This CDSS provides decision support only.
        Final diagnosis and treatment decisions
        remain the responsibility of healthcare professionals.
        """
    )