"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""

number_of_rows = int(input("Enter the number of rows: "))

# for loop to print rows
for row_num in range(1, number_of_rows+1):
    # for numeber stars
    for stars_count in range(row_num):
        print("*", end=" ")
        
    print() # here used to come to new line
