# factorial

# find the factorial of 5 -> 5! = 120
# 5! = 5 * 4 * 3 * 3 * 2 * 1

# fact_num = int(input("Enter the number whoes factorial you want to know: "))

# reccurssion
# recalling any function inside a function 
# recurring call of the function


def factorial(k):
	# 5! = 5 * 4 * 3 * 2 * 1
	# 5! = (5) * (5-1) * ((5-1)-1) * (((5-1)-1) -1) * ((((5-1)-1) -1)-1) * ... 
	# 5! = 5 * 4 * 3 * 2 * 1
	if k == 1:
		return k
	return k * factorial(k - 1)

print(factorial(5))