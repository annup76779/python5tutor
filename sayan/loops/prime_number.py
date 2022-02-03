# a numeber completly divisible by 1 or itself

n = 2

if n == 2:
	print("Is is a prime")

elif n % 2 == 0:
	print("Not a prime number.")
else:
	flag = True # all the numbers are prime
	for i in range(3, n,2):
		if n % i == 0:
			print(i)
			flag = False
			break # break means forcefully stoping the normal looping of the for loop
	if flag:
		print("It is a prime")
	else:
		print("Not a prime number")

# fibonacci series
# pattern printing
# working with string and list in for loop