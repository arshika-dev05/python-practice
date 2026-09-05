# 
enter=int(input("enter num="))
for x in range(enter):
        print("1"*x)

for x in range(1,enter):
    for i in range(1,x+1):    
        print(i,end=" ")
    print()

        