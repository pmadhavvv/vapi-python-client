from enum import Enum


class BashToolName(str, Enum):
    BASH = "bash"

    def __str__(self) -> str:
        return str(self.value)
