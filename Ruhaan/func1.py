def add(num1, num2, mnum):
	addition = num1 + num2
	res = addition * mnum
	return res


num1 = int(input("Enter the first num: "))
num2 = int(input('Enter the second num: '))
mnum = int(input("Enter the multiplier: "))

result = add(num1, num2, mnum)
print("The result is", result)