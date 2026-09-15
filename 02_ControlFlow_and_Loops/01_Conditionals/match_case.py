# match is same as switch case
a = int(input("Enter your number: "))

match a:
    case 2:
        print("You won a pen!")
    case 5:
        print("You won a pencil!")
    case 6:
        print("You won a eraser!")
    case 8:
        print("You won a notebook!")
    case _:
        print("Better luck next time!")