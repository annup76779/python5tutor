from copy import copy

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


subjects_database = dict()
for i in range(5):
    create_subject(subjects_database)
print(subjects_database)
