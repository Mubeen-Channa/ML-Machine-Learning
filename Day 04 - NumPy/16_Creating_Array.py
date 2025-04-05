import numpy as np

# 1. Basic NumPy Array Operations

# Creating arrays
"""
    NumPy arrays are created using the `np.array` function, which can convert lists or tuples into arrays.
"""

# Example: Creating a NumPy array from a list
list_data = [1,2,3,4,5]
array_data_1 = np.array(list_data)
print("Array from list:", array_data_1)

# Example: Creating a NumPy array from a tuple
tuple_data = (6,7,8,9,10)   # Immutable
array_data_2 = np.array(tuple_data)
print("Array from tuple:", array_data_2)

print("List_data:  "); type(array_data_1)
print("Tuple_data: "); type(array_data_2)


array_data = np.array([[1,2,3], [4,5,6]])
print("Array:\n", array_data)
print("Shape:", array_data.shape)  # Shape of the array
print("Size:", array_data.size)    # Total number of elements
print("Data type:", array_data.dtype)  # Data type of elements
print("Number of dimensions:", array_data.ndim)  # Number of dimensions