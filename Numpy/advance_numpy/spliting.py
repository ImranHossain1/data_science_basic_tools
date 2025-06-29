"""
np.split()
equal
np.hsplit()
np.vsplit()
np.dsplit()
"""

import numpy as np
# Create a 1D array
arr = np.array([10, 20, 30, 40, 50, 60])
# Split the array into 3 equal parts
arr_split = np.split(arr, 3)  # Split into 3 equal parts
print("Original array:", arr)
print("Array after splitting into 3 equal parts:", arr_split)