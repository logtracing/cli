from pathlib import Path
from logtracing import (
    SUCCESS, CONFIG_DIR_ERROR, CONFIG_FILE_ERROR
)

CONFIG_FOLDER_PATH = Path(f"{Path.home()}/.logtracing")
CONFIG_FILE_PATH = CONFIG_FOLDER_PATH / "config.ini"

def init(db_config: dict[str, str]) -> int:
    init_status_code = _init_config_file()

    if init_status_code != SUCCESS:
        return init_status_code

    return SUCCESS

def exists() -> bool:
    return CONFIG_FILE_PATH.exists()

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

if __name__ == "__main__":
    print(init())
