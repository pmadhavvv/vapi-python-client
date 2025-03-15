from enum import Enum


class BashToolWithToolCallType(str, Enum):
    BASH = "bash"

    def __str__(self) -> str:
        return str(self.value)
