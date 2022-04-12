#--------------
# mode of files
# -------------

# 1. x : creating a file
# 2. w : write mode + (create and write mode)
# 3. r : read mode
# 4. a : append mode

my_file = open("leaning.txt", "w") # opens the file and returns an object of that file

my_file.write("This is file handling class\n") # line 1
my_file.write("I learned modes of file\n")# line 2 
my_file.write("I am writing into the file\n") # line 3

# saving into the file 
my_file.flush()

my_file.write("Hello")
my_file.close()