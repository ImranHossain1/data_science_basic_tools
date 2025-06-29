"""
np.insert(array, index, values, axis=None)
array: The input array into which values are inserted.
index: The index at which values are inserted. If axis is None, index is interpreted as the flattened index.
values: The values to be inserted into the array.
axis: The axis along which to insert values. If None, the input array is flattened before insertion.
axis = None: The input array is flattened before insertion.
axis= 0 , rows are inserted.
axis= 1 , columns are inserted.
"""
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = np.insert(arr, 2, 100, axis=None)  # Insert 100 at index 2 in the flattened array
print("Original array:", arr)
print("Array after insertion:", new_arr)