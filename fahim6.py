a = """
     *
    ***
   *****
  *******
 *********
 *********
  *******
   *****
    ***
     *

"""
# for normal the number will be 0 and for inverse the number will be 1
def triangle(n):
	if n == 0:
		space = 4
		star = 1
		# stoping when stars are equal to 9
		# for i in range(star, 10, 2):
		# 	print(" "*space,"*"*i)
		# 	space = space -1
		# stoping when spaces are equal to 0
		for i in range(space,-1, -1):
			print(" "*i,"*"*star)
			star = star + 2
	elif n == 1:
		space = 0
		star = 9
		# stopping when space  = 5
		# for i in range(space, 5,1):
		# 	print(" "*i,"*"*star)
		# 	star = star -2

		#stoping when stars are equal to  0
		for i in range(star,0,-2):
			print(" "*space,"*"*i)
			space = space + 1
			



while True:
	triangle_type = input("enter the type of triangle - 0 for normal and 1 for invers (nothing to stop printing): ")
	if triangle_type == "0" or triangle_type == "1":
		triangle(int(triangle_type))
	else:
		break