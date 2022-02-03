stud_main_details = [0, 1, "Anruag", 21,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, "Kanpur", "India",  "KIT", "BTech", "CSE"]
stud_parant_details = ["Ak Pandey", 46, "14/01/1976"]

# extend() method of list
# this method is used to merge any two pre-existing lists
## for example
stud_main_details.extend(stud_parant_details)

print(stud_main_details)
# insert(index, data) is used to put data at any specific index of the list

stud_main_details.insert(5, "ROOMA")
print(stud_main_details)

# remove(data) is used to remove the first orccurence of any data in the list it finds.
stud_main_details.remove("Kanpur")
print(stud_main_details)

# count(data) is a method of list used to count the total occurrance of any data in the list.
print(stud_main_details.count(2))

# pop(index) is used to remove any data from any specific index of the list.
stud_main_details.pop(3)
print(stud_main_details)