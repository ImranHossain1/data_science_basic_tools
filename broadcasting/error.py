import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)
arr2 = np.array([[1,2]])  # shape (1, 2)

result = arr1 + arr2  # Broadcasting arr2 to match the shape of arr1
print("Original arr1:\n", arr1)
print("Original arr2:\n", arr2)
print("Result after broadcasting addition:\n", result)