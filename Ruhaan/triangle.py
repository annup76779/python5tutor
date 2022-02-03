def tri1(size):
	"""
	* * * * * *
	* * * * *
	* * * *
	* * *  
	* *
	*
	
	"""
	for row in range(size, 0, -1): # keeping track of the current row.
		for star in range(row): # inner for loop is responsible for printing all the stars in the given row
			print("* ", end="")
		print()
tri1(6)

# 10, 9, 8, 7 , 6, 5, 4 , 3
# if i have to start from 10 and stop at 3 in the range
# to make a range  from larger number to smaller number 
# range(largers_number, smalle_number-1, -1)
# range(10, 2, -2)