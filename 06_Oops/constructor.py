# defing a constructor


class employee:
    def __init__(self, name,salary,age,bond):
        self.name= name
        self.salary=salary
        self.age=age
        self.bond=bond

    def getSalary(self):
            return self.salary

    def getInfo(self):
            return f"Name is {self.name}. Salary is {self.salary}. Age is {self.age}. Bond is {self.bond}"

e1= employee("Aadi", 50000, 22, 5)

print(e1.getSalary())
print(e1.getInfo())