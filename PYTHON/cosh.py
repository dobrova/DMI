# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def mans_cos(x,n):
    k=0
    S=0
    while k <= n:
        a = x**(2*k)/math.factorial(2*k)
        S += a
        k += 1
    return S
a=0.0
b=4.0
c=np.cosh(a)
d=np.cosh(b)

x = np.arange (a,b,0.01)
y = np.cosh(x)

plt.plot(x,y)

colors=['r','g','b','y','c','k']
for i in range(0,5,1):
     f = mans_cos(x,i)
     plt.plot(x,f, colors[i])

plt.show ()




print"y (x)= cosh(x)"
print"       500"
print"      ------"
print"      \ "
print"       \ x^(2*k)"
print"        \-------"
print"s(x) =  / (2-k)!"
print"       /"
print"      /"
print"      ------"
print"       k = 0"

areaRect = (b-a)*(d-c)
print areaRect
#areaFunc = areaRect * len(green_x) / N
#print areaFunc
