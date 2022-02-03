import os
import time
import random
import copy


class Cell (object ):

    def __init__(self,alive=False):
        self.alive=alive
    
    def __str__(self):
        if self.alive:
            return "O"
        else:
            return "."
    
    def is_alive(self):
        return self.alive

    def update_cell(self, matrix):
        if len(matrix) != 3 and len(matrix[0]) != 3 and len(matrix[1]) != 3 and len(matrix[2]) != 3:
            print("Matrix size must be 3x3")
            return 
        # for x in matrix:
        #     print("".join(x))
        status = {
            True: 0, False: 0
        }
        
        for x in matrix:
            for y in x:
                if y != matrix[1][1]:
                    status[y.is_alive()] += 1
        # print(status)
        
        if status.get(True) >= 4: # overpopulation
            self.alive = False
        elif status.get(True) == 3: # alive condition
            self.alive = True
        elif status.get(True) <= 1: # lonlyness 
            self.alive = False

class Tissue ( object ):
    # CellType=
    def __init__(self, rows=1, cols=1, CellType = Cell):
        # matrix=[]
        self.matrix=[[CellType() for _ in range(cols)] for _ in range(rows)]
        self.rows=rows
        self.cols=cols
        self.CellType=CellType

    def __str__(self):
        string_matrix=[[str(col) for col in row] for row in self.matrix]
        return "\n".join(["".join(row) for row in string_matrix])


    def __setitem__(self,key, cell):
        self.matrix[key] = cell

    def __getitem__(self, key):
        return self.matrix[key]

    def seed_from_matrix(self, test_matrix):
        self.matrix=copy.copy(test_matrix)
        return self.__str__()
        

    def seed_from_file(self, path, CellType = Cell):
        new_matrix=[]
        with open(path,'r') as f:
            for raw_line in f.readlines():
                line=[]
                for data in raw_line.strip():
                    if data=='.':
                        line.append(CellType())
                    else:
                        line.append(CellType(True))
                if self.cols!=len(line):
                    raise IndexError("Column of matrix doesnot match the given column counts.")
                new_matrix.append(line)
            self.matrix=new_matrix


    def seed_random(self, confluency:float, CellType = Cell):
        new_matrix=[]
        for row in range(self.rows):
            __row=[]
            for col in range(self.cols):
                cfy=round(random.random())
                __row.append(CellType(True if cfy<confluency else False))
            new_matrix.append(__row)
        self.matrix=new_matrix


    def next_state(self):
        new_matrix = copy.deepcopy(self.matrix)
        for i, x in enumerate(self.matrix): # x is refered as x axis of the matrix
            for j, y in enumerate(x): # y is refered as y axis of the matrix
                sub_matrix = []
                # in case the current element is the element of the first row
                if i == 0:
                    sub_matrix.append([self.CellType(False) for _ in range(3)]) 
                
                # in case the current element is the element of the elemet of first column of the matrix
                if j == 0:
                    if i != 0:
                        sub_matrix.append([self.CellType(False), self.matrix[i-1][j], self.matrix[i-1][j+1]])
                    sub_matrix.append(
                        [self.CellType(False), self.matrix[i][j], self.matrix[i][j+1]],
                    )
                    if i != len(self.matrix) -1:
                        sub_matrix.append(
                                [self.CellType(False), self.matrix[i+1][j], self.matrix[i+1][j+1]]
                            )
                    
                # in case the current element is the element of the last column of the matrix
                elif j == len(x) - 1:
                    if i != 0:
                        sub_matrix.append([self.matrix[i-1][j-1], self.matrix[i-1][j], self.CellType(False)])
                    sub_matrix.append(
                        [self.matrix[i][j-1], self.matrix[i][j],self.CellType(False)]
                    )
                    if i != len(self.matrix) -1:
                        sub_matrix.append(
                            [self.matrix[i+1][j-1], self.matrix[i+1][j], self.CellType(False)]
                        )
                
                else:
                    if i != 0:
                        sub_matrix.append(
                            [self.matrix[i -1][j-1], self.matrix[i-1][j], self.matrix[i-1][j+1]]
                        )
                    sub_matrix.append([self.matrix[i][j-1], self.matrix[i][j], self.matrix[i][j+1]])
                    if i != len(self.matrix) -1:
                        sub_matrix.append([self.matrix[i + 1][j-1], self.matrix[i+1][j], self.matrix[i+1][j+1]])

                if i == len(self.matrix) - 1:
                    sub_matrix.append([self.CellType(False) for _ in range(3)])
                
                new_matrix[i][j].update_cell(sub_matrix)

                # for m in sub_matrix:
                #     print("".join([str(k) for k in m]))
                # print(i, j, end="\noutput\n")
                # print()
                # string_matrix=[[str(col) for col in row] for row in new_matrix]
                # print("\n".join(["".join(row) for row in string_matrix]))
                # input()
        self.matrix = new_matrix


class Cancer(Cell):
    def __init__(self,alive=False) -> None:
        self.alive=alive
    def __str__(self):
        if self.alive:
            return 'X'
        else:
            return '.'

    def is_alive(self):
        return self.alive

    def update_cell(self, matrix):
        if len(matrix) != 3 and len(matrix[0]) != 3 and len(matrix[1]) != 3 and len(matrix[2]) != 3:
            print("Matrix size must be 3x3")
            return 

        status = {
            True: 0, False: 0
        }
        
        for x in matrix:
            for y in x:
                if y != matrix[1][1]:
                    status[y.is_alive()] += 1
        
        if status.get(True) >= 5: # overpopulation
            self.alive = False
        elif status.get(True) == 3: # alive condition
            self.alive = True
        elif status.get(True) <= 1: # lonlyness 
            self.alive = False

tissue = Tissue(10, 40, Cell)
print(tissue)
print()
tissue.seed_from_file("sample.txt")
# tissue.seed_random(0.5, Cell)
print(tissue)
# .OO
# ...
# ..O

# ...last
# ...
# O..
# O..
# this code should be run from your terminal or command prompt
# from terminal, move your current working directory to be
# this script.py and cellsim.py are located
# then run "python3 script.py", where script.py contains the
# tissue.next_state()
for i in range(0,99):
    os.system('clear') #will be os.system('cls')
    tissue.next_state()
    # time.sleep(0.1)
print()
print(tissue)