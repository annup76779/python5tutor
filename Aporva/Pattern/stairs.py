'''
-----
	-----
		-----
			-----
				-----
					-----
				-----
			-----
		-----
	-----
-----
'''

s = "-----"

stair_count = 5
start = 0
staris_status = 0

while True:
	if start< 5 and staris_status == 0:	
		print("\t"*start, end = s+"\n")
		start += 1
	elif start >= 0 and staris_status == 1:
		print("\t"*start, end = s+"\n")
		start -= 1 
		if start == -1:
			break
	if start == stair_count:
		start=3
		staris_status = 1

# start = 5
# while start >=0:
	# print("\t"*start, end = s+"\n")
	# start -= 1 