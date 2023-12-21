import curses
import sys

from .procman import App

COMMANDS: dict[str, list[str]] = {
    "help": ["-h", "--help", "help"],
    "start": ["-s", "--start", "start"],
}


invalid_arg_text: str = f"""
Invalid argument: unrecognized option(s) '{[sys.argv[i] for i in range(1, len(sys.argv))]}'
"""

error_text: str = "Error: no operation specified (use '-h' for help)"

help_text: str = f"""
Usage: procman <operation>

Operations:
    procman {str(COMMANDS['start']):>27}  start
    procman {str(COMMANDS['help']):>27}  help

For help menu use 'procman -h'
"""


def main() -> None:
    if len(sys.argv) == 2:
        if sys.argv[1] in COMMANDS["start"]:
            curses.wrapper(App)
        elif sys.argv[1] in COMMANDS["help"]:
            print(help_text)
        else:
            print(invalid_arg_text)
    elif len(sys.argv) < 2:
        print(error_text)
    else:
        print(invalid_arg_text)


if __name__ == "__main__":
    main()
