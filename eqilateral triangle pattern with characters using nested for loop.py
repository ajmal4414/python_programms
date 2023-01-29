n=int(input("enter a no:"))

k=65

for i in range(0,n):

    for m in range(0,n-i-1):
        print(" ",end="")

    for j in range(0,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()