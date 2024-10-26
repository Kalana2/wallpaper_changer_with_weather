import time
import requests
from threading import Thread
import json


class ImageDownloder(Thread):
    def __init__(self, acces_key, queries, page = 1, delay = 5):
        super(ImageDownloder, self).__init__()
        self.acces_key = acces_key
        self.queries = queries
        self.page = page
        self.delay = delay


    

    def run(self):
        query = self.queries.get()
        print("Query",query)
        while query is not None:
            self.__search_photos(self.acces_key, self.page, query)
            # time.sleep(self.delay)
            query = self.queries.get()
            


    def __search_photos(self, access_key, query, page=1):
        url = f'https://api.unsplash.com/search/photos?client_id={access_key}&page={page}&query={query}'
        response = requests.get(url)
        
        if response.status_code == 200:
            response_json = json.loads(response.content)
            results = response_json['results']
            print(len(results))
        # if response.status_code == 200:
        #     jasonContent = json.loads(response.content)
        #     wether = jasonContent["result"]
        #     if wether:
        #         return wether[0]


