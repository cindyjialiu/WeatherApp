import os
import datetime
import requests
from django.shortcuts import render


def index(request):
    api_key=os.environ['WEATHER_API_KEY']
    today = datetime.datetime.today()

    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid={api_key}')
    # TODO: handle extra errors
    weather_data = response.json()

    response2 = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q=London,uk&units=metric&appid={api_key}')
    # TODO: handle extra errors
    weather_forecast_data = response2.json()

    weather_summary = get_weather_summary(weather_data)
    weather_forecast_summary = get_temps_for_tomorrow(get_weather_forecast_temp_and_dt(weather_forecast_data['list']), today)

    return render(request, 'index.html', { 'weather_forecast_summary': weather_forecast_summary,
                                           'weather_summary': weather_summary
                                           })


def get_weather_summary(weather_data):
    return {
      'temp': weather_data['main']['temp'],
      'min': weather_data['main']['temp_min'],
      'max': weather_data['main']['temp_max'],
      'humidity':weather_data['main']['humidity']
    }

def get_weather_forecast_temp_and_dt(weather_forecast_data):
    return list(map(lambda x: {
        'temp': x['main']['temp'],
        'dt': x['dt_txt']
      }, weather_forecast_data))


def get_temps_for_tomorrow(filtered_forecast_data, today):
    tomorrow = str(today + datetime.timedelta(days = 1)).split(' ')[0]
    print(today)

    return list(filter(lambda x: x['dt'].split(' ')[0] == tomorrow, filtered_forecast_data ))
