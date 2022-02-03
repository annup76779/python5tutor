class Human:
    parent = "GOD"
    def __init__(self, name: str, height:float , color: str, country: str, age: int):
        # self.variable_name makes an instance variable
        self.name = name
        self.height = height
        self.color = color
        self.country = country
        self.age = age

    def show_human(human1):
        print(human1.name)
        print(human1.height)
        print(human1.color)
        print(human1.country)
        print(human1.age)

human1 = Human(name="Anurag", height=5.76, color="fair", country="India", age=21) # making a object of human class
human2 = Human(name="Apoorva", height=5.4, color="fair", country="India", age=14) # making a object of human class

f = 27

human1.show_human()

print(human2.name)
print(human2.height)
print(human2.color)
print(human2.country)
print(human2.age)


print("Printing the types of instance")

print(type(human1))
print(type(human2))
print(type(Human))
print(type(type))