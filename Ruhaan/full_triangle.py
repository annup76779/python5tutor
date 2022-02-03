"""
     *
    ***
   *****
  *******
 *********
***********
"""

def full_triangle(size):
	star = 1 # the inital count of star
	for space in range(size, -1, -1):
		print(" "*space,end="")
		print("*"*star)
		star += 2

full_triangle(5)

def upside_down_full_triangle(size):
	star = (5*2)-1 # the inital count of star
	for space in range(1, size+1):
		print(" "*space,end="")
		print("*"*star)
		star -= 2

upside_down_full_triangle(5)