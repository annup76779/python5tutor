"""
Name: 
Username: 
ID number: 

Description
-

A program which calculates a future date from the current date and a number of days.
"""

# taking inputs
import random, datetime
def get_new_date(current_date, change_in_date):
	datelist = current_date.split('/')
	dd, mm, yyyy = int(datelist[0]), int(datelist[1]), int(datelist[2]) # dd-> date, mm-> month, yyyy-> year in the date given

	# ndd -> new date, nmm-> new_date, nyyyy-> new_year
	ndd, nmm, nyyyy = ((dd+change_in_date) % 30), (mm + ((dd + change_in_date) // 30))% 12, (yyyy + ((dd + change_in_date) // (30 * 12)))

	return '/'.join((str(ndd + (ndd == 0)), str(nmm+ (nmm == 0)), str(nyyyy)))

current_date = datetime.datetime.now().strftime("%d/%m/%Y")
change_in_date = random.randint(1, 10000)

print("In", change_in_date, "days,",current_date,"will be", get_new_date(current_date, change_in_date))