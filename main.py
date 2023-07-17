import streamlit as st
import plotly.express as px
from backend import get_data
from PIL import Image
from io import BytesIO
import requests

st.title("Weather Forecaster for the Next 5 Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, 
                 max_value=5, help="Select the number of days you want to know the weather of.")
option = st.selectbox("Select data to view: ", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        data = get_data(place, days)
    except:
        st.error("Please enter a valid place!")
    dates = [dict["dt_txt"] for dict in data]

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperature(C)"})
        st.plotly_chart(figure)

    elif option == "Sky":
        weather = [dict["dt_txt"]+": "+ dict["weather"][0]["main"] for dict in data]
        weather_icon = [dict["weather"][0]["icon"] for dict in data]
        weather_responses = [requests.get(f"https://openweathermap.org/img/wn/{icon}@2x.png") for icon in weather_icon]
        weather_images = [Image.open(BytesIO(response.content)) for response in weather_responses]
        st.image(weather_images, weather, width=200)
