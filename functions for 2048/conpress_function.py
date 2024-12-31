
matrix = [[2,2,2,2], [2,2,2,2], [2,2,2,2], [2,2,2,2]]
a = [[0,0,0,0], [2,2,2,2], [2,2,2,2], [2,2,2,2]]  # this is the matrix
length = len(matrix[0]) -1      # finds the length of the indinces of the matrix... the assumption is that it will be 4by4
length_of_matrix = len(matrix) 
direction = 'right'

def compress(direction):
    # LEFT DIRECTION
    if direction == 'left':
        count = 0 
        for i in range(length_of_matrix):
            while count != length:
                left = matrix[i][count]
                right= matrix[i][count+1]
                sum1 = 0

                if left == right and left != 0:
                    sum1 = left + right
                    matrix[i][count] = sum1
                    matrix[i][count+1] = 0

                count += 1
            count = 0

        print(matrix)

    #RIGHT DIRECTION    
    elif direction == 'right':
        count = length 
        for i in range(length_of_matrix):
            while count != 0:
                left = matrix[i][count-1]
                right= matrix[i][count]
                sum1 = 0

                if left == right and left != 0:
                    sum1 = left + right
                    matrix[i][count] = sum1
                    matrix[i][count -1] = 0

                count -= 1
            count = length

        print(matrix)

    #UP DIRECTION
    elif direction == 'up':
        for i in range(4):
            print(matrix[i])

        count = 0 
        for i in range(length_of_matrix):
            while count != length:
                up = matrix[count][i]
                down = matrix[count+1][i]
                sum1 = 0

                if up == down and up != 0:
                    sum1 = up + down
                    matrix[count][i] = sum1
                    matrix[count+1][i] = 0

                count += 1
            count = 0

        print(matrix)

        for i in range(4):
            print(matrix[i])

    #DOWN DIRECTION
    elif direction == 'down':
        print(length_of_matrix)
        for i in range(4):
            print(matrix[i])
            
        count = length 
        for i in range(length_of_matrix):
            while count != 0:  
                up = matrix[count-1][i]
                down = matrix[count][i]
                sum1 = 0

                if up == down and up != 0:
                    sum1 = up + down
                    matrix[count-1][i] = 0
                    matrix[count][i] = sum1

                count -= 1
            count = length

        print(matrix)

        for i in range(4):
            print(matrix[i]) 


compress(direction)