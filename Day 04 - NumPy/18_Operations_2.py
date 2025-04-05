import numpy as np

# Task 4: Use NumPy functions to generate arrays and perform operations
arange_array = np.arange(0, 21, 3)          # 0 to 20 but space of 3 
linspace_array = np.linspace(0, 1, 10)      # 10 values from 0 to 1, evenly spaced.
logspace_array = np.logspace(0, 2, 5)  # Start, stop (10^start to 10^stop), number of samples
identity_matrix = np.eye(3)                 # Identity Matrix
random_array = np.random.random((4, 4))     # 4 by 4 Random Matrix

print("Task 4:")
print("Array using arange:", arange_array)
print("Array using linspace:", linspace_array)
print("Array using logspace:", logspace_array)
print("Identity matrix:\n", identity_matrix)
print("Random array:\n", random_array)
print()

# Task 5: Combine and compare arrays
array3 = np.array([1, 2, 3, 4, 5])
array4 = np.array([6, 7, 8, 9, 10])

concatenated_array = np.concatenate((array3, array4))   # Concitinate Both Arrays
comparison = array4 > array3                            # Compare Each value from Array

print("Task 5:")
print("Array 3:", array3)
print("Array 4:", array4)
print("Concatenated Array:", concatenated_array)
print("Comparison (Array 4 > Array 3):", comparison)

