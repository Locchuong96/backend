import requests
import requests

base_url  = "http://127.0.0.1:5000"

#a = requests.get(base_url + "/")
a = requests.get(base_url + "/user/Lisa")

print(a.json())