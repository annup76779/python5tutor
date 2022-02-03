# continue

def main():
	userIn = input("Enter all the number in a same line seperated with space: \n").split()
	for i in userIn:
		if int(i) % 2 == 0:
			continue
		print(i)
		print(int(i)**2)
	else:
		print("check")


class Human:
	def __init__(self, name, dob):
		self.name = name 
		self.dob = dob

print("A new baby took birth.")
apoorva = Human("Apoorva", "1/1/2007")

print("what is you name?", apoorva.name)