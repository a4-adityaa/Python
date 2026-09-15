# use of static and class method

class employee:
    company="HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    # instance method
    def getInfo(self):
        info =f"Name is {self.name} and salary is {self.salary}"
        return info

    @staticmethod # staic method is used to pass arguement without passing self
    def sum(a,b):
        return a+b

    # class method
    @classmethod
    def printComapny(cls):
        print(cls.company())

    @classmethod
    def changeCompany(cls,new_company):
        cls.company=new_company

e1= employee("aadi",50000)
e2 = employee("john",44500)

print(e1.getInfo())
print(e2.getInfo())

print(e2.sum(5,6))

print(employee.company)
print(employee.changeCompany("Acer"))
print(employee.company)