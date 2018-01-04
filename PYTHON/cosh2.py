# -*- coding: utf-8 -*-

import random
import math
import numpy as np
import matplotlib.pyplot as plt

N=100000
a=0.0
b=4.0
c=-5
d=30
x = []
y = []

plt.plot(x,y)

for i in range(N):
    x.append(random.uniform(a,b))
for i in range(N):
    y.append(random.uniform(c,d))

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < np.cosh(x[i]) and y[i] > 0) \
    or (y[i] > np.cosh(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()



plt.show()


areaRect = (b-a)*(d-c)
print areaRect
areaFunc = areaRect * len(green_x) / N
print areaFunc
