import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

teams = [
    'Pakistan',
    'South Africa',
    'India',
    'New Zealand',
    'Sri Lanka',
    'West Indies',
    'Australia',
    'England',
    'Bangladesh',
    'Zimbabwe',
    'Afghanistan',
    'Ireland',
    'Netherlands'
]

st.title("T20 Cricket Score Predictor")

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("Select the Batting Team", sorted(teams))
with col2:
    bowling_team = st.selectbox("Select the Bowling Team", sorted(teams))

col3, col4, col5, col6 = st.columns(4)

with col3:
    current_score = st.number_input("Current Score", min_value=0)
with col4:
    overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10)
with col6:
    crr = st.number_input("Current Run Rate", min_value=0.0)


if st.button("Predict Score"):

    input_df = pd.DataFrame({
        'battingTeam': [batting_team],
        'bowlingTeam': [bowling_team],
        'current_score': [current_score],
        'balls': [overs],
        'wickets': [wickets],
        'crr': [crr]
    })
    

    predicted_score = pipe.predict(input_df)[0]
    st.header(f"Predicted Final Score: {int(predicted_score)}")

