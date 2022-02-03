"""
51 42 71
my fist number is greater than second number

"""

num = 3
num1 = 3
num2 = 1

if num >= num1:
    # if first numeber is the larger than second number
    if num > num2:
        # if num is larger than the second number as well as the third number
        print("Num 1 is the largest number")
    else:
        # this means that third number is greater than the second and the first number
        print("Third number is the largest number")

elif num1 >= num:
    # if my second number is larger than the first number
    if num1 > num2:
        # if my second number is greater than the first number as well as the last number
        print("Second number is the largest number")
    else:
        # this means my number is the largest number
        print("Third number if the largest number")

else:
    print("Third number is the largest number")


