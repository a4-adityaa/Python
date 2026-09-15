# implementing inheritance

class Animal:
    region = "Australia"

    def __init__(self, name):
        self.name= name

    def sound(self):
        return "generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        s=super().sound()
        return s,"Meowww"

    
# a1 = Animal("Bruno")
# print(a1.sound())

d1 = Dog("Bruno")
print(d1.sound())

c1 =Cat("mily")
print(c1.sound())


print(d1.name)
print(c1.name)

print(c1.sound)