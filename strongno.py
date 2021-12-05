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
