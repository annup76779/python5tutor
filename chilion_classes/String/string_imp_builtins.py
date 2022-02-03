name = input("Enter your name and I will show you some string magic: ")

# question 1
# my entry is - anurag pandey
# what I want is  - ANURAG PANDEY

# print(name.upper() ,"- upper()")

# question2
# my entry is - anurag pandey
# what I want is  - Anurag Pandey
# print(name.title(), "- title()")

# question3
# my entry is - Anurag Pandey or ANURAG PANDEY or Anurag pandey
# what I want is  - anurag pandey
# print(name.lower(), "- lower()")


# string.capitalize()
# print(name.capitalize(), "-capitalize()")

"""
    `CASE CHANGE FUNCTIONS`
    ---------------------

    upper() -> print(name.upper())
        It makes all the letter of the string capitale

    lower() -> print(name.lower())
        It make all the letter of the string small or lower.

    title() -> print(name.title())
        it make the the first letter of all the words in the string capitale

    capitalize() -> print(name.capitalize())
        it make only the first letter of the string capitale

    `CHECKING CASE FUNCTIONS`
    ------------------------

    islower() -> print(name.islower())
        it prints True or False depending on whether the string is in lower case or not

    istitle() -> print(name.istitle())
        it prints True or False depending on whether the string is in title case or not

    isupper() -> print(name.isupper())
        it prints True or False depending on whether the string is in upper case or not
"""

# if user enters aNurag Pandey -> AnURAG pANDEY 
print(name.swapcase())