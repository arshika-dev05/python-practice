# print number 20 to 1 
 
def printnum(num):
    if num!=20:
        while num!=20:
            num=int(input("enter num again="))
    else:
        for x in range(1,num):
            return x
     

num=int(input("enter num="))     
print(printnum(num))
