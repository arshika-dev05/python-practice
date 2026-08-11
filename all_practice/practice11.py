# 
# start=int(input("enter starting no="))
num=int(input("enter ending no="))
count=0
store=[]
# display all prime no 
if num==1:
    print("prime no")
else:
    for x in range(2,num): 
        if num%x==0:
            count+=1   
            print(x)
print("count prime",count)            