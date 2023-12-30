import typer

from .sort import generate_proc_list

from rich import box

from pynput.keyboard import Listener, Key, Events
from rich.table import Table, Column
from rich.console import Console
from rich.live import Live

from . import sort

ROWS: int = 20

app = typer.Typer()
selected: int = 0


def create_process_table(rows: int, selected: int) -> Table:
    table: Table = Table(
        Column(" ", style="bold green", justify="center"),
        "User",
        "Name",
        "PID",
        "PPID",
        "Mem Usage",
        "Uptime",
        "Status",
        title="Process Manager",
        highlight=True,
        box=box.SIMPLE,
    )

    proc_list = generate_proc_list(rows)

    for i in range(len(proc_list)):
        table.add_row(
            "●" if i == selected else "",
            proc_list[i].username,
            proc_list[i].name,
            str(proc_list[i].pid),
            str(proc_list[i].ppid),
            str(proc_list[i].get_mem_usage()),
            str(proc_list[i].uptime()),
            "[bold green]Running[/bold green]"
            if proc_list[i].active
            else "[bold red]IDLE[/bold red]",
        )

    return table


def on_press(key: Key):
    global selected

    try:
        if key == Key.up:
            if selected > 0:
                selected -= 1
            else:
                selected = ROWS - 1

        elif key == Key.down:
            if selected < ROWS - 1:
                selected += 1
            else:
                selected = 0

    except AttributeError:
        pass


@app.command(short_help="View process manager")
def App():
    global selected

    console = Console()

    listener: Listener = Listener(on_press=on_press, suppress=True)
    listener.start()  # Starts a non-blocking event to listen to keyboard press

    with Live(console=console, screen=True, refresh_per_second=1) as live:
        while True:
            live.update(create_process_table(ROWS, selected))
