# number of dimensions of the array
import numpy as np
# Creating a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
# Creating a 2D array
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6]])   
# Creating a 3D array
arr3d = np.array([[[1, 2], [3, 4]], 
                  [[5, 6], [7, 8]]])

# Getting the number of dimensions
print("Number of dimensions of the array 1d:", arr1d.ndim)  # Output: 2
print("Number of dimensions of the array 2d:", arr2d.ndim)  # Output: 2
print("Number of dimensions of the array 3d:", arr3d.ndim)  # Output: 2