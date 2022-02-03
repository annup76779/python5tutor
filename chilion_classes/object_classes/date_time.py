class Date:
    def __init__(self, date, delimeter = "-", pattern = 0):
        if isinstance(date, str):
            lst_date = date.split(delimeter) # spliting the date string into parts to get the parts of date
            if len(lst_date) == 3:
                if pattern == 0:
                    self.year = int(lst_date[0])
                    self.month = int(lst_date[1])
                    self.date = int(lst_date[2])
                else: 
                    self.year = int(lst_date[2])
                    self.month = int(lst_date[1])
                    self.date = int(lst_date[0])
            else:
                raise ValueError(f"Date string must have three sections but got {len(lst_date)} sections.")

    def __str__(self):
        return f"{str(self.year).rjust(4, '0')}-{str(self.month).rjust(2, '0')}-{str(self.date).rjust(2, '0')}"

    def __repr__(self):
        return str(self)

    def get_date(self, pattern = 0):
        if pattern == 0:
            return f"{str(self.year).rjust(4, '0')}-{str(self.month).rjust(2, '0')}-{str(self.date).rjust(2, '0')}"
        else:
            return f"Date({str(self.date).rjust(2, '0')}-{str(self.month).rjust(2, '0')}-{str(self.year).rjust(4, '0')})"


    def __add__(self, other: int):
        if isinstance(other, int):
            # ((dd+change_in_date) % 30), (mm + ((dd + change_in_date) // 30))% 12, (yyyy + ((dd + change_in_date) // (30 * 12)))
            dd, mm, yyyy = self.date, self.month, self.year
            date = ((dd + other) % 30)  # new date is given here
            month = (mm + (dd + other) // 30) # new month is given here
            year  = (yyyy + ((dd + other) // (30 * 12))) # new year is given here

            return Date(f"{year}-{month}-{date}")

        else: 
            raise TypeError(f"'+' is not defined for Date and {other.__class__.__name__}")

    def __sub__(self, other):
        if isinstance(other, Date):
            diff = 0
            yeardiff = (self.year - other.year) * 365
            diff += yeardiff

            monthdiff = (self.month - other.month) * 30
            diff += monthdiff

            daydiff = (self.date - other.date)
            diff += daydiff

            if diff <= 0:
                return 0

        elif isinstance(other, str):
            new = Date(other) # making new date object from the string given
            return self - new

        else:
            raise TypeError(f"'-' is not defined for Date and {other.__class__.__name__}")
        return diff

    def __lt__(self, other):
        if isinstance(other, Date):
            if self.year > other.year:
                return True
            elif self.year == other.year:
                if self.month > other.month:
                    return True
                elif self.month == other.month:
                    if self.date > other.date:
                        return True
            return False
        else:
            return TypeError(f"'<' is not defined for Date and {other.__class__.__name__}")


    def __del__(self):
        print("")

    def is_leap(self):
        if (self.year % 4 == 0) and (self.year % 100 == 0) and (self.year % 400 == 0):
            return True
        return False

def get_day_in_year(year):
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return 366
    return 365
        
# we have to make a class which can take any datetime instance or any string of date with delimeter
# and then we have to return a date instance

date = Date("2000-12-04")
d = date
del date
print(d.is_leap(), "whatever")
print(d, "new whatever")
# date2 = Date("2001-11-01")
# print(date2.is_leap())
# print(date)

# print(date.get_date())
# print(date2 - "2002-12-05")

# print(date)


# print(date + 20)

# date3 = Date("2000/10/01", delimeter = "/")
# date4 = Date("2000-12-01")

# if date < date2:
#     print('Hello')
# elif date < date: 
#     print('Yup')

# elif date < date4:
#     print("Abdullah Shahid")