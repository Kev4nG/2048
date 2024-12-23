import random

# x = random.randrange()

matrix = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,0,2,2]]
length_of_matrix = len(matrix) 
spawn_possiblities = [2,4]
spawn = random.choice(spawn_possiblities)



list_of_locations = []
for y in range(length_of_matrix):
    placement = [(y, i) for i, x in enumerate(matrix[y]) if x == 0]
    for x in placement:
        list_of_locations.append(x)

try:
    randomLocation = random.choice(list_of_locations)
    matrix[randomLocation[0]][randomLocation[1]] = spawn
except IndexError:
    pass

  
print(matrix)


