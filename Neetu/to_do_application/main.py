from service.task_service import read_task, add_to_task_list
from core.viewModels import TaskVM


def main():
    readTask: TaskVM = read_task()
    add_to_task_list(readTask)


if __name__ == '__main__':
    main()
