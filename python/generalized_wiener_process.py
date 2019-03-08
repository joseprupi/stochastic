import numpy as np
import matplotlib.pyplot as plt

T = 10
n = 1000
dT = T / n
a = 0.05
b = 20


def randomwalk(n, dT, b):
    normal_values = np.random.normal(0, b * dT ** (1 / 2), n)
    walk = np.cumsum(normal_values)
    return walk


particularWalk = randomwalk(n, dT, b)
drift = np.cumsum(np.full(n, a))

plt.plot(np.arange(n), particularWalk, color='green')
plt.plot(np.arange(n), particularWalk + drift, color='royalblue')

x = np.arange(n)

plt.plot(x, drift, linewidth=1, color='red')

plt.grid()
plt.show()
