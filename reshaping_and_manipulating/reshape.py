"""
reshape(rows, columns) specifies the number of rows and columns to reshape the array.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3) # Reshaping to 2 rows and 3 columns
print(reshaped_arr)  # Output: [[1 2 3] [4 5 6]]