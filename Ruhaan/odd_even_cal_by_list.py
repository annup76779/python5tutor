# we have to take numbers from the user and the way we will take the numbers are like
# the number that comes at odd index will go to list1 and the other ones will go to list 2

# and at last we have to add all the number

def take_input(size):
	list1, list2 = [], []

	# looping for size times and take the inputs.
	for _ in range(size):
		num1 = int(input("Enter the number for first list: "))
		list1.append(num1)

		num2 = int(input("Enter the number for the second list: "))
		list2.append(num2)

	return list1, list2

print(take_input(5))