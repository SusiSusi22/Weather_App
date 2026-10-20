import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
print(os.getenv("API_KEY"))

def get_weather():

   while get_weather:
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name:\n")


    request_url = f"https://api.openweathermap.org/data/2.5/weather?&lang=de&appid={os.getenv('API_KEY')}&q={city}&units=metric"

    response = requests.get(request_url)
    data = response.json()

    if response.status_code == 200:
        print("API funktuniert!")
        #pprint(data)
    else:
        print("Fehler:", response.status_code)
        print(response.text)

    #print(request_url)
    print(f"Aktuellen Wetter für die Stadt {data['name']}")
    print(f"Die Temperatur beträgt {data['main']['temp']}")
    print(f"Gefühlt wie {data['main']['feels_like']} und {data['weather'][0]['description']}")

    input("Willst du das Wetter einer anderen Stadt wissen? J für 'J', N für 'Nein'\n")
    if input == "J":
       get_weather()

    else:
       break 


get_weather()