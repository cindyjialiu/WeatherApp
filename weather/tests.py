from django.test import TestCase
from .views import get_weather_summary
from .views import get_weather_forecast_temp_and_dt
from .views import get_temps_for_tomorrow
import datetime

class WeatherTest(TestCase):

    def test_get_weather_summary(self):
        weather_data = {
          "main": {
            "temp": 8.08,
            "pressure": 1006,
            "humidity": 76,
            "temp_min": 6,
            "temp_max": 10
          }
        }
        expected = {
          'temp': 8.08,
          'min': 6,
          'max': 10,
          'humidity': 76
        }
        self.assertEquals(get_weather_summary(weather_data), expected)

    def test_get_weather_forecast_temp_and_dt(self):
        weather_forecast_data = [
          {
            "dt": 1545177600,
            "main": {
              "temp": 7.92,
              "temp_min": 7.92,
              "temp_max": 8.38,
              "pressure": 1007.99,
              "sea_level": 1015.53,
              "grnd_level": 1007.99,
              "humidity": 98,
              "temp_kf": -0.46
            },
            "weather": [
              {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10n"
              }
            ],
            "clouds": {
              "all": 48
            },
            "wind": {
              "speed": 4.45,
              "deg": 252.012
            },
            "rain": {
              "3h": 2.3875
            },
            "sys": {
              "pod": "n"
            },
            "dt_txt": "2018-12-19 00:00:00"
          },
          {
            "dt": 1545264000,
            "main": {
              "temp": 6.68,
              "temp_min": 6.68,
              "temp_max": 7.03,
              "pressure": 1008.82,
              "sea_level": 1016.43,
              "grnd_level": 1008.82,
              "humidity": 99,
              "temp_kf": -0.34
            },
            "weather": [
              {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "02n"
              }
            ],
            "clouds": {
              "all": 8
            },
            "wind": {
              "speed": 4.01,
              "deg": 216.001
            },
            "rain": {},
            "sys": {
              "pod": "n"
            },
            "dt_txt": "2018-12-20 00:00:00"
          }
        ]
        expected = [
          {
            "temp": 7.92,
            "dt": "2018-12-19 00:00:00"
          },
          {
            "temp": 6.68,
            "dt": "2018-12-20 00:00:00"
          }
        ]

        self.assertEquals(get_weather_forecast_temp_and_dt(weather_forecast_data), expected)

    def test_get_temps_for_tomorrow(self):
        filtered_forecast_data = [
          {
            "temp": 7.92,
            "dt": "2018-12-19 00:00:00"
          },
          {
            "temp": 6.68,
            "dt": "2018-12-20 00:00:00"
          }
        ]
        expected = [
          {
            "temp": 6.68,
            "dt": "2018-12-20 00:00:00"
          }
        ]

        today = datetime.datetime(2018,12,19)

        self.assertEquals(get_temps_for_tomorrow(filtered_forecast_data, today), expected)


