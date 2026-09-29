# Index_Error
def indexerror(again):
   try:
      user=int(input("enter index="))
      print("index is avaible",li[user])
   except IndexError:
      print("enter a vaild index")

li=[20,34,54,58]
print(li)
print(li[1])
try:
   user=int(input("enter index="))
   print("index is avaible",li[user])
except IndexError:
   print("enter a valid index please you have list index only")
   indexerror(user)
   