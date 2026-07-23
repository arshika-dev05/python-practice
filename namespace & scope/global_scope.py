# Global scope
word="zombi"
print("variable outside the function =",word)

def call():
    def ok():
        word="hero"
        print("variable inside the function =",word)
    ok()

# call function 
call()   
print(word) 


