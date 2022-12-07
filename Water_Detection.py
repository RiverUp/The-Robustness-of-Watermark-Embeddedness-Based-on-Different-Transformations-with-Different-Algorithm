#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pywt
import difflib

def detectWatQuan(wat_embedded,matrix):
    t2=200
    t1=115
    X2=10
    watLen=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>=t1+X2 and abs(matrix[i][j])<=t2-X2:
                watLen+=1
    wat_detected=np.empty(watLen,dtype=bool)
    watNo=0
    for i in range(40):
        for j in range(40):
            if abs(matrix[i][j])>=t1+X2 and abs(matrix[i][j])<=t2-X2:
                if abs(matrix[i][j])<(t1+t2)/2:
                    wat_detected[watNo]=False
                if abs(matrix[i][j])>(t1+t2)/2:
                    wat_detected[watNo]=True
                watNo+=1
    return difflib.SequenceMatcher(None,wat_embedded,wat_detected).quick_ratio()

