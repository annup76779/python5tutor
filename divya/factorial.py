# 5! = 5 * 4 * 3 * 2 * 1
# 5 * 4 = 20
# 20 * 3 = 60
# 60 * 2 = 120
# 120 * 1 = 120

# this is taking input from the user
userIn = int(input("Enter the number to find the factorial: "))

# this variable will hold the output of the calculation
factorial = userIn
one_less_number = factorial - 1

# here in while loop
# the condition for while loop is userIn should be greater than 1
while userIn > 1:
	print(f"{factorial} * {one_less_number}", end = " = ")
	factorial = factorial * one_less_number
	print(f"{factorial}")
	userIn -= 1 # 1
	one_less_number = userIn - 1 # 0

# Brute force algorithim
# greedy 

print(factorial)