import pyperclip as ppc # this is the pyperclip program.
import re
import sys

def spn(s):
	"""
	This take supply line text and return the index of the supply lines list.
	params: s: This the pattern matched while finding the supply lines
	Returns: index: index of that supply line repective the provided list of the supply lines.
	"""
	index = s.split("-")[0][-1]
	return int(index)

def nou(s):
	"""
	This takes number of units of with # and return only the units.
	params: s: the number of unit with #
	Returns: unit: the clean unit in integer datatype
	"""
	unit = re.search("[0-9]+",str(s))[0]
	return int(unit)

def main():
	try:
		bundle = ppc.paste() #saving the data bundle using pyperclip
		k = re.findall("[H][0-9]-[0-9]+",bundle) # using regex to fetch supply lines
		l = re.findall("[#][0-9]+", bundle) # using regex to fetch the number of units
		data = [[spn(x),nou(y)] for x,y in zip(k,l)] # arranging every data
		lines = ["Tango","Sierra","Victor","Foxtrot","Xray","Hotel","Delta","Romeo","India","Echo"] # List of all the provided supply lines as per the docx.
		#printing all the supply lines and their number of units ordered.
		printSupplyLines(data, lines)
	except:
		sys.exit()# exiting if any error raises.


def printSupplyLines(data, lines):
	"""
	This takes data and the provided supply lines and prints the supply lines and their ordered number of units.
	"""
	sums = {
	"Tango":0, "Sierra":0, "Victor":0, "Foxtrot":0, "Xray":0, "Hotel":0, "Delta":0, "Romeo":0, "India":0, "Echo":0
	}
	
	print(data)
	for i in data:
		k, l = i
		sums[lines[k]] += l # calculating sum number of units for all the supply lines.

	for _, j in enumerate(sums.items()):
		k, l = j
		print(f"Supply Line {k} ---> {l}")

if __name__ == '__main__':
	main()
# copied to use this text as input for the program.

"""
H9-4234 #12 H8-2432 #89 H8-42323 #23
H7-2423 #44 H5-423 #849 H6-948 #45 H7-3243 #89 H5-897 #78 
H5-433 #78 H7-2343 #2343 H4-2434 #223 H3-2434 #283 H4-2434 #25 H3-2434 #223 H2-2434 #823 H1-2434 #23 H2-2434 #223 H1-2434 #223
H0-2434 #4223 H9-2434 #223
H9-4234 #12 H8-2432 #89 H8-42323 #23
H7-2423 #44 H5-423 #849 H6-948 #45 H7-3243 #89 H5-897 #78 
H5-433 #78 H7-2343 #2343 H4-2434 #223 H3-2434 #283 H4-2434 #25 H3-2434 #223 H2-2434 #823 H1-2434 #23 H2-2434 #223 H1-2434 #223
H0-2434 #4223 H9-2434 #223H9-4234 #12 H8-2432 #89 H8-42323 #23
H7-2423 #44 H5-423 #849 H6-948 #45 H7-3243 #89 H5-897 #78 
H5-433 #78 H7-2343 #2343 H4-2434 #223 H3-2434 #283 H4-2434 #25 H3-2434 #223 H2-2434 #823 H1-2434 #23 H2-2434 #223 H1-2434 #223
H0-2434 #4223 H9-2434 #223
"""
