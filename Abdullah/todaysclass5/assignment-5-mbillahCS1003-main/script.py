import os
import time
import random
import copy
import cellsim




tissue=cellsim.Tissue(6,6,cellsim.Cell)
print(tissue.matrix)
print(tissue.rows)
print(tissue.cols)
print(tissue.CellType)
print(tissue)

# tissue = cellsim.Tissue(10,40,cellsim.Cell) 
# test_matrix = list()
# for i in range(10):
#     test_matrix.append([]) 
#     for j in range(40):
#         test_matrix[i].append(cellsim.Cell(False)) 
# test_matrix[5][5] = cellsim.Cell(True) 
# test_matrix[5][6] = cellsim.Cell(True) 
# test_matrix[5][7] = cellsim.Cell(True) 
# tissue.seed_from_matrix(test_matrix) 
# print(tissue)
# print(tissue[5][6])

# tissue2 = cellsim.Tissue(3,3,cellsim.Cell) 
# test_matrix = list()
# for i in range(3):
#     test_matrix.append([]) 
#     for j in range(3):
#         test_matrix[i].append(cellsim.Cell(random.choice([False,True]))) 
# tissue2.seed_from_matrix(test_matrix)
# print(tissue2)
# test_matrix=[['.','O','.'],['.','.','.'],['.','O','.']]



