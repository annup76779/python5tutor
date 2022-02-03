# prime number is a property of a numeber - which means a number which is divisible by only 1 or itself
# 2 is the only even prime number


# i want to save first 100 prime numbers into a list.

# first write the code to print first 100 prime number
# now modify your code to put all the numbers into the list.

def is_prime(num):
	"""
		this function is ment to check if any number is a prime number or not
		Return : True or False (bool)
	"""
	if num == 2: 
		return True

	if num % 2 == 0:
		return False

	edge = round(num/2)
