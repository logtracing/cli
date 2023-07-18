import pydoc

import typer
from rich import print
from rich.console import Console
from rich.__main__ import make_test_card

from logtracing.database import LogTracingDB

log_app = typer.Typer()
console = Console()

@log_app.command(help="Print a list of logs.")
def show(
    flow: str = typer.Option(
        ...,
        '--flow',
        '-f',
    ),
    limit: int = typer.Option(
        50,
        '--limit',
        '-l'
    )
    ) -> None:
    logtracing_db = LogTracingDB()
    logs = logtracing_db.get_logs(flow=flow, limit=limit)

    if not logs:
        print('No logs found.')
        raise typer.Exit()

    output = '\n'.join(map(lambda log: log.text(), logs))

    with console.pager(styles=True):
        console.print(output)

