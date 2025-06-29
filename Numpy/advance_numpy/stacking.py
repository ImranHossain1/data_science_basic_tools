"""
vstack() row wise stacking
hstack() column wise stacking
dstack() depth wise stacking

"""

import numpy as np
arr1= np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])

print("Original arrays")
print("arr1:\n", arr1)
print("arr2:\n", arr2)

print("vstack: ",np.vstack((arr1, arr2)))  # Stack arrays vertically (row wise)
print("hstack",np.hstack((arr1.T, arr2.T)))  # Stack arrays horizontally (column wise)
print("dstack", np.dstack((arr1, arr2)))  # Stack arrays depth wise