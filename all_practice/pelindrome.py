# 
def rev(copy):
    store=0
    if copy>=0:
        while copy!=0:
           digit=copy%10
           store=store*10+digit
           copy=copy//10
    else:
        print("invalid no")        
    return(store)

user=int(input("enter no for palindrome="))
copy=user
reverse=rev(copy) 
if reverse==user:
    print("pelindrome")
else:
    print("not pelindrome")    
