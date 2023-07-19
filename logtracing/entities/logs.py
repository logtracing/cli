from datetime import datetime
from typing import Optional
from enum import Enum

class Log:
    def __init__(
            self,
            level: str,
            flow: str,
            content: str,
            created_at: datetime,
            group_name: Optional[str]) -> None:
        self.level = level
        self.flow = flow
        self.content = content
        self.created_at = created_at
        self.group_name = group_name
        self.colors = {
            "TRACE": "cyan",
            "INFO": "green",
            "DEBUG": "blue",
            "WARN": "yellow",
            "ERROR": "red",
            "FATAL": "magenta",
        }

    def _get_color(self):
        return self.colors[self.level]

    def _get_formatted_level(self):
        color = self._get_color()

        return f"[{color}][{self.level.ljust(5)}][/{color}]"

    def _get_formatted_date(self):
        formatted_date = self.created_at.strftime("%d-%m-%Y %H:%M:%S")

        return f"[white][{formatted_date}][/white]"

    def text(self):
        return f"{self._get_formatted_level()}{self._get_formatted_date()}: {self.content}"

class LogLevel(str, Enum):
    trace = "TRACE"
    info = "INFO"
    debug = "DEBUG"
    warn = "WARN"
    error = "ERROR"
    fatal = "FATAL"
