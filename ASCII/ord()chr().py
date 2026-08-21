password=input("enter password=")
password_decode=""
for encode in password:
    change=ord(encode)-40
    change_char=chr(change)
    password_decode+=change_char
print("decode=",password_decode)
pass_decode=""
for decode in password_decode:
     deco=ord(decode)+40
     change_deco=chr(deco)
     pass_decode+=change_deco
print("decode=",pass_decode)     