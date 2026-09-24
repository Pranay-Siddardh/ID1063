import numpy as np

m, n = map(int, input("Enter matrix size (m n): ").split())

T = int(input("Enter threshold: "))

print(f"Enter {m} x {n} matrix:")
a = np.array([list(map(int, input().split())) for _ in range(m)])

a = np.where(a >= T, 255, 0)

print("Thresholded matrix:")
print(a)
