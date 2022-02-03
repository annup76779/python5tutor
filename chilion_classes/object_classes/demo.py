# OOPs -> object oriented programming

# what is an object?
# object is any entity which is made by using any predefined set of rules or design or blueprint which are termed as classes

# what is class?
# the part of code where in we define all the rules and regulation to be followed make an and object and what are things we can do
# with that object is classed classes.


# defining a class
class Book:
    book_count = 2
    # going to define the methods
    def __init__(self, title, author): # instance method
        self.title = title # instance variable
        self.author = author  # instance variable

    def show(self):
        print(self.title, self.author)

# making an object of a class
english_book = Book("Merchant of Venice", "Shakespere") # instance
english_book.show() 

math_book = Book("CBSE Maths", "RDSharma")
math_book.show()

# what are these instance variables?
# the term instance means that anything following the blueprint by the class and also unique.
# these instance variables are local to an object of any class


# but class variables are local to any class but public and same for all the objects of that class