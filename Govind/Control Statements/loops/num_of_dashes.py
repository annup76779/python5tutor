def num_to_dashes(num):
    s = "" # empty string
    counter = 0 # counter to track number of dashed in the string
    while counter < num:
        s = s + "-"
        counter+= 1 # increment counter when a new dash pushed into the strings
    return s

dashed = num_to_dashes(20)
print(len(dashed), dashed) 