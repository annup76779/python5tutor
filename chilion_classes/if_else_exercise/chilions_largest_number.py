num = int(input("enter the first number: "))
num1 = int(input("enter the second number: "))
num2 = int(input("enter the third number: "))

if num >= num1:
    if num > num2:
        print("The first number is the largest number")
    else:
        print("Third number is the largest number")
elif num1 >= num:
    if num1 > num2:
        print("The second number is the largest number")
    else:
        print("Third number is the largest number")
else:
    print("third number is the largest number")

# print(num1 > num  and num > num2)


# if my first number is greater than the second number
# but my first number is not greater than the third number