"""
slicing 
array[start:stop:step]
arr[start: end] # Slicing a 1D array from start to end
negative step, -1 reverse the array
"""

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr[1:5])  # Slicing from index 1 to 3 (4 is exclusive)
print(arr[:5])  # Slicing from the start to index 5 (5 is exclusive)
print(arr[: : 2])  # Slicing the array with a step of 2
print(arr[5:])  # Slicing from index 5 to the end
print(arr[::-1])  # Reversing the array