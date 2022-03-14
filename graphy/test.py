import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 2000)
y1 = np.sin(x1)


plt.plot(x1, y1, "g.", label="vzorky")
plt.legend()
plt.ylim(-1.5, 1.5)


plt.show()


