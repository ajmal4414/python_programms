r=int(input("enter the no of rows:"))

k=ord("A")

for i in range(0,r+1):

    for m in range(0,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()