n=int(input("enter fibonacci sequence:"))
n1=0
n2=1
i=0
if (n<0):
    print("enter positive values")
elif (n==1):
    print(n1)
else:
    print(n1)
    print(n2)
    while (i<n):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        i+=1