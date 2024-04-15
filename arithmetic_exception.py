def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None

# Example usage
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
result = safe_divide(numerator, denominator)
if result is not None:
    print("Result of division:", result)
