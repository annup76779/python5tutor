import random

def question():
	num = random.choice(range(2, 20))
	multiple = random.choice(range(1, 10))
	print("What will be the value of", num ,"*", multiple,":", end = " ")
	output = int(input())

	if output == num * multiple:
		print("WOoho correct ans.")
	else:
		print("Bad luck try again")

question()
# game for you
 
# rule - nothing but don't use calculator
# create -
	# scoreboard
	# the program should keep asking question and it will exit what you enter 'n' for the question (more (y/n)? )