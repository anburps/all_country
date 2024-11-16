from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.get_countries, name='get_countries'),
    path('states/<int:country_id>/', views.get_states, name='get_states'),
    path('cities/<str:state_name>/', views.get_cities, name='get_cities'),
]
