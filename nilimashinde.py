print()
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or (row==col and (col>0 and col<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()

print()
for row in range (7):
    for col in range (5):
        if col==2 or (row==0 or row==6) and col!=2:
            print("*",end="")
        else:
            print(end=" ")
    print()