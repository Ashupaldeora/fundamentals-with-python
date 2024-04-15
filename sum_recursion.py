def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage
number = int(input("Enter a number to find the sum of its digits: "))
result = sum_of_digits(number)
print("Sum of digits of", number, "is", result)
