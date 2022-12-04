# encoding=UTF-8
import random
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 13)
a = 10
a = a / (2 ** 0.5)
print(a)

add   = a + x
minus = a - x

expon = 2 * x
expon = expon * (add ** (-1.5))
y = add ** (-2) + expon  - minus ** (-2)
y = 10_000_000_000 * y * (-1)

m = np.arange(0, 20)
print(m)
n = m * 0

plt.xlabel('X/m')
plt.ylabel('E/(')
plt.plot(m, n)
plt.plot(x, y)
plt.show()




