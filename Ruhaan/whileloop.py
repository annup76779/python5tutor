# we want to make a code by which can print all the number starting from 1 to the 12 even number

counter = 0
num = 1
end = int(input("Enter the end: "))
while counter < end:
	if num % 2 == 0:
		counter += 1
	print(num)
	num+=1