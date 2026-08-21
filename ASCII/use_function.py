def length(password):
    length=len(password)
    div=length//2
    return div

def encode(password):
    encode_password=""
    for encode in password:
        change_ord=ord(encode)+length(password) # call lengh() function
        change_char=chr(change_ord)
        encode_password+=change_char   
    return encode_password    

def decode(encode_result):
    decode_password=""
    for encode in encode_result:
            change_ord=ord(encode)-length(encode_result)
            change_char=chr(change_ord)
            decode_password+=change_char   
    return decode_password    
    
user_password=input("enter your password=")
l=length(user_password)
encode_result=encode(user_password) 
print(encode_result)
decode_result=decode(encode_result)

yes_or_no=input("you want to decode your password if you want then type 'y' otherwise type 'n' =")
if yes_or_no=="y":
    print(decode_result)
else:
    print("ok")
        