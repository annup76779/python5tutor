# what are functions?
# function are the block of code are usually ment to solve a smaller problem in the complete problem set and also they are made to
# reuse any functionality

## facitlities we get by using functions are
#1. code reusalblity
#2. helps us in seperating each process of problem in our code

####
# functions are used in 'Divide and Conqure' way of solving the problem

# when we make any function by ourself, we say then user defined functions

# type of function
# 1. builtin functions
# 2. user defined function -|
						#   |-> lambda function (one line functions)

####
# what is defining a function means?
# when we define a function we are basically writting the set of operations which will be perform in sequence when that 
# function will be called.


def foo():
	print("Hello")
	print("User!")
	print("Happy to see you :-)")

	def bar():
		print("I")
		print("Am")
		print("Happy")

	print("Done making the inner block")
	bar()

print("Done learning function")
foo()

# indentation in python
# user defined function