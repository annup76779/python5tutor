"""
Name: 
Username: 
ID number: 

Description
-

A program to gernerate the Pokemon's name

1. A random number index_start1 between 2 and half the length of the first word(rounded down).
2. A random number length_substring1 between 2 and half the length of the first word(rounded down).
3. A random number index_start2 between 2 and half the length of the second word(rounded down).
4. A random number length_substring2 between 2 and half the length of the second word (rounded down).


1. Get a substring from the first word, starting at index_start1 and with a length oflength_substring1.
2. Get a substring from the second word, starting at index_start2 and with a length oflength_substring2.
3. Concatenate the first substring and the second one.
"""

import random

first_pokemon_name = input("Enter the first word: ")
second_pokemon_name = input("Enter the second word: ")

index_start1 = random.randint(2, len(first_pokemon_name)//2)# starting index of first substring
length_substring1 = random.randint(2, len(first_pokemon_name)//2) # ending index + 1 of the substring

first_substring = first_pokemon_name[index_start1 :][: length_substring1] # first_substring of the name

index_start2 = random.randint(2, len(second_pokemon_name)//2)# starting index of first substring
length_substring2 = random.randint(2, len(second_pokemon_name)//2) # ending index + 1 of the substring

second_substring = second_pokemon_name[index_start2 :][: length_substring2] # first_substring of the name


# finding the output string
output = "Your Pokemon name is " + first_substring.capitalize() + second_substring

print("*" * (len(output)+4))
print("*", " " * len(output), "*")
print("*", output, "*")
print("*", " " * len(output), "*")
print("*" * (len(output)+4))