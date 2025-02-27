# Loops (for, while)

# Example 1: for loop (iteration over a sequence)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Example 2: for loop (using range)
print("\nCounting from 1 to 5:")
for m in range(1, 6):
    print(m)

# Example 3: while loop
num = 1
while num <= 5:
    print("Current number:", num)
    num += 1

# # Example 4: Infinite loop with break statement
while True:
    user_input = input("Enter a number (type 'exit' to quit): ")
    if user_input == 'exit':
        break
    print("You entered:", user_input)