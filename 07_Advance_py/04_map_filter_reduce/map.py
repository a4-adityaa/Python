
number=[1,2,6,21,11]

def squre(num):
    return num*num

squares = list(map(squre,number))

print("the list of Squares are: ", squares)