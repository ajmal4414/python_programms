rows=int(input("enter rows:"))

for i in range(rows):
    print(" "*(rows-i)+" *"*(i+1))

for k in range(rows-1):
    print(" "*(k+2)+" *"*(rows-1-k))