import requests
from django.http import JsonResponse
from django.shortcuts import render

# Replace 'anbu' with your GeoNames username.
COUNTRY_API = "http://api.geonames.org/countryInfoJSON?username=anbu"
STATE_API = "http://api.geonames.org/childrenJSON?geonameId={country_id}&username=anbu"
CITY_API = "http://api.geonames.org/searchJSON?q={state_name}&username=anbu"

# Fetch countries
import logging
logger = logging.getLogger(__name__)

def fetch_countries():
    response = requests.get(COUNTRY_API)
    if response.status_code == 200:
        data = response.json()
        logger.info(f"GeoNames Country API Response: {data}")
        return data.get('geonames', [])
    logger.error(f"GeoNames Country API Error: {response.status_code} - {response.text}")
    return []

# Fetch states based on country ID
def fetch_states(country_id):
    response = requests.get(STATE_API.format(country_id=country_id))
    if response.status_code == 200:
        return response.json().get('geonames', [])
    return []

# Fetch cities based on state name
def fetch_cities(state_name):
    response = requests.get(CITY_API.format(state_name=state_name))
    if response.status_code == 200:
        return response.json().get('geonames', [])
    return []

# Main view to render the form
def location_view(request):
    countries = fetch_countries()
    return render(request, 'index.html', {'countries': countries})


# AJAX to load states
def load_states(request):
    country_id = request.GET.get("country_id")
    states = fetch_states(country_id)
    return JsonResponse({"states": states})

# AJAX to load cities
def load_cities(request):
    state_name = request.GET.get("state_name")
    cities = fetch_cities(state_name)
    return JsonResponse({"cities": cities})
