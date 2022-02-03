def square(x):
    return x * x

def rectangel(length, width):
    return length * width


def main():
    """  this will be used to take user input and then find the
        area of the complete firgure which has only rectangels and squares
    """

    side_of_square = int(input("Enter the sides of the square"))

    length_of_the_rectangle = int(input("Enter the length of the rectangle"))
    width_of_the_rectangle = int(input("Enter the width of the rectangle"))
    
    complete_figure_area = square(side_of_square) + rectangel(length_of_the_rectangle, width_of_the_rectangle)

    print('The complete firgure area is -', complete_figure_area)


var = 45.4
print(id(var))