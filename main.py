num=int(input("enter the number:"))
n=num//2

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    if num%2 ==0:
        for j in range(2*(n-i-1):
            print(" ", end="")

    else:
        for j in range(2*(n-i-1)+1):
            print(" ",end="")
    for j in range(i+1):
        print("* ", end="")
    print()