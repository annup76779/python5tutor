

def cal():
	# open("result.txt","x") # creating the result.txt file need to be uncommented when there is no result.txt file
	f = open("fahim.txt","r")# reading the fahim.txt file
	r = open("result.txt","a")# opening result.txt file to append the total and status of each student in that file.
	marks = f.readlines() # getting the list of each line in the file fahim.txt and saving to marks variable.
	status = "Fail" # by default each student will be considered as Fail
	for i in marks:# looping on the list of lines 
		english, maths, hindi, science, sst = list(map(int, i.split())) # here I am using map function to convert all the data of i.split() into a integer
		# i.split == ["54","32","78","67","5"] and list(map(int, i.split())) == [54,32,78,67,5]
		total = english + maths + hindi + science + sst # total marks of the student
		if english >33 and maths >33 and hindi > 33 and science >33 and sst >33: # checking if the student is pass or fail.
			status = "Pass"# changing the default status of student from Fail to Pass
		r.write(f"{total} {status}\n") # writing total marks and status to the result.txt file in order to read it later
	r.close()# closing result.txt file 
	f.close()# closing fahim.txt file.


def main():
	# open("fahim.txt","x")# creating fahim.txt fiel if there is no fahim.txt file.
	f = open("fahim.txt","a") # opening the fahim.txt file to append student marks in that file
	while True:
		try:
			eng = int(input("Enter English: "))
			math = int(input("Enter Maths: "))
			hindi = int(input("Enter Hindi: "))
			sci = int(input("Enter Science: "))
			sst = int(input("Enter Social Science: "))
			f.write(f"{eng} {math} {hindi} {sci} {sst}\n")
		except:
			break

	f.close()# closing fahim.txt file.



main()
cal()
