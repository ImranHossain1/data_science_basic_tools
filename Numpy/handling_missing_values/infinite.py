# np.isinf() 10^1000
# 1/0
import numpy as np

# np.isinf(array) checks for infinite values in a NumPy array.
arr1d = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr1d))  # Output: [False False  True False  True False]