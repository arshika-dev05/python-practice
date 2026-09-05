for x in range(10):
    print("arsh")

for i in range(5+1):
    print(i,"arshika") 

x="9th"      
list_my=["first","second","third","fourth","5th","6th","7th","8th",x]
print(list_my)
num=int(input("enter num="))
for x in range(num+1):
    print(list_my[x])
    for i in range(x):
        print(i,end=", ")
    print()    