# defing a class and objects

class employee:
    company ="HP"

    def get_salary(self): # self is important here because self is used to refrence the object if calss is being created
        return 3000

e1 = employee()
print(e1.get_salary())

e2 = employee()
print(e2.get_salary())
print(e2.company)