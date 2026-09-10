# Code by Pranay
# Date 10-09-2026

from math import e, log
import matplotlib.pyplot as p
import numpy as n
import subprocess

x = n.linspace(-2, 2, 500)
y = e**x - 2

# Solution
sol = log(2)
print("Solution: x =", sol)

# Plot
p.plot(x, y)

# Grid
p.grid(True)

# Circle the point
p.scatter(sol, 0, facecolors='none', edgecolors='red', s=100)

# Axes
p.axhline(0)
p.axvline(0)

p.xlabel("X-Axis")
p.ylabel("Y-Axis")

p.savefig("graph.pdf")
subprocess.run("termux-open graph.pdf", shell=True)
