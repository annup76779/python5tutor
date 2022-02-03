# In this we will learn about how can we access any value from the dictionary.
# we have directly two way to access key from the dictionary.
# 1. Normal access -> dict['key']
# 2. Using get method of dictionay -> dict.get("key", "default value")

mydict = {"name": "Anurag Pandey", "email": "annup76779@gmail.com", "phone": "+91 8726771497", "state": "India", "state": "Singapore"}
# ----------------------------
# using normal access #
# ----------------------------

# name_of_user = mydict["name"] # accessing name of user from dictionary
# print(name_of_user) 

# ----------------------------------------
# accessing a key not in the dictionary #
# ----------------------------------------
# name_of_user = mydict["user_name"] # accessing name of user from dictionary
# print(name_of_user) 

# by running the code in line 17 we get a 'KeyError' which means you don't have the key you are accessing from the dictionary.
# one way is to user following code-
'''
try:
    name_of_user = mydict["user_name"] # accessing name of user from dictionary
    print(name_of_user)
except KeyError:
    name_of_user = "Anurag"
    print(name_of_user)
'''

# OR 
# by using get method of dictionary
 
# ------------------------------------------------------------
# accessing a key not in the dictionary using get method #
# ------------------------------------------------------------
name_of_user = mydict.get("user_name", "Anurag") # not giving any default value because by default None is the default value in get method.
print(name_of_user)


# next topic is accessin value by for loop.