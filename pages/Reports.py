import streamlit as st
import pandas as pd
import os
from cdss_brain import risk_engine
from ui_style import apply_ui

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="CDSS Reports",
    page_icon="📄",
    layout="wide"
)
apply_ui()

st.title("📄 Clinical Reports Module")

st.caption(
    "Patient reports, clinical audit and risk documentation"
)



# =========================
# LOGIN CHECK
# =========================

if "login" not in st.session_state or not st.session_state["login"]:

    st.warning("🔐 Please login first")

    st.stop()



# =========================
# LOAD DATA
# =========================


@st.cache_data
def load_data():

    file_path = os.path.join(
        "data",
        "patients.xlsx"
    )

    df = pd.read_excel(file_path)

    df.columns = df.columns.str.strip()


    df["patientID"] = pd.to_numeric(
        df["patientID"],
        errors="coerce"
    )


    df = df.dropna(
        subset=["patientID"]
    )


    df["patientID"] = df["patientID"].astype(int)


    return df



df = load_data()



# =========================
# APPLY CDSS ENGINE
# =========================


risk_score=[]
risk_level=[]
clinical=[]
recommendation=[]


for _,row in df.iterrows():

    score,level,reason,rec = risk_engine(row)

    risk_score.append(score)

    risk_level.append(level)

    clinical.append(
        ", ".join(reason)
    )

    recommendation.append(rec)



df["Risk Score"] = risk_score

df["Risk Level"] = risk_level

df["Clinical Findings"] = clinical

df["Recommendation"] = recommendation




# =========================
# REPORT STATISTICS
# =========================


st.markdown("---")

st.subheader("📊 Report Statistics")


c1,c2,c3,c4 = st.columns(4)


c1.metric(
    "Total Patients",
    len(df)
)


c2.metric(
    "High Risk",
    len(df[df["Risk Level"]=="HIGH"])
)


c3.metric(
    "Medium Risk",
    len(df[df["Risk Level"]=="MEDIUM"])
)


c4.metric(
    "Low Risk",
    len(df[df["Risk Level"]=="LOW"])
)



# =========================
# SAVED PDF REPORTS
# =========================


st.markdown("---")

st.subheader("📂 Generated PDF Reports")



report_folder = "reports"



if os.path.exists(report_folder):


    pdf_files = [

        f for f in os.listdir(report_folder)

        if f.endswith(".pdf")

    ]



    if len(pdf_files)>0:


        for pdf in pdf_files:


            file_path = os.path.join(
                report_folder,
                pdf
            )


            with open(file_path,"rb") as file:


                st.download_button(

                    label=f"⬇ Download {pdf}",

                    data=file,

                    file_name=pdf,

                    mime="application/pdf"

                )



    else:


        st.info(
            "No PDF reports generated yet"
        )


else:


    st.info(
        "Reports folder not found"
    )





# =========================
# HIGH RISK PATIENT REPORT
# =========================


st.markdown("---")

st.subheader(
    "🚨 Critical Patient Reports"
)



critical = df[
    df["Risk Level"]=="HIGH"
]



if not critical.empty:


    st.error(
        f"{len(critical)} High Risk Patients Detected"
    )


    st.dataframe(

        critical[
            [
                "patientID",
                "gender",
                "GCS",
                "creatinine (mg/dl)",
                "Risk Score",
                "Risk Level",
                "Recommendation"
            ]
        ],

        use_container_width=True

    )


else:


    st.success(
        "No critical patients found"
    )




# =========================
# SEARCH PATIENT REPORT
# =========================


st.markdown("---")

st.subheader(
    "🔍 Patient Report Search"
)



pid = st.number_input(
    "Enter Patient ID",
    step=1
)



if st.button("View Report"):


    result = df[
        df["patientID"]==pid
    ]



    if result.empty:


        st.error(
            "Patient not found"
        )


    else:


        patient=result.iloc[0]


        st.success(
            "Report Generated ✔"
        )


        st.info(
f"""
🆔 Patient ID:
{patient['patientID']}


⚠ Risk Level:
{patient['Risk Level']}


📊 Risk Score:
{patient['Risk Score']}


🧠 Clinical Findings:

{patient['Clinical Findings']}


📢 Recommendation:

{patient['Recommendation']}

"""
        )





# =========================
# AUDIT LOG
# =========================


st.markdown("---")

st.subheader(
    "📋 Clinical Audit Log"
)



st.dataframe(

    df[
        [
            "patientID",
            "Risk Score",
            "Risk Level",
            "Clinical Findings",
            "Recommendation"
        ]
    ],

    use_container_width=True

)