import streamlit as st
import pandas as pd
import os
from datetime import date
from cdss_brain import risk_engine


st.set_page_config(
    page_title="Add New Patient",
    layout="wide"
)


st.title("➕ New ICU Patient Registration")

st.caption(
    "Enter clinical parameters to add a new patient into CDSS"
)


# ==========================
# LOGIN CHECK
# ==========================

if "login" not in st.session_state or not st.session_state["login"]:

    st.warning("Please login first")

    st.stop()



# ==========================
# DATABASE PATH
# ==========================

file_path = os.path.join(
    "data",
    "patients.xlsx"
)



# ==========================
# FORM
# ==========================

with st.form("patient_form"):


    st.subheader("👤 Patient Information")


    col1,col2,col3 = st.columns(3)


    with col1:

        patientID = st.number_input(
            "Patient ID",
            step=1
        )


        caseID = st.text_input(
            "Case ID"
        )


        birthdate = st.date_input(
            "Birth Date"
        )


    with col2:

        gender = st.selectbox(
            "Gender",
            ["Male","Female","Other"]
        )


        GCS = st.number_input(
            "GCS Score",
            min_value=3,
            max_value=15,
            value=15
        )


        breathing = st.number_input(
            "Breathing Rate",
            value=18
        )


    with col3:

        bp = st.number_input(
            "Systolic Blood Pressure",
            value=120
        )


        creatinine = st.number_input(
            "Creatinine",
            value=1.0
        )


        bilirubin = st.number_input(
            "Bilirubin",
            value=1.0
        )



    st.subheader("🫀 ICU Parameters")


    col4,col5,col6 = st.columns(3)


    with col4:

        platelets = st.number_input(
            "Thrombocytes",
            value=200000
        )


        adrenaline = st.number_input(
            "Adrenaline Dose",
            value=0.0
        )


    with col5:

        dopamine = st.number_input(
            "Dopamine Dose",
            value=0.0
        )


        noradrenaline = st.number_input(
            "Noradrenaline Dose",
            value=0.0
        )


    with col6:

        MAP = st.number_input(
            "MAP",
            value=80
        )


        oxygen = st.number_input(
            "PaO2/FiO2",
            value=300
        )



    submit = st.form_submit_button(
        "💾 Save Patient"
    )





# ==========================
# SAVE DATA
# ==========================


if submit:


    new_patient = {


        "patientID":patientID,

        "caseID":caseID,

        "date":date.today(),

        "birthdate":birthdate,

        "gender":gender,

        "GCS":GCS,

        "breathing_rate (per minute)":breathing,

        "systolic_blood_pressure (mmHg)":bp,

        "bilirubin (mg/dl)":bilirubin,

        "thrombocytes (per µl)":platelets,

        "creatinine (mg/dl)":creatinine,

        "adrenaline_dose (µg/kg/min)":adrenaline,

        "dopamine_dose (µg/kg/min)":dopamine,

        "noradrenaline_dose (µg/kg/min)":noradrenaline,

        "MAP (mmHg)":MAP,

        "paO2/FiO2 (mmHg)":oxygen

    }



    patient_df = pd.DataFrame(
        [new_patient]
    )



    # RUN CDSS ENGINE

    score,level,reasons,rec = risk_engine(
        patient_df.iloc[0]
    )



    patient_df["Risk Score"] = score

    patient_df["Clinical Findings"] = ", ".join(reasons)

    patient_df["Risk Level"] = level

    patient_df["Status"] = "Active"

    patient_df["Recommendation"] = rec



    # OLD DATA LOAD


    if os.path.exists(file_path):

        old_df = pd.read_excel(file_path)


        final_df = pd.concat(
            [
                old_df,
                patient_df
            ],
            ignore_index=True
        )

    else:

        final_df = patient_df



    final_df.to_excel(
        file_path,
        index=False
    )



    st.success(
        "✅ Patient Added Successfully"
    )


    st.info(
f"""
Patient ID: {patientID}

Risk Level: {level}

Risk Score: {score}

Recommendation:
{rec}
"""
    )