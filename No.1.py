# random output number from X to Y

# !/usr/bin/env python

import random

Y = int(input("max = "))
X = int(input("min = "))
array1 = []
t = Y - X
for i in range(X-1,Y):
    array1.append(i)

for j in range(t+1):
    input("press Enter")
    a = random.randint(0, t)
    print("The number is: %s" % array1[a])
    print("------------------------------------------")
    del array1[a]
    t = t - 1