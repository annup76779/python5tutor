userIn = input("Enter the character: ")

if (userIn >= "a" and userIn <= "z") or (userIn >= "A" and userIn <= "Z"):
	print("Alphabet")

elif userIn in "0123456789":
	print("Numeric")

else:
	print("Nothing")