import curses
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
