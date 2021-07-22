import requests 

url = "http://127.0.0.1:5000/"

data = [
          {"likes":70240,"name":"Tom and Jerry","views":2000},
          {"likes":5054,"name":"HellBoy","views":5450},
         {"likes":3423,"name":"Robinson Curse","views":76400},
]

for i in range(len(data)):
    print("http://127.0.0.1:5000/video/"+ str(i))
    response = requests.put("http://127.0.0.1:5000/video/"+ str(i), data[i])
    print(response)

input() # Hold until you press enter
response = requests.get("http://127.0.0.1:5000/video/2")
print(response.text)

