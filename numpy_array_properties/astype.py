import numpy as np
arr = np.array([1.2, 2.5, 3.8])
print("Original array type:", arr.dtype)
int_arr = arr.astype(int)
print("Converted array type:", int_arr.dtype)
print("Converted array:", int_arr)  # Output: [1 2 3] 