# PE_CDSS
A Streamlit-based Clinical Decision Support System (CDSS) for Pulmonary Embolism risk assessment with patient analytics, risk prediction, and PDF report generation.
# Pulmonary Embolism Clinical Decision Support System (PE-CDSS)

## Overview

This project is a Clinical Decision Support System (CDSS) developed for Pulmonary Embolism (PE) risk assessment.

The application allows clinicians to:

- Login securely
- View patient profiles
- Calculate PE Risk Score
- Generate clinical recommendations
- Visualize patient analytics
- Export PDF reports

---

## Features

- Doctor Login
- Patient Dashboard
- Risk Prediction
- Clinical Recommendation
- Analytics Dashboard
- PDF Report Generation
- Streamlit Interface

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- FPDF

---

## Folder Structure

```
PE-CDSS-System
│
├── app.py
├── cdss_brain.py
├── dashboard.py
├── report.py
├── pages/
├── data/
├── screenshots/
└── requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/PE-CDSS-System.git
```

Move inside project

```bash
cd PE-CDSS-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

## Dataset

The patient dataset is stored inside the **data** folder.

---


---

## Author

Abhishek Verma

M.Sc. Data Science and Machine Learning

University of Oldenburg

Requirements.txt
streamlit
pandas
numpy
plotly
openpyxl
fpdf



.gitignore

__pycache__/
*.pyc
*.pyo

.venv/
venv/

.env

.idea/
.vscode/

reports/

*.pdf


LICENSE

MIT License


#Bash
git init

git add .

git commit -m "Initial commit - PE CDSS System"

git branch -M main

git remote add origin https://github.com/<your-username>/PE-CDSS-System.git

git push -u origin main
