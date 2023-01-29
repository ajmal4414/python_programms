word = str(input("enter anything:"))
leng = len(word)

for i in range (0,leng):
    if i ==0 or i == leng-1:
        print(leng *(word[i]+' '))
    else:
        print(word[i]+((leng-2)*"  ")+' '+word[i])