# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:25:45 2019

@author: Ayush RKL
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

f = pd.read_csv("3D_spatial_network.txt", header = None, delimiter = ',')
f1 = open("cost_values.txt", 'w+')

print(len(f[1]))
def calc_cost(n, y, y_calc):
    return (1/(2*n))*np.sum((y-y_calc)**2)


def gradient_descent(x2, x3, y, learn_rate):
    b = 4
    c = -12
    d = 680
    n = len(y)
    
    y_calc = b*x2 + c*x3 + d
    cost = 10
    last_cost = 0
    print("yes")
    i = 0;
    while abs(last_cost - cost) > 0.00001:
        i+=1
        y_calc = b*x2 + c*x3 + d
        last_cost = cost
        print(cost)
        cost = calc_cost(n, y, y_calc)
        b_deriv = -(1/n)*np.sum(x2*(y-y_calc))
        c_deriv = -(1/n)*np.sum(x3*(y-y_calc))
        d_deriv = -(1/n)*np.sum(y-y_calc)
        
        b = b - learn_rate * b_deriv
        c = c - learn_rate * c_deriv
        d = d - learn_rate * d_deriv
        if i%1000 == 0:
            f1.write(str(cost))
            f1.write("\n")
            print(cost)
            print(b, c, d, '\n')
    print(b, c, d, '\n')
    f1.write("%d %d %d" %(b, c, d))
        
f1_train, f1_test, f2_train, f2_test, y_train, y_test = train_test_split(f[1], f[2], f[3], test_size = 0.3, random_state = 0)
gradient_descent(f1_train, f2_train, y_train, 0.00001)
f1.close()
        
        