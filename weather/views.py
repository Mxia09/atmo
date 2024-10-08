from django.shortcuts import render
import requests
from decouple import config
from weather.forms import CityForm

def index(request): 
    api_key = config('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid={api_key}'
    # city = 'San Francisco'
    # city_weather = requests.get(url.format(city)).json()
    # print(city_weather)
    form = CityForm()
    # weather = {
    #     'city' : city,
    #     'temperature' : city_weather['main']['temp'],
    #     'description' : city_weather['weather'][0]['description'],
    #     'icon' : city_weather['weather'][0]['icon']
    # }
    weather_data = []
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)