def CheckTriangle(x, y, z):
    if x == y == z:
        print("Equilateral Triangle")
    elif x == y or y == z or z == x:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

# Define side lengths
x = 8
y = 7
z = 9

# Call the function with the defined side lengths
CheckTriangle(x, y, z)

