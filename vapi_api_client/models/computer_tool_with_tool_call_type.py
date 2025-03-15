from enum import Enum


class ComputerToolWithToolCallType(str, Enum):
    COMPUTER = "computer"

    def __str__(self) -> str:
        return str(self.value)
