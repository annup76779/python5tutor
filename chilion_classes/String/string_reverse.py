# reverse means -> lets say we have "anurag" so by reversing it we will get "garuna"
# palindrome -> it is a type of words in which the reversed word is same as the original word, example -> Nitin -> nitiN

def reverse_str(string:str) -> str:
	"""
	this function will reverse the provided string
	Parameter:
		string:str -> the string to be reversed

	Return new_string: str -> the reversed string
	"""
	new_string = ""

	for item in range(len(string)):
		new_string = string[item] + new_string
	return new_string



reversed_string = reverse_str("Chilion")
print("the reversed string we get is->", reversed_string)

# new_string = str1[0] + new_string # -> new_string == 'C'
# new_string = str1[1] + new_string #-> new_string == 'hC'
# new_string = str1[2] + new_string # -> new_string == "ihC"
# new_string = str1[4] + new_string # -> new_string == "lihC"
# new_string = str1[5] + new_string # -> new_string == "ilihC"
# new_string = str1[6] + new_string # -> new_string == "oilihC"
# new_string = str1[7] + new_string # -> new_string == "noilihC"