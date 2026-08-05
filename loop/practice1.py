# question1
st=int(input("enter start no="))
end=int(input("enter end no="))
sum=0
for x in range(st,end+1):
    if x%3==0:
        print(x,end="")
        print()
        sum+=x
print(sum)        