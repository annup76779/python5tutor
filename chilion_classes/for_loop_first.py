# how to write for loops in python
"""
*********
 ******* 
  ***** 
   ***
    *
""" 
# input from user
userIn = int(input("Enter the base size of triangle "))

spaces = userIn // 2

for i in range(spaces+1):
    stars = userIn # setting stars to 1
    num_of_stars_removed = i * 2 # how number of spaces did I lost in this step

    stars = stars - num_of_stars_removed # this will be final number of stars
    print(" " * i, "*" * stars)
