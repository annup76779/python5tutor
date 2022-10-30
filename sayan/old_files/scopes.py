# lets say we have 2 variables arrange in following way

name = "Anurag" # <- global name

def foo(): # <- global name
	# global name
	name = "Sayan" # <- local variable

def bar():
	foo()
	if something:
		name = "lksdjfks"

foo()
print(name)

if something:
	name = "lksdjfks"

# when you initailize any name without any kind of indentation in it the program then that name is said to be initialized in
# global scope

# AND
# when we make any name inside any 'class' or 'function' are called local to that 'class or function.'


# what is scope?
# it is basically used when we are talking about any type of name (variable name, function, etc.), where does that name belong 
# and where can we access that name.

# categories of scope: -
# 1. gloable - names which can be accessed anywhere in the program
# 2. local - names which are only accessable in some portion(like function) in the program.


