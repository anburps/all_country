# geolocation/views.py
import requests
from django.http import JsonResponse
from django.shortcuts import render

COUNTRY_API = "http://api.geonames.org/countryInfoJSON?username=your_username"
STATE_API = "http://api.geonames.org/childrenJSON?geonameId={country_id}&username=your_username"
CITY_API = "http://api.geonames.org/searchJSON?q={state_name}&username=your_username&featureClass=P&maxRows=10"

def get_countries(request):
    response = requests.get(COUNTRY_API)
    countries = response.json().get('geonames', [])
    return JsonResponse(countries, safe=False)

def get_states(request, country_id):
    response = requests.get(STATE_API.format(country_id=country_id))
    states = response.json().get('geonames', [])
    return JsonResponse(states, safe=False)

def get_cities(request, state_name):
    response = requests.get(CITY_API.format(state_name=state_name))
    cities = response.json().get('geonames', [])
    return JsonResponse(cities, safe=False)


def index(request):
    return render(request, 'index.html')
