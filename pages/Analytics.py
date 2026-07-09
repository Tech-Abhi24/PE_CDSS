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
    page_title="PE-CDSS Analytics",
    layout="wide"
)

apply_ui()


st.title(
    "📊 Pulmonary Embolism Clinical Analytics"
)

st.caption(
    "Analysis of PE risk patterns using Wells-inspired clinical scoring"
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



    # Patient ID Fix
    df["patientID"] = pd.to_numeric(
        df["patientID"],
        errors="coerce"
    )


    df = df.dropna(
        subset=["patientID"]
    )


    df["patientID"] = df["patientID"].astype(int)



    # =========================
    # AGE FIX
    # =========================

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



for _,row in df.iterrows():


    score,level,reason,rec = risk_engine(row)


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
# KPI CARDS
# =========================

st.markdown("---")

st.subheader(
    "🫁 PE Clinical Statistics"
)



c1,c2,c3,c4 = st.columns(4)



c1.metric(
    "Total Patients",
    len(df)
)



c2.metric(
    "High PE Suspicion",
    len(
        df[df["PE Probability"]=="HIGH"]
    )
)



c3.metric(
    "Average Wells Score",
    round(
        df["Wells Score"].mean(),
        2
    )
)



c4.metric(
    "Average Age",
    round(
        df["Age"].fillna(0).mean(),
        1
    )
)





# =========================
# PE DISTRIBUTION
# =========================


st.markdown("---")

st.subheader(
    "🫁 PE Probability Distribution"
)



fig1 = px.pie(

    df,

    names="PE Probability",

    title="Pulmonary Embolism Risk Classification"

)


st.plotly_chart(
    fig1,
    use_container_width=True
)





# =========================
# WELLS SCORE
# =========================


st.markdown("---")


st.subheader(
    "🧮 Wells Score Analysis"
)



fig2 = px.histogram(

    df,

    x="Wells Score",

    color="PE Probability",

    title="Distribution of Wells PE Scores"

)


st.plotly_chart(
    fig2,
    use_container_width=True
)





# =========================
# CLINICAL PARAMETERS
# =========================


st.markdown("---")

st.subheader(
    "🧪 PE Clinical Parameter Analysis"
)



col1,col2 = st.columns(2)



with col1:


    fig3 = px.scatter(

        df,

        x="breathing_rate (per minute)",

        y="Wells Score",

        color="PE Probability",

        title="Respiratory Rate vs PE Score"

    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )




with col2:


    fig4 = px.scatter(

        df,

        x="paO2/FiO2 (mmHg)",

        y="Wells Score",

        color="PE Probability",

        title="Oxygenation vs PE Score"

    )


    st.plotly_chart(
        fig4,
        use_container_width=True
    )





# =========================
# OXYGEN MONITORING
# =========================


st.markdown("---")


st.subheader(
    "🫁 Oxygenation Monitoring"
)



fig5 = px.histogram(

    df,

    x="paO2/FiO2 (mmHg)",

    color="PE Probability",

    title="Oxygenation Distribution"

)


st.plotly_chart(
    fig5,
    use_container_width=True
)





# =========================
# INSIGHTS
# =========================


st.markdown("---")


st.subheader(
    "💡 Clinical Decision Insights"
)



high = df[
    df["PE Probability"]=="HIGH"
]



if len(high)>0:


    st.warning(

f"""
⚠ {len(high)} patients show high probability of Pulmonary Embolism.


Clinical Findings:

{high["Clinical Findings"].head(5).tolist()}


Recommendation:

{high["Recommendation"].iloc[0]}

"""
    )


else:


    st.success(
        "No high PE probability pattern detected."
    )





# =========================
# SUMMARY TABLE
# =========================


st.markdown("---")


st.subheader(
    "📋 PE Patient Risk Summary"
)



st.dataframe(

    df[

        [
            "patientID",
            "Age",
            "gender",
            "Wells Score",
            "PE Probability",
            "Clinical Findings",
            "Recommendation"
        ]

    ],

    use_container_width=True

)