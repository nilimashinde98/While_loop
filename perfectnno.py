a=int(input("enter the number"))
i=1
sum=0
while i<a:
    if a%i==0:
        sum+=i
    i=i+1
print(sum)
if a==sum:
    print("it is a perfect number")
else:
    print("it is not a perfect no")


             