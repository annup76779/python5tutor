# we will learn about split method of str and join method of str

# -------------------------
# split method of str     #
# -------------------------

# MOTO: let's say we are making an application which will count the number of words in an essay.

string = \
"""
Just as an exercise,          let's consider how this solution would look using processes instead of threads.
We do not want a new process started for each email          that we need to send, so instead we could use the
Pool class from the multiprocessing                 module. This class creates a specified number of processes 
(which are forks of the main process) and all those processes wait to receive jobs to run, given to
the pool via the apply_async method. This could be an interesting approach for a busy site, but we 
will stay with the threads for now.
"""

words = string.split(" ") # this will give us a list of all the words in the paragraph.

count = len(words)  # number of words in the the list of words
print(f"total words are: {count}")

refracted_string = " ".join(words)
print(refracted_string) 