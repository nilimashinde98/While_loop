#  Write a program to print the Fibonacci series till n terms (Accept n from user)
# n=int(input("enter your number"))
# i=0
# x=0
# y=1
# z=0
# while i<=n:
#     x=y
#     y=z
#     z=x+y
#     print(z)
#     i=i+1


i=int(input("enter a no"))
sum=0
orig=i
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("armstrong")
else:
    print("not armstrong")


# i=int(input("enter your number you want to cheaek"))
# sum=0
# orig=i
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if orig==sum:
#     print("armstrong no")
# else:
#     print("not armstrong no")
