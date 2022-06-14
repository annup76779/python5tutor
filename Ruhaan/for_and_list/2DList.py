'''
let's say I have list of 4 digits
and what I want is to add 1 to the last digit and do the in place changes in the list
you should add 1 to the list digits of the list in such a way that the out look like addition is 
done on the number comprising of the list digits.

lst = [1,2,3,4]
1234+1 -> 1235 -> [1,2,3,5]
# after running the program if I print lst
print(lst)
Output wil be 
[1, 2, 3, 5]
'''

lst = [9,9,9,9]
carry = 1 # so that I can add 1 to the last digit and hold the carry further on if any

# now we need to keep the track of the index on which we have to add the current carry
current_index = len(lst) - 1


while carry: # 0 is False and anything which is not 0 is called True

    # first add the value the current_index with the current carry
    res = lst[current_index] + carry

    # now we need to put the once place value at the current index of the list
    lst[current_index] = res % 10 # this will give the once place value

    # now I have to put the tens place value in the carry variable
    carry = res // 10 # gives tens place value

    # once the current index addition is complete we need to move to the next index 
    # next index in the sense we have to decrement the index to get the next index
    
    if current_index < 0:
        current_index = 0
        lst.insert(0, 0) # this will put an extra 1 before the first digit of the list
        continue
    current_index -= 1

    print(lst, carry)