from collections.abc import Callable
from typing import Any, Iterable, Mapping
import requests
from threading import Thread
import json


class ImageDownloder(Thread):
    def __init__(self, acces_key, query, page = 1):
        super(ImageDownloder, self).__init__()
        self.acces_key = acces_key
        self.params = {
            'page': page,
            'query': query
        }
        self.headers = {
        'Authorization': f'Client-ID {access_key}'
    }
    

    def run(self, headers, params):
         while True:
            url = 'https://api.unsplash.com/search/photos'
            response = requests.get(url, headers=headers, params=params)



def search_photos(query, page=1):
    access_key = 'UpI8zJvXTJj-AmnaIpeJ_cK7WxrLcDTUtNspOthpiG8'
    url = 'https://api.unsplash.com/search/photos'

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
