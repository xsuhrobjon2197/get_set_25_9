#4-m
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def fullname(self):
        return self.name
    
    @fullname.setter
    def fullname(self, new_name):
        self.name = new_name
        
e1 = Employee("John", 20000)
print(e1.fullname)

res = e1.fullname
print(res)

e1.fullname = "<NAME>"
print(e1.fullname)
