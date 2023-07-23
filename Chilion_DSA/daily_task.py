from linkList2 import LinkList


class TaskScheduler:
    def __init__(self):
        self.__list = LinkList()
        self.check = False

    def add_new_task(self, task: str):
        """Adds a new task to the queue"""
        self.__list.appendData(task.capitalize())
        self.check = True

    def mark_current_task_completed(self):
        """Mark the last to be done task as completed"""
        self.__list.deleteStartNode()
        self.check = self.__list.head is not None

    def delete_a_task(self, position):
        if self.check:
            previous, current = self.__list.move_to_desired_position(position)
            if current is not None:
                previous.ref = current.ref
                del current
        else:
            print("There are no tasks to check.")
        self.check = self.__list.head is not None

    def change_task_details(self, new_task_detail: str, position: int):
        """Change the task details"""
        if self.check:
            _, current = self.__list.move_to_desired_position(position)
            current.data = new_task_detail.capitalize()
        else:
            print("There are no tasks to check.")

    def task_list(self):
        node = self.__list.head
        count = 1
        print("Printing out all the tasks left to do. ")
        while node is not None:
            print(str(count).rjust(4), node.data)
            node = node.ref
            count += 1


def main():
    ts = TaskScheduler()
    check = True
    while check:
        if ts.check:  # if the task scheduler is not empty
            choice = input("(1) Add new task?\n(2)or change a task?\n(3) or delete a task?\n(4)or mark as "
                           "completed?\n(5) View all tasks.")
            if choice.isdigit():
                choice = int(choice)
            if choice not in [1, 2, 3, 4, 5]:
                print("Please choose correct options - ")
                continue
            if choice == 1:
                task = input("Enter a new task: ")
                ts.add_new_task(task)
            elif choice == 2:
                ts.task_list()
                task = input("Enter a new task: ")
                pos = int(input("Enter the position of task from the task list - "))
                ts.change_task_details(task, pos)
            elif choice == 3:
                ts.task_list()
                pos = int(input("Enter the position of task from the task list - "))
                ts.delete_a_task(pos)
            elif choice == 4:
                ts.mark_current_task_completed()
            elif choice == 5:
                ts.task_list()
        else:
            task = input("Enter a new task: ")
            ts.add_new_task(task)
        print("Do you want to exit? - ")
        check_in = input("Enter y/n: ")
        check = check_in.lower() != "y"


if __name__ == '__main__':
    main()
