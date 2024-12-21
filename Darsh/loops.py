# for loops
# we saw about range and iterators and generators

"""
* * * * * * *   row = 6, columns = 6  , star_count = 7
  * * * * * *   row = 5, columns = 5  , star_count = 6
    * * * * *   row = 4, columns = 4  , star_count = 5
      * * * *   row = 3, columns = 3  , star_count = 4
        * * *   row = 2, columns = 2  , star_count = 3
          * *   row = 1, columns = 1  , star_count = 2
            *   row = 0, columns = 0  , star_count = 1
"""

for row in range(7):
    for space in range(7 - row - 1):
        print(" ", end=" ")
    for column in range(row+1):
        print("*", end=' ')
    print()

