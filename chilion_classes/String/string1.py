# huge_str = "some huge strings"
# # slicing means just to make a new string of an older string which is the part of the older string.

# h_var = huge_str[ : 9]
# print(h_var)

# if "sgome" in huge_str:
#     print("we got `some`")


# Builtins present in the strings
 
new_str = "green, red, blue, orange, red, yellow, red, green"

print(new_str.count("d"))

# suppose we want to check that if anything(say 'red') is presend in the string as a substring
print(new_str.find("red"))

print(new_str.rfind("red"))