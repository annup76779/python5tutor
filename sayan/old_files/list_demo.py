stud_lst = ["Anurag", "Sayan", "Vandita", "Jhon", "chilion", "Ritchi", "Robert", "Shashank"]
print(stud_lst[4])

# adding new data to the list
# there are 3 ways to add new data to the list
## append()
## insert()
## extend()
print(stud_lst)
stud_lst.append("Vishal") # it adds the new given data at the end of the list
stud_lst.append("Matheli")
print(stud_lst)


# using insert() method of the list
stud_lst.insert(0, "Bob") # the index you give must not be more than the length of the list
print(stud_lst)

print(len(stud_lst))
print(stud_lst.pop(4))
print(stud_lst)

print("Name")
print("-" * 20)
print("\n".join(stud_lst))