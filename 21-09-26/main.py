#Code by Pranay
#21-09-26

import subprocess
import numpy as np
import matplotlib.pyplot as plt

#Taking a sample v for plotting
V = 5
tau = 40
t = np.linspace(0, 140, 1000)

#Expression
vc = V * (1 - np.exp(-t / tau))
t95 = -tau * np.log(0.05)
v95 = 0.95 * V

#printing the theritcal values
print(f"The Voltage(assuming isput is 5*u(t)) is {v95} and time is {t95}")

plt.plot(t, vc, linewidth=2)
plt.axhline(v95, linestyle='--')
plt.scatter(t95, v95, s=80, facecolors='none', edgecolors='red', linewidths=2)

plt.annotate(f'95% = {v95:.2f} V\n t = {t95:.2f} s',
             (t95, v95), xytext=(t95 + 8, v95 - 0.6),
             arrowprops=dict(arrowstyle='->'))

plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.savefig("graph.pdf")
subprocess.run(["termux-open","graph.pdf"])
