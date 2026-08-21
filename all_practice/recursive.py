# reversed by using recursive function
def recur(num):
    copy=num
    for x in num:
       rev=copy[::-1]
    print(rev)
    # recur(num)
num=input("enter word=")
recur(num) 