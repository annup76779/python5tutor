from core.viewModels import TaskVM
from dbConfig import *
from datetime import datetime


def write_task_in_db(task: TaskVM):
    # I will take a TaskVM object in parameter
    # I have to check if the there is any task present into our database for current date or not
    # if there is any task for current date, I will add our new task at the end of the database that date's array
    # but if there is no task for current date, then I have to a new key in the database, value should be an array
    # with current task

    current_date = datetime.now().date().strftime("%Y-%m-%d")

    # if there is any task in database for current date
    # we will get that array, else we will get empty array

    # Another logic that you can find in market
    # if current_date in DATABASE.keys():
    #     DATABASE[current_date].append(task.to_json())
    # else:
    #     DATABASE[current_date] = [task.to_json()]

    # My Logic that I like to write
    current_date_task_array = DATABASE.get(current_date, [])
    current_date_task_array.append(task.to_json())
    DATABASE[current_date] = current_date_task_array

    write_db(DATABASE)

