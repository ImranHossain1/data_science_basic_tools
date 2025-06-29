"""
np.delete(array, index, axis= None) is used to delete elements from a NumPy array along a specified axis.
flattened array: If axis is None, the input array is flattened before deletion.
"""
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
new_arr = np.delete(arr, 2, axis=None)  # Delete the element at index 2 in the flattened array
print("Original array:", arr)   
print("Array after deletion:", new_arr)