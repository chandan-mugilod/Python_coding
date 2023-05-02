import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# For slicing we use syntax -> [start:end:step]
print(arr[1:4:2])  # [2 4]

# Negative indexing
print(arr[-1:-5:-2])  # [7 5]

# SLICING 2D ARRAYS

arr2 = np.array([[1, 2, 3, 4, 5, 50], [6, 7, 8, 9, 10, 17]])

# To get 9 10 17
print(arr2[1, 3:])
# To get 3 4 5
print(arr2[0, 2:5])
# From both elements, slice index 1 to 4 in arr2 , This will return a 2-D array
print(arr2[0:2, 1:4])       # [[2 3 4] [7 8 9]]
