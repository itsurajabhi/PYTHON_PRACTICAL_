import cmath
# Coefficients
a = 1
b = 5
c = 6

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Calculate the two solutions using the quadratic formula
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

# Print the solutions
print("The solutions are {0} and {1}".format(sol1, sol2))
