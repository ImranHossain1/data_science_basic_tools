import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
# Broadcasting the vector to match the shape of the matrix
result = matrix + vector  # The vector is added to each row of the matrix   
print("Original matrix:\n", matrix)
print("Vector to be added:\n", vector)
print("Result after broadcasting addition:\n", result)
