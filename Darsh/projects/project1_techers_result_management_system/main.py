from copy import deepcopy

constants = {
    "inputs": {
        "max_marks": "Enter maximum marks (default: 100): ", 
        "min_marks": "Enter minimum marks (default: 0): ", 
        "subject_type": "Choose subject type: (1: Theory (defuault), 2: Practical): ", 
        "subject_name": "Enter subject name: "
    },
    "messages": {
        "subject_type": "\"Setting subject type to Theroy.\"",
    },
    "defaults": {
        "max_marks": 100, 
        "min_marks": 0
    }, 
    "practical": "Practical", 
    "therory": "Theory",
    "subject_dict": {
        "max": None, 
        "min": None,
        "type": None, 
        "marks": None
    },
}


# Making functionality to create subject into the application
# We will make a list of the subjects created and can be accessed whenever required with their name

def create_subject(subjects_database: dict) -> dict:
    # take subject name
    name = ""
    while name.strip() == "":
        name = input(constants["inputs"]['subject_name'])

    # by default we will make max marks to 100
    max_marks = input(constants["inputs"]["max_marks"])
    if max_marks.strip().isnumeric():  # not accept float value as well
        max_marks = int(max_marks)
    else:
        max_marks = constants["defaults"]["max_marks"]

    # by default we will make min mark to 0
    min_marks = input(constants["inputs"]["min_marks"])
    if min_marks.strip().isnumeric():  # not accept float value as well
        min_marks = int(min_marks)
    else:
        min_marks = constants["defaults"]["min_marks"]

    # Type of subject
    subject_type = input(constants["inputs"]["subject_type"]).strip()
    if subject_type == "2":
        subject_type = constants["practical"]
    else:
        print(constants["messages"]["subject_type"])
        subject_type = constants["therory"]

    # we have all the data and we are going to save this subject into the subject database
    subject_data = copy(constants["subject_dict"])
    for key, value in zip(subject_data.keys(), [max_marks, min_marks, subject_type, None]):
        subject_data[key] = value

    subjects_database[name] = subject_data
    return subjects_database


def create_result(subject_database: dict, result_database: dict):
    n = input("How many students do you want to enter: ")
    while not n.isnumeric():
        n = input("(Bad value: Expected number but got %s)\nHow many students do you want to enter: " % n)

    n = int(n)
    # loop for n number of time 
    for i in range(n):
        name = input("Enter students (%s) name: " % i)
        roll = input("Enter %s's roll number: " % name)

        result_database[name] = {
            "roll_number": roll, 'subject': {deepcopy(subject_database)}
        }

        # We will take obtained marks of all the subjects
        for subject_name in result_database.get(name, {}).key('subject', {}).keys():
            obtained_marks = input("Enter %s's obtained marks of %s: " % (name, subject_name))
            while not is_valid_marks(obtained_marks):
                obtained_marks = input("(Bad value: Expected number but got `%s`)\nEnter %s's obtained marks of %s: " % (obtained_marks, name, subject_name))

            # we know that obtained marks is valid, we can directly parse it to float number
            obtained_marks = float(obtained_marks)
            subject_database[subject_name]['marks'] = obtained_marks


# utitly functions 
def is_valid_marks(str_marks) -> bool:
    if str_marks.count(".") > 1: # a floating point number can have single "."
        return False

    # if there is one or no "."
    if str_marks.count(".") == 1:
        str_marks_copy = str_marks.replace(".", "").strip()
        return str_marks_copy.isnumeric()
    else:
        return str_marks.strip().isnumeric()


def main():
    subjects_database = dict()
    result_database = dict() 
    # create subject for the teacher
    create_subject(subjects_database)
    # create results for the teacher
    create_result(subject_database, result_database)


if __name__ == "__main__":
    main()

