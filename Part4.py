# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 00:10:16 2019

@author: Ayush RKL
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 

f = pd.read_csv("3D_spatial_network.txt", header = None, delimiter = ',')
f1 = open("cost_values.txt", 'w+')

a = np.zeros([3, 3])
b = np.zeros([3, 1])

f1_train, f1_test, f2_train, f2_test, y_train, y_test = train_test_split(f[1], f[2], f[3], test_size = 0.3, random_state = 0)
n = len(f1_train)
a[0][0] = np.sum(f1_train**2)
print(a[0][0])

a[0][1] = np.sum(f1_train*f2_train)
print(a[0][1])

a[0][2] = np.sum(f1_train)
print(a[0][2])

a[1][0] = a[0][1]

a[1][1] = np.sum(f2_train*f2_train)
a[1][2] = np.sum(f2_train)
a[2][0] = a[0][2]
a[2][1] = a[1][2]
a[2][2] = n

b[0][0] = np.dot(np.transpose(y_train), f1_train)
b[1][0] = np.dot(np.transpose(y_train), f2_train)
b[2][0] = np.sum(y_train)
#print(b)
#n = int(len(f[1])*0.7)
#for i in range(n):
#    """updating values of row1 of 'a' matrix"""
#    a[0][0] += f[1][i]**2
#    a[0][1] += f[1][i]*f[2][i]
#    a[0][2] += f[1][i]
#    
#    a[1][0] += f[1][i]*f[2][i]
#    a[1][1] += f[2][i]**2
#    a[1][2] += f[2][i]
#    
#    a[2][0] += f[1][i]
#    a[2][1] += f[2][i]
#    
#    b[0][0] += f[3][i]*f[1][i]
#    b[1][0] += f[3][i]*f[2][i]
#    b[2][0] += f[3][i]
#    
#a[2][2] = n
print(a)
print(b)

c = np.linalg.inv(a)
print(c)
w = np.dot(c, b)
print(w)