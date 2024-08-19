import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check the nature of the roots based on the discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The equation has two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"The equation has one real root: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"The equation has two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

# Take input from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Ensure that 'a' is not zero to maintain the quadratic nature of the equation
if a == 0:
    print("Coefficient 'a' cannot be zero in a quadratic equation.")
else:
    # Find and print the roots
    result = find_roots(a, b, c)
    print(result)
