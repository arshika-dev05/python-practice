# Local scope
def local():
    # local scope 
    # variable inside the function
    word="zombi"
    return word

# call function 
result=local()
print(result)

# give NameError 
# print("variable outside the function =",word)
# name 'word' is not defined. Did you mean: 'ord'?