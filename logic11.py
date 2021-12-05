# 14. Write a program to display the number names of the digits of if the number is 231 
# then output should be Two a number entered by user, for example Three One




num=int(input("enter a number"))
i=0
a=str(num)
while i<len(a):
    if a[i]=="0":
        print("zero",end="")
        
    elif a[i]=="1":
        print("one",end="")
        
    elif a[i]=="2":
        print("two",end="")
        
    elif a[i]=="3":
        print("three",end="")
        
    elif a[i]=="4":
        print("four",end="")
        
    elif a[i]=="5":
        print("five",end="")
      
    elif a[i]=="6":
        print("six",end="")
    
    elif a[i]=="7":
        print("seven",end="")
    
    elif a[i]=="8":
        print("nine",end="")
    
    elif a[i]=="10":
        print("ten",end="")
    print()    
    i+=1