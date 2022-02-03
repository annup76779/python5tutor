s = "My name is         anurag pandey"

def main():
	word = ""
	for char in s:
		if char != " ":
			word += char
		else:
			if word != "":
				print(word[0])
			word = ""
	if word != "":
		print(word[0])
main()