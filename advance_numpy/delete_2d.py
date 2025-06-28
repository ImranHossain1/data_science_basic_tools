import numpy as np
# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

new_arr_2d = np.delete(arr_2d, 0, axis=0)  # Delete the row at index 1
print("Original 2D array:\n", arr_2d)
print("Array after deleting the row at index 0:\n", new_arr_2d)