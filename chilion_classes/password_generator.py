from random import choice, shuffle
from array import array
import sys

def generate_random_password(length = 12):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # list of digits

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z'] # all the lower case letters

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
                    '*', '(', ')', '<'] # all the symbols
    
    COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + SYMBOLS + [char.upper() for char in LOCASE_CHARACTERS] # making a list which has all of the things

    # in our password we need at least 1 digit, 1 lowcase, 1 upcase, 1symbole
    temp_password = choice(DIGITS) + choice(LOCASE_CHARACTERS) + choice(SYMBOLS) + choice(LOCASE_CHARACTERS).upper()

    for _ in range(length - 4):
        # making an array of the password characters to shuffle it
        temp_arr = array('u', temp_password)
        shuffle(temp_arr) # shuffling the characters of the password

        # taking back the shuffled password from array to string
        temp_password = temp_arr.tounicode() # back to string
        temp_password += choice(COMBINED_LIST)
    
    return temp_password

def main():
    try:
        length = int(sys.argv[-1])

        # calling function
        password = generate_random_password(length)
    except ValueError:
        password = generate_random_password() # calling function with default length => which is 12

    print(password)

if __name__ == '__main__':
    main()