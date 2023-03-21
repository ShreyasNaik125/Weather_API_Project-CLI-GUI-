from tkinter import *
import requests

def get_weather(city):
  global Temperature,CityName,CountryCode,FeelsLike,WindSpeed,Weather
  url = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,API_KEY))
  weather = url.json()

  feelsliketemp = int(weather['main']['feels_like']-273.15)
  windspeedtoKmph = int(weather['wind']['speed']*1.852)
  
  Temperature = int(weather['main']['temp'] - 273.15)
  CityName = weather['name']
  CountryCode = weather['sys']['country']
  FeelsLike = f'Feels Like:{feelsliketemp}°C'
  WindSpeed = f'Wind speed:{windspeedtoKmph}Kmph'
  Weather = 'Weather:',(weather['weather'][0]['main'])


def showResult():
  city = city_entry.get()
  get_weather(city)
  TemperatureLabel['text'] = '{}°C'.format(Temperature)
  CityNameLabel['text'] = '{},{}'.format(CityName,CountryCode)
  FeelsLikeLabel['text'] = '{}'.format(FeelsLike)
  WeatherLabel['text'] = '{}'.format(Weather)
  WindSpeedLabel['text'] = '{}'.format(WindSpeed)

  

root = Tk()

root.geometry('380x370')
root.title('Weather App')

city_entry = Entry(root,width=23,font=('Helvetica',15))
city_entry.place(x=40,y=30)

search_button = Button(root,text='Search',width=6,background='#00adcc',font=('Helvetica',10),fg='#fff',command=showResult)
search_button.place(x=300,y=29)

TemperatureLabel = Label(text='',font=('Helvetica',80))
CityNameLabel = Label(text = '',font=('Helvetica',20))
FeelsLikeLabel = Label(text = '',font=('Helvetica',12))
WeatherLabel = Label(text = '',font=('Helvetica',12))
WindSpeedLabel = Label(text = '',font=('Helvetica',12))

TemperatureLabel.place(x=80,y=90)
CityNameLabel.place(x=130,y=210)
FeelsLikeLabel.place(x=150,y=270)
WeatherLabel.place(x=130,y=290)
WindSpeedLabel.place(x=130,y=310)

root.mainloop()