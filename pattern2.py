# 1 1 1 1 
# 2 2 2 
# 3 3 
# 4 

n = int(input('Enter number of rows : '))
i = 1
while i <= n :
    j = n
    while j >= i:
        print(i, end = " ")
        j -= 1
    print()
    i += 1

