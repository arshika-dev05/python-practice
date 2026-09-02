# f=open("ab.txt","w")
# write=input("enter text=")
# f.write(write)
# f.close

f=open("ab.txt","r")
write=f.read()
i=1
# count=0
for x in f:
    if 'w' in x:
        count=x.count('w')
        # count+=1
        print(f"line no{i} = no of time={count}")
    i+=1
f.close()    