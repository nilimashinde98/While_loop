
# num=int(input("enter a year"))
# while num<=1:
#     # user=int(input("enter your year:-"))
#     if num%4==0:
#         print("leap year")
#     else:
#         print("not a leap year")
    

num=int(input("enter a no"))
num=0
while num<1:
    if num%4==0:
        print("leap year")
    else:
        print("not leap year")
    num=num+1
    
# i=1
# while(i==1):
#     x=int(input("Enter the year:-"))
#     if(x%4==0 or x%400==0):
#         print("Leap year") 
#     else:
#         print("Not Leap year") 
#     i=i+1           


# num1=int(input("enter a starting year"))
# num2=int(input("enter ending year"))
# # num1=0
# while num1<=num2:
#     # num1=num1+1
#     if num1%4==0:
#         print(num1,"leap year")
#     # else:
#     #     print(num1,"not a leap year")
#     num1=num1+1


# a=int(input("enter your number"))
# i=1
# sum=0
# while i<a:
#     if a%i==0:
#         sum+=i
#     i=i+1
#     # print(sum)
# if a==sum:
#     print("perfect number")
# else:
#     print("not perfect number")


# strong no

num=int(input("enter a number"))
sum=0
num2=num
while(num):
    i=1
    f=1
    b=num%10
    while(i<=b):
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if(sum==num2):
    print("this is a strong no")
else:
    print("this is not a strong no")
