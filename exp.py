exp1=int(input("enter the exp of 1st person:"))
exp2=int(input("enter thr exp of 2nd person:"))
exp3=int(input("enter the exp of 3rd person:"))

if (exp3>exp2) & (exp3>exp1):
    if (exp2>exp3):
        print("you have 3yrs of exp")
    else:
        print("you have 2yrs of exp")
elif(exp1<exp3):
    if (exp3<exp2):

        print("you have 3 yrs of exp")

    else:
        print("you have 2 yrs of exp")

else:
    print("you have no exp")

