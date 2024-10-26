import time
import requests
from threading import Thread
from multiprocessing import Process, Queue
import json
import queue

class ImageDownloder(Process):
    def __init__(self, access_key, queries, page = 1, delay = 5):
        super(ImageDownloder, self).__init__()
        self.access_key = access_key
        self.queries = queries
        self.page = page
        self.delay = delay
   

    def run(self):
        query = self.queries.get()
        

        while query is not None:
            print("Query ",query)
            self.__search_photos(self.access_key, self.page, query)
            time.sleep(self.delay)
            query = self.queries.get()
            

            
            
            
            
            
            # query = self.queries.get(timeout = 1)
            # print("Query",query)

            # url = f'https://api.unsplash.com/search/photos?client_id={self.access_key}&page={self.page}&query={query}'
            
            # response = requests.get(url)
            
            # if response.status_code == 200:
            #     response_json = json.loads(response.content)
            #     results = response_json['results']
            # else:
            #     print("Image couldn\'t be retreived")
            # query = self.queries.get()

            
    def __search_photos(self, access_key, query, page=1):
                url = f'https://api.unsplash.com/search/photos?client_id={access_key}&page={page}&query={query}'
                response = requests.get(url)
                
                if response.status_code == 200:
                    response_json = json.loads(response.content)
                    results = response_json['results']
                    print("Number of results    ", len(results))
                else:
                    print("Image couldn\'t be retreived")
