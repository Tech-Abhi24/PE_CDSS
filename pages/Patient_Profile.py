import streamlit as st
import pandas as pd
import os
from cdss_brain import risk_engine, calculate_age
from fpdf import FPDF
from ui_style import apply_ui


# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="PE Patient Profile",
    layout="wide"
)

apply_ui()


st.title("🫁 PE Patient Clinical Profile")

st.caption(
    "Pulmonary Embolism assessment using Wells-inspired clinical scoring"
)



# ==============================
# LOAD DATA
# ==============================

file_path = os.path.join(
    "data",
    "patients.xlsx"
)


df = pd.read_excel(file_path)


df.columns = df.columns.str.strip()



# Patient ID cleaning

df["patientID"] = pd.to_numeric(
    df["patientID"],
    errors="coerce"
)


df = df.dropna(
    subset=["patientID"]
)


df["patientID"] = df["patientID"].astype(int)



# Case ID fix

if "caseID" in df.columns:

    df["caseID"] = (
        pd.to_numeric(
            df["caseID"],
            errors="coerce"
        )
        .fillna(0)
        .astype(int)
    )




# ==============================
# SEARCH PATIENT
# ==============================


pid = st.number_input(
    "Enter Patient ID",
    step=1
)





# ==============================
# PDF GENERATION
# ==============================


def generate_pdf(
        patient,
        age,
        score,
        level,
        reasons,
        rec):


    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )


    pdf.cell(
        200,
        10,
        "Pulmonary Embolism CDSS Report",
        ln=True,
        align="C"
    )


    pdf.ln(5)



    data=[


        f"Patient ID: {patient['patientID']}",

        f"Case ID: {patient['caseID']}",

        f"Date: {patient['date']}",

        f"Age: {age}",

        f"Gender: {patient['gender']}",


        "",

        "Clinical Parameters",

        f"Respiratory Rate: {patient['breathing_rate (per minute)']}",

        f"Blood Pressure: {patient['systolic_blood_pressure (mmHg)']}",

        f"MAP: {patient['MAP (mmHg)']}",

        f"Oxygenation: {patient['paO2/FiO2 (mmHg)']}",


        "",

        f"Wells-inspired PE Score: {score}",

        f"PE Probability: {level}",


        "",

        f"Clinical Findings: {', '.join(reasons)}",


        "",

        f"Recommendation: {rec}"


    ]



    for item in data:

        pdf.cell(
            200,
            10,
            item,
            ln=True
        )



    filename="PE_patient_report.pdf"


    pdf.output(filename)


    return filename





# ==============================
# SEARCH BUTTON
# ==============================


if st.button("🔍 Search Patient"):


    pid=int(pid)


    result=df[
        df["patientID"]==pid
    ]



    if result.empty:


        st.error(
            "❌ Patient Not Found"
        )


        st.write(
            "Sample IDs:",
            df["patientID"].head(10).tolist()
        )



    else:


        row=result.iloc[0]


        age=calculate_age(
            row["birthdate"]
        )


        score, level, reasons, rec = risk_engine(row)



        st.success(
            "Patient Found ✔"
        )



        # ==============================
        # PATIENT INFORMATION
        # ==============================


        st.markdown("---")


        st.subheader(
            "👤 Patient Information"
        )


        c1,c2,c3,c4=st.columns(4)


        c1.metric(
            "Patient ID",
            row["patientID"]
        )


        c2.metric(
            "Age",
            age
        )


        c3.metric(
            "Gender",
            row["gender"]
        )


        c4.metric(
            "Case ID",
            row["caseID"]
        )





        # ==============================
        # PE INDICATORS
        # ==============================


        st.markdown("---")


        st.subheader(
            "🫁 PE Clinical Indicators"
        )



        c1,c2,c3,c4=st.columns(4)


        c1.metric(
            "Respiratory Rate",
            row["breathing_rate (per minute)"]
        )


        c2.metric(
            "Blood Pressure",
            row["systolic_blood_pressure (mmHg)"]
        )


        c3.metric(
            "MAP",
            row["MAP (mmHg)"]
        )


        c4.metric(
            "Oxygenation",
            row["paO2/FiO2 (mmHg)"]
        )




        c5,c6=st.columns(2)


        c5.metric(
            "Creatinine",
            row["creatinine (mg/dl)"]
        )


        c6.metric(
            "Platelets",
            row["thrombocytes (per µl)"]
        )





        # ==============================
        # PE RESULT
        # ==============================


        st.markdown("---")


        st.subheader(
            "🫁 Pulmonary Embolism Assessment"
        )



        c1,c2=st.columns(2)


        c1.metric(
            "🧮 Wells-inspired Score",
            score
        )


        c2.metric(
            "🫁 PE Probability",
            level
        )



        st.warning(
            "Clinical Findings"
        )


        for r in reasons:

            st.write(
                "•",
                r
            )



        st.info(
            "📢 Recommendation\n\n"+rec
        )





        # ==============================
        # SUMMARY CARD
        # ==============================


        st.markdown("---")


        st.subheader(
            "📌 PE Clinical Summary Card"
        )



        st.info(
f"""
🆔 Patient ID: {pid}

👤 Age: {age}

⚕ Gender: {row['gender']}


💨 Respiratory Rate:
{row['breathing_rate (per minute)']}


🫁 Oxygenation:
{row['paO2/FiO2 (mmHg)']}


🧮 Wells-inspired PE Score:
{score}


🫁 PE Probability:
{level}


💡 Findings:

{", ".join(reasons)}


📢 Recommendation:

{rec}

"""
        )





        # ==============================
        # PDF DOWNLOAD
        # ==============================


        pdf_file=generate_pdf(
            row,
            age,
            score,
            level,
            reasons,
            rec
        )



        with open(pdf_file,"rb") as f:


            st.download_button(

                "📄 Download PE Clinical Report",

                f,

                file_name=f"PE_patient_{pid}_report.pdf",

                mime="application/pdf"

            )