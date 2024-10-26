from collections.abc import Callable
from typing import Any, Iterable, Mapping
import requests
from threading import Thread
import json


class ImageDownloder(Thread):
    def __init__(self, acces_key, queries, page = 1):
        super(ImageDownloder, self).__init__()
        self.acces_key = acces_key
        self.queries = queries
        self.page = page

    

    def run(self):
         while True:
            query = self.queries.get()
            url = f'https://api.unsplash.com/search/photos?client_id={access_key}&page=1&query={qurey}'
            



def search_photos(query, page=1):
    access_key = 'UpI8zJvXTJj-AmnaIpeJ_cK7WxrLcDTUtNspOthpiG8'
    url = 'https://api.unsplash.com/search/photos?client_id={access_key}&page=1&query={cloudyweather}'

    # Parameters for the search query
    params = {
        'page': page,
        'query': query
    }

    # Headers for the request
    headers = {
        'Authorization': f'Client-ID {access_key}'
    }

    # Make the request to the Unsplash API
    response = requests.get(url, headers=headers, params=params)

    # Check the response status code
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        raise Exception(f'Failed to authenticate: {response.status_code} - {response.json()}')
