#  what are function in python?
# function are nothing but a part of code that you wanted to use again and again in your code so you just wrapped it up 
# kept it at one place and now yor are using the same wrapped code again and again.

# and also function can act themself as seperate program and so these function can be used in the same program as well as
# in some other program.

# def foo():
# 	print("Bar")

# foo()

# you have 3 numbers num1, num2, num3 respectively, now what you need to do is (num1 + num2) * num3

def area_of_circle():
	radius = float(input("Enter the radius: "))
	PI = 22/7
	area = PI * (radius * radius)
	print("The area of the circle with radius",radius, "is", area, "unit sq.")

area_of_circle()