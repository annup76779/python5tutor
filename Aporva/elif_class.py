
def take_username() -> str:
	# it will take username from the user
	username = input("Enter your username as an aplhabetical data: ")
	if username.isalpha():
		print("username saved successfully!")
		return username
	else:
		while True:
			username = input("username should an aplhabetical data: ")
			if username.isalpha():
				break

		return username


def take_password() -> str:
	# it will take password of the user
	password = input("Enter your password as numerical data: ")
	if password.isnumeric():
		print("Account created successfully!")
		return password
	else:
		password = input("password should be a numerical data: ")
		assert password.isnumeric()
		return password


def main():
	# this will take the username and password and use the function(check_username  and check_pass) to verify the username and password and give the output accordingly
	username = take_username()
	password = take_password()

	print("Hello",username)
	print("Your password is", password)

main()
