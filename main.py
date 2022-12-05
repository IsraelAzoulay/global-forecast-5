# Eighth project -
import streamlit as st
# Importing the module 'express' of the 'plotly' library for creating the line-graph.
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
forecast_days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {forecast_days} days in {place}")


# Getting the data from the backend only in case that the user entered a 'place', so there won't be
# a "key_error" in the beginning before the user entered a 'place'.
if place:
    try:
        # Getting a list with all the forecast hour updates based on the 'forecast_days' the user entered.
        filtered_data = get_data(place, forecast_days)

        # Once the data is filtered based on the 'forecast_days' the user entered and I got it in
        # the 'filtered_data' variable, I filter it again based on the 'option' the user entered.
        if option == "Temperature":
            # Extracting a list with all the temperatures, and dividing them by 10 in order to get the accurate temp.
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Creating a 'plotly' figure for the line-graph in the graph.
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            # Creating the Temperature graph.
            st.plotly_chart(figure)

        if option == "Sky":
            # Extracting a list with all the sky's cases.
            sky_cases = [dict["weather"][0]["main"] for dict in filtered_data]
            # Creating a dictionary that contains all the sky's cases and their corresponding image.
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            # Translating all the sky's cases to their corresponding image.
            images_path = [images[case] for case in sky_cases]
            st.image(images_path, width=115)
    except KeyError:
        st.info("The place you entered doesn't exist. Please enter an existing place.")