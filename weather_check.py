import json
from threading import Thread
import requests 
import time

class WeatherCheck(Thread):

    def __init__(self, api_key, city, delay = 20) :
        super(WeatherCheck, self).__init__()
        self.api_key = api_key
        self.city = city
        self.delay = delay

    def run(self):
        while True:
         Weather = self.__getWeatherReport(self.api_key, self.city)
         print(Weather)
         time.sleep(self.delay)


    def __getWeatherReport(self, api_key, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            jasonContent = json.loads(response.content)
            wether = jasonContent["weather"]
            if wether:
                return wether[0]