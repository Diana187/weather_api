import requests

from config import API_KEY

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY = 'London'

params = {
    'q': CITY,
    'appid': API_KEY
}
response = requests.get(BASE_URL, params=params).json()

def kelvin_tklelsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


temperature_kelvin = response['main']['temp']
temtemperature_celsius = kelvin_tklelsius(temperature_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_celsius = kelvin_tklelsius(feels_like_kelvin ) 

print(f'Temperature in {CITY}: {temtemperature_celsius:.2f} С, feels like {feels_celsius:.2f} C.')
