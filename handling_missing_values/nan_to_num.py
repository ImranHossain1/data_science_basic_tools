# np.nan_to_num(array , nan=value) replaces NaN with a specified value in a NumPy array.
import numpy as np
arr= np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8])
cleaned_array = np.nan_to_num(arr, nan= 100)  # Replace NaN with 0
print("Cleaned array:", cleaned_array)