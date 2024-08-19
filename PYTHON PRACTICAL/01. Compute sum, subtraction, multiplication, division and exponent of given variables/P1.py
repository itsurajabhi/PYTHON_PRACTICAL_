# Function to compute sum, subtraction, multiplication, division, and exponent
def compute_operations(a, b):
    sum_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b
    division_result = a / b if b != 0 else "undefined (division by zero)"
    exponent_result = a ** b
    
    return sum_result, subtraction_result, multiplication_result, division_result, exponent_result

# Take input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform the calculations
sum_result, subtraction_result, multiplication_result, division_result, exponent_result = compute_operations(a, b)

# Display the results
print(f"Sum: {sum_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")
print(f"Exponent: {exponent_result}")
