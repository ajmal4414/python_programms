#largest among three numbers

a=int(input("enter a value of a"))
b=int(input("enter the value of b"))
c=int(input("enter a value of c"))

if (a>b):
    if (a>c):
        print("a is large" )
    else:
        print("c is large")

elif (b>c):
    print("b is large")
else:
    print("c is large")
