# if we have to check what is in the string
# by this I mean that is that string has alphabet or number or both(alpha, number) or string has a digit, or it is has white space

# the method to verify what is in the string are stated below:- 
# 1. isalpha()
# 2. isalnum() 
# 3. isdigit()
# 4. isnumeric()
# 5. isspace()

# s1 = "lkasdjfklsdkjk"
# s2 = "ajsdfklsd23423kjkjksadjf"
# s3 = "2342342332423"
# s4 = "6"
# s5 = "|t"


# print("for s1 ->"\
#     "\n1.", s1.isalpha(),\
#     "\n2.", s1.isalnum(),\
#     "\n3.", s1.isnumeric(),\
#     "\n4.", s1.isdigit(),\
#     "\n5.", s1.isspace()
#     )


# print("for s2 ->"\
#     "\n1.", s2.isalpha(),\
#     "\n2.", s2.isalnum(),\
#     "\n3.", s2.isnumeric(),\
#     "\n4.", s2.isdigit(),\
#     "\n5.", s2.isspace()
#     )


# print("for s3 ->"\
#     "\n1.", s3.isalpha(),\
#     "\n2.", s3.isalnum(),\
#     "\n3.", s3.isnumeric(),\
#     "\n4.", s3.isdigit(),\
#     "\n5.", s3.isspace()
#     )


# print("for s4 ->"\
#     "\n1.", s4.isalpha(),\
#     "\n2.", s4.isalnum(),\
#     "\n3.", s4.isnumeric(),\
#     "\n4.", s4.isdigit(),\
#     "\n5.", s4.isspace()
#     )

# print("for s5 ->"\
#     "\n1.", s5.isalpha(),\
#     "\n2.", s5.isalnum(),\
#     "\n3.", s5.isnumeric(),\
#     "\n4.", s5.isdigit(),\
#     "\n5.", s5.isspace()
#     )

# startswith()
# endwith()

# startswith is method of string which is used to check if any string starts with any specific sub string
# endwith is method of string which is used to check if any string ends with any specific sub string

longstr = " hello this is anurag teaching to apoorva."
# print(longstr.startswith(" hello"))
print(longstr.endswith("apoorva."))
