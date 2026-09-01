lis=[5,-2,10,-7,0,28]
copy=lis
 
print(lis)
leng=len(lis)
for x in range(leng):

    for i in range(x+1,leng):
        if lis[x]>lis[i]:
           lis[x],lis[i]=lis[i],lis[x]
              
   
print(copy)           
print("sorting",lis)
rev=lis[::-1]
print("reverse=",rev)
