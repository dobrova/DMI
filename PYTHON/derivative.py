# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

def mans_cos(x):
     k=0
     S=0
     while k <= 70:
          a = x**(2*k)/np.math.factorial(2*k)
          S += a
          k += 1
     return S

a = 0
b = 3 * np.pi
x = np.arange(a,b,0.5)
y = mans_cos(x)

plt.plot(x,y)
plt.grid()





n = len(x)
y_prim = []

for i in range(n-1):
     delta_y = y[i+1] - y[i]
     delta_x = x[i+1] - x[i]
     y_prim.append(delta_y / delta_x)


n = len(x)
y_2prim = [] 

for i in range(n-2):
     print i, x[i], y[i] ,
     delta_y_prim = y_prim[i+1] - y_prim[i]
     delta_x = x[i+1] - x[i]
     y_2prim.append(delta_y_prim / delta_x)

plt.plot (x[:n-1],y_prim)
plt.plot (x[:n-2],y_2prim)
plt.show()
