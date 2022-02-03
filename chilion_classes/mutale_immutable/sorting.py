import random

def get_lst():
    lst = []
    for i in range(10):
        lst.append(random.randint(10, 1000))

    return lst

# # [213, 301, 66, 388, 476, 311, 175, 913, 328, 959]
# def sort(lst):
#     for i in range(len(lst)):

#         for j in range(i+1, (len(lst)):


def main():
    new_lst = get_lst()
    print(new_lst)

    new_lst.sort()

    print(new_lst)


main()