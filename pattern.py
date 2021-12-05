# num=int(input("enter a number"))
# i=1
# while i<=num:
#     print("+"+"a"+str(i)+","+"z"+str(i)+"")
#     i=i+1




# i=1
# j=5
# while i<5:
#     print("*")
#     i=i+1
#     i=1
#     j=5
#     while j>5:
#         print("*")
#         j=i+1




# n = int(input('Enter number of rows : '))
# i = 1
# while i <= n :
#     j = n
#     while j >= i:
#         print("*", end = " ")
#         j -= 1
#     print()
#     i += 1

n=int(input("enter number of rows"))
i=1
while i<=n:
    print("*",end="")
    j=n
    while j<i:
        print("*",end="")
        j=j+1
    print()
    i=i+1

