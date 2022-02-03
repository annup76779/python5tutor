# # what are decorators in python
# # these are a bit advance function which does nothing but to add some extra feature to the function given to them.



# class MyClass:
#     def __init__(self, name, date):
#         self.__name = name
#         self.__date = date

#     def __str__(self):
#         return f"{self.__name} has {self.__date}"

#     @property
#     def username(self):
#         return self.__name


    
# obj = MyClass(name="Anurag", date = "2021-10-27")
# print(obj)

# # obj.name = "Chilion"
# obj.__date = "2021-10-28"
# print(obj.username)


# Python program to demonstrate
# use of a class method and static method.
# from datetime import date

# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	# a class method to create a
# 	# Person object by birth year.
# 	@classmethod
# 	def fromBirthYear(cls, name, year):
# 		return cls(name, date.today().year - year)

# 	# a static method to check if a
# 	# Person is adult or not.
# 	@staticmethod
# 	def isAdult(age):
# 		return age > 18

# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 2011)

# print(person1.age)
# print(person2.age)

# # print the result
# print(Person.isAdult(person2.age))


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def set_length(self, length):
        self.__length = length

    @width.setter
    def set_width(self, width):
        self.__width = width

    @property
    def area(self):
        return self.__width * self.__length

    @property
    def perimeter(self):
        return 2 * (self.__width + self.__length)

    @classmethod
    def from_string(cls, d):
        data = [float(x) for x in d.split("x")[: 2]]
        return cls(length=data[0], width=data[1])

    @staticmethod
    def do_something():
        print("I am doing something.")


rect = Rectangle.from_string("45x89")
Rectangle.do_something()
print(rect.area)
print(rect.perimeter)