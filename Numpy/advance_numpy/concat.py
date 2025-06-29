"""
np.concatenate((array1, array2), axis=0)
axis 0 > vertical concatenation (adding rows)
# axis 1 > horizontal concatenation (adding columns)
"""
import numpy as np

arr1= np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])

new_arr = np.concatenate((arr1, arr2), axis=0)  # Concatenate vertically
print("Array after vertical concatenation:\n", new_arr)
new_arr_horizontal = np.concatenate((arr1.T, arr2.T), axis=1)  # Concatenate horizontally
print("Array after horizontal concatenation:\n", new_arr_horizontal)
