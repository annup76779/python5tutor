from p1 import make_lst

class MyDate:
    def __init__(self, date, delimiter):
        self.date, self.month, self.year = [int(x.lstrip("0")) for x in date.split(delimiter)]

    def __str__(self):
        return f"{self.date}-{self.month}-{self.year}"

    def __repr__(self):
        return str(self)

    def __add__(self, change_in_date):
        ndd, nmm, nyyyy = ((self.date+change_in_date) % 30), (self.month + ((self.date + change_in_date) // 30))% 12, (self.year + ((self.date + change_in_date) // (30 * 12)))

        return MyDate('/'.join((str(ndd + (ndd == 0)), str(nmm+ (nmm == 0)), str(nyyyy))), "/")

    
date = MyDate("02/07/2020", "/")
new_lst = [date + x for x in range(10, 50)]
make_lst(new_lst)
