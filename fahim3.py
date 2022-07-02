s, y = "", "y"
while y in "yY" and y != "":
	salary = int(input("Enter the salary: "))
	percent = 0.7*salary
	s = s + str(percent) +" "
	y = input("more? ")
	print(s)
else:
	print(s)


range()