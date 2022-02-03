# i want to use both the function I have made namely addition() and multiply()
## i want to use the result of the addition as num1 in the multiply()

def addition():
	print("\n--------------------------------------")
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	return num1 + num2


def multiply():
	print("\n--------------------------------------")
	num1 = addition() # we get the returned value from addition() saved in num1
	num2 = int(input("Enter the number to multiply"))
	print(num1 * num2)

multiply()


# what is hard coding any data
# when you write directly any data into your code
# instead of taking that data from any data source like
# user input or database or file, that way of taking data
# is called hardcoding of the data

## what is the best practice to write code when working with function 
## we have to always try to write function which only perform one functionality of the big program 


##################
# return statement
##################
# it is used in function to give the cooked result of the function back to the caller pointer