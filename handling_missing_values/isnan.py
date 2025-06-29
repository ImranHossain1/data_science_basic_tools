# np.isnan(array) checks for NaN values in a NumPy array.
import numpy as np
arr1d = np.array([1, 2, np.nan, 4, 5])
print(np.isnan(arr1d))  # Output: [False False  True False False]