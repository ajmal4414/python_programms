print(" enter pyramid size:")
n=int(input("enter rows:"))
for i in range(0,n):
    for m in range(0,n-i-1):
        print(" ",end="")

    for k in range(0,i+1):
        print("* ", end="")

    print()