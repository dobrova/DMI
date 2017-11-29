
# -*- coding: utf-8 -*-

import math
x = float(input("Lietotaj ievadi argumentu (x): "))
print type(x)

y = math.cosh(x)
print "cos(%.2f)=%.2f"%(x,y)
k=0
s=0
while k <= 3:
    k += 1
    a = x**(2*k)/math.factorial(2*k)
    s += a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,s)
