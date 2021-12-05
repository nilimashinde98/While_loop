# num=int(input("enter the number"))
# num2=num
# sum=0
# while sum!=1 and sum!=4:
#     while num2!=0:
#         num=int(num2%10)
#         sum=sum+num*num
#         num2=num/10
# if sum==1:
#     print(num,"is a happy no")
# else:
#     print(num,"it is a not happy no")

num=int(input("enter a number"))
sum=0
while num>0:
    num=num%10
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if num%1==0:
    print("happy number")
else:
    print("sad number")