# we want to check the user password and say if the user has some 


def check(password: str) -> tuple:

	up = low = sym = num = 0
	for char in password:
		print(char.isalnum())
		if char.isnumeric():
			num += 1
		elif char.isalpha() or char.isspace():
			if char.isupper():
				up += 1
			elif char.islower() or char.isspace():
				low+=1
		else:
			sym+=1

	return up, low, sym, num, len(password)


def show_status(status: tuple)-> str:

	up, low, sym, num, length = status
	print(status)

	# checking for very strong password
	if up >= 3 and low >= 3 and num >= 5 and sym >= 4 and length >= 18:
		msg= "Very strong password"

	# checking for strong password
	elif up >= 2 and low>= 2 and num >=3 and sym >= 3 and length >= 12:
		msg = "Strong Password"

	# checking for Normal Password
	elif up >= 1 and low >= 1 and num >= 2 and sym >= 2 and length >= 8:
		msg = "Normal Password"

	# checking for weak password
	elif up >= 0 and low >= 1 and num >= 2 and sym >= 1 and length >= 5:
		msg="Weak Password"
	else: 
		msg= "Hillarious password"

	return msg


def main():
	password = input("Enter the password: ").strip()

	status = check(password)
	msg = show_status(status)
	print(msg)

if __name__ == '__main__':
	main()