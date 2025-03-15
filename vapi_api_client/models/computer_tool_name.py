from enum import Enum


class ComputerToolName(str, Enum):
    COMPUTER = "computer"

    def __str__(self) -> str:
        return str(self.value)
