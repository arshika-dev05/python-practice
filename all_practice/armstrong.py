# armstrong
num=int(input("enter num="))
copy=num
total_length_is_power=len(str(num))      
count=0
while num>0:
    digit= num%10
    count=count+digit**total_length_is_power
    num=num//10
print(count)    
if count==copy:
   print("armstrong")
else:

   print("not armstrong")    
    
