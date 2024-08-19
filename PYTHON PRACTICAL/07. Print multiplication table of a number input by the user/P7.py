#Print multiplication table of a number input by the user.

# Get user input
number = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):  # Typically, multiplication tables go from 1 to 10
    print(f"{number} x {i} = {number * i}")
