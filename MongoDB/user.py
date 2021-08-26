import requests
  
# api-endpoint
URL = "http://127.0.0.1:5000"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'task':"MongoDB","summary":"Study all!"}
  
# sending get request and saving the response as response object
r = requests.post(url = URL + '/todo/3',params = PARAMS)

print(r)

# extracting data in json format
data = r.json()

print(data)