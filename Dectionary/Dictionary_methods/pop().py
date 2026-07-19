# The pop()method removes the specified key and returns its value.
student={"name":"Arshika",
         "age":20,
         "roll_no":22}

print(student)
delete=student.pop("roll_no")
print(delete)
print(student)
delete=student.pop("age")
print(delete)
print(student)