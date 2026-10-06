# KeyError
dict_list={101:"Arshika",
           102:"priya",
           103:"rekha",
           }

# insert elemet
def insert(dict_list):
    user_name=input("enter name=")
    user_roll=int(input("enter roll no="))
    # dict_list[user_roll]=user_name
    dict_list.update({user_roll:user_name})
    ask=input("you want to add key yes or no")
    if ask=="yes":
       insert()
    else:
       print("ok")   
    print("successfully update your name=",dict_list) 

# search your name and key by the help of key 
def search(dict_list):
    try:
        user_key=int(input("enter roll="))
        print("your name is Available",dict_list[user_key])

    except KeyError:
        print("enter a valid roll no(key) please")


# delete element
def delete(dict_list):
    delete=int(input("enter roll for delete name="))
    dict_list.pop(delete)
    print(dict_list)


# user wnat to insert key(rollno or name) or want to search name
user_ask=input("what you want' insert','search' ,'delete'=")
if user_ask=='delete':
    delete(dict_list)
elif user_ask=='insert':
    insert(dict_list)
elif user_ask=='search':
    search(dict_list)    