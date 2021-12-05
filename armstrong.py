i=int(input("enter your number you want to cheaek"))
sum=0
orig=i
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("armstrong no")
else:
    print("not armstrong no")


# a=100
# sum=0
# orig=a
# while a<=100:
#     sum=sum+(orig%10)*(orig%10)*(orig*10)
#     orig=orig//10
#     orig=orig+1
# if orig==sum:
#     print("armstrong no hai")
# else:
#     print("armstrong no nahi hai")
