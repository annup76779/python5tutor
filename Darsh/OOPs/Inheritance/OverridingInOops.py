class Person:
    def __init__(self, name, age, fav_food):
        self.name = name
        self.age = age
        self.fav_food = fav_food

    def tell_name(self):
        print("I am a person and my name is", self.name)

    def tell_age(self):
        print("I am a person and my age is", self.age, "and I was born in", 2025 - self.age)

    def tell_fav_food(self):
        print("I am a person and I like to eat", self.fav_food)


## Overriding of methods <- Polymorphism
### In overriding we update the body of a method that already exists in the Parent class but not the definition and signature
### Override concept can only be done within class, and we need inheritance for it

class SportsPerson(Person):
    def tell_name(self):
        print("I am a sports person and my name is", self.name)


class Musician(Person):
    pass


class Doctor(Person):
    pass


def main():
    person = SportsPerson("John", 30, "Pizza")
    person.tell_name()
    person.tell_age()
    person.tell_fav_food()

if __name__ == "__main__":
    main()