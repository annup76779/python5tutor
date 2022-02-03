from area_functions import square, rectangel


def parimeter_of_squares(side):
    return 4 * side

def parimeter_of_rectangles(length, width):
    return length + width + length + width

def funtion_to_find_parimeter():
    """This will find the parimeter_of_rectangles and sqaures
    """
    
    side_of_square = int(input("Enter the side of the square "))

    length_of_rectangle = int(input("Enter the side of the rectangle "))
    width_of_rectangle = int(input("Enter the width of the rectangle "))

    parimeter_of_square = parimeter_of_squares(side_of_square)

    parimeter_of_rectangle = parimeter_of_rectangles(length_of_rectangle, width_of_rectangle)

    final_parimeter = (parimeter_of_rectangle - side_of_square) + parimeter_of_square

    print(final_parimeter)
    funtion_to_find_area(side_of_square, length_of_rectangle, width_of_rectangle)


def funtion_to_find_area(side, length, width):
    print("Area of square :", square(side))

    print("Area of rectangle :", rectangel(length, width))


if __name__ == "__main__":
    funtion_to_find_parimeter()