# he wants you make her a program which will take input and then tells her is it an prime number or not

def prime_funtion(number): # this portion is funtion definition (means what this function will do.)
	status = True
	for i in range(2, int(number ** (1/2))):
		if (number % i) == 0:
			status = False
			break

	if status:
		print(number, "is a prime number.")
	else:
		print(number, "is not a prime number")


def add(num1, num2): #
	return num1 + num2

print("\n The value of __name__ in prime_function.py is ->", __name__)


import sys

if __name__ == '__main__':
	n,k = list(map(int, sys.stdin.readline().strip().split()))
	task = list(map(int, sys.stdin.readline().strip().split()))[:n]
	task.sort()
	summ = 0
	i = 0
	while summ <= k:
		summ+=task[i]
		i+=1

	sys.__stdout__.write(str(i-1))