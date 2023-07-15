from typing import Optional

import typer
from rich import print

from logtracing import config
from logtracing.database import LogTracingDB

log_app = typer.Typer()

@log_app.command(help="Print a list of logs.")
def show(
    flow: str = typer.Option(
        ...,
        '--flow',
        '-f',
    )
    ) -> None:
    print('Logs...')
