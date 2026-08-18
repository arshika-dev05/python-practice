# find string lenght without using bult in function
user=input("enter word to check lenght of word=")
count=0
for x in user:
    if x in user:
        count+=1
    # elif     
print("len=",count)        