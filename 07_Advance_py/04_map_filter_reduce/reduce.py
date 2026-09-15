
from functools import reduce

number=[5,2,1,7,6,11]

def sum(num1, num2):
    return num1+num2

new = reduce(sum,number)

print(new)