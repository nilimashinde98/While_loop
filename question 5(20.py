# take an integer input in a variable named n. Take user input as many times as the value of n.

# Finally, print the sum of all those numbers which you have taken as an input.

# Example: If the user has put n value as 6, then take input for 6 times.

# n=int(input("how much times you want:"))
# i=1
# while n>0:
#     user=int(input("enter a no"))
#     sum=0
#     sum=sum+i
#     i=i+1
# print()

i=1
sum=0
num=int(input("number of input you taken:"))
while i<=num:
    n=int(input("enter the no:"))
    sum=sum+n
    i=i+1
print( sum)

