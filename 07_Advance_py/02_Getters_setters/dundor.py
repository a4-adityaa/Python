# dundor mean double under stock

class employee:
    company="HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    def __str__(self):
        return f"name: {self.name} and salary: {self.salary}"

    def __repr__(self):
        return f"name: {self.name} \nsalary: {self.salary}"

    def __len__(self):
        return len(self.name)

e1= employee("aadi",18000)

print(str(e1))
print(repr(e1))
print(len(e1))