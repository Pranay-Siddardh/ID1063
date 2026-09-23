#Code by pranay
#date 23-09-26

import numpy as np

def runLength(a, i):
    #breaking and returning under the case that a[i] = 0
    if a[i] == 0:
        return 0

    count = 0
#remaining values checker of array exceeding i
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

#breaknig and printing the conditions but not, then running fot all the i till the loop is broken
    if length > k:
        answer = i + k + 1
        break

print(f"n = {n}")
print(f"k = {k}")

print("Entries:", *a)

print(f"Output = {answer}")
