# lets say we have to substring 'divya' from a long string, which we have to find where is it and do it is present their or not
# or user is making fool of user.


some_str = "first things first: Stop waiting around to be inspired to take action."

index = some_str.rfind("first")
index = some_str.find("first")

first, mid, last = some_str[:index], "first", some_str[index+len("first"): ]

print(first+"||"+mid+"||"+last)

print(some_str.replace("first", "||first||"))