# Write a program to accept 10 numbers from the user and display the largest & smallest number.

i=0
largest=0
smallest=0
while i<10:
    user=int(input("enter a number"))
    if i==0:
        smallest=user
    if user<smallest:
        smallest=user
    if user>largest:
        largest=user
    
    i+=1
print(largest)
print(smallest)











# 5
# 54
# 543
# 5432
# 54321

# 5
# 44
# 333
# 2222
# 11111
# i=5

# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(j,end="")
#         j=j-1
#     print()
#     i=i-1