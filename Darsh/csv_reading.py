import os
import csv


def get_path_if_exists():
    """
    Asks for user input for the file path, and then checks if the provided path exists or not

    Returns : path:str: path that exists
            : False if path does not exist
    """
    path = input("Enter the CSV file path: ")
    if os.path.exists(path):
        return path
    return False


def main():
    path = get_path_if_exists()
    if not path:
        print("The entered path is not valid/exists, please check it again.")
        return

    # finally when it sure that the file path exists and valid, start reading the file and do calculation
    sum_ = 0
    with open(path, 'r') as csv_file:
        # create a read of csv file
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # move to next position by simply reading the first line and ignoring it 

        for line in csv_reader:
            # [Anrag Pandey, Banana, 10, 2, 8]
            line_data = list(map(lambda x: x.strip(), line))
            if line_data:
                sum_ += float(line_data[-1])

    # WE ARE DONE READING THE CSV FILE, NOW WE HAVE TO WRITE INTO THE FILE 
    with open(path, 'a+', newline="") as csv_file:
        writer = csv.writer(csv_file)  # initalized a writer for csv file
        writer.writerow(["", "", "", "", str(sum_)])  # writting the csv data

main()


## NOTE: Before performing any append operation on a csv file, make sure that the file is have an empty line at the end of csv file, else the new data written will be placed in continuation of previous row's data