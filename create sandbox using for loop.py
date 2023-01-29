n=int(input("enter the value:"))

for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

for k in range(0,n):
    print(" "*(n-k-1)+ "* "*(k+1))