# # row=5
# # i=0
# # i=row-1
# # while i>=0:
# #     j=0
# #     while j<i:
# #         print('',end=" ")
# #         j+=1
# #     k=i
# #     while k<= row-1:
# #         print("*",end=" ")
# #         k+=1
# #     print()
# #     i-=


# # row=5
# # i=row-1
# # while i>=0:
# #     j=0
# #     while j<i:
# #         print('',end=" ")
# #         j+=1
# #     k=i
# #     while k<= row-1:
# #         print("*",end=" ")
# #         k+=1
# #     print()
# #     i-=1


# row=int(input("enter number of row"))
# i=row-1
# while i>=0:
#     j=1
#     while j<i:
#         print(' ',end="")
#         j+=1
#     k=i
#     while k<=row-1:
#         print("*",end=" ")
#         k+=1
#     print()
#     i-=1


k=1
i=1
while i<=5:
    b=1
    while (b<=5-i):
        print(' ',end=" ")
        b=b+1
    j=1
    while j<=k:
        print("*",end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1
i=1
k=7
while i<=5:
    j=1
    while j<=i:
        print(" ",end=" ")
        j=j+1
    s=1
    while s<=k:
        print("*",end=" ")
        s=s+1
    k=k-2
    print()
    i=i+1