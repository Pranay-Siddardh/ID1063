import numpy as np

n = int(input("Enter the value of n: "))

v = np.arange(1, n + 1).reshape(n, 1)

t= v @ v.T

print(t)
