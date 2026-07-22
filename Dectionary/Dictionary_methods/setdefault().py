# setdefault()

student={"name":"Arshika",
         }
student.setdefault("age",20)
print(student)
student.setdefault("name","Riya")
print(student)
student.setdefault("course","AI")
print(student)
student.setdefault("name","Rohan")
print(student)
student.update({"name":"Rohan"})
print(student)