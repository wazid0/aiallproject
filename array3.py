import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("sum of the array=",arr.sum())
print("maximum of the array=",arr.max())
print("minimum of the array=",arr.min())
print("maximum of the array=",arr.max(axis=1))
print("minimum of the array=",arr.min(axis=1))
print("cumsum of the array=",arr.cumsum(axis=1))
print("avg =", np.average(arr))
