# WAP a program to check input no is a perfect no or not.
num=int(input("enter number="))
store=[]
total=0
for x in range(1,num):
    if num%x==0:
        store.append(x)
print(store) 
for i in store:
    total+=i 
       
if total==num:
    print("perfect" ,total)
else:
    print("not perfect",total)    