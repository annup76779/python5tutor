# for loops on stings
# in operator- 
#	if just checks the membership of anything in anything.

strings = "jsdhfks3432jsdkjfkj234jjlsdjf23j4  sjdfk23 "
new_str = ""

for member in strings:
	if member == "-":
		new_str = new_str + " "

	elif member != " ":
		new_str = new_str + member

print(new_str)