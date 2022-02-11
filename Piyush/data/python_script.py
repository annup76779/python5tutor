import pandas as pd
import os
import re
from numpy import nan


class MeasurementVerification(object):
    @staticmethod
    def get_criteria_key_name(expected_key: str, key_type: int = 0)-> str:
        '''
            Parameter: 
                expected_key: str: the expected key from which the actual key has to be made
                key_type: int: 0 means filename -> actual key and 1 means Part Number + Revi\
                    sion -> actual key
            
            Return: actualkey: str
        '''
        # Eg: filename is 000002_Rev-B_Part_2 -> key_name = 000002_Rev-B
        # OR
        # Eg: Part Number + Revision is 000002B -> key_name = 000002_Rev-B
        if key_type == 0:
            exp = re.compile(r"([0-9]{6}_Rev-[A-Z]+)")
            actual_key_groups = re.search(exp, expected_key)
            actual_key = actual_key_groups.group()
        else:
            exp = re.compile(r"([0-9]{6})([A-Z]+)")
            actual_key_groups = re.match(exp, expected_key)
            actual_key = "_Rev-".join(actual_key_groups.groups())
        return actual_key

    @staticmethod
    def get_criteria_files(criteria_path: str, required_keys:set) -> dict:
        """
            make a dict of all the filesobject in the criteria_path and also listed in the
            requeired_keys list retrieved from measurements.csv file
            Returns: dict: file_dict
        """
        file_dict = dict()
        for filename in os.listdir(criteria_path):
            # making the key of the file based on the filename
            # Eg: filename is 000002_Rev-B_Part_2 -> key_name = 000002_Rev-B
            key_name = MeasurementVerification.get_criteria_key_name(filename, 0)
            file_df_dict = dict()
            if key_name[:6]+key_name[-1] in required_keys:
                file_df = pd.read_csv(os.path.join(criteria_path, filename))
                for value in file_df.values:
                    file_df_dict[value[4]] = value[5:]

                file_dict[key_name] = file_df_dict

        print(file_dict)
        return file_dict

    def __init__(self, path_:str, criteria_path: str):
        '''
            Parameters:
                path_: str: path of the measurement file
                criteria_path: path of Measurement Criteria
        '''
        self.__df = pd.read_csv(path_)
        
        # taking out the Part number and revision as a set of tuples
        self.criteria = MeasurementVerification.get_criteria_files(criteria_path, set(self.__df["Part Number + Revision"]))

    def verify(self):
        output = []
        for row_index in self.__df.index:
            # get the current row in measurements.csv
            part_rev, _, characteristics, value  = self.__df.loc[row_index]

            # retrive the key to be searched in self.criteria
            if part_rev is nan:
                output.append(nan)
                continue

            key_name = MeasurementVerification.get_criteria_key_name(str(part_rev), 1)

            # getting the data of the part from self.criteria
            part_data = self.criteria.get(key_name, None)
    
            # if part_data is not present in self.criteria then put 'Data not provided'
            # and continue
            # else check for range and verify it
            if part_data is None:
                output.append("Data not provided")
            else:
                # get the current row characteristics for self.criteria
                current_part_value_checks = part_data.get(str(characteristics), None)
                if current_part_value_checks is None:
                    output.append(characteristics)
                elif value is nan:
                    output.append(nan)
                else:
                    # there are few places where the value is not numeric
                    # like at one place in any file value is 0.12a which is not a float data
                    try:
                        if float(value) <= current_part_value_checks[1] and float(value) >= current_part_value_checks[-1]:
                            output.append("Passed")
                        else:
                            if float(value) > current_part_value_checks[1]:
                                output.append("above tolerance")
                            elif float(value) < current_part_value_checks[-1]:
                                output.append("below tolerance")
                            else:
                                output.append(nan)
                    except ValueError:
                        output.append("Not valid type of value.")

        # putting the output of the verification at 4th index of the dataframe columns
        self.__df.insert(4, "Status", output, True)
        print(self.__df)

    def export(self):
        self.__df.to_csv("verified_measurements.csv")

measurement = MeasurementVerification("./data/measurements.csv", "./data/Measurement Criteria")
measurement.verify()
measurement.export()