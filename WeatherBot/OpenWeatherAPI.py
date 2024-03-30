import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_KEY = getenv("OPEM_WEATHER_API_KEY")


def get_weather(city):
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY}')
    weather_data = response.json()
    description = weather_data['weather'][0]['description']
    temperature = round(weather_data['main']['temp'])
    temperature_feel = round(weather_data['main']['feels_like'])
    wind_speed = round(weather_data['wind']['speed'])
    answer = (f'В городе {city}:\n{description.capitalize()}\nТемпература {temperature}°C\n'
              f'Ощущается как {temperature_feel}°C')

    if wind_speed < 5:
        answer += "\nВетра почти нет!"
    elif wind_speed < 10:
        answer += "\nВетренно 🍃"
    elif wind_speed < 20:
        answer += "\nСильный ветер 💨"

    return answer
