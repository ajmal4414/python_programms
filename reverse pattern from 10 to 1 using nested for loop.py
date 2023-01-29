n=int(input("enter the no of rows:"))

for i in range(n):

    for j in range(n-i-1,-1,-1):
        print(j+1,end=" ")
    print()
