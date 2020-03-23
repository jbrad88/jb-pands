# Jody Bradley
# This program displays a plot of the following functions:
# 1. f(x) = x
# 2. g(x) = x**2
# 3. h(x) = x**3
# ... in the range of [0,4]

import numpy as np
import  matplotlib.pyplot as plt
x = np.arange(0, 4)

f = x
plt.plot(x, f)

g = x ** 2
plt.plot(x, g)

h = x ** 3
plt.plot(x, h)

plt.savefig('plot.png')

plt.show('plot.png')


