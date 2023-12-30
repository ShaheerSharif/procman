import time

from rich.live import Live
from rich.table import Table, Column

# from . import units
# from . import process

table = Table(
    "Row ID",
    "Description",
    Column(header="Level", justify="right"),
    title="Table",
    highlight=True,
)
# table.add_column("Row ID")
# table.add_column("Description")
# table.add_column("Level")

with Live(table, refresh_per_second=4, vertical_overflow="visible") as live:
    for row in range(50):
        # live.console.print(f"Working on row #{row}")
        time.sleep(0.2)
        table.add_row(f"{row}", f"description {row}", "[red]ERROR")
