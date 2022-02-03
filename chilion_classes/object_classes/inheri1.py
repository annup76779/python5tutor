class Triangle:
    """
    equilateral, isoscles, scalene
    each of them has 3 sides,
    each them have any area
    and sum of any two sides of a trinagle must be greater than the third to make it triangle
    """
    def __init__(self, side1, side2, side3):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)

    @property
    def is_valid(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return sum(sides[:2]) > sides[2]

    @property
    def area(self):
        s = (self.side1 + self.side2 + self.side3)/2

        _area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return _area

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        Triangle.__init__(self, side, side, side) # this line must be the first line the __init__()
        if not self.is_valid:
            raise ValueError("Triangle sides must follow the rule")
        self.side = float(side)
    # override => overwrite

    @property
    def area(self):
        print("Eqt")
        return ((3 ** 0.5) / 4) * self.side ** 2

eqt = EquilateralTriangle(7)
print(eqt.area)