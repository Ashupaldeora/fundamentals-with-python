start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

def is_prime(num):
    if num <= 1:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

for num in range(start_num, end_num):
        if is_prime(num):
            print(num, end=" ")