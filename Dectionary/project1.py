import art
print(art.logo)

def compare_price(information):
     high_price = 0
     winner=""
     for key,value in information.items():
        # price= information[key]
        # if high_price < price:
            #high_price=price
        if high_price < value:
            high_price=value
            winner =key 

     print( f"{winner} ={high_price}")


store_information={ }

continue_loop= True
while continue_loop:
    name = input("what is your name=")
    bid = float(input("what is your bid="))
    store_information[name] = bid
    anyone = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if anyone=="no":
        continue_loop=False
        compare_price(store_information)
    elif anyone =="yes":
        print("*" *40)
        print("\n" * 20)
    else:
        print("Please type only 'yes' or 'no'")
