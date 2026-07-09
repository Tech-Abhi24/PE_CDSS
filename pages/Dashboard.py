import streamlit as st
import pandas as pd
import os
import plotly.express as px

from cdss_brain import risk_engine
from ui_style import apply_ui


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="PE-CDSS Dashboard",
    layout="wide"
)

apply_ui()


# =========================
# LOGIN CHECK
# =========================

if "login" not in st.session_state or not st.session_state["login"]:
    st.warning("🔐 Please Login First")
    st.stop()



# =========================
# TITLE
# =========================

st.title(
    "🫁 Pulmonary Embolism Clinical Decision Support System"
)

st.caption(
    "AI-assisted PE risk assessment using a Wells-inspired clinical scoring model"
)



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


    # Patient ID fix

    df["patientID"] = pd.to_numeric(
        df["patientID"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["patientID"]
    )

    df["patientID"] = df["patientID"].astype(int)



    # AGE FIX

    if "Age" not in df.columns:

        if "birthdate" in df.columns:

            df["birthdate"] = pd.to_datetime(
                df["birthdate"],
                errors="coerce"
            )

            today = pd.Timestamp.today()

            df["Age"] = (
                today.year -
                df["birthdate"].dt.year
            )

        else:

            df["Age"] = 0


    return df



df = load_data()



# =========================
# APPLY PE ENGINE
# =========================

scores=[]
levels=[]
findings=[]
recommendations=[]


for _, row in df.iterrows():

    score, level, reason, rec = risk_engine(row)

    scores.append(score)

    levels.append(level)

    findings.append(
        ", ".join(reason)
    )

    recommendations.append(rec)



df["Wells Score"] = scores

df["PE Probability"] = levels

df["Clinical Findings"] = findings

df["Recommendation"] = recommendations




# =========================
# SIDEBAR FILTER
# =========================


st.sidebar.header(
    "🔍 PE Filters"
)


gender = st.sidebar.selectbox(
    "Gender",
    ["All"] +
    list(df["gender"].dropna().unique())
)


if gender != "All":

    df = df[
        df["gender"] == gender
    ]



probability = st.sidebar.selectbox(
    "PE Probability",
    [
        "All",
        "HIGH",
        "MODERATE",
        "LOW"
    ]
)


if probability != "All":

    df=df[
        df["PE Probability"]==probability
    ]





# =========================
# KPI CARDS
# =========================


st.markdown("---")

st.subheader(
    "📊 PE Clinical Overview"
)



high = len(
    df[df["PE Probability"]=="HIGH"]
)


moderate = len(
    df[df["PE Probability"]=="MODERATE"]
)


low = len(
    df[df["PE Probability"]=="LOW"]
)



c1,c2,c3,c4 = st.columns(4)



c1.metric(
    "👥 Total Patients",
    len(df)
)


c2.metric(
    "🔴 High PE Suspicion",
    high
)


c3.metric(
    "🟡 Moderate Suspicion",
    moderate
)


c4.metric(
    "🟢 Low Suspicion",
    low
)



c5,c6,c7,c8 = st.columns(4)


c5.metric(
    "🧮 Average Wells Score",
    round(df["Wells Score"].mean(),2)
)


c6.metric(
    "🎂 Average Age",
    round(df["Age"].mean(),1)
)


c7.metric(
    "💨 Avg Respiratory Rate",
    round(
        df["breathing_rate (per minute)"].mean(),
        2
    )
)


c8.metric(
    "🫁 Oxygenation",
    round(
        df["paO2/FiO2 (mmHg)"].mean(),
        2
    )
)





# =========================
# PE DISTRIBUTION
# =========================


st.markdown("---")


st.subheader(
    "🫁 PE Probability Distribution"
)



fig = px.histogram(
    df,
    x="PE Probability",
    color="PE Probability",
    title="Pulmonary Embolism Risk Classification"
)


st.plotly_chart(
    fig,
    use_container_width=True
)




# =========================
# HIGH PE ALERT
# =========================


st.markdown("---")


st.subheader(
    "🚨 High PE Suspicion Alert"
)



critical=df[
    df["PE Probability"]=="HIGH"
]



if len(critical)>0:

    st.error(
        f"⚠ {len(critical)} Patients with High PE Suspicion"
    )


    st.dataframe(

        critical[
            [
                "patientID",
                "Age",
                "gender",
                "Wells Score",
                "PE Probability",
                "Recommendation"
            ]
        ],

        use_container_width=True

    )


else:

    st.success(
        "No High PE Suspicion Patients Found"
    )




# =========================
# PE CLINICAL VIEW
# =========================


st.markdown("---")


st.subheader(
    "🫁 PE Clinical Indicators"
)



patient=df.iloc[0]



a,b,c=st.columns(3)



a.metric(
    "Respiratory Rate",
    patient["breathing_rate (per minute)"]
)



b.metric(
    "Blood Pressure",
    patient["systolic_blood_pressure (mmHg)"]
)



c.metric(
    "Oxygenation",
    patient["paO2/FiO2 (mmHg)"]
)





d,e,f=st.columns(3)


d.metric(
    "MAP",
    patient["MAP (mmHg)"]
)


e.metric(
    "Creatinine",
    patient["creatinine (mg/dl)"]
)


f.metric(
    "Wells Score",
    patient["Wells Score"]
)





# =========================
# RECENT PATIENTS
# =========================


st.markdown("---")


st.subheader(
    "📋 Recent PE Patient Monitoring"
)



st.dataframe(

    df[
        [
            "patientID",
            "Age",
            "gender",
            "Wells Score",
            "PE Probability",
            "Recommendation"
        ]
    ].head(10),

    use_container_width=True

)




# =========================
# FOOTER
# =========================


st.markdown("---")


st.caption(
    "🫁 Pulmonary Embolism Clinical Decision Support System | Wells-inspired Model | Version 1.0"
)