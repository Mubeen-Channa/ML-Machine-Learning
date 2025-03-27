
# Python does not have a built-in array type like other languages, 
# but it provides two main ways to use arrays:

    # Using Lists (Built-in, but slower)
        arr = [1, 2, 3, 4, 5]  
        print(arr[0])  # Output: 1

    
    # Using NumPy Arrays (Faster & More Efficient)
        import numpy as np 

        arr = np.array(arr)  
        print(arr[0])  # Output: 1

# For large datasets, NumPy arrays are preferred due to better performance