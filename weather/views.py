from django.shortcuts import render
import requests
from decouple import config
from weather.forms import CityForm
from weather.models import City

def index(request): 
    api_key = config('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid={api_key}'
    cities = City.objects.all()
    # form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        
        weather = {
            'city': city, 
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        
        weather_data.append(weather)
        
    context = {'weather_data': weather_data}
    return render(request, 'index.html', context)