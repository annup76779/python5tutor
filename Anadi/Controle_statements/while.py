# print n number of start in the smae line, where n will be entere by the user.

# n = int(input("Enter the number of start in a single row: "))
# m = int(input("Enter the number of row: "))  # 7

# row_count = 0

# while row_count < m:
#     no_of_stars_printed = 0

#     while no_of_stars_printed < n:
#         print("*", end=" ")
#         no_of_stars_printed += 1

#     print()
#     row_count += 1

# for _ in range(m):
#     for __ in range(n):
#         print("*", end= " ")
#     print()



# print the following pattern
'''
              *
            ***
          *****
        *******
      *********
    ***********
  *************
***************
*
***
*****
******* 
*********
***********
*************
***************
'''
# stars = 1
row = int(input("Enter the number of row: "))
row_count = 0

while row_count < row:
    i = 0
    while i < row_count:
        print(end = "**")
        i+=1
    print("*")
    row_count += 1