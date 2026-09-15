# getters
class employee():
    def __init__(self, name, salary):
        self.name=name
        self.salary= salary

    def firstname(self):
        l= self.name.split(" ")
        print(l)
        print(l[0])

e = employee("Aditya kumar", 55000)
print(e.firstname())