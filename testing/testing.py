import copy

grid = [[2,4,6,8], [3,5,7,9], [0,0,0,0], [0,0,0,0]]

checkMatrix = []

matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

checkMatrix = copy.deepcopy(matrix)

matrix[0][2] += 8

print(matrix)
print(checkMatrix)

checkMatrix.pop()

print(checkMatrix)

checkMatrix = []
print(checkMatrix)