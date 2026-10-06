# handle error not found error 
try:
    file_name=input("enter a text file name=")
    f=open(file_name,"r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("file not found")    