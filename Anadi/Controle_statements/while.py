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

# stars = 1
# row = int(input("Enter the number of row: "))
# row_count = 0

# while row_count < row:
#     i = 0
#     while i < row_count:
#         print(end = "**")
#         i+=1
#     print("*")
#     row_count += 1


# print the following pattern
'''

you have to take the number of row always from the user
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


$$$$$
$000$
$000$
$000$
$$$$$


    $$$$$
   $$$$$
  $$$$$
 $$$$$
$$$$$


    $$$$$$$$$$$
   $$$$$   $$$$$
  $$$$$     $$$$$
 $$$$$       $$$$$
$$$$$         $$$$$
       $$$$$
       $000$
       $000$
       $000$
       $$$$$

'''

'''
you have to take the number of row always from the user
              *
            ***
          *****
        *******
      *********
    ***********
  *************
***************
'''

user_in = int(input("Enter the number of rows: ")) # 7
row = user_in
star_counter = 1
while user_in > 0:
  print(" "* (((row*2)-1)-star_counter), end="")
  print("*"*star_counter)
  star_counter += 2
  user_in -=1 # terminating opertation


# row = 7
# characters_in_row = (row * 2) - 1

# and if no. of start in 3rd row are 5 
# then tell me how many dashes must be there in row 3
# """
# ------------*
# ----------***
# --------*****
# """