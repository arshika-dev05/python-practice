# ASCII
# ord() chr() change lower to upper
word=input("enter word=")
store=""
for x in word:
    if x>="a" and x<="z":
        change=ord(x)-32
        change_char=chr(change)
        store+=change_char
    elif x>="A" and x<="Z":
        store+=x 

print(store)        



    