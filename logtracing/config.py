import configparser
from pathlib import Path
from rich import print
from logtracing import (
    SUCCESS, CONFIG_DIR_ERROR, CONFIG_FILE_ERROR
)

CONFIG_FOLDER_PATH = Path(f"{Path.home()}/.logtracing")
CONFIG_FILE_PATH = CONFIG_FOLDER_PATH / "config.ini"

def init(db_config: dict[str, str]) -> int:
    init_status_code = _init_config_file()

    if init_status_code != SUCCESS:
        return init_status_code

    db_status_code = _save_db_config(db_config)

    if db_status_code != SUCCESS:
        return db_status_code

    return SUCCESS

def exists() -> bool:
    return CONFIG_FILE_PATH.exists()

def print_config() -> None:
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)

    for section in config_parser.sections():
        print(f"[green][{section}][/green]")
        for option in config_parser.options(section):
            print(f"{option} = {config_parser.get(section, option)}")

def _init_config_file() -> int:
    try:
        CONFIG_FOLDER_PATH.mkdir(exist_ok=True)
    except OSError:
        return CONFIG_DIR_ERROR

    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return CONFIG_FILE_ERROR

    return SUCCESS

def _save_db_config(db_config: dict[str, str]) -> int:
    config_parser = configparser.ConfigParser()
    config_parser['Database'] = db_config

    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return CONFIG_FILE_ERROR

    return SUCCESS

if __name__ == "__main__":
    print(init())
