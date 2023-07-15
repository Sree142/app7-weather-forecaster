import streamlit as st

st.title("Weather Forecaster for the Next 5 Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, 
                 max_value=5, help="Select the number of days you want to know the weather of.")
option = st.selectbox("Select data to view: ", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")