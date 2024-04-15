def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = perimeter_of_rectangle(length, width)
print("Perimeter of the rectangle with length", length, "and width", width, "is", perimeter)
