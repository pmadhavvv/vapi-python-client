from enum import Enum


class ToolMessageStartType(str, Enum):
    REQUEST_START = "request-start"

    def __str__(self) -> str:
        return str(self.value)
