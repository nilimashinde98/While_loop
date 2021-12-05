# Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms

# n=int(input("enter a number"))
# i=0
# while i<=n:
#     j=1
#     while j<=i:
#         j=j+1
#         print("2"*i,end="  , ")
#     i=i+1


# Write a program to print the following series till n terms.1 4 9 16 25 _ _ _ _ _ n  terms

# n = int(input("Enter the range of number:"))
# i=1
# while i<=n:
#     print(i*i,end=" ")
#     i=i+1

# Write a program to print only odd numbers from the given list using  a while loop .
#  L = [23, 45, 32, 25, 46, 33, 71, 90]

a = [23, 45, 32, 25, 46, 33, 71, 90]
i=0
b=len(a)
while i<=len(b):
    if  int(b)%2==0:
        print( b)
    i=i+1