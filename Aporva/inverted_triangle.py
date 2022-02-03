'''
____
	____
		____
			____
				____
'''

stair = "____"

for step in range(0, 5):
	print("\t" * step, end=stair+"\n")

for step in range(3, -1, -1):
	print("\t" * step, end=stair+"\n")