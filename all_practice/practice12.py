lis=[5,-2,10,-7,0,28]
ass=[]
copy=ass
print(lis)
leng=len(lis)
for x in range(leng):

    for i in range(x+1,leng):
        if lis[x]>lis[i]:
           lis[x],lis[i]=lis[i],lis[x]
              
ass.append(lis)             
print("sorting",ass)
rev=ass[::-1]
print(rev)
