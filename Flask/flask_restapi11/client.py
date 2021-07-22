import requests 

response = requests.put("http://127.0.0.1:5000/video/1", data = {"name":"Black Mirror","views":100,"likes":33} )

print(response.json())