n=int(input("enter the rows:"))

for i in range(n):

    for k in range(n-i-1,-1,-1):

        print(k+1,end=" ")
    print()