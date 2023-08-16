# The backend of the program.
import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

def get_data(place, forecast_days):
    # The url of the api of the 'openweathermap.org' website.
    url_api = f"http://api.openweathermap.org/data/2.5/forecast?" \
              f"q={place}&" \
              f"appid={API_KEY}"
    # Making the request for the url of the api.
    url_api_response = requests.get(url_api)
    # Getting all the url data in a dictionary.
    data = url_api_response.json()
    # Filtering all the data we got in the 'json()' format, and getting all the 40 forecast updates which
    # are for the maximum days number - 5 days (since there is a forecast update every 3 hours).
    filtered_data = data["list"]
    # Filtering now all the 40 hours forecast updates based on the 'forecast_days' the user entered,
    # and returning it in a list to the main.py file. The minimum of forecast updates are 8 which are
    # for the minimum days number - 1 day.
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data


# The 'get_data()' func will run only when the backend.py file is executed and
# not when the func is imported to somewhere else.
if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))