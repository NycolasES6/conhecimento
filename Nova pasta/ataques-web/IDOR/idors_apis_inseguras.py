import requests
import json

def get(url):
    return requests.get(url)

req = get("http://94.237.56.188:50730/profile/api.php/profile/5").text

load = eval(req)

print(load)