user=int(input("enter no of row="))
i=0
while i<user:
    if i%2==0:
        print("@ " * i)
    else:
        print("# "* i)

    i+=1