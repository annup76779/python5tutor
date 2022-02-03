# OOPs concept is a paradigm of writing code to solve a complex problem in a simpler way

class MyDate:

    def __init__(self, date: str, delimiter: str):
        # self.date, self.month, self.year = [int(x) for x in date.split(delimiter)]
        lst = []

        for x in date.split(delimiter):
            lst.append(int(x))

        self.date, self.month, self.year = lst

    def __str__(self):
        return f"{self.date}-{self.month}-{self.year}"

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    date = MyDate("5/9/2021", "/") # what is making an object? neams you initalized it
    print(date)

# in python there is thing called magic methods (dunder methods)
# it just adds some magic to aur code.

# 5/9/2021 -> / [5, 9, 2021]