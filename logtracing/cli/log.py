from typing import Optional

import typer
from rich import print

from logtracing.database import LogTracingDB

log_app = typer.Typer()

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

    for log in logs:
        print(log.text())
