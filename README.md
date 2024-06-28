# WeatherApp

WeatherApp is a simple Python application that retrieves and displays weather information for a specified city using the OpenWeatherMap API.

## Features

- Fetches current weather data for a given city.
- Displays city name, temperature, weather description, humidity, and wind speed.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/WeatherApp.git
    cd WeatherApp
    ```

2. Install the required dependencies:

    ```sh
    pip install requests
    ```

## Usage

1. Obtain your API key from [OpenWeatherMap](https://openweathermap.org/api).

2. Replace `"Your API Key Here"` with your actual API key in the `main` function.

3. Run the application:

    ```sh
    python weather_app.py
    ```

4. Enter the name of the city when prompted.

## Example

```sh
Enter city name: London
City: London
Temperature: 15°C
Weather: light rain
Humidity: 82%
Wind Speed: 4.1 m/s
