fibonacci = [0,1]
num = int(input("Enter n : "))
for i in range(0,num):
    prev1 = fibonacci[i]
    prev2 = fibonacci[i+1]
    new_num = prev1+prev2
    fibonacci.append(new_num)

print(fibonacci)
