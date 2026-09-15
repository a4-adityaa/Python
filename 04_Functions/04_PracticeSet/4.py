# calculate area

def calculate_area(length, width=10):
    area = length* width
    return area

length= int(input("enter the length: "))
# width = int(input("enter the width: "))

# print("Area of reactagle: ", calculate_area(length,width))

print("Area of rectangle: ", calculate_area(length))