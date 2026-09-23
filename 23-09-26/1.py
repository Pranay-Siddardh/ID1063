import numpy as np

data = np.array([3,4,0,5])
data1 = np.array([1,-1,1,-1])
data2 = np.array([7.5])

rms = np.sqrt(np.square(np.linalg.norm(data))/4)
rms1 = np.sqrt(np.square(np.linalg.norm(data1))/4)
rms2 = np.sqrt(np.square(np.linalg.norm(data2))/1)

print(f"The Rms value of the test case 4, 3 4 0 5 is {rms}")
print(f"The Rms value of the test case 4, 1 -1 1 -1 is {rms1}")
print(f"The Rms value of the test case 1, 7.5 is {rms2}")
