from core.utitlity import get_enum_member
from core.enums import PriorityEnum
from core.viewModels import TaskVM
from repository import write_task_in_db


# A function to take task a user input
def read_task() -> TaskVM:
    title = input("~ Task title: ")
    description = ""
    print("~ Task description (leave a line blank to exit of editor): ")
    while True:
        line = input()
        if line.strip() == '':
            break
        description += (" " + line.strip())

    while True:
        priority_selection = get_enum_member(PriorityEnum, input("~ Task priority (s - severe, m - medium, l - low(default)):").strip()[:1])  # l
        if priority_selection != None:
            break
        print("Invalid priority selection, please select from the options -----")

    return TaskVM(title=title, description=description, _priority=priority_selection)


def add_to_task_list(task: TaskVM):
    write_task_in_db(task)
