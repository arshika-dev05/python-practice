from art import logo
from data import data_list
import random
LEVEL=10
randam_no=random.choice(data_list) 
print(randam_no)
print(logo)

guess="" 
blank="_" *len(randam_no)
print(blank)
change=list(blank)
change_again=str(change)
if randam_no!=guess:
    while LEVEL>0:
        if LEVEL!=0:
            print(f"you have  {LEVEL} chance ") 
            guess=input("enter letter=").lower()
            for x in range(len(randam_no)):
                if randam_no[x]==guess:
                    change[x]=guess
        
                else:
                    change[x]="_" 
                    print(change)
                LEVEL-=1  
            print(change)     
        else:
            print("you lose this game")  

elif randam_no==guess:
    print("you winner")
                         
print(change)  
print("\n"*4) 
      