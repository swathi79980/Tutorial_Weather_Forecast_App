import requests
import os
from datetime import datetime
user_api=os.environ['current_weather']
city=input("Enter the city name:")
api_link="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api
api_l=requests.get(api_link)
api_data=api_l.json()
if api_data['cod']=='404':
    print("Invalid City!!:{},Please check your City name".format(city))
else:
    tempc=((api_data['main']['temp'])-273.15)
    wcity=api_data['weather'][0]['description']
    hcity=api_data['main']['humidity']
    winds=api_data['wind']['speed']
    dt=datetime.now().strftime("%d %b %Y| %I:%M:%S %p")
    print("***************************************************************")
    print("Weather Forecast for-{}||{}".format(city.upper(),dt))
    print("***************************************************************")
    print("Current temperature is:{:.2f} degree Celcius".format(tempc))
    print("Current weather description:",wcity)
    print("Current humidity:", hcity,"%")
    print("Current Wind Speed :",winds,"kmph")
    print("Thank You for Visiting!!!!!!")



    