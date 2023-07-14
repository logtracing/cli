from typing import Optional

import typer
from rich import print

from logtracing import SUCCESS, ERRORS, config

config_app = typer.Typer()

@config_app.command(help="Create the configuration file.")
def create(
    db_user: str = typer.Option(
        ...,
        "--db-user",
    ),
    db_password: str = typer.Option(
        ...,
        "--db-pass",
    ),
    db_host: str = typer.Option(
        ...,
        "--db-host",
    ),
    db_port: str = typer.Option(
        ...,
        "--db-port",
    ),
    db_database: str = typer.Option(
        ...,
        "--db-name",
    ),
    force: Optional[bool] = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite the current configuration",
    )
    ) -> None:
    if not config.exists() or force:
        db_config = {
            'user': db_user,
            'pass': db_password,
            'host': db_host,
            'port': db_port,
            'db_name': db_database,
        }

        status = config.init(db_config=db_config)

        if not status == SUCCESS:
            print(f"\n[red]Something went wrong with '{ERRORS[status]}'[/red]\n")
            raise typer.Exit(1)

        print('\n[green]Initial configuration was done![green]\n')
        raise typer.Exit()
    else:
        print("\n[red]The config file already exists. Use the option --force or -f to overwrite it.[/red]\n")

@config_app.command(help="Show your current configuration.")
def show() -> None:
    config.print_config()
