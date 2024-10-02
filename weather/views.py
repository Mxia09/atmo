from django.shortcuts import render
import requests
from decouple import config


# def index(requests):
#     return render(requests, 'index.html')


# def index(request):
#     api_key = config('OPENWEATHER_API_KEY')
#     url = f'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid={api_key}'
#     city = 'San Francisco'
#     city_weather = requests.get(url.format(city)).json()
#     print(city_weather)
#     return render(request, 'index.html')

def index(request): 
    api_key = config('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid={api_key}'
    city = 'San Francisco'
    city_weather = requests.get(url.format(city)).json()
    print(city_weather)
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    context = {'weather': weather}
    return render(request, 'index.html', context)