
class ParentClass:
    def __init__(self):
        self.attribute1 = 10
        self.attribute2 = "Darsh"


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.child_attribute = 50
        self.child_attribute2 = "Mountains"


class ChildClass2(ParentClass):
    def __init__(self):
        super().__init__()
        self.child_attribute = 100
        self.child_attribute2 = "Water"


class ChildClass3(ParentClass):
    def __init__(self):
        super().__init__()
        self.child_attribute = 1
        self.child_attribute2 = "Food"


obj = ChildClass()
print(obj.child_attribute)
print(obj.child_attribute2)
print(obj.attribute1)
print(obj.attribute2)


obj = ChildClass2()
print(obj.child_attribute)
print(obj.child_attribute2)
print(obj.attribute1)
print(obj.attribute2)


obj = ChildClass3()
print(obj.child_attribute)
print(obj.child_attribute2)
print(obj.attribute1)
print(obj.attribute2)