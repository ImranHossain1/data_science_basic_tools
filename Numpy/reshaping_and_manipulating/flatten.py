"""
.ravel -> view of the array, flattened to 1D
.flatten -> copy of the array, flattened to 1D
"""

import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Using ravel to flatten the array
arr_ravel = arr_2d.ravel()
print("Using ravel:" , arr_ravel)  # Output: [1 2 3 4 5 6]
# Using flatten to flatten the array
arr_flatten = arr_2d.flatten()
print("Using flatten:", arr_flatten)  # Output: [1 2 3 4 5 6]

# Modifying the original array to show the difference
arr_ravel[0] = 10
print("Modified original array after ravel:", arr_2d)  # Output: [[10  2  3]

arr_flatten[0] = 20
print("Modified original array after flatten:", arr_2d)  # Output: [[10  2  3]