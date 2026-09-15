
def is_divisible_by_2(num):
    if num%2:
        return False
    else:
        return True

numbers =[2,8,3,7,11,26,11]

new = list(filter(is_divisible_by_2,numbers))

print(new)