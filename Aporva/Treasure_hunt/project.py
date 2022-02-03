# we want to make a project which will encrypt our message according to the letter value 
# we give it.

# first requirement
# we have to take the letter values.

# second requirement is the sentence/word whatever.


def take_letter_values(permission:bool = False) -> dict:
	"""
		It will give a dictionary of letters with their replacements

		Parameters:
			permission: if it is False then you get default dict of letter replacements
						else you will be asked for letter replacements

		Returns:
			letter_replacement_dict: dict
	"""
	# default one
	letter_replacement_dict = {
		"A": "D", "B": "E", "C": "F", "D":"G", "E":"H", "F": "I", "G": "J", "H": "K", "I": "L", "J":"M", "K":"N", "L": "O", "M":"P","N":"Q", "O":"R", "P":"S", "Q":"T", "R":"U", "S":"V", "T":"W", "U":"X", "V":"Y", "W":"Z", "X":"A","Y":"B", "Z": "C",
		"a": "d", "b": "e", "c": "f", "d":"g", "e":"h", "f": "i", "g": "j", "h": "k", "i": "l", "j":"m", "k":"n", "l":"o", "m":"p","n":"q", "o":"r", "p":"s", "q":"t", "r":"u", "s":"v", "t":"w", "u":"x", "v":"y", "w":"z", "x":"a","y":"b", "z": "c"
	}
	if permission:
		keys = list(letter_replacement_dict.keys())
		capital_letters = keys[:26]

		letter_shift = int(input("Enter the letter shift: "))
		index = letter_shift
		count = 0

		letter_replacement_dict["A"] = capital_letters[index]
		letter_replacement_dict["a"] = capital_letters[index].lower()
		index += 1
		count += 1
		while index != letter_shift:
			if index == len(capital_letters):
				index = 0

			letter_replacement_dict[capital_letters[count]] = capital_letters[index]
			letter_replacement_dict[capital_letters[count].lower()] = capital_letters[index].lower()
			index += 1
			count += 1

	return letter_replacement_dict


def replacement(text:str, letter_replacement_dict) -> str:
	index = 0
	end = len(text) # getting length of the text
	new_text = ""

	while index < end:
		# running the while to the end of text
		# "anurag"
		new_text += letter_replacement_dict.get(text[index]) if text[index] in letter_replacement_dict else text[index]
		index += 1 # incrementing index to exit the loop after the index become greater than end
	return new_text

def main():

	is_replace = bool(int(input("You want default replacement or have custom letter shift? (1 for yes/0 for no) ")))
	letter_replacement_dict = take_letter_values(is_replace)

	user_text = input("Enter the Treasure_hunt text: ")
	new_encrypted_text = replacement(user_text, letter_replacement_dict)
	print(new_encrypted_text)

if __name__ == '__main__':
	main()
