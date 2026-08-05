num=int(input("enter positive no="))
rev=0
if num>=0:
    while num!=0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print("Reversed Number is :",rev)
else:
    print("Please enter valid no")        