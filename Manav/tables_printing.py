import random
import secrets


def get_list():
    lst = [[
        secrets.token_urlsafe(random.randint(5, 20)) for i in range(5)
    ] for i in range(200)]

    return lst


def print_table(lst):
    # fist we need to fetch the maximun length of the string for each column
    # column Count is 5
    header = ["column 1", "column 2", "column 3", "column 4", "column 5"]
    col_width_list = []

    # getting the length of each header.
    for i in header:
        col_width_list.append(len(i))

    for item in lst:
        for index, val in enumerate(item):
            col_width_list[index] = max(col_width_list[index], len(val))

    final_length = sum(col_width_list)
    print("+", "-"*(final_length-2 + 14), "+")


    # print headers
    for index, item in enumerate(header):
        print("|", item.center(col_width_list[index]), end=" ")

    print("|")
    print("+", "-"*(final_length-2 + 14), "+")


    for item in lst:
        for index, val in enumerate(item):
            print("|", val.center(col_width_list[index]), end = " ")
        print("|")
    print("+", "-"*(final_length-2 + 14), "+")

lst = get_list()
print_table(lst)

