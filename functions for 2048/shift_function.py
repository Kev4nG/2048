#this is for shigtin
            #0 1 2 3
matrix = [[0,0,0,2], [2,4,0,8], [0,2,4,0], [0,0,0,8]]
length = len(matrix[0]) -1
length_of_matrix = len(matrix) 
direction = 'up'

def shift(direction):
    # LEFT DIRECTION
    if direction == 'left':
        count = 0 
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

                    count = -1

                count += 1
            count = 0

        print(matrix)

    #RIGHT DIRECTION    
    elif direction == 'right':
        print(matrix)
        count = 0 
        for i in range(length_of_matrix):
            while count != length:
                left = matrix[i][count]
                right = matrix[i][count+1]

                if right == 0 and left != 0: #swapped
                    right ^= left
                    left ^= right
                    right ^= left  

                    matrix[i][count] = left
                    matrix[i][count + 1] = right     

                    count = -1
                count += 1
            count = 0

        print(matrix)   
    #UP DIRECTION
    elif direction == 'up':
        count = 0 
        for i in range(length_of_matrix):
            while count != length:
                up = matrix[count][i]
                down = matrix[count+1][i]

                if up == 0 and down != 0:
                    up ^= down
                    down ^= up
                    up ^= down  

                    matrix[count][i] = up
                    matrix[count + 1][i] = down     

                    count = -1

                count += 1
            count = 0


        for i in range(4):
            print(matrix[i])    
    #DOWN DIRECTION
    elif direction == 'down':
        count = 0 
        for i in range(length_of_matrix):
            while count != length:
                up = matrix[count][i]
                down = matrix[count+1][i]

                if down == 0 and up != 0:
                    up ^= down
                    down ^= up
                    up ^= down  

                    matrix[count][i] = up
                    matrix[count + 1][i] = down     

                    count = -1

                count += 1
            count = 0

        for i in range(4):
            print(matrix[i]) 


shift(direction)