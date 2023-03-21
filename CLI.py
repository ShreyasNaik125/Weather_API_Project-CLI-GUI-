import requests
import time

                   
url = f'https://api.ipgeolocation.io/ipgeo?apiKey={IpApikey}&ip={ipAddr}'#insert API key and your IP address
res1 = requests.get(url).json()
cityRecieved = res1['city'] #nearby city 


url = f'https://api.openweathermap.org/data/2.5/weather?q={cityRecieved}&appid={api_key}'# insert your Weather API key
res = requests.get(url).json()

print('City Name:',res['name'])
time.sleep(0.11)
print('Temperature:',int(res['main']['temp']-273.15),'°C')
time.sleep(0.11)
print('Feels Like:',int(res['main']['feels_like']-273.15),'°C')
time.sleep(0.11)
print('Wind speed:',int(res['wind']['speed']*1.852),'Kmph')
time.sleep(0.11)
print('Weather:',res['weather'][0]['main'])
input()
