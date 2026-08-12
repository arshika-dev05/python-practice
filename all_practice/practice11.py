# 
start=int(input("enter starting no="))
end=int(input("enter ending no="))
 
store=[]
for x in range(start,end+1):
    is_prime=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            is_prime=False
            break
    if is_prime:            
        store.append(x) 
        
        
 
print(store)
 

    