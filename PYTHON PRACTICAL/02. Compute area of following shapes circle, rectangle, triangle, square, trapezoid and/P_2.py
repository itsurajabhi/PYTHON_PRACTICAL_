import math

def compute_areas():
    # Circle
    radius = float(input("Enter the radius of the circle: "))
    circle_area = math.pi * radius ** 2
    print(f"Area of the circle: {circle_area:.2f}")
    
    # Rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle_area = length * width
    print(f"Area of the rectangle: {rectangle_area:.2f}")
    
    # Triangle
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triangle_area = 0.5 * base * height
    print(f"Area of the triangle: {triangle_area:.2f}")
    
    # Square
    side = float(input("Enter the side length of the square: "))
    square_area = side ** 2
    print(f"Area of the square: {square_area:.2f}")
    
    # Trapezoid
    base1 = float(input("Enter the first base of the trapezoid: "))
    base2 = float(input("Enter the second base of the trapezoid: "))
    height_trap = float(input("Enter the height of the trapezoid: "))
    trapezoid_area = 0.5 * (base1 + base2) * height_trap
    print(f"Area of the trapezoid: {trapezoid_area:.2f}")
    
    # Parallelogram
    base_para = float(input("Enter the base of the parallelogram: "))
    height_para = float(input("Enter the height of the parallelogram: "))
    parallelogram_area = base_para * height_para
    print(f"Area of the parallelogram: {parallelogram_area:.2f}")

# Call the function to compute areas
compute_areas()
