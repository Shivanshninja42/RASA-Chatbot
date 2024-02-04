
import requests

def Weather(city): 


   api_address='https://api.openweathermap.org/data/2.5/weather?appid=db5beab488f2ba1c5b9db48d480429dd&q='

   # city=input('city name :')
   url=api_address+city

   json_data=requests.get(url).json()

   format_add = json_data['main']
 
   print(format_add)

   print( "weather is {0}",(json_data['weather'][0]['main'],int (format_add['temp_min']-273),int(format_add['temp_max']-272) ) )

   return format_add


# 