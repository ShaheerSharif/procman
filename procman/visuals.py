import curses
import platform
import threading
import time
import traceback

DISPLAY: dict[str, str] = {
    "command": "Command",
    "pid": "PID",
    "mem": "Memory Usage",
    "cpu": "CPU Usage",
    "uptime": "Uptime",
}

SYSTEM_INFO: dict[str, str] = {
    "os": f"OS: {platform.system()}",
    "release": f"Release: {platform.release()}",
    "arch": f"Architecture: {platform.machine()}",
}


def startscreen(stdscr) -> None:
    (ROWS, COLS) = stdscr.getmaxyx()
    title: str = "Welcome To Procman"
    prompt: str = "Press any key to start"

    titlewin = curses.newwin(ROWS, COLS, 0, 0)
    titlewin.border()

    titlewin.addstr(2, (COLS // 2) - (len(title) // 2), title, curses.A_BOLD)
    titlewin.addstr(6, 2, SYSTEM_INFO["os"])
    titlewin.addstr(8, 2, SYSTEM_INFO["release"])
    titlewin.addstr(10, 2, SYSTEM_INFO["arch"])
    titlewin.addstr(
        ROWS // 2 + 1, (COLS // 2) - (len(title) // 2), prompt, curses.A_BLINK
    )

    titlewin.getch()

    stdscr.touchwin()
    stdscr.refresh()
