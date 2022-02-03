# i want to make a program which will take input from user(the input will be the things he want to do today , seperated) 
# and save that in a file
# and also we have to show the list to the user when he comes back to see what he has to do today.

from datetime import datetime

def set_todo():
    print("\nYou selected set_todo")

    userIn = input("Enter your todo(, seperated) for today: \n")

    # x -> create a file only
    # w -> create if not exsist and write in it
    # r -> read the file and raise an error when file doesn't exist
    # rb -> read the binary file
    # wb -> write in the binary file
    # a -> append to the file


    todo_file = open(r'chilion_classes\file_and_exceptions\TODO_FILE.txt', 'w')
    todo_file.write(str(datetime.now()))
    for item in userIn.split(','):
        todo_file.write(f'\n{item.strip()}')

    # todo_file.flush() # saving only 
    todo_file.close() # saving changes and closing

def get_todo():
    todo_file = open(r'chilion_classes\file_and_exceptions\TODO_FILE.txt', 'r') # reading the TODO_FILE.txt

    print("\nPresenting your todo list for ->", end=" ")
    for line in todo_file.readlines():
        print(line, end="")

    todo_file.close() # closing

def main():
    try:
        print("What you want to do".rjust(50, '-'), end="-"*50)
        print()
        print("1. If you want to set your To-Do list for today press 1")
        print("2. if you want to see your To-Do list press 2")

        selection = int(input("Enter your choice(1/2): "))

        set_todo() if selection == 1 else get_todo() # if 1 then setting the todo and if 2 then getting the todo

    except ValueError:
        print("Invalid input - enter 1 or 2 for the choice")

    except FileNotFoundError:
        print("No data found! Please give us any to-do list for you to show.")

    except KeyboardInterrupt:
        print("\nNice to see you! Lets meet again.")

if __name__ == '__main__':
    main()