import requests
import json
import weather_check

city = "Colombo"
api_key = "3ecde5c26ac89c3412bba58e4df629db"





if __name__== "__main__":
    print("starting dynamic wallpaper")

    image = search_photos("Rain")
    print(image)

    weatherEngine = weather_check.WeatherCheck(api_key, city)
    weatherEngine.start()
    weatherEngine.join()

    image = search_photos("Rain")
    print(image)

