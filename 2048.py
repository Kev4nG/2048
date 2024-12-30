from calendar import c
import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("------  2048 Test Game  ------")
    stdscr.addstr(1,0, "--- Click any key to continue ---")
    stdscr.refresh()
    stdscr.getkey()


def display_grid(stdscr, matrix):
    stdscr.clear()
    stdscr.addstr( 0, 0,f" {matrix[0]}")
    stdscr.addstr( 1, 0,f" {matrix[1]}")
    stdscr.addstr( 2, 0,f" {matrix[2]}")
    stdscr.addstr( 3, 0,f" {matrix[3]}")
    stdscr.refresh()


def spawn(stdscr, matrix):
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

    display_grid(stdscr, matrix)


def shift(stdscr, direction, matrix):
    length = len(matrix[0]) -1
    length_of_matrix = len(matrix) 

    # LEFT DIRECTION
    if direction == 'a':
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

    #RIGHT DIRECTION    
    elif direction == 'd':
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
    elif direction == 'w':
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

    #DOWN DIRECTION
    elif direction == 's':
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

    display_grid(stdscr, matrix)


def compress(stdscr, direction, matrix):
    length = len(matrix[0]) -1
    length_of_matrix = len(matrix) 


    # LEFT DIRECTION
    if direction == 'a':
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


    #RIGHT DIRECTION    
    elif direction == 'd':
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


    #UP DIRECTION
    elif direction == 'w':
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

    #DOWN DIRECTION
    elif direction == 's':
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

    display_grid(stdscr, matrix)


def grid(stdscr):
    direction_list = []
    index_of_direction = -1
    game_state = True

    matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    display_grid(stdscr, matrix)
    spawn(stdscr, matrix)

    while game_state == True:
        try:
            direction = stdscr.getkey() # w a s d for valid direction inputs 
            if direction == "w" or 'a' or 's' or 'd':
                index_of_direction += 1
                direction_list.append(direction)

                

                shift(stdscr, direction_list[index_of_direction], matrix)
                compress(stdscr, direction_list[index_of_direction], matrix)
                shift(stdscr, direction_list[index_of_direction], matrix)
                spawn(stdscr, matrix)
                
        except:
            continue    # note this blocks it... like an input... now it does not bc of the nodelay




        # if ord(direction) == 27 or direction == "\x1b": #escape key to leave
        #     break

    print(direction_list)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    grid(stdscr)

    
    
    
wrapper(main)