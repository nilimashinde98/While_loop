# num=int(input("enter the no"))
# fact=1
# while num>0:
#     fact=fact*num
#     num=num-1
# print(fact,"factorial")

i=int(input("enter no"))
rev=0
while i>0:
    rev=(rev*10)+(i%10)
    i=i//10
print("reverce=",rev)


# i="nilima"
# k=list(i)
# k.reverse()
# j=0
# t=' '
# while j<len(k):
#     a=k[j]
#     t+=a
#     j=j+1
# print(t)


# reverse string
s = "nilima"
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))  