import numpy as np  # np is Alias name of numpy here

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# To print third value in first of first array (3)
print(arr[0, 0, 2])

# To print first value inn second of second array (10)
print(arr[1, 1, 0])
