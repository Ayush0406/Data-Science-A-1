# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:25:45 2019

@author: Ayush RKL
"""

import pandas as pd

f = pd.read_csv("3D_spatial_network.txt", header = None, delimiter = ',')
f1 = open("cost_values.txt", 'w+')

def calc_cost(n, y, y_calc):
    return (1/(2*n))*sum((y-y_calc)**2)


def gradient_descent(x2, x3, y, learn_rate):
    b = 1.54
    c = 0.12
    d = -0.012
    n = len(y)
    
    y_calc = b*x2 + c*x3 + d
    cost = 10
    last_cost = 0
    print("yes")
    i = 0;
    while abs(last_cost - cost) > 0.0001:
        i+=1
        y_calc = b*x2 + c*x3 + d
        last_cost = cost
        cost = calc_cost(n, y, y_calc)
        b_deriv = -(1/n)*sum(x2*(y-y_calc))
        c_deriv = -(1/n)*sum(x3*(y-y_calc))
        d_deriv = -(1/n)*sum(y-y_calc)
        
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
        
gradient_descent(f[1], f[2], f[3], 0.00001)
f1.close()
        
        