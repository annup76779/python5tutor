# lst = [1, 2,3,4,5] -> 1D list
# 2Dlst = [[1,2,3,3], [3,4,5,43], [4,5,6,7]]
# when you put lists as the only type of data in an outermost list, the outermost list is called 2d list

lst = [[1,2,3,3], [3,4,5,4], [4,5,6,7]]

max_ = 0
for nested_list in lst:
	current_sum = sum(nested_list)
	if max_ < current_sum:
		max_ = current_sum
		current_max_lst = nested_list

print(current_max_lst)