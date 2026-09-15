
# defing a constructor


class employee:
    company= "hp"
    def __init__(self, name,salary,age,bond,company):
        self.name= name
        self.salary=salary
        self.age=age
        self.bond=bond
        self.company=company # here company act as an instance, if no instance is given the default value of class variable is taken

    def getSalary(self):
            return self.salary

    def getInfo(self):
            return f"Name is {self.name}. Salary is {self.salary}. Age is {self.age}. Bond is {self.bond} and comany is {self.company}"

e1= employee("Aadi", 50000, 22, 5,"Asus")

print(e1.getSalary())
print(e1.getInfo())
print(e1.company)

print(employee.company)

print(dir(e1)) # Used to intrspect the object