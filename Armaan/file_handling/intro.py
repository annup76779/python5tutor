'''
when you have to perform any kind of operation on files using python 
we use file handling of python

types of files supported by python
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
'''

f = open('Armaan/file_handling/test2.txt','x')

f.write("Hellow my name is anurag")