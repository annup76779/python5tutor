# I want to find out all the number which are even in the given list of numbers(in string format)

ListA = ["23", "87", "89", "14", "45", "58", "92", "100", "11"]

# ListA[5] = int(ListA[5]) # "58" -> 58
# # i am changing the value at index 5 in the list to "89"
length = len(ListA) # 8
print("\n\nlength of the list is", length, end="\n\n")

for index in range(length):
	ListA[index] = int(ListA[index])
	# print(ListA)
print(ListA)

def is_prime(n):
	if n == 2:
		return True

	elif n % 2 == 0:
		return False
	else:
		flag = True # all the numbers are prime
		for i in range(3, n,2):
			if n % i == 0:
				flag = False
				break # break means forcefully stoping the normal looping of the for loop
		if flag:
			return True
		else:
			return False



def get_output_lst(input_lst): # declared the function
	# odd -> when 1 is the remainder of mod 2 of any number
	# even -> when 0 is the remainder of mod 2 of any number
	length = len(input_lst) # finding the length of the input list
	op_lst = [] # result storing list
	for index in range(length):
		num = input_lst[index] # this will give the value at current index
		check_result = (num % 2) # number mod 2
		print(num, check_result)

		if is_prime(num):
			op_lst.append(2)

		elif check_result == 0: # checking even
			op_lst.append(0) # putting 0[denotion of even in the op_lst at corresponding index]

		elif check_result == 1:
			op_lst.append(1)# putting 1[denotion of odd in the op_lst at corresponding index]
	return op_lst


output_lst = get_output_lst(ListA) # using it
print(output_lst)


# I have teach you next way(which is directly accessing the data from the list in the for loop)