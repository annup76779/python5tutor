"""
	this game will ask you a question in which it will give you two things first the number and the multiple
	what will be 4 * 3 = 12 : 

required : 
	your game will exit only if you enter  N or n for the question (more (y/n)? )
	are result of the should hold the number of correct answer and wronge answers
"""

from random import choice

score = 0
wronge = 0
correct = 0

def random_question_generator() -> tuple:
	"""
		This funtion will generate a random question for the player
	"""

	# this will choose a number between 2 - 100
	random_number = choice(range(2, 101))

	random_multiple = choice(range(1, 11))

	return random_number, random_multiple

def main() -> bool:
	"""
		this main() will handle every aspect of the game.
	"""
	global score
	global wronge
	global correct

	# this will take "number" and its "muliple" from the random_question_genreator() -> this will be random things
	number, multiple = random_question_generator()

	print("What will be", number, "*", multiple,":", end=" ")
	answer = input()

	if answer.isnumeric():
		answer = int(answer)
		if number * multiple == answer:
			# if the answer is correct then you will be awarded with two points
			score += 2
			correct += 1
		else:
			# else 1 point will be deducted
			score -= 1
			wronge += 1

		play_more = input("more(y/n)? ")
		if play_more == "n" or play_more == "N":
			return False
		else:
			return True
	else:
		print("That was a bad datatype for the answer, answer should consist of digits.")
		return False

if __name__ == '__main__':
	while True:
		if not main():
			print("\n\nScore:", score)
			print("Correct:", correct)
			print("Wronge:",wronge)
			break