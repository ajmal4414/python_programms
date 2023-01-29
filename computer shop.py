shop1=int(input("enter the 1st laptop shop:"))

if (shop1==1):
    print("welcome to the laptop shop, which laptop you want")
    print("1 for apple laptop & 2 for dell laptop & 3 for hp laptop")
    b=int(input("enter you choice:"))

    if b==1:
        print("you buy apple laptop")
    elif b==2:
        print("you buy dell laptop")

    elif b==3:
        print("you buy hp laptop")

    else:
        print("you didn,t choose the laptop")