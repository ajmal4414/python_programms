for row in range(7):
    for coloumn in range(7):
        if coloumn==0 or coloumn ==6 or ((row==coloumn) and (coloumn>0 and coloumn <4)) or (row==1 and coloumn==5) or (row==2 and coloumn ==4):

            print("*",end="")
        else:
            print(end=" ")

    print()