from typing import Optional
import typer
from logtracing import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
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
