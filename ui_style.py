import streamlit as st


def apply_ui():

    st.markdown(
        """
        <style>

        /* Main Background */

        [data-testid="stAppViewContainer"] {

            background-color:#f4f7fb;

        }



        /* Header */

        h1,h2,h3 {

            color:#1a1a1a;
            font-family:Arial;

        }



        /* Cards */

        [data-testid="stMetric"] {

            background:white;

            padding:20px;

            border-radius:15px;

            box-shadow:
            0px 3px 12px rgba(0,0,0,0.10);

        }



        /* Metric Value */

        [data-testid="stMetricValue"] {

            font-size:28px;

            font-weight:bold;

        }



        /* Buttons */

        .stButton>button {

            background-color:#0066ff;

            color:white;

            border-radius:10px;

            padding:10px 20px;

            font-weight:bold;

        }


        .stButton>button:hover {

            background-color:#004ecc;

            color:white;

        }



        /* Info Box */

        [data-testid="stAlert"] {

            border-radius:12px;

        }


        </style>
        """,

        unsafe_allow_html=True
    )