# -*- coding: utf-8 -*-
# a0

#from math import sin
import numpy as np
import matplotlib.pyplot as plt

#def mans_sinuss(x):
def mans_sinuss(x,n):
     k = 0
     a = (-1)**0*x**1/(1)
     S = a


     #while k < 2:
     while k < n:
          k = k + 1
          R = (-1) * x**2 /(2*k*(2*k+1))
          a = a * R
          S = S + a
     return S
x = np.arange (0.0,4,0.01)
y = np.sin(x)
#yy = mans_sinuss(x)


plt.plot(x,y)


colors=['r','g','b','y','c','k']
for i in range(0,5,1):
     f = mans_sinuss(x,i)
     plt.plot(x,f, colors[i])
  

plt.show ()



'''
x = 0.56
y = sin(x)
yy = mans_sinuss(x)
print x, y, yy
'''





'''
x=0.89

k = 0
a = (-1)**0*x**1/(1)
S = a


while k <= 3:
     k = k + 1
     R = (-1) * x**2 /(2*k*(2*k+1))
     a = a * R
     S = S + a

y=sin(x)
print x, y, S

'''



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
