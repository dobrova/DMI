# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss (x):
     

     k = 0
     a = (-1)**0*x**1/(1)
     S = a

     
     while k<500:
          k = k + 1
          R = (-1) * x**2 /(2*k*(2*k+1))
          a = a * R
          S = S + a
     return S
a = 0
b = 3 * np.pi
x = np.arange(a,b,0.5)
y = mans_sinuss(x)

plt.plot(x,y)
plt.grid()
#plt.show()




n = len(x)
y_prim = []

for i in range(n-1):
     #print i, x[i], y[i] ,
     delta_y = y[i+1] - y[i]
     delta_x = x[i+1] - x[i]
     #y_prim = delta_y / delta_x
     #print y_prim
     y_prim.append(delta_y / delta_x)

#plt.plot (x[:n-1],y_prim)
#plt.show()





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








'''
k = k + 1
a = a * (-1) * x**2 /(2*k(2*k+1))
S = S + a
print "a1 = %6.2f S1 = %6.2f"%(a,S)



k = k + 1
a = a * (-1) * x**2 /(2*k(2*k+1))
S = S + a
print "a2 = %6.2f S2 = %6.2f"%(a,S)




k = k + 1
a = a * (-1) * x**2 /(2*k(2*k+1))
S = S + a
print "a3 = %6.2f S3 = %6.2f"%(a,S)
'''
