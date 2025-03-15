from enum import Enum


class BashToolType(str, Enum):
    BASH = "bash"

    def __str__(self) -> str:
        return str(self.value)
