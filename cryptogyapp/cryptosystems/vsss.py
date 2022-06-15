import random
import textwrap
from .message import *
from sympy import isprime
from PIL import Image
from django.conf import settings  

def normalize_image(url):    
    picture = Image.open(url)
    width, height = picture.size
    # Process every pixel
    for x in range(0,width):
        for y in range(height):
            current_color = picture.getpixel((x,y))
            color=[]
            # Generate the new color
            for i in current_color:
                if i>127:
                    color.append(255)
                else:
                    color.append(0)
            new_color = convert(color)
            picture.putpixel( (x,y), new_color)
    print("ok")
    #Save the picture as T1 and T2. This will be modified later
    picture.save(settings.BASE_DIR+"/media/images/"+"temp_img_t1.jpg")
    picture.save(settings.BASE_DIR+"/media/images/"+"temp_img_t2.jpg")

def convert(list):
    return tuple(i for i in list)