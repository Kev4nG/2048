from calendar import c
import curses
from curses import wrapper
import time


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("2048 Test Game")
    stdscr.addstr(1,0, "Click any key to continue")
    stdscr.refresh()
    stdscr.getkey()

def end_screen(stdscr, wpm):
    stdscr.clear()
    stdscr.addstr("Finished")
    stdscr.addstr(1,0, f"Word per second : {wpm}")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):

    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)

        if char != correct_char:
            color = curses.color_pair(3)

            

        stdscr.addstr(0, i, char, color)
    
    


def wpm_test(stdscr):
    target_text = "This is the example text for this game ig."
    current_text = []
    wpm = 0

    start_time = time.time()
    stdscr.nodelay(True)


    while True:   
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text)/ (time_elapsed/60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:        #stringifies lists very useful
            stdscr.nodelay(False)
            break


        try:
            key = stdscr.getkey()
        except:
            continue    # note this blocks it... like an input... now it does not bc of the nodelay

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)        

    end_screen(stdscr, wpm)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)


    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)