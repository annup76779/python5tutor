# why do we use Object oriented programming
# 1. to make code look good and clean
# 2. to relate our coding much closer to the real live practice.

class machine:

    def __init__(self, name_of_machine, creator_name) -> None:
        self.name = name_of_machine
        self.creator = creator_name


    def show(self) -> None:
        print("Name of machine is", self.name)
        print("Creator is", self.creator)


obj1 = machine("Laptop", "Dell")
obj1.show()