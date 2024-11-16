from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_view, name='location_form'),
    path('load-states/', views.load_states, name='load_states'),
    path('load-cities/', views.load_cities, name='load_cities'),
]
