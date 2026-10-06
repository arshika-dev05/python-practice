# private, public, protected 
class ppp:
    def __init__(self,name,roll,phone,salary):
        self.n=name
        self._r=roll
        self.__p=phone
        self.__s=salary
        print("name=",self.n)
        print("roll=",self._r)
        print("phone=",self.__p)

    def salary(self,salary):
        print(salary)  
           

name=input("enter name=")
roll=int(input("enter roll no="))
phone=int(input("enter phone no="))
salary=int(input("enter salary="))
print("\n"*4)
b=ppp(name,roll,phone,salary)       
b.salary(450)