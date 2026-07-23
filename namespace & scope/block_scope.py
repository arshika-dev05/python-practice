# Block scope 
num=18
if 15 < 18:
    num=15
print(num)
sum=num+15
print(sum)


for x in range(2):
    sum=2+4
    print(sum)
print(sum)


def block_scope():
    num1=12
    num2=13
    return num1+num2

result=block_scope()
print("sum =",result)
# print(num1)
# print(num2)




 
