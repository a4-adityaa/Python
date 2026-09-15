# Decoartor is a function that takes a function, creates a new function and then return a new function;

def NewFction(func):
    def wrapper():
        print("I'm about to execute an function....")
        func()
        print("I executed a function....")
    return wrapper

@NewFction
def oldFction():
    print("i'm the function")

# a = NewFction(oldFction)
# a()
oldFction()