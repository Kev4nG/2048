from calendar import c
import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("2048 Test Game")
    stdscr.addstr(1,0, "Click any key to continue")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):

    stdscr.addstr(target)

    for i, char in enumerate(current):
        stdscr.addstr(0, i, char, curses.color_pair(1))
    
    


def wpm_test(stdscr):
    target_text = "This is the example text for this game ig."
    current_text = []


    while True:        
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)
        



def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)


    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)