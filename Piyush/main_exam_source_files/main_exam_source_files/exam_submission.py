"""
CP1404 2022-52 Main Exam - Online Assignment
Name: XXX

Where needed, use additional code files.
Ensure that each question's answer is clearly identifiable.
"""


# 7.
# Explanation:

# Code:
# Refactor the code and explain your reasons
length = float(input("Length? "))
width = float(input("Width "))
if length * width >= 30:
    print("Room of size {} sqm => Big".format(length * width))
elif length * width >= 10:
    print("Medium room of size {} sqm".format(length * width))
else:
    print("Your room is small at only {} sqm".format(length * width))


# 8.
# Explanation:

# Code:
# Remove vowels from text in the function
def remove_vowels(text):
    text = "".join([x for x in text if x.lower() not in "aeiou"])

# Start with "ElephAnt" and pass into function to change to "lphnt"
text = "ElephAnt"
remove_vowels(text)
print(text)



# 9.
# Code:
def main():
    in_file = open("data.txt")
    data = get_data(in_file)
    in_file.close()
    average(data, len(data))


def get_data(in_file):
    values = []
    for line in in_file:
        values.append(float(line))
    return values


def average(data, length):
    average = sum(data) / length
    print("The average is", average)


main()


# Explanation:


# 10.

# 11.
# def function(??
#     return x + y + z
#
#
# print(function(2, y=5))  # prints 30
# print(function(y=10))  # prints 41
# print(function(100))  # prints 138


# 12.
my_graph = ["124", "23", "3124", "412"]

# 13.
data_string = "date='2021-08-18'| close=174.740005 | volume=7063500"
data_string = "close=180.139999| volume=8697000 | date='2021-08-27'"



# 14.
numbers = [10, 20, -13, -20, 55, 107, 200, -100, -222]


# 15.
pairs = ((2010, 'cm'), (1234, 'm'), (129.59, 'km'), (41231, 'm'), (67, 'km'))


# 16.
strings = ["some789", "th3e4r1e23", "r3oos5ting5", "2honk3honk45"]


# 17.
d = {"Iron": 26, "Oxygen": 8, "Neon": 10, "Tin": 50}


# 18.
# Explanation:

def init_this(things):
    """Initialize empty list"""
    things = [1, 2, 3]

some_things = []
init_this(some_things)
print(some_things)


# 19.
values = [4, 2, -3, 12, 8, 2, 9, -3]


# 20. Answer in basketball_players.py
# 21. Answer in employee.py
# 22. Answer in auctions.py
