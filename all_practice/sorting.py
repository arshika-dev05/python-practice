# sorting list but without using In built function
l=[78,-31,105,0,2,73,101,-2,44,39]
length=len(l)
for x in range(length):
    for i in range(1,length):
        if l[x]>l[i]: 
            l[x],l[i]=l[i],l[x]

print(l)