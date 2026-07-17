# List comprehension
num=[1,2,3,4,5]
square=[x*x for x in num]
print("square=",square)

square=[x*x for x in range(6,11)]
print("square=",square)

num=[1,2,3,4,5,6,7,8,9,10]
even=[x for x in num if x % 2==0]
print("even num=",even)

odd=[x for x in range(10) if x % 2==1]
print("odd num",odd)