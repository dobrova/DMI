#-*- coding: utf-8 -*-
from numpy import sin, arange

a = 1.57
b = 4.71

funa = sin(a)
funb = sin(b)

if funa * funb > 0:
    print "Inetrvālā [%.2f,%.2f] sākņu nav vai ..."%(a,b)
    exit

delta_x = 1.e-3 #0.001
k = 0
while (b - a) > delta_x:
    x = (a+b)/2.
    funx = sin(x)
    if funa * funx > 0:
        a = x
    else:
        b = x
    k = k + 1
    print "dalīts %d reizes, x = %.5f a = %.5f b = %.5f"%(k,x,a,b)
    print b-a

print sin(x), sin(a), sin(b)
