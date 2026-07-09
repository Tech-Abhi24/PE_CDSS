# 🫁 Pulmonary Embolism Clinical Decision Support System (PE-CDSS)

A Clinical Decision Support System (CDSS) developed using **Python** and **Streamlit** to assist clinicians in the **early assessment of Pulmonary Embolism (PE)** using a **Wells-inspired clinical scoring model**.

---

# 📌 Overview

Pulmonary Embolism (PE) is a life-threatening condition that requires rapid assessment in the Emergency Department.

This project provides an interactive Clinical Decision Support System that helps healthcare professionals:

- Assess PE risk
- Calculate Wells-inspired clinical score
- Classify patients into PE probability groups
- Display ICU clinical information
- Generate PDF clinical reports
- Monitor patients through an analytics dashboard

> **Note:** This system is intended for educational and research purposes only. It supports clinical decision-making and does not replace physician judgment.

---

# ✨ Features

✅ Doctor Login Authentication

✅ Dashboard for PE Risk Monitoring

✅ Patient Registration Form

✅ Patient Search by Patient ID

✅ Wells-inspired PE Risk Scoring

✅ Clinical Recommendation Generation

✅ ICU Patient Monitoring

✅ Interactive Analytics Dashboard

✅ PDF Report Generation

✅ Responsive Streamlit UI

---



# 🏗️ System Architecture

```
                Doctor

                   │

             Login Authentication

                   │

            Patient Registration

                   │

            Patient Dataset (.xlsx)

                   │

           Data Validation & Cleaning

                   │

           Wells-inspired Risk Engine

                   │

        PE Probability Classification

                   │

        Dashboard / Analytics / Report

                   │

         Clinical Recommendation
```

---

# 📂 Project Structure

```
PE_CDSS_System
│
├── app.py
├── cdss_brain.py
├── ui_style.py
├── style.css
├── requirements.txt
│
├── data
│   └── patients.xlsx
│
├── pages
│   ├── login.py
│   ├── Dashboard.py
│   ├── Patient_Profile.py
│   ├── Analytics.py
│   └── Patient_Registration.py
│
├── assets
│
├── utils
│
└── README.md
```

---

# 🧠 Clinical Workflow

```
Doctor Login

↓

Patient Registration / Search

↓

Patient Clinical Parameters

↓

Wells-inspired Risk Calculation

↓

PE Probability Classification

↓

Clinical Recommendation

↓

PDF Report Generation
```

---

# ⚙️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL
- FPDF
- NumPy

---

---

# Login Credentials:
Username-doctor
Password-admin

---

# 🚀 Installation

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/PE_CDSS_System.git
```

### Open Project

```bash
cd PE_CDSS_System
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---


# 📊 Dataset

The project uses an ICU clinical dataset stored as

```
data/patients.xlsx
```

The dataset contains:

- Patient ID
- Case ID
- Birth Date
- Gender
- GCS
- Blood Pressure
- MAP
- Respiratory Rate
- Creatinine
- Bilirubin
- Platelets
- Vasopressor Doses
- Oxygenation (PaO₂/FiO₂)

---

# 🫁 PE Risk Classification

The system calculates a Wells-inspired clinical score.

| Score | Probability |
|--------|-------------|
| Low | Low PE Probability |
| Medium | Moderate PE Probability |
| High | High PE Probability |

---

# 📈 Modules

### Dashboard

- Hospital Statistics
- High Risk Alerts
- ICU Monitoring
- Recent Patients

---

### Patient Profile

- Patient Information
- Vital Signs
- Laboratory Results
- Wells Score
- PE Probability
- Clinical Recommendation
- PDF Report

---

### Analytics

- PE Probability Distribution
- Wells Score Analysis
- Oxygenation Analysis
- Clinical Insights

---

### Patient Registration

Allows clinicians to register a new ICU patient and automatically save the patient record.

---

# 📄 PDF Report

The system generates a downloadable clinical report including

- Patient Information
- Vital Signs
- Wells Score
- PE Probability
- Clinical Findings
- Clinical Recommendation

---

# 🔒 Security Features

- Login Authentication
- Session Management
- Data Validation
- Patient ID Validation

---

# 📚 Academic Context

Developed as part of the

**Clinical Decision Support Systems (CDSS)**

Master of Data Science

Carl von Ossietzky University of Oldenburg

---

# 👨‍💻 Author

**Abhishek Verma**

M.Sc. Data Science

University of Oldenburg

---

# 📜 License

This project is released under the MIT License.
