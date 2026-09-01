# 
def height_cm(feet,inches):
    total_inches=(feet*12)+inches
    height=total_inches*2.54
    return height


feet=int(input("enter feet="))
inches=int(input("enter inches="))
result=height_cm(feet,inches) 
print(f"height:{round(result,2)}cm") #rounded () 2 decimal places