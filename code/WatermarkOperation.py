#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pywt
import difflib
import pandas as pd
import cv2

def detectWatQuan(wat_embedded,matrix,t1,t2):
    X2=t2/20
    watLen=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>=t1+X2 and abs(matrix[i][j])<=t2-X2:
                watLen+=1
    wat_detected=np.empty(watLen,dtype=bool)
    wat_correlated=np.empty(watLen,dtype=bool)
    watNo=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>=t1+X2 and abs(matrix[i][j])<=t2-X2:
                if abs(matrix[i][j])<(t1+t2)/2:
                    wat_detected[watNo]=False                    
                elif abs(matrix[i][j])>(t1+t2)/2:
                    wat_detected[watNo]=True
                wat_correlated[watNo]=wat_embedded[40*i+j]  
                watNo+=1
    length=len(wat_correlated)           
    sum0=0
    for i in range(length):
            if(wat_correlated[i]==True):
                ii=1
            else:
                ii=0
            if(wat_detected[i]==True):
                jj=1
            else:
                jj=0
            sum0+=ii*jj
    
    sum1=0
    for i in range(length):
        if(wat_correlated[i]==True):
                ii=1
        else:
                ii=0
        sum1+=np.square(ii)
        
    sum2=0
    for i in range(length):
        if(wat_detected[i]==True):
                jj=1
        else:
                jj=0
        sum2+=np.square(jj)
    
    #print(wat_detected)
    NCC1=np.sqrt(sum1)
    NCC2=np.sqrt(sum2)
    NCC=sum0/(NCC1*NCC2)
    return NCC
                
    #return difflib.SequenceMatcher(None,wat_correlated,wat_detected).quick_ratio()

def embedWatQuan(matrix,t1,t2):
    X1=t2/10
    wat=np.random.choice(a=[False,True],size=1600)
    for i in range(40):
        for j in range(40):
            if (matrix[i][j]>t1 and matrix[i][j]<t2) and wat[40*i+j]==True:
                matrix[i][j]=t2-X1
            elif (matrix[i][j]>t1 and matrix[i][j]<t2) and wat[40*i+j]==False:
                matrix[i][j]=t1+X1
            elif (matrix[i][j]<-t1 and matrix[i][j]>-t2) and wat[40*i+j]==True:
                matrix[i][j]=-t2+X1
            elif (matrix[i][j]<-t1 and matrix[i][j]>-t2) and wat[40*i+j]==False:
                matrix[i][j]=-t1-X1 
    return wat

def embedWatAddi(matrix,t1):
    k=0.175
    wat=np.random.randn(1600)
    watNo=0
    for i in range(40):
        for j in range(40):
            if matrix[i][j]>t1 or matrix[i][j]<-t1:
                matrix[i][j]+=abs(matrix[i][j])*k*wat[40*i+j]
    return wat

def detectWatAddi(wat_embedded,matrix,t2):
    correlation=0
    N=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>t2:
                correlation+=matrix[i][j]*wat_embedded[40*i+j]
                N+=1
    corr=correlation/N
    return corr