import requests 

#r = requests.get("http://127.0.0.1:5000/users")

r = requests.put("http://127.0.0.1:5000/users/0",json= {"name":"Pump"})

print(r.json())