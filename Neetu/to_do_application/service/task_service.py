from core.utitlity import get_enum_member
from core.enums import PriorityEnum


# A function to take task a user input
def read_task() -> dict:
    title = input("~ Task title: ")
    description = ""
    print("~ Task description (leave a line blank to exit of editor): ")
    while True:
        line = input()
        if line.strip() == '':
            break
        description += (" " + line.strip())

    priority_selection = get_enum_member(PriorityEnum, input("~ Task priority (s - severe, m - medium, l - low(default)):").strip()[:1])  # l
    if priority_selection == None:
        pass
    



# A function print a task on the console 
