# the first thing is I want to take the filename(.txt) from user and then make a file with that name

import os # module to hanlde operating system

FOLDER = r"E:\Python's Tutor\python\chilion_classes\file_and_exceptions"

def make_file(filename: str):
    """
    filename shouldn't have any (.) and "/\\"
    """

    new_filename = filename.replace(".", "").replace("\\", "").replace("/", "")

    return open(os.path.join(FOLDER, new_filename+".txt"), "w"), new_filename

# we have to take a complete paragraph as input and if user enters nothing in any line then we have to stop taking input

def take_para(_file):
    while True:
        line = input()
        if line.strip() != "":
            _file.write(line+"\n")
        else:
            break
    _file.flush() # saving the content entered by the user

# we have to show the user what he has written in the file
def show_file(filename: str):
    try:
        with open(os.path.join(FOLDER, filename+".txt")) as _file:
            for line in _file.readlines():
                print(line, end= "")
    except:
        print("No such file found.")


def main():
    filename = input("Enter the filename: ")
    _file, new_filename = make_file(filename) # making and getting the new file and filename

    print("Ypu can start writting into the file -")
    take_para(_file) # taking user input as paragraph

    print("\nSaving the file...")
    print(f"File saved as {new_filename}.txt")
    _file.close()

    # now we are reading the file and showing to the user
    print("\nOpening the file -\n")
    show_file(new_filename)

if __name__ == '__main__':
    main()