# ValueError
i=1
li=[]
while i<5:
    try:
        a=int(input("enter number="))
        add=li.append(a)
        b=a**2
        i+=1
    except ValueError:
        print("enter valid value ")
