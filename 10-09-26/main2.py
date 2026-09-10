import numpy as np

print("Equations:")
print("2x + 3y = 6")
print("4x + 6y = 3k")
print()

# -------------------------------------------------
# Function to construct and row-reduce the matrix
# -------------------------------------------------

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


# -------------------------------------------------
# Same-line case
# -------------------------------------------------

print("=" * 50)
print("SAME LINE CASE")
print("=" * 50)

solve_matrix(4)


# -------------------------------------------------
# Parallel-line cases
# -------------------------------------------------

print("\n\n" + "=" * 50)
print("PARALLEL LINE CASES")
print("=" * 50)

for k in [1, 2, 3, 5, 6]:

    print("\n" + "-" * 40)

    solve_matrix(k)
