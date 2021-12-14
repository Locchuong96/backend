import time 
import concurrent.futures  
import os
from PIL import Image,ImageFilter 

start = time.perf_counter()

imgs = os.listdir("./pics")

size = (1200,1200)

def image_process(img_name):
    img = Image.open("./pics/"+img_name)
    print(f"Starting process {img}")
    img = img.filter(ImageFilter.GaussianBlur(10))
    img.thumbnail(size) # resize the img
    img.save(f'./processed/{img_name}')
    

if __name__ == "__main__":
    
    # for img_name in imgs:
    #     image_process(img_name)
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(image_process,imgs)
        
    finish = time.perf_counter()
    
    print(f"Finished in {round((finish-start),2)} seconds (s)")