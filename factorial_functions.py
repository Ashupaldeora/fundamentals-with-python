def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print("Factorial of", number, "is", result)
