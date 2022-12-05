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

data = get_data(place, forecast_days, option)

# Creating a 'plotly' figure for the line-graph in the graph.
#figure = px.line(x= , y= , labels={"x":" ", "y":""})
# Creating the graph.
#st.plotly_chart(figure)