import requests
import json
import time
from multiprocessing import Queue

import weather_check
import image_downloader
import engine



city = "colombo"o
api_key = "3ecde5c26ac89c3412bba58e4df629db"

access_key = 'UpI8zJvXTJj-AmnaIpeJ_cK7WxrLcDTUtNspOthpiG8'


if __name__== "__main__":
    print("starting dynamic wallpaper")

    queries = Queue()
    images = Queue()
    weather ={}

    weatherEngine = weather_check.WeatherCheck(api_key, city, queries)
    weatherEngine.start()

    downloader = image_downloader.ImageDownloder(access_key, queries, images)
    downloader.start()
    
    engine = engine.Engine(images)
    engine.start()

    weatherEngine.join()
    downloader.join()


