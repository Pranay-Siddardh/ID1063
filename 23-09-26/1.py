import numpy as np

data = np.array([3,4,0,5])
data1 = np.array([1,-1,1,-1])
data2 = np.array([7.5])

rms = np.sqrt(np.mean((data@data.T)/4))
rms1 = np.sqrt((data1@data1.T)/4)
rms2 = np.sqrt(np.mean((data2@data2.T)/1))

print(f"The Rms value of the test case 4, 3 4 0 5 is {rms}")
print(f"The Rms value of the test case 4, 1 -1 1 -1 is {rms1}")
print(f"The Rms value of the test case 1, 7.5 is {rms2}")
