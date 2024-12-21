grid = [[2,4,6,8], [3,5,7,9], [0,0,0,0], [0,0,0,0]]

#GOING TO THE LEFT
for i in range(3):
    for j in range(3):
        first = grid[i][j]
        if j != 3:
            second = grid[i][j + 1]

        print("first value:")
        print(first)
        print("second value")
        print(second)
        print('')


for i in range(4):
    print(grid[i])

local_list= [2,4,0,0]

