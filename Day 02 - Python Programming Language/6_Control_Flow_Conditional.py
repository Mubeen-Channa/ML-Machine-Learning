# Conditional Statements (if, elif, else)

    # Example 1: Basic if statement
    x = 10
    if x > 5:
    print("x is greater than 5")

    # Example 2: if-else statement
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")

    # Example 3: if-elif-else statement
    z = -1
    if z > 0:
        print("z is positive")
    elif z == 0:
        print("z is zero")
    else:
        print("z is negative")

    # Example 4: Nested if statements
    a = 15
    b = 20
    if a > 10:
        if b > 15:
            print("Both a is greater than 10 and b is greater than 15")