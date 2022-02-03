starting_number = 1
ending_number = 10

# the value which we set to our variable are of two types
# first Type:
	# hard coded value
	# dynamic value
	# ##################
	# dynamic values can we further classified in two parts-
		# 1. we take input from the user
		# 2. our program creates that value by itself.

# setting conditions part
while starting_number <= ending_number:

	# performance zone
	print(starting_number)

	# part of code which is used to make the condition of while False
	if starting_number % 2==0:
		starting_number+=2
	else:
		starting_number+=1