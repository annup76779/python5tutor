lst = [
    "Python Introduction", "Function", "Controle Statements", "Debuging", "Scope", "Strings", "Mutable and Immutable Object",
     "Recursion", "Files and Exceptions", "ClassesI", "ClassesII"
     ]

print(lst[10])
print(lst[-1])

print(lst[7])
print(lst[-4])


s = "Hello"
backend_s = ["H","e", "l", "l", "o"]

tp = (
    "Python Introduction", "Function", "Controle Statements", "Debuging", "Scope", "Strings", "Mutable and Immutable Object",
     "Recursion", "Files and Exceptions", "ClassesI", "ClassesII"
)



# slicing -> it takes 3 things -> 
                            # first thing -> starting point
                            # seconds thing -> ending point
                            # third thing -> incrementing/skips

starting_point = 1
ending_point = 7
skips = 1 # skiping given - 1 -> default increment/skip is 1

new_tp = tp[len(tp) - 1: : -2]
print(new_tp)