import numpy as np

def daysElapsed(day, month):
    days = np.array([31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31])

    total = day

    for i in range(month - 1):
        total += days[i]

    return total


day = input("Enter The Day: ")
month = input("Enter The Month: ")

output = daysElapsed(day, month)

print(f"day = {day}")
print(f"month = {month}")
print(f"Days Elapsed = {output}")
