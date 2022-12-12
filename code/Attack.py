#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

#blur

#compress

def sharpen(img):
    sharpened=cv2.Laplacian(img,cv2.CV_16S,5)
    abs_sharpened=cv2.convertScaleAbs(sharpened)
    return abs_sharpened

def saltAndPepper(img,snr):
    h=img.shape[0]
    w=img.shape[1]
    img1=img.copy()
    sp=h*w   # 计算图像像素点个数
    NP=int(sp*(1-snr))   # 计算图像椒盐噪声点个数
    for i in range (NP):
        randx=np.random.randint(1,h-1)   # 生成一个 1 至 h-1 之间的随机整数
        randy=np.random.randint(1,w-1)   # 生成一个 1 至 w-1 之间的随机整数
        if np.random.random()<=0.5:   # np.random.random()生成一个 0 至 1 之间的浮点数
            img1[randx,randy]=0
        else:
            img1[randx,randy]=255
    return img1

def rotate(img):
    h,w=img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -90, 1)
    rotated=cv2.warpAffine(img, M, (w, h))
    return rotated

def crop(img):
    cropped=np.array(img)
    cropped[200:320,0:320]=0
    cropped[0:320,200:320]=0
    return cropped

