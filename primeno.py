# num=int(input("enter the no"))

# count=0
# i=1
# while(i<=50):
#     if i%2!=0:
#         if i%i==0:
#             count=count+1
#             print(i)
#     i=i+1


# if(count==2):
#     print("prime no")
# else:
#     print("not a prime no")

a=int(input("Enter your number:"))
i=1
count=0
while i<=10:
    if a%i==0:
        count=count+i
    i=i+1
print(count)
if count==2:
    print("prime number")
else:
    print("not prime number")
    
