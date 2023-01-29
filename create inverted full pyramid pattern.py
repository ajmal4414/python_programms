n=int(input("enter the rows:"))

for i in range(n):
    for k in range(i):
        print(" ",end="")

    for k in range(n-i):

        print("*",end=" ")
    print()