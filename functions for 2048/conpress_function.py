

matrix = [[2,2,0,0], [2,4,4,0], [2,2,4,0], [0,0,8,8]]
length = len(matrix[0]) -1
length_of_matrix = len(matrix) 
direction = 'down'

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
        count = 0 
        for i in range(length_of_matrix):
            while count != length:
                left = matrix[i][count]
                right= matrix[i][count+1]
                sum1 = 0

                if left == right and left != 0:
                    sum1 = left + right
                    matrix[i][count + 1] = sum1
                    matrix[i][count] = 0

                count += 1
            count = 0

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


compress(direction)