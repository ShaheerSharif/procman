import typer

from .sort import generate_proc_list

from rich.table import Table
from rich.console import Console
from rich.live import Live

from . import sort

app = typer.Typer()


def create_process_table(rows: int) -> Table:
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
    )

    for proc in generate_proc_list(rows):
        table.add_row(
            proc.username,
            proc.name,
            str(proc.pid),
            str(proc.ppid),
            str(proc.get_mem_usage()),
            str(proc.uptime()),
            "[bold green]Running[/bold green]"
            if proc.active
            else "[bold red]IDLE[/bold red]",
        )

    return table


@app.command(short_help="View process manager")
def App():
    console = Console()

    with Live(console=console, screen=True, refresh_per_second=2) as live:
        while True:
            live.update(create_process_table(24))
