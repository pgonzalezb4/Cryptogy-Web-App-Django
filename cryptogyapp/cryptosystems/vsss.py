import random
import textwrap
from .message import *
from sympy import isprime
from PIL import Image
from django.conf import settings  
import random
import numpy as np
from random import randrange

Bk=(0,0,0) #1
R=(255,0,0)
G=(0,255,0)
B=(0,0,255)
Y=(255,255,0)
M=(255,0,255)
C=(0,255,255)
W=(255,255,255) #0

X_Bk = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,R,G,Bk,Bk,Bk,Y,M,C,Bk,W,Bk]]

X_R = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,Bk,G,Bk,Bk,Bk,Y,M,C,Bk,W,R]]

X_G = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,R,Bk,Bk,Bk,Bk,Y,M,C,Bk,W,G]]

X_B = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [Bk,R,G,Bk,Bk,Bk,Y,M,C,Bk,W,B]]

X_Y = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,R,G,Bk,Bk,Bk,W,M,C,Bk,Bk,Y]]
    
X_M = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,R,G,Bk,Bk,Bk,Y,W,C,Bk,Bk,M]]

X_C = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,R,G,Bk,Bk,Bk,Y,M,W,Bk,Bk,C]]

X_W = [[R,G,B,Y,M,C,Bk,Bk,Bk,Bk,Bk,W],
       [B,R,G,Bk,Bk,Bk,Y,M,C,Bk,Bk,W]]

def normalize_image(url):    
    picture = Image.open(url)
    width, height = picture.size
    new_picture = Image.new( mode = "RGB", size = (width, height))
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
            new_picture.putpixel( (x,y), new_color)
    print("ok")
    #Save the picture as T1 and T2. This will be modified later
    new_picture.save(settings.BASE_DIR+"/media/images/temp_clear_img.png", "PNG")
    

def encrypt_image(url):
    normalize_image(url)
    picture = Image.open(settings.BASE_DIR+"/media/images/temp_clear_img.png")
    width, height = picture.size
    img_t1 = Image.new( mode = "RGB", size = (width*6, height*2))
    img_t2 = Image.new( mode = "RGB", size = (width*6, height*2))

    for x in range(0,width):
        for y in range(height):
            current_color = picture.getpixel((x,y))
            c1, c2 = new_colors(current_color)
            # print("c1-----")
            # print(c1)
            # print("c2-----")
            # print(c2)
            for i in range(0,6):
                for j in range(0,2):
                    img_t1.putpixel((6*x+i,2*y+j), c1[2*i+j])
                    img_t2.putpixel((6*x+i,2*y+j), c2[2*i+j])
    # img_array = np.asarray(img_t1)
    # print(img_array)
    # img_array2 = np.asarray(img_t2)
    # print(img_array2)
    img_t1.save(settings.BASE_DIR+"/media/images/temp_img_t1.png","PNG")
    img_t2.save(settings.BASE_DIR+"/media/images/temp_img_t2.png","PNG")

def decrypt_image(url1,url2):
    picture1 = Image.open(url1)
    picture2 = Image.open(url2)
    width, height = picture1.size
    clear_img = Image.new( mode = "RGB", size = (width, height))
    for x in range(0,width):
        for y in range(height):
            current_color1 = picture1.getpixel((x,y))
            current_color2 = picture2.getpixel((x,y))
            new_color = get_new_color(current_color1,current_color2)
            for i in range(0,8):
                clear_img.putpixel( (x,y), new_color)
    clear_img.save(settings.BASE_DIR+"/media/images/clear_image.png","PNG")
    return None

def convert(list):
    return tuple(i for i in list)

def new_colors(current_color):
    t = randrange(2)
    indexes = np.arange(0,12).tolist()
    random.shuffle(indexes)
    if current_color==(0,0,0):
        a=X_Bk[0]
        b=X_Bk[1]
    elif current_color==(255,0,0):
        a=X_R[0]
        b=X_R[1]        
    elif current_color==(0,255,0):
        a=X_G[0]
        b=X_G[1]
    elif current_color==(0,0,255):
        a=X_B[0]
        b=X_B[1]
    elif current_color==(255,255,0):
        a=X_Y[0]
        b=X_Y[1]
    elif current_color==(255,0,255):
        a=X_M[0]
        b=X_M[1]
    elif current_color==(0,255,255):
        a=X_C[0]
        b=X_C[1]
    else:
        a=X_W[0]
        b=X_W[1]
    
    indexes1,colors1=zip(*sorted(zip(indexes, a)))
    indexes2,colors2=zip(*sorted(zip(indexes, b)))

    if t==1:
        return colors1,colors2
    else:
        return colors2,colors1
    

def get_new_color(color1,color2):
    color=[]
    for i in range(3):
        if color1[i]==255 and color2[i]==255:
            color.append(255)
        else:
            color.append(0)
    new_color = convert(color)
    return new_color


