string = input("Enter a string : ")
count = len(string)-1
countReverse = 0;
reversedString=string
isPalindrome = False
while (count>=0):
    reversedString[countReverse] = string[count]
    count=count-1
    countReverse=countReverse+1

for i in range(string):
    for v in range(reversedString):
        if i!=v:
            isPalindrome = False

        else:
            isPalindrome=True    

if isPalindrome==True:
    print("String is palindrome")