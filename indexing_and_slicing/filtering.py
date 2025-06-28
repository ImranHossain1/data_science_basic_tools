import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(arr[arr> 25])  # Filtering elements greater than 25
print(arr[arr < 50])  # Filtering elements less than 50
print(arr[(arr > 25) & (arr < 75)])  # Filtering elements