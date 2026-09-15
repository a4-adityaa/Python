# Use of try and except

while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print("The didvsion is: ", result)

    except ValueError:
        print("Please don't perform bad typecast!")

    except ZeroDivisionError:
        print("Don't divide by Zero!")

    except Exception as error:
        print("you have an error, try again!", error)