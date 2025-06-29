import numpy as np
arr_2d = np.array([[1, 2], [3,4]])
print("Original 2D array:\n", arr_2d)
new_arr_2d = np.insert(arr_2d, 1, [100, 200], axis=0)  # Insert a new row at index 1
print("Array after inserting a new row at index 1:\n", new_arr_2d)