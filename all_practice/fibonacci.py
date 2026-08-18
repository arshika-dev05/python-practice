def fobo(num):
    a=0
    b=1
    for x in range(num):
        print(a ,end=" ")
        a,b=b,a+b
num=int(input("enter no for fibonacci="))
fobo(num)
