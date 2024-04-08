import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("weatherapi")

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    fl=data['main']['feels_like']
    feels_like=round(fl-273.15,2)
    temperature=round(temp-273.15,2)
    wind=data['wind']['speed']
    wind_updated=round(wind*3.6,2)
    print(f'Temperature: {temperature} C')
    print(f'Feels like: {feels_like} C')
    print(f'Description: {desc}')
    print('Wind speed:', wind_updated, 'km/h')
else:
    print('Error fetching weather data')
