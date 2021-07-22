import requests 

video_id    = input("Please ID of the video ")
name        = input("Please Name of the video: ")
views       = int(input('Please View of the video: '))
likes       = int(input('Please Likes of the video: '))

response = requests.put("http://127.0.0.1:5000/video/"+video_id, 
                            data = {"name":name,"views":views,"likes":likes})

print( response.json() )