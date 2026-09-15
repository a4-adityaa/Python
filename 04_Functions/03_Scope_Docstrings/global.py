
def sum(a,b):
    print("i'm summing two number")
    global z # enforce to use gloabl variable and in return it can overwrite
    z =0
    c= a+b
    return c

z=10
print(sum(5,8))
print(z)