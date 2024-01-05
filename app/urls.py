from django.contrib import admin
from django.urls import path
from .views import getCountries, getCities, getWeather


urlpatterns = [
    path("countries/", getCountries),
    path("cities/", getCities),
    path("weather/", getWeather),
]
