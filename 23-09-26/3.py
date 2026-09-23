import numpy as np

def runLength(a, i):
    if a[i] == 0:
        return 0

    count = 0

    while i < len(a) and a[i] == 1:
        count += 1
        i += 1

    return count


a = np.array(list(map(int, input("Enter the array: ").split())))

k = int(input("Enter k: "))

n = len(a)
answer = 0

for i in range(n):
    length = runLength(a, i)

    if length > k:
        answer = i + k + 1
        break

print(f"n = {n}")
print(f"k = {k}")

print("Entries:", *a)

print(f"Output = {answer}")
