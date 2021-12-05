print("guessing game")
i=0
while i<6:
    num=int(input("enter your guessing number"))
    if num<5:
        print("your guessing number is smaller than real one ")
    elif num==5:
        print("your guessing number is right")
        break
    else:
        print("your guessing number is greater than real one ")
    
    i=i+1
    print()
    