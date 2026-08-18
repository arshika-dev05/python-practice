# armstrong
def arm(num):
    
    total_length_is_power=len(str(num))      
    count=0
    while num>0:
       digit= num%10
       count=count+digit**total_length_is_power
       num=num//10
    return count    
num=int(input("enter num="))
copy=num
result=arm(num) 
if result==copy:
   print("armstrong")
else:

   print("not armstrong")    
    
