# Simulates a simple calculator using match calculator
a= int(input("enter your first number: "))
b= int(input("enter your first number: "))

operation=int(input("Enter the operation as Addition as 1, Subtracton as 2, multipliaction as 3 and division as 4: "))

match operation:
    case 1:
        print(f"Addition of {a} and {b} is: ",a+b)
    case 2:
        print(f"Subtraction of {a} and {b} is: ",a-b)
    case 3:
        print(f"Multiplication of {a} and {b} is: ",a*b)
    case 4:
        print(f"Division of {a} and {b} is: ",a/b)