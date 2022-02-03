def try_it():
	num1 = 67
	num2 = 34
	return num1 % num2

def divide():
	res1 = try_it()
	res2 = addition()
	k = 5
	print("Result =", res1/res2+k)

def addition():
	num1, num2, num3 = 5, 6, 8
	return num1 + num2 + num3

def main():
	divide()

main()