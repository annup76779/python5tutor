class A:
    def __init__(self, name):
        print("A.__init__", name)

class A2:
    def __init__(self, name):
        print("A2.__init__", name)

class B(A2, A):
    def __init__(self):
        print("B.__init__")
        # A.__init__(self, "anurag")
        # A2.__init__(self, "Shurtha")
        super().__init__("Anurag") # works for very single level inheritance 
        # super builtin function gives us the proxy object 
        # of the first parent class used for inheritance

class D:
    pass

D()
print(D.__mro__)


# I want you to write a class 
# which can take a decimal(integer) number when it's object is created
# you have implement following methods for the class-
#   1. to_bin(self) -> return the binary string of the number
#   2. to_hex(self) -> return the hex string of the number
#   3. you have to override the operators methods of the class
#       # a. addition by using __add__(self),
        # b. subtraction by using __sub__(self)
# NOTE: your __add__(self), __sub__(self) should support addition to the number with any decimal(in interger format or string format)
# or hex and binary string addtion.

class K:
    pass

k = K(10)
print(k+10)
print(k+"16")
print(k+"0x8B") # hex
print(k+"0b101") # bin