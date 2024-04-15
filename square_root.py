def square_root(num):
    if num < 0:
        return "Square root is not defined for negative numbers"
    elif num == 0:
        return 0
    else:
        return num ** 0.5

# Example usage
number = float(input("Enter a number to find its square root: "))
result = square_root(number)
print("Square root of", number, "is", result)
