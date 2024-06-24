while True:
    import requests

    class weather():
        def __init__(self, api_key):
            self.api_key = api_key
            self.baseurl = "https://api.openweathermap.org/data/2.5/weather?"
        
        def getWeatherData(self, city):
            completeURL = f"{self.baseurl}q={city}&APPID={self.api_key}&units=metric"
            response = requests.get(completeURL)
            return response.json()
        
    class WeatherApp:
        def __init__(self, api_key):
            self.weather_api = weather(api_key)


    class WeatherData:
        def __init__(self, data):
            self.city = data['name']
            self.temperature = data['main']['temp']
            self.weather_description = data['weather'][0]['description']
            self.humidity = data['main']['humidity']
            self.wind_speed = data['wind']['speed']

        def display(self):
            print(f"City: {self.city}")
            print(f"Temperature: {self.temperature}°C")
            print(f"Weather: {self.weather_description}")
            print(f"Humidity: {self.humidity}%")
            print(f"Wind Speed: {self.wind_speed} m/s")

    class WeatherApp:
        def __init__(self, api_key):
            self.weather_api = weather(api_key)

        def run(self):
            city = input("Enter city name: ")
            weather_data = self.weather_api.getWeatherData(city)
            if weather_data['cod'] == 200:
                data = WeatherData(weather_data)
                data.display()
            else:
                print("Your entered city is not found.")

    def main():
        api_key = "Your API Key Here"
        app = WeatherApp(api_key)
        app.run()

    if __name__ == "__main__":
        main()
