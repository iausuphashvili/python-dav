import requests
import json
from win10toast import ToastNotifier

API_KEY = 'fdfef344fb8eeb709cfa9c6db8f16e52'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def print_weather_info(weather_data):
    name = weather_data['name']
    temp = weather_data['main']['temp']
    desc = weather_data['weather'][0]['description']
    print(f'City: {name}')
    print(f'Temperature: {temp}°C')
    print(f'Description: {desc}')

def display_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)

city_name = input('Enter a city name: ')
weather_data = get_weather(city_name)

save_to_json(weather_data, 'weather_data.json')

print_weather_info(weather_data)


title = f"Weather in {city_name}"
message = f"Temperature: {weather_data['main']['temp']}°C"
display_notification(title, message)