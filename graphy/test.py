from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 50e-3, 300000)
#x1 = np.linspace(0, 10, 2000)
u = 3.3 * np.sin(2*3.14*50*t)
u2 = 5 * np.cos(2*3.14*50*t)


plt.plot(t, u, label = "U1")
plt.plot(t, u2, label = "U2")
plt.grid()
plt.legend()
#plt.ylim(-1.5, 1.5)


plt.show()


