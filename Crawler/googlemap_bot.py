import pandas as pd 
from selenium import webdriver
import time
import winsound

google_url = "http://www.google.com/maps/search/"

file_name = input("Enter data's path: ")

df = pd.read_excel("./" + file_name + ".xlsx")
driver = webdriver.Chrome()

address = df["mainAddress"]

driver.get("http://www.google.com/maps")

latitude = []
longitude = []

input("Clear all?")

for add in address:
    
    url = google_url + add.replace(" ","")
    driver.get(url)
    
    time.sleep(4)
    url_now = driver.current_url
    element = url_now.split('/')
    
    flag = False
    lat = None
    long = None
    
    for i in element:
        
        if '@' in i:
            flag =True
            latlng = i.split(',')
            lat = latlng[0]
            lat = lat.replace('@','')
            
            long = latlng[1]
            print(add,lat,long)
            break
            
    latitude.append(lat)
    longitude.append(long)
              
driver.close()

df['lat'] = latitude
df['long'] = longitude

df.to_excel(file_name + "_1.xlsx")

print("Done!")
winsound.Beep(frequency = 600, duration = 3000)