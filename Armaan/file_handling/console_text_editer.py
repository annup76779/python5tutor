"""
we have to make a project in which we want to enable user to write into a file directly from console.
Feature-
    1. take filename form user
    2. show user the option to read or write or orverwrite into the file.
    3. based on the choice
        a. if the choice is read, show the user file content.
        b. if the choice is to write into the file take the content from user and append into the file.
        c. if the choice is to overwrite the file, clear everything and then take the content and put into the file.
"""

def show_menu():
    '''
    this function will show the menu stated above
    '''
    print("Choose any of the following operations: ")
    print("\t1. read file")
    print("\t2. write file")
    print("\t3. overwrite file")


def read_file(filename):
    """here we will read the file and show the content to the user """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())

def append_content_to_file(filename):
    """
    here we have to take the content from the user and them put it into the file
    NOTE: user may want to enter some content into new like.
    """
    print("\nStart entering the content you want to append into the file -")
    with open(filename, 'a', encoding="utf-8") as f:
        while True:
            user_in = input()
            if user_in.strip() == "":
                break
            f.write(user_in+"\n")


def write_content_to_file(filename):
    """
    here we have to take the content from the user and them put it into the file
    NOTE: user may want to enter some content into new like.
    """
    print("\nStart entering the content you want to append into the file -")
    with open(filename, 'w', encoding="utf-8") as f:
        while True:
            user_in = input()
            if user_in.strip() == "":
                break
            f.write(user_in+"\n")


def main():
    """main function to work on"""

    filename = input("Enter the filename with extension(example: text.txt): ")
    # showing the menu to the user
    show_menu()
    # asking the user to enter his\her choice
    choice = int(input())

    if choice == 1: 
        read_file(filename)
    elif choice == 2:
        append_content_to_file(filename)
    elif choice == 3:
        write_content_to_file(filename)

main()