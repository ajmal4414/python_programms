onlineshoppingapp1=int(input("enter the shopping app:"))

if (onlineshoppingapp1==1):
    print("welcome to online shopping, choose what type of product you want:")
    print("1 for home appliances & 2 for kitchen appliances & 3 for electronics")

    x= int(input("enter your choice:"))

    if x==1:
        print("you buy home appliances")

    elif x==2:
        print("you buy kithcen appliances ")

    elif x==3:
        print("you buy electronics")

    else:
        print("you didn,t buy products ")
