import numpy as np
import matplotlib.pyplot as plt
from math import pi

jmeno = str(input("zadej název grafu: "))
frekvence = int(input("zadej frekvenci: "))
amplituda = float(input("zadej amplitudu: "))
doba = int(input("pocet period: "))
offsety = float(input("posun osa y: "))
posun = float(input("fázový posun: "))

t = np.linspace(0, doba*1/frekvence, frekvence*10000)
u = amplituda * (np.sin(2*pi*frekvence*t + np.deg2rad(posun))) + offsety


plt.plot(t, u, label = jmeno)
plt.xlabel
plt.grid()
plt.legend()


plt.show()


