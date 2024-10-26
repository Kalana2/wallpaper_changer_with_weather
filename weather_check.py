import json
from threading import Thread
import requests 
import time
from queue import Queue

class WeatherCheck(Thread):

    def __init__(self, api_key, city, queries, delay = 5) :
        super(WeatherCheck, self).__init__()
        self.api_key = api_key
        self.city = city
        self.queries = queries
        self.delay = delay

    def run(self):
        # while True:
         weather = self.__getWeatherReport(self.api_key, self.city)
         self.__updateWeather_obj(weather)
         self.queries.put(weather)
         print("weather is ", weather )
         time.sleep(self.delay)


    def __updateWeather_obj(self, weather):
        # self.weather.put(weather)
        for attr in ["id", "main", "description", "icon"]:
            self.queries[attr] = weather[attr]



    def __getWeatherReport(self, api_key, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            jsonContent = json.loads(response.content)
            wether = jsonContent["weather"]
            if wether:
                return wether[0]