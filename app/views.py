from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

from .models import Countries
from .serializers import CountriesSerializer

from .utils import saveToCountriesTable,requestCountries,requestCities,requestWeather

headers = {"Content-type": "application/json", "Accept": "text/plain"}


# Create your views here.


# API : getting country list
@api_view(["GET"])
def getCountries(request):
    countries = Countries.objects.all()
    # if countries list not found then fetch from api and save to table Countries (FIRST TIME)
    if len(countries) == 0:
        data = requestCountries().json()
        countriesList = data.get("data")

        saveToCountriesTable(countriesList)
        return Response(countriesList, headers=headers)

    else:
        data = CountriesSerializer(countries, many=True).data
        return Response(data=data, headers=headers)


# API : getting city from country selected
@api_view(["GET"])
def getCities(request):
    name = request.GET.get("name")  # getting country name

    if name == None:
        return Response({"error": "Country is required"}, status=400)
    else:
        data = requestCities(country=name).json()
        return Response(data=data.get("data"), headers=headers)


# API : get weather of city
@api_view(["GET"])
def getWeather(request):
    name = request.GET.get("name")  # getting city name

    if name == None:
        return Response({"error": "Something went wrong"}, status=400)
    else:
        
        #requesting for weather details for requested city
        data = requestWeather(city=name).json()
        
        if data.get("error") != None:  #for error if city data not available
            return Response(data={"error": "Cannot find weather update of selected city"}, status=400,headers=headers)
        else:
            print(data, "ddddd")
            return Response(data=data,headers=headers)
