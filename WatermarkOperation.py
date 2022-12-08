#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pywt
import difflib
import cv2

def detectWatQuan(wat_embedded,matrix,t1,t2):
    X2=t2/20
    watLen=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>=t1+X2 and abs(matrix[i][j])<=t2-X2:
                watLen+=1
    wat_detected=np.empty(watLen,dtype=tuple)
    watNo=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>=t1+X2 and abs(matrix[i][j])<=t2-X2:
                if abs(matrix[i][j])<(t1+t2)/2:
                    wat_detected[watNo]=(False,40*i+j)
                if abs(matrix[i][j])>(t1+t2)/2:
                    wat_detected[watNo]=(True,40*i+j)
                watNo+=1
    satisfiedNo=0
    wat_satisfied=list() 
    for watmk_detected in wat_detected:
        for watmk_embedded in wat_embedded:
            if watmk_detected[1]==watmk_embedded[1]:
                wat_satisfied.append(watmk_detected)
                break     
                
    return difflib.SequenceMatcher(None,wat_embedded,wat_satisfied).quick_ratio()

def embedWatQuan(matrix,t1,t2):
    X1=t2/10
    watLen=0
    for i in range(40):
        for j in range(40):
            if (matrix[i][j]>t1 and matrix[i][j]<t2) or (matrix[i][j]<-t1 and matrix[i][j]>-t2):
                watLen+=1
    wat=np.random.choice(a=[False,True],size=watLen)
    wat_stored=np.empty(watLen,dtype=tuple)
    watNo=0
    for i in range(40):
        for j in range(40):
            if (matrix[i][j]>t1 and matrix[i][j]<t2) and wat[watNo]==True:
                matrix[i][j]=t2-X1
                wat_stored[watNo]=(True,40*i+j)
                watNo+=1
            elif (matrix[i][j]>t1 and matrix[i][j]<t2) and wat[watNo]==False:
                matrix[i][j]=t1+X1
                wat_stored[watNo]=(False,40*i+j)
                watNo+=1
            elif (matrix[i][j]<-t1 and matrix[i][j]>-t2) and wat[watNo]==True:
                matrix[i][j]=-t2+X1
                wat_stored[watNo]=(True,40*i+j)
                watNo+=1
            elif (matrix[i][j]<-t1 and matrix[i][j]>-t2) and wat[watNo]==False:
                matrix[i][j]=-t1-X1
                wat_stored[watNo]=(False,40*i+j)
                watNo+=1  
    return wat_stored