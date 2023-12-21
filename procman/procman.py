from . import visuals

import curses


def App(stdscr):
    curses.curs_set(0)
    visuals.startscreen(stdscr)
