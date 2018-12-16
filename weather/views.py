import os

import requests
from django.shortcuts import render


def index(request):
    api_key=os.environ['WEATHER_API_KEY']
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid={api_key}')
    # TODO: handle extra errors
    weather_data = response.json()

    weather_summary = get_weather_summary(weather_data)

    return render(request, 'index.html', weather_summary)


def get_weather_summary(weather_data):
    return {
      'temp': weather_data['main']['temp'],
      'min': weather_data['main']['temp_min'],
      'max': weather_data['main']['temp_max'],
      'humidity':weather_data['main']['humidity']
    }
