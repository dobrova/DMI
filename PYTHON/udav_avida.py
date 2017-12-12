# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def mans_cos_kv(x,n):
    k=0
    S=0
    while k <= n:
        a = (-1)**(k+1)*x**(2*k)*2**(2*k-1)/math.factorial(2*k)
        S += a
        k += 1
    return S

x = np.arange (0.0,3,0.1)
y = (1+np.cos(2*x))/2

plt.plot(x,y)

colors=['r','g','b','y','c','k']
for i in range(0,5,1):
     f = 1-mans_cos_kv(x,i)
     plt.plot(x,f, colors[i])
     
plt.show ()


