

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end = " ")
    
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == rows:
            print(j, end = " ")
        else:
            print(" ", end = " ")
    
    print()