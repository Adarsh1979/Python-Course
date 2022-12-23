class Student:
    id = 100        # Class attribute

adarsh = Student()
# adarsh.id = 200     # Instace attribute
# if we write something like above then that will not change the original class attribute at all
#   instead it will create a instance or local attribute related to that object
adarsh.salary = "10k"       # Instance attributes can be created as well at the time of craeting instance(object)
print(adarsh.id)
Student.id = 2
print(adarsh.id)
print(adarsh.salary)
