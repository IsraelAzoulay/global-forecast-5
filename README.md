# GlobalForecast5

GlobalForecast5 is a web application designed to provide weather forecasting for any place globally for up to 5 days. You can choose to view temperature or sky conditions, visualized using line graphs or relevant images.

![App Design](App_Design.png)

## Features

- Weather forecast for any global location
- Selection of forecast duration up to 5 days
- Option to view temperature trends or sky conditions
- Interactive user interface using Streamlit
- Visual representation using Plotly for temperature and images for sky conditions

## Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- pip

## Installation & Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/[YourUsername]/GlobalForecast5.git

## Navigate to the project directory:

cd GlobalForecast5

## Install the necessary dependencies:

pip install -r requirements.txt

## Environment Variable Setup:

Before running the application, you need to set up your OpenWeatherMap API key. Create a .env file in the project root and add your API key:

OPEN_WEATHER_API_KEY=your_api_key_here

## Run the Streamlit app:

streamlit run main.py

Open the provided link in your browser and enjoy the application!

## Directory Structure

- 'main.py': The main application file containing the Streamlit UI components and logic.
- 'backend.py': Backend logic for fetching and processing weather data.
- 'requirements.txt': List of Python dependencies.
- 'images/': Directory containing images representing different sky conditions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
