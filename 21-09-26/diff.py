#code by t.pranay
#date 21-09-26

import numpy as np
import subprocess
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 0, 500)
x2 = np.linspace(0, 5, 500)

#a=0,b=2
y1 = np.sin(2*x1)
y2 = 2*x2

plt.plot(x1, y1)
plt.scatter(0, 0, facecolors='none', edgecolors='black', s=100)
plt.plot(x2, y2)

plt.axhline(0)
plt.axvline(0)
plt.grid()

plt.savefig("graphs.pdf")
subprocess.run(["termux-open","graphs.pdf"])
