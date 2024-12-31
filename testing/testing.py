import copy

grid = [[2, 4, 6, 8], [3, 5, 7, 9], [0, 0, 0, 0], [0, 0, 0, 0]]

checkMatrix = []

matrix = [[21, 3, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

checkMatrix = copy.deepcopy(matrix)

matrix[0][2] += 8

print(matrix)
print(checkMatrix)

checkMatrix.pop()

print(checkMatrix)

checkMatrix = []
print(checkMatrix)

adjust_to_largest = 0

for element in matrix:
    for element in element:
        if len(str(element)) > adjust_to_largest:
            adjust_to_largest = len(str(element))



#find a way to find the largest lenght of number and adjust them to keep each number in the same column
# print( 0, 0,f" {str(matrix[0][0]).rjust(adjust_to_largest)} {str(matrix[0][1]).rjust(adjust_to_largest)} {str(matrix[0][2]).rjust(adjust_to_largest)} {str(matrix[0][3]).rjust(adjust_to_largest)}")
# print( 1, 0,f" {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} {matrix[1][3]}")
# print( 2, 0,f" {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} {matrix[2][3]}")
# print( 3, 0,f" {matrix[3][0]} {matrix[3][1]} {matrix[3][2]} {matrix[3][3]}")

# for x in range(len(matrix)):
#     print( 0, 0,f" {" ".join(str(matrix[x][i]).rjust(adjust_to_largest) for i in range(len(matrix[0])))}")




for y in range(len(matrix)):
    print(f" {" ".join(str(value).rjust(adjust_to_largest) for value in matrix[y])}")