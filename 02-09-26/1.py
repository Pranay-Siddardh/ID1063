x = int(input("Enter a number n"))
import numpy as np


arr = np.arange(1, x + 1)
matrix = np.outer(arr, arr)

print(str(matrix))

