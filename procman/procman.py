import typer

from .sort import generate_proc_list

from pynput.keyboard import Listener, Key, KeyCode
from rich.table import Table, Column
from rich.console import Console
from rich.live import Live
from rich.style import Style


from . import sort

ROWS: int = 24

app = typer.Typer()

__row_select: int = 0
__exit_flag: bool = False


def __check_row(i: int, row_select: int) -> Style:
    return "#fcf000 on #404040" if i == row_select else ""


# TODO Show different process filtering methods
def create_process_table(rows: int, row_select: int) -> Table:
    table: Table = Table(
        "User",
        "Name",
        "PID",
        "PPID",
        "Mem Usage",
        "Uptime",
        "Status",
        title="Process Manager",
        highlight=True,
        expand=True,
    )

    proc_list = generate_proc_list(rows)

    for i in range(len(proc_list)):
        table.add_row(
            proc_list[i].uname,
            proc_list[i].name,
            str(proc_list[i].pid),
            str(proc_list[i].ppid),
            str(proc_list[i].get_mem_usage()),
            str(proc_list[i].uptime()),
            proc_list[i].status(),
            style=__check_row(i, row_select),
        )

    return table


def on_press(event: Key) -> None:
    global __row_select, col_select, __exit_flag

    try:
        if event == KeyCode.from_char("q") or event == KeyCode.from_char("Q"):
            __exit_flag = True

        # TODO Implement kill process method
        elif event == KeyCode.from_char("k") or event == KeyCode.from_char("K"):
            pass

        elif event == Key.up:
            if __row_select > 0:
                __row_select -= 1
            else:
                __row_select = ROWS - 1

        elif event == Key.down:
            if __row_select < ROWS - 1:
                __row_select += 1
            else:
                __row_select = 0

        # TODO Implement sorting processes method
        elif event == Key.left:
            pass

        elif event == Key.right:
            pass

    except AttributeError:
        pass


@app.command(short_help="View process manager")
def App():
    global __row_select

    console = Console()

    listener: Listener = Listener(
        on_press=on_press,
        suppress=True,
    )

    listener.start()  # Starts a non-blocking event to listen to keyboard press

    with Live(console=console, screen=True, refresh_per_second=1) as live:
        while True:
            proc_table: Table = create_process_table(ROWS, __row_select)

            live.update(proc_table)

            if __exit_flag:
                listener.stop()
                break
