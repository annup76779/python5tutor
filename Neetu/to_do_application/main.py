from service.task_service import read_task
from core.viewModels import TaskVM


def main():
    readTask: TaskVM = read_task()

    print("Title: ", readTask.title)
    print("description: ", readTask.description)
    print("priority: ", readTask._priority)
    print("status:", readTask.status)
    print("time:", readTask.time)

    # suppose we were using dictionaries for returning read task from user
    # so we would be using .get("key name") to fetch value from the returned object
    # and also there was no surity that the fields actually existed in the dictionary


if __name__ == '__main__':
    main()
