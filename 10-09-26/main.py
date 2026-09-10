#Code by pranay
#Date 10-09-2026

from math import e
import matplotlib.pyplot as p
import numpy as n

#defining x values
x = n.linspace(-10,10,1000)

#labeling axes
p.xlabel("X-Axis")
p.ylabel("Y-Axis")

#plotting graph
p.plot(x,e**x -2)

#saving
p.savefig("graph.png")

