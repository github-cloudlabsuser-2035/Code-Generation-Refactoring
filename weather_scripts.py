import requests
import os

# Set your OpenWeatherMap API key here
API_KEY = "022573a260dee6ec2ddfc75a5e30b2f4"
# os.getenv('OPENWEATHERMAP_API_KEY')

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    if weather_data:
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to retrieve weather data")

if __name__ == "__main__":
    main()