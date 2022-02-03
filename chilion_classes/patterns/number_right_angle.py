"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
# trying to print this pattern using for loop

row = 5 # we will print row from 1 to 5
col = 1 # setting the starting of the columns
_max = 0
# i = 1, 2, 3, 4, 5
for i in range(row, _max - 1, -1):
    for j in range(col, i + 1):
        print(j, end=" ")
    print()

# trying to make this using while loops
# the number of data in each row depends upon in which row we are
# Eg. for 3rd row there are 3 data


col = 1 # for first time columns is 1
row = 1 # as we will start printing from first row
_max = 5

while row <= _max: # this means rows can be less that _max or equal to _max
    while col <= row: # number of columns in each row can be less than or equal to row count
        print(col, end = " ")
        col += 1 # incrementing the column count 

    row += 1 # incremnting the row count
    col = 1 # reseting column count back to 1
    print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""



