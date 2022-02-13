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
	if num == 2:  # 2 is the only even which is prime
		return True
	if num % 2 == 0: # any even other than 2 can never be a prime number
		return False

	# so by the above theory we came to know that all the prime numbers other than 2
	# are odd number and only divible by an odd number. 

	# FACT: no number can be complete divisible by any number greater than it's half else by itself.
	edge = round(num/2)
	for n in range(3, edge+1, 2):# 3, 5, 7, 9,..
		if num % n==0:
			return False
	return True
	

prime_100_lst = []

counter_num = 2
while len(prime_100_lst) <100000:
	if is_prime(counter_num) == True:
		prime_100_lst.append(counter_num)
	counter_num += 1

print(len(prime_100_lst))
print(prime_100_lst)