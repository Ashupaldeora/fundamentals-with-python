import math

def area_of_circle(radius):
    return math.pi * (radius * radius)

# Example usage
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print("Area of the circle with radius", radius, "is", area)
