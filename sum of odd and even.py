n=5
sum=0
while n<=20:
    if n%2==0:
        sum=n+sum
        print(n,sum,"even")
    else:
        if n%2!=0:
            sum=n+sum
            print(n,sum,"odd")
    n=n+1
