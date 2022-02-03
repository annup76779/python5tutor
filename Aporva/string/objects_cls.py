class Animal:
    # methods name starting and ending with __ is also called magic methods.

    def __init__(self, color: str, height: float, legs: int = 0, head: int = 1, hand: int =0, eyes: int =0, ears: int=0): # initalize
        self.color = color # self.color is an instance variable
        self.something = "Something"

human = Animal('fair', 5.8) # we are making an instance of Animal class
# human is an object of Animal class 
print(human.color)
print(human.something)

human.name = "Jhon"
print(human.name)

human.job = "Engg."
print(human.job)
