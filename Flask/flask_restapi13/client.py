import requests 

name = input("Please Name of the video: ")
views = int(input('Please View of the video: '))
likes = int(input('Please Likes of the video: '))

response = requests.put("http://127.0.0.1:5000/video/1", data = {"name":name,"views":views,"likes":likes})
print( response.json() )