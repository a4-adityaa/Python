# throw an intensional error

num1= int(input("enter a number: "))
num2= int(input("enter other number: "))

if num2==0:
    raise ZeroDivisionError("please don't divide by 0")
result= num1/num2
print("the answer is: ", result)