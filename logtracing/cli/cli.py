from typing import Optional

import typer

from logtracing import __app_name__, __version__
from logtracing.cli.config import config_app
from logtracing.cli.log import log_app

app = typer.Typer()

def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}.")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the LogTracing CLI App version",
        callback=_version_callback,
        is_eager=True
    )
    ) -> None:
    return

# commands
app.add_typer(config_app, name="config", help="Set up the required configuration for the CLI app.")
app.add_typer(log_app, name="log", help="Handle the logs stored via the LogTracing packages.")
