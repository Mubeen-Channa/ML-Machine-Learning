import numpy as np

# Basic array operations
"""
    NumPy supports a wide range of operations on arrays, including arithmetic operations, statistical operations,
    and more.
"""

# Example: Arithmetic operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("Array1:", array1)
print("Array2:", array2)

print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)

# Example: Statistical operations

array_data = np.array([[1, 2, 3], [4, 5, 6]])

print("Mean:", array_data.mean())
print("Sum:", array_data.sum())
print("Standard Deviation:", array_data.std())
print("Max:", array_data.max())
print("Min:", array_data.min())