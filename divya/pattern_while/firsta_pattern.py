"""
1 2 3 4 5
1 2 3 4
1 2 3 
1 2
1
"""

col = 1 # columns number
row = 1 # row number
_max = 5 # maximum number of columns

while col <= _max: # starts from 1 and go upto 5
	while row <= col: # row data cannot exceed the numeber of columns in that row
		print(row, end=" ")
		row += 1 # incremented row with one
	col += 1 # one is added to col value
	row = 1 # reseting row data value one
	print()

print()
print()
print()

row = 1
_max = 5

while row <= _max:
	print(row)
	row += 1

col = 1
_max = 5

while col <= _max:
	print(col, end = " ")
	col += 1
print()



col = 1
row = 1
_max = 5

# merging the above row and col code
print()
while row <= _max:
	while col <= _max:
		print(col, end = " ")
		col += 1
	row += 1
	col = 1
	print()