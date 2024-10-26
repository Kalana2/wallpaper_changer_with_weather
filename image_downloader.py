import time
import requests
from threading import Thread
from multiprocessing import Process, Queue
import json
import queue

class ImageDownloder(Process):
    def __init__(self, access_key, queries, images, page = 1, delay = 5):
        super(ImageDownloder, self).__init__()
        self.access_key = access_key
        self.queries = queries
        self.imagers = images
        self.page = page
        self.delay = delay
        self.previousQuety = None
   

    def run(self):
        query = self.queries.get()
        print("Query ",query)
        while query is not None:

            if self.previousQuety == query:
                print("Same query is requested")
                query = self.queries.get()
                continue

            self.__search_photos(self.access_key, self.page, query)

            time.sleep(self.delay)

            query = self.queries.get()
            self.previousQuety = query
                      
    def __search_photos(self, access_key, query, page=1):
                url = f'https://api.unsplash.com/search/photos?client_id={access_key}&page={page}&query={query}'
                response = requests.get(url)
                
                if response.status_code == 200:
                    response_json = json.loads(response.content)
                    results = response_json['results']
                    if len(results) > 0 :
                         self.__downlaodImage(results[0])
                else:
                    print("Image couldn\'t be retreived")   

    def __downlaodImage(self, image):
        urls= image["urls"] 
        raw = urls["raw"]
        print(raw)

        res = requests.get(raw, stream=True, )
        if res.status_code == 200:
            res.raw.decode_content = True

            firstPart = raw.split("?")
            imageName = firstPart[0].split("/")[-1]

            fileName = f"./images/{imageName}.jpg"

            with open(fileName,'wb') as f:
                f.write(res.content)
            
            self.imagers.put(fileName)

            print("Image sucessfuly downloaded : ", fileName)

        else:
             print("image Dosen\'t retrived ")
