# this file is to find the even odd of any number

# Indentation -> space from the left side to match any block

def check_even_odd(x):
	""" This will check the user input is even or odd """
	output = x % 2
	return output

number = int(input("Enter the number you want to check"))

status = check_even_odd(number)

if status == 0:
	print("The number is even.")
else:
	print("Then number is odd.")