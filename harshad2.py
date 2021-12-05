i=int(input("enter your no"))
sum=0
c=i
while c>0:
    r=c%10
    sum=sum+r
    c=c//10
if c%sum==0:
    print("harshad hai")
else:
    print("harshad nahi hai")

    