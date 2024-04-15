def is_armstrong_number(num):
  
    num_str = str(num)
    num_digits = len(num_str)
    
   
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    
   
    return sum == num

number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

