# n=1
# sum=0
# while n<=10:
#     user=int(input("enter a number"))
#     sum=user+sum
#     avg=sum/user
#     n=n+1
# print(avg)



i=100
sum=0
sum2=0
while i<=500:
    if i%2==0:
        sum=sum+i
        
    else:
        sum2=sum2+i
    i=i+1
print(sum)
print(sum2)