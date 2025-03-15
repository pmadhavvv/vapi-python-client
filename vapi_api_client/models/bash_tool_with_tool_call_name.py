from enum import Enum


class BashToolWithToolCallName(str, Enum):
    BASH = "bash"

    def __str__(self) -> str:
        return str(self.value)
