def reverse_number(num):
    reversed_num = 0
    
   
    while num > 0:
       
        digit = num % 10
        
       
        reversed_num = reversed_num * 10 + digit
        
        
        num = num // 10
    
    return reversed_num

# Example usage
number = int(input("Enter a number to reverse: "))
result = reverse_number(number)
print("Reversed number:", result)
