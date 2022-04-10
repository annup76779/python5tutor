'''
basic types
1. integer (int)
2. floating point (float)
3. string (str)
4. boolean (bool)
5. complex number (complex)

advance datatypes (these are also called builtin datastructures)
1. list
2. tuple
3. set
4. dictionary (dict)

https://www.w3schools.com/python/python_operators.asp
'''

# list
lst = [4,4,4,423,"aflksad", True, 443.34]
lst[4] = 78
lst.append(323)
print(lst)

# tuples
tup = (4,4,4,423,"aflksad", True, 443.34, lst)
print(tup)

# set
st = {4,4,4,423,"aflksad", True, 443.34}
print(st)

# dict
dic = {
    "Dollar": lst,
    "Singaporean Dollar": 102.2
}
print(dic["Dollar"])