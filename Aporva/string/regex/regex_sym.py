import re
import demo

def pattern_search(exp, _str):
    return re.findall(exp, _str)


def main():
    userIn = input("Enter any string: ")
    # exp = re.compile(r"he*")
    exp = re.compile(r"he.")

    search_obj = pattern_search(exp, userIn)

    print(search_obj)

if __name__ == '__main__':
    main()
    print(demo.__name__)