# in python or any other programming language there is concept called if elif else


# lets see what is if

# if you have 40 then you will buy noodles or if you if you have still 20 left then you will also buy a appy fizz

userIn = int(input("How much you have: "))
print(userIn >= 40)

if userIn >= 40:
	print("You can buy noodles")
	userIn -= 40

if userIn >= 20:
	print("You can have an appy fizz also.")
	userIn -= 20

if userIn <20:
	print("You cannot buy anything.")

print('You have', userIn, "bucks left with you.")