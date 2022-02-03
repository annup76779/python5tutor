# what is the use of *args and **kwargs?
# when you are specific about the number of parameter to be used then use these things

# *args -> this is a tuple of arguments
# we have to take any numeber of numeric data and we have to find out the sum of thier squareroots and round it to
#  2 decimal places
# def sum_sqrt(*anurag):
#     _sum = 0
#     for arg in anurag:
#         _sum += arg ** (0.5)
#         yield round(_sum, 2)

# for current_sum in sum_sqrt(54,2,23,23324,234,324,324,32,423,4,324,32,4,324,23,4,234,23,423,43543,34,534,534):
#     print(current_sum)

# **kwargs -> this is a dictionary of arguments
# def my_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"My {key} is {value}.")

# my_info(name = "Anurag Pandey", location = "UP")

# s = "20/12/2020"
# funtion using both of them
def show_my_date(*args, **kwargs):
    if kwargs.get("date") is None:
        dd, mm, yyyy = args[0], args[1], args[2]

    else:
        delimiter = kwargs.get("delimiter", "-")
        dd, mm, yyyy  = kwargs.get("date").split(delimiter)

    print(f"{dd}, {mm}, {yyyy}")


show_my_date(20, 12, 2020)
show_my_date(date = "20/12/2020", delimiter = "/")