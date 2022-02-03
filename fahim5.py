def factorial(number):
	a = number
	for i in range(number-1,0,-1):
		a = a * i
	return a

def takeinput():
	num1 = int(input("enter the first number: ")) # find the factorial of num1
	num2 = int(input("enter the second number: "))# find the factorial of num2
	operation = input("enter the operation: ")
	# do the operation defined on the factorials of the numbers num1 and num2
	if operation == "+":
		fact1 = factorial(num1)
		fact2 = factorial(num2)
		sum = fact1 + fact2
		print(sum)
	elif operation  == "-":
		fact1 = factorial(num1)
		fact2 = factorial(num2)
		sub = fact1 -fact2
		print(sub)
	elif operation == "*":
		fact1 = factorial(num1)
		fact2 = factorial(num2)
		multiple = fact1* fact2
		print(multiple)
	elif operation == "/":
		fact1 = factorial(num1)
		fact2 = factorial(num2)
		division = fact1/fact2
		print(division)

takeinput()
