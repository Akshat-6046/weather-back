from .models import Countries
import requests

#common header
headers = {"Content-type": "application/json", "Accept": "text/plain"}
#weather api params
paramsWeatherApi = {
            "key": "dac9e99825dc41bb9e1121322240501",  # personal weather api key used
            "days": 3,  # 3 days forecast
            "aqi": "no",
            "alerts": "no",
        }

def saveToCountriesTable(data):
    for d in data:
        name = d.get("name")
        iso3 = d.get("iso3")
        unicodeFlag = d.get("unicodeFlag")

        # saving to table to avoid unnecessary api calls
        Countries.objects.create(name=name, iso3=iso3, unicodeFlag=unicodeFlag)

def requestCountries():
    return requests.get(
            "https://countriesnow.space/api/v0.1/countries/flag/unicode"
        )

def requestCities(country):
    return requests.post(
            url="https://countriesnow.space/api/v0.1/countries/cities",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"country": country},
        )
    
def requestWeather(city):
    paramsWeatherApi['q'] = city #setting city for query
    return requests.get(
            url="http://api.weatherapi.com/v1/forecast.json",
            params=paramsWeatherApi,
        )