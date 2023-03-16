import time
import requests

def Image(delay):

    time.sleep(delay)
    url = requests.get(
        "https://dog.ceo/api/breeds/image/random").json()[0]['url']

    return url
