# there are two types of scopes in python or we can say this rule is followed for all the languages - C/C++ , Java, Ruby, R, Perl, Pascle, JavaScript, Go, dart etc.

# Global Scope

def dummyfunc():
	var2 = 2 # local variable 
	return var2

def dummyfunc2():
	var3 =  20
	return dummyfunc(), var3

while True:
	var1 = 1
	break

print(var1)
print(dummyfunc2())




# the object which is create without indentation or it is create within any block which in not callable and runs automatically then it is called global object.

# the object which created inside any block(object) that is callable and only runs when it is called to run is called local object or that thing is called local to that callable object.


# function and classes are considered as a sub program