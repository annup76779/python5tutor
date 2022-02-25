# '''
# input -> 5

# *****
# *****
# *****
# *****
# *****
# '''

# def get_square(size):
#     s = ""
#     row,col = 0,0

#     # loop for rows
#     while row < size:
#         # now loop for columns
#         while col < size:
#             s = s + "*"
#             col+=1 # increment columns 
#         # one row completed after on complete loop of inner while loop
#         # so row incremented outside of inner loop
#         s = s+ "\n"
#         row += 1
#         col = 0
#     return s

# res = get_square(5)
# print(res)


'''
*
* *
*   *
*     *
* * * * *

* * * * *
* * * *
'''

def get_triangle(size):
    s = ""
    row,col = size,0

    # loop for rows
    while row >= 0:
        if row == size:
            print("* " * size)
        else:
            # now loop for columns
            while col < row:
                if col == 0 or col == row-1:
                    s = s + "* "
                else:
                    s = s + "  "
                col+=1 # increment columns 
        # one row completed after on complete loop of inner while loop
        # so row incremented outside of inner loop
            s = s+ "\n"
        row -= 1
        col = 0
    return s

res = get_triangle(5)
print(res)