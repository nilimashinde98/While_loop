# We will call this game a guessing game.
# In this game we take any number, let us suppose this number is number 5.
# After this we take any number as an input from the user between 1 to 10. 
# The user tries to guess this number.


# print("guessing game")

# i=0
# while i<=10:
#     num=int(input("enter your guess number "))

#     if num==5:
#         print("your guessing number is right🙂 ")
#         break
#     else:
#         print("you guessing number is wrong 🙃 ")
#         i=i+1
#     print()
    

# import random
# >>> random.randint(1, 100)
# 95           
# >>> random.randint(1, 100)
# 49

print("guessing game")
import random
i=0
h=random.randint(1,10)
while i<=6:
    num=int(input("enter your guess number "))
    if num<h:
        print("num is smaller, enter a greater number")
    elif num>h:
        print("num is greater, enter a smaller number")
    elif h==num:
        print(h," your guessing number is right🙂 ")
        break
    i=i+1
    print()