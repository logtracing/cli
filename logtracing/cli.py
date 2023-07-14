from typing import Optional
from rich import print
import typer
from logtracing import (
    SUCCESS, ERRORS, __app_name__, __version__, config
)

app = typer.Typer()

def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def init(
    db_user: str = typer.Option(
        None,
        "--db-user",
        prompt="Database user",
    ),
    db_password: str = typer.Option(
        None,
        "--db-pass",
        prompt="Database password",
    ),
    db_host: str = typer.Option(
        None,
        "--db-host",
        prompt="Database host",
    ),
    db_port: str = typer.Option(
        None,
        "--db-port",
        prompt="Database port",
    ),
    db_database: str = typer.Option(
        None,
        "--db-name",
        prompt="Database name",
    )
    ) -> None:
    if not config.exists():
        db_config = {
            'user': db_user,
            'pass': db_password,
            'host': db_host,
            'port': db_port,
            'db_name': db_database,
        }

        status = config.init(db_config=db_config)

        if not status == SUCCESS:
            print(f"\n[bold red]Something went wrong with '{ERRORS[status]}'[/bold red]\n")
            raise typer.Exit(1)

        print('\n[green]Initial configuration was done![green]\n')
        raise typer.Exit()
    else:
        print("\n[bold red]The config file already exists[/bold red]\n")
    

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
