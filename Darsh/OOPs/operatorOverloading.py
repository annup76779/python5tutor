class MyIntegerNumber:
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.value = value

    def __add__(self, other):
        if not isinstance(other, MyIntegerNumber):
            raise TypeError("Both objects must be of type MyIntegerNumber")
        return MyIntegerNumber(self.value + other.value)

    def __sub__(self, other):
        return MyIntegerNumber(self.value - other.value)

    def __str__(self):
        return f"MyIntegerNumber({self.value})"

n1 = MyIntegerNumber(10)
n2 = MyIntegerNumber(20)

print(n1 - n2)
