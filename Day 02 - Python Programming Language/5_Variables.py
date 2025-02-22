# Variable : A Location in memory to store a value.

    # Types of Variables: Four main types of variables.
        # 1.Integer (int) → Whole numbers
            age = 23

        # 2. Float (float) → Decimal numbers
            height = 5.6

        # 3. String (str) → Text
            name = "Mubeen"

        # 4. Boolean (bool) → True/False values
            flag = True 


    # Deleting Variables: You can delete a variable using the del keyword. This removes the variable from memory.
    x = 10
    del x
    print(x)  # NameError: name 'x' is not defined


    # Python is dynamically typed, so you don’t need to define types explicitly.
    age = 10         # Automatically an int  
    height = 5.6     # Automatically a float  
    name = "Mubeen"  # Automatically a string  


# Casting
    # If you want to specify the data type of a variable, this can be done with casting.
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0


# We can get the data type of a variable with the type() function.
    print(type(age))
    print(type(name))


# In the print() function, you output multiple variables, separated by a comma:
    age = 23
    height = 5.6
    name = "Mubeen"
    print(age, height, name)
