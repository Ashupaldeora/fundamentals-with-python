num1 = int(input("Enter 1st number : "))
count = num1
factorial = 1

while(count>1):
   factorial*=count 
   count=count-1
   
print("Factorial is ",factorial)
