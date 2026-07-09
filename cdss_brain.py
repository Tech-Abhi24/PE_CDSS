import pandas as pd

# =====================================================
# PE-CDSS (Wells-inspired Clinical Decision Engine)
# =====================================================

def risk_engine(row):

    score = 0
    findings = []

    # -----------------------------
    # Oxygenation
    # -----------------------------
    if row["paO2/FiO2 (mmHg)"] < 300:
        score += 3
        findings.append("Reduced oxygenation (possible PE indicator)")

    # -----------------------------
    # Blood Pressure
    # -----------------------------
    if row["systolic_blood_pressure (mmHg)"] < 90:
        score += 2
        findings.append("Hypotension")

    # -----------------------------
    # Respiratory Rate
    # -----------------------------
    if row["breathing_rate (per minute)"] > 20:
        score += 2
        findings.append("Tachypnea")

    # -----------------------------
    # MAP
    # -----------------------------
    if row["MAP (mmHg)"] < 65:
        score += 1
        findings.append("Low Mean Arterial Pressure")

    # -----------------------------
    # Noradrenaline Support
    # -----------------------------
    if row["noradrenaline_dose (µg/kg/min)"] > 0:
        score += 1
        findings.append("Hemodynamic support required")

    # =====================================================
    # PE Probability (Wells-inspired)
    # =====================================================

    if score >= 7:

        probability = "HIGH"

        recommendation = (
            "High clinical suspicion of Pulmonary Embolism.\n"
            "Immediate physician assessment.\n"
            "Recommend CT Pulmonary Angiography (CTPA).\n"
            "Consider anticoagulation according to hospital protocol."
        )

    elif score >= 4:

        probability = "MODERATE"

        recommendation = (
            "Moderate clinical suspicion of Pulmonary Embolism.\n"
            "Recommend D-dimer testing.\n"
            "If D-dimer is positive, perform CTPA."
        )

    else:

        probability = "LOW"

        recommendation = (
            "Pulmonary Embolism is currently unlikely.\n"
            "Continue routine clinical monitoring."
        )

    return score, probability, findings, recommendation


# =====================================================
# AGE CALCULATION
# =====================================================

def calculate_age(birthdate):

    try:

        birthdate = pd.to_datetime(birthdate)

        today = pd.Timestamp.today()

        age = today.year - birthdate.year

        if (
            today.month,
            today.day
        ) < (
            birthdate.month,
            birthdate.day
        ):
            age -= 1

        return age

    except:
        return "N/A"