import requests

WEATHER_URL = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

response = requests.get(WEATHER_URL).json()

def filter_today_forecast(forecast):
    return forecast['dateLabel'] == '今日'

description = response['description']['text']
forecasts = response['forecasts']
forecast_today = [f for f in forecasts if f['dateLabel'] == '今日'][0]
telop = forecast_today['telop']
image_url = forecast_today['image']['url']
# temp_max = forecast_today['temperature']['max']['celsius']
# temp_min = forecast_today['temperature']['min']['celsius']

print(telop, image_url, description)