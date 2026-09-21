#Code BY T.Pranay
#Date 10-09-26

import sys
import subprocess
import numpy as np
sys.path.append("/sdcard/.github/matgeo/codes/CoordGeo")
from line.funcs import *
import matplotlib.pyplot as plt

print("Equations:")
print("2x + 3y = 6")
print("4x + 6y = 3k \n")

#making a solving function for the spec matrix of ours
def solve_matrix(k):

    # Augmented matrix
    M = np.array([
        [2.0, 3.0, 6.0],
        [4.0, 6.0, 3.0 * k]
    ])

    print("k =", k)
    print("Augmented Matrix:")
    print(M)

    # Gaussian elimination
    M[1] = M[1] - 2 * M[0]

    print("\nAfter R2 -> R2 - 2R1:")
    print(M)

    # Check the result
    if abs(M[1][2]) < 1e-10:
        print("\nResult: Infinitely many solutions")
        print("The two equations represent the SAME LINE.")

        # 2x + 3y = 6
        # Let y = t
        # x = (6 - 3t)/2

        print("\nFirst 100 solutions:")
        print("No.\t x\t\t y")

        for i in range(1, 101):
            y = float(i)
            x = (6 - 3 * y) / 2

            print(f"{i}\t{x:.2f}\t\t{y:.2f}")

    else:
        print("\nResult: NO SOLUTION")
        print("The two equations represent PARALLEL DISTINCT LINES.")


# Same-line case

print("=" * 50)
print("SAME LINE CASE")
print("=" * 50)

solve_matrix(4)


# Parallel-line cases

print("\n\n" + "=" * 50)
print("PARALLEL LINE CASES")
print("=" * 50)

for k in [1, 2, 3, 5, 6]:

    print("\n" + "-" * 40)

    solve_matrix(k)

x = line_gen(-10,10)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

k_val = i
    
y1 = (6-2*x)/3
y2 = (3*k_val-4*x)/6
plt.plot(x,y1)
plt.plot(x,y2)

plt.savefig("graphy.pdf")
subprocess.run(["termux-open","graphy.pdf"])
