import requests
from django.http import JsonResponse
from django.shortcuts import render

COUNTRY_API = "http://api.geonames.org/countryInfoJSON?username=anbu"
STATE_API = "http://api.geonames.org/childrenJSON?geonameId={country_id}&username=anbu"
CITY_API = "http://api.geonames.org/searchJSON?q={state_name}&username=anbu"

def fetch_countries(request):
    response = requests.get(COUNTRY_API)
    if response.status_code == 200:
        data = response.json().get('geonames', [])
        return JsonResponse({'countries': data})
    return JsonResponse({'error': 'Unable to fetch countries'}, status=500)

def fetch_states(request, country_id):
    response = requests.get(STATE_API.format(country_id=country_id))
    if response.status_code == 200:
        data = response.json().get('geonames', [])
        return JsonResponse({'states': data})
    return JsonResponse({'error': 'Unable to fetch states'}, status=500)

def fetch_cities(request, state_name):
    response = requests.get(CITY_API.format(state_name=state_name))
    if response.status_code == 200:
        data = response.json().get('geonames', [])
        return JsonResponse({'cities': data})
    return JsonResponse({'error': 'Unable to fetch cities'}, status=500)

def location_form(request):
    return render(request, 'location_app/location_form.html')
