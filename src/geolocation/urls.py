from django.urls import path
from .views import fetch_countries, fetch_states, fetch_cities, location_form

urlpatterns = [
    path('', location_form, name='location_form'),
    path('countries/', fetch_countries, name='fetch_countries'),
    path('states/<int:country_id>/', fetch_states, name='fetch_states'),
    path('cities/<str:state_name>/', fetch_cities, name='fetch_cities'),
]
