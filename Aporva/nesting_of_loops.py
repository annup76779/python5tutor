# when to use nesting?

from time import sleep
# when we have to loop over any inner data (lets say a list has lists inside it)

matrix = [ 
	[1,2,3], 
	[4,5,6], 
	[8,9,11] ]

# inside a list of lists we want to findout how many number are even
# row = []
for row in matrix:
	for item in row:
		if item % 2 == 0:
			print(item , "->", "is a even number")
	print(row)
	sleep(10)