# Question 5

# Take input of weights of 11 people and then print their average
# and then check whether the average weight is a multiple of 5 or not? 
# This means that when you will divide the average weight by 5, the remainder should be 0.
# Note :-
# Here you have to use input function. You can also use raw input to take the weights 
# as inputs, inside the loop.


i=0
sum=0
avg=0
while i<11:
    user=int(input("enter your weight"))
    sum=sum+user
    avg=sum/11
    print(avg)
    i=i+1
# avg=sum/5
print("sum",sum)
if avg%5==0:
    print("divisible by 5::",avg)
else:
    print("not divisible by 5")