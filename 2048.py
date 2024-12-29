from calendar import c
import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("------  2048 Test Game  ------")
    stdscr.addstr(1,0, "--- Click any key to continue ---")
    stdscr.refresh()
    stdscr.getkey()


def spawn(stdscr):
    pass


def shfit(stdscr):
    pass


def compress(stdscr):
    pass






def grid(stdscr):
    matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    game_state = True

    #spawn function

    while game_state == True:
        try:
            direction = stdscr.getkey() # w a s d for valid direction inputs 
        except:
            continue    # note this blocks it... like an input... now it does not bc of the nodelay

        #shift
        #compress
        #shift again
        #spawn



        if ord(direction) == 27: #escape key to leave
            break




def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    grid(stdscr)

    
    
    
wrapper(main)