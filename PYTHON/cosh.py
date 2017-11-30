# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def mans_cos(x,n):
    k=0
    S=0
    while k <= n:
        k += 1
        a = x**(2*k)/math.factorial(2*k)
        S += a
    return S
x = np.arange (0.0,4,0.01)
y = np.cosh(x)

plt.plot(x,y)

colors=['r','g','b','y','c','k']
for i in range(0,5,1):
     f = mans_cos(x,i)
     plt.plot(x,f, colors[i])
  
plt.show ()


