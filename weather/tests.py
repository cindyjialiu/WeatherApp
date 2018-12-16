from django.test import TestCase
from .views import get_weather_summary

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
