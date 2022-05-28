'''
sequences in python
for which ever datatype or data structure are you are able to get
more than one data of any type or same type that is called sequence in python


who are tha sequences(iterators/iterables) in python?
1. string -> immutable sequence of character
2. list
3. tuple
4. dictionary
5. range
6. set
7. map
'''


# write a program to reverse the string provided
s = "Array_memory"
# s = s[::-1]
# reversed(s)

rev_str = '' # so that we can store the reversed string

for ch in s:
    rev_str = ch + rev_str
    print(ch, "     ", rev_str)

print(rev_str)


# conver a decimal number to binary string