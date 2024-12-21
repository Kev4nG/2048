from operator import xor
from threading import local

#this is for shigtin
            #0 1 2 3
matrix = [[2,0,2,2], [2,0,2,0], [2,4,2,0], [2,0,2,8]]
arr= [2,0,2,0]

length = len(arr) -1
length_of_matrix = len(matrix) 
count = 0 
# if local 
for i in range(length_of_matrix):
    while count != length:
        left = matrix[i][count]
        right= matrix[i][count+1]

        if left == 0 and right != 0:
            left ^= right
            right ^= left
            left ^= right  

            matrix[i][count] = left
            matrix[i][count + 1] = right     

            count = 0

        count += 1
    count = 0

print(matrix)