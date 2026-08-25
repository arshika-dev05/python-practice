# kaprikar no
# 297 --> 88209 --> 88+209 =297 
def kaprikar(num):
    if num!=0:
        square=num**2
        print(f"{num}={square}")
        change_str=str(square)
        length=len(change_str)
        if length%2==0:
            # split left and right 
            a=length//2
            left=change_str[:a]
            right=change_str[a:length]
            sum=int(left)+int(right)   
            print(f"{left}+{right}={sum}")       
            return sum
        else:
            a=length//2
            left=change_str[:a]
            right=change_str[a:length]
            sum=int(left)+int(right) 
            print(f"{left}+{right}={sum}")
            return sum    
    else:
        again_no=int(input("enter valid num please="))
        kaprikar(again_no)
         
num=int(input("enter num="))
result=kaprikar(num)
print(result)

if num==result:
    print("yes Kaprikar no")
else:
    print("not Kaprikar no")    
 
    
         
 