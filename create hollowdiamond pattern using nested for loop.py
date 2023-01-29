row=11
col=11

for i in range(row):
    for m in range(col):
        if(i+m==5) or(m-i==5) or (i+m==15) or (i-m==5):
            print("*",end="")
        else:
            print(" ",end="")

    print()