#Code by pranay
#Date 10-09-2026

from math import e
import matplotlib.pyplot as p
import numpy as n

x = n.linspace(-10,10,1000)

p.xlabel("X-Axis")
p.ylabel("Y-Axis")

p.plot(x,e**x -2)
p.savefig("graph.png")

