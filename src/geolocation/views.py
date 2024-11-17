# location_app/views.py

import requests
from django.http import JsonResponse
from django.shortcuts import render

USERNAME = "anbu"  
COUNTRY_API = f"http://api.geonames.org/countryInfoJSON?username=anbu"
STATE_API = "http://api.geonames.org/childrenJSON?geonameId={country_id}&username={username}"
CITY_API = "http://api.geonames.org/searchJSON?q={state_name}&username={username}"


def fetch_countries(request):
    try:
        response = requests.get(COUNTRY_API)
        response.raise_for_status()  
        print("+++++++++++++++++++++",response)
        countries = response.json().get('geonames', [])
        return JsonResponse({'countries': countries}, safe=False)
    except requests.exceptions.HTTPError as e:
        print("error",e)
        return JsonResponse({'error': f"HTTP Error: {str(e)}"}, status=response.status_code)
    except Exception as e:
        print("________________",e)
        return JsonResponse({'error': f"Error: {str(e)}"}, status=500)


def fetch_states(request, country_id):
    try:
        response = requests.get(STATE_API.format(country_id=country_id, username=USERNAME))
        response.raise_for_status()
        states = response.json().get('geonames', [])
        return JsonResponse({'states': states}, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f"Failed to fetch states: {str(e)}"}, status=500)

def fetch_cities(request, state_name):
    try:
        response = requests.get(CITY_API.format(state_name=state_name, username=USERNAME))
        response.raise_for_status()
        cities = response.json().get('geonames', [])
        return JsonResponse({'cities': cities}, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f"Failed to fetch cities: {str(e)}"}, status=500)

def location_form(request):
    return render(request, 'index.html')
