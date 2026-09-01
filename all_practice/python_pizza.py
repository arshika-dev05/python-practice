print("Welcome to Python Pizza Deliveries!")

sum1=0
size = input("What size pizza do you want? S, M or L:🍕 ")
if size == "s":
    sum1=+15
    print(sum1)
    yes=input("Add pepperoni for small pizza (Y or N):")
    if yes=="y":
        sum1+=2
        print(sum1)
elif size =="m":
    sum1+=20
    print(sum1)

elif size =="l":
    sum1+=25
    print(sum1)

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="y":
    sum1+=5
    print(sum1)


extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="y":
    sum1+=3
    print(sum1)
print(f"you pay💸(●'◡'●)👉{sum1}")
