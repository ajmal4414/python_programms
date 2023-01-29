num=input("enter the no of digits:")

leng1=len(num)

for i in  range(leng1):
    for j in range(leng1):
        if (i==j or i+j==8):
            print(num[i],end=" ")
        else:
            print(" ",end=" ")
    print()
