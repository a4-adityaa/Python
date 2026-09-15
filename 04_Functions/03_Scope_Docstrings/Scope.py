
def sum(a,b):
    c= a+b
    d=2 #local variable, can't overwrite global variable
    return c

d = 5 # global variable
print(sum(5,6))